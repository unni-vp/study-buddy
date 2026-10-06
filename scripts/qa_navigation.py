"""Render one topic's combined question bank, grouped only by marks."""
from dataclasses import dataclass
from html import escape
import re
from urllib.parse import unquote, urlsplit, urlunsplit
from html_utils import render_md


@dataclass
class MarkGroup:
    marks: int
    questions: list

    @property
    def title(self):
        return f'{self.marks} ' + ('mark' if self.marks == 1 else 'marks')

    @property
    def id(self):
        return f'marks-{self.marks}'


def parse_qa(raw):
    title = re.match(r'^# (.+)\n', raw)
    if not title:
        raise ValueError('Q&A must begin with its document title')
    source_parts = re.split(r'^## Past-paper sources\s*$', raw, maxsplit=1, flags=re.M)
    question_text = source_parts[0]
    sources = source_parts[1].strip() if len(source_parts) == 2 else ''
    headings = list(re.finditer(r'^## (\d+) marks?\s*$', question_text, re.M))
    if not headings or question_text[title.end():headings[0].start()].strip():
        raise ValueError('Q&A content must be assigned to a mark group')
    groups = []
    numbers = []
    for i, heading in enumerate(headings):
        body = question_text[heading.end():headings[i+1].start() if i+1 < len(headings) else len(question_text)]
        starts = list(re.finditer(r'^\*\*(\d+)\.\*\* ', body, re.M))
        if not starts or body[:starts[0].start()].strip():
            raise ValueError('Every question must have a plain numbered prompt')
        questions = []
        for j, start in enumerate(starts):
            number = int(start[1])
            text = body[start.start():starts[j+1].start() if j+1 < len(starts) else len(body)].strip()
            if not re.search(r'\n\n\*\*Answer:\*\*(?:[ \t]+\S|\n\n\S)', text):
                raise ValueError(f'Answer missing for question {number}')
            if re.search(r'^#{1,6} ', text, re.M):
                raise ValueError(f'Question {number} must not have its own heading')
            questions.append((number, text))
            numbers.append(number)
        groups.append(MarkGroup(int(heading[1]), questions))
    marks = [g.marks for g in groups]
    if marks != sorted(set(marks)) or marks[0] < 1:
        raise ValueError('Mark groups must be unique and in increasing order')
    if numbers != list(range(1, len(numbers)+1)):
        raise ValueError('Questions must be numbered consecutively across the topic')
    return title[1], groups, sources


def build_qa_pages(source, target, subject, topic, topicpage, write, link):
    title, groups, sources = parse_qa(source.read_text(encoding='utf-8'))
    source_page = target.with_name(target.stem+'-sources.html')
    full = target.with_name(target.stem+'-all.html')
    crumbs = [(subject.split(' - ')[0], source.parents[2]/'index.html'), (topic, topicpage)]

    def render(page, md):
        def relocate(match):
            url = match[2]
            if re.match(r'^(https?:|#|mailto:)', url):
                return match[0]
            parts = urlsplit(url)
            relocated = link(page, (source.parent/unquote(parts.path)).resolve())
            return match[1]+'="'+urlunsplit(('', '', relocated, parts.query, parts.fragment))+'"'
        return re.sub(r'(href|src)="([^"]+)"', relocate, render_md(md))

    def content(page):
        jumps = ''.join(f'<a href="#{g.id}">{g.title}</a>' for g in groups)
        sections = []
        for group in groups:
            pairs = []
            for n, text in group.questions:
                if text.count('**Answer:**') != 1:
                    raise ValueError(f'Question {n} must have exactly one answer label')
                prompt, answer = text.split('**Answer:**', 1)
                answer_id = f'answer-{n:02}'
                disclosure = (f'<details class="qa-answer" id="{answer_id}">'
                              f'<summary aria-label="Answer to question {n}">Answer:</summary>'
                              f'<div class="qa-answer-body">{render(page, answer.strip())}</div></details>')
                pairs.append(f'<div class="qa-question" id="q{n:02}">{render(page, prompt.strip())}{disclosure}</div>')
            sections.append(f'<section class="qa-mark-group" id="{group.id}"><h2>{group.title}</h2>'+''.join(pairs)+'</section>')
        controls = ('<div class="reader-tools qa-answer-controls" role="group" aria-label="Answer controls">'
                    '<button type="button" data-qa-action="expand">Expand all</button>'
                    '<button type="button" data-qa-action="collapse">Collapse all</button></div>')
        return f'<article class="reading qa-reading"><h1>{escape(title)}</h1>'+controls+f'<nav class="qa-mark-links" aria-label="Jump to mark group">{jumps}</nav>'+''.join(sections)+'</article><script defer src="'+link(page, target.parent.parent/'qa.js')+'"></script>'

    source_link = f'<a href="{link(target, source_page)}">Past-paper sources</a>' if sources else ''
    write(target, title, f'<div class="reader-tools qa-tools"><a href="{link(target, topicpage)}">← Back to topic</a>{source_link}<button onclick="window.print()">Print Q&amp;A</button></div>'+content(target), crumbs, subject)
    # Retain the complete-view URL for existing bookmarks; it contains the same bank.
    write(full, title, f'<div class="reader-tools"><a href="{link(full, target)}">← Questions &amp; answers</a><button onclick="window.print()">Print all Q&amp;A</button></div>'+content(full), crumbs, subject)
    if sources:
        source_content = render(source_page, '# Past-paper sources\n\n'+sources)
        write(source_page, 'Past-paper sources', f'<div class="reader-tools"><a href="{link(source_page, target)}">← Questions &amp; answers</a></div><article class="reading">{source_content}</article>', crumbs+[('Questions & answers', target)], subject)
    # These derived pages belonged to the earlier thematic split. Remove only
    # this resource's generated group files, never the editable source documents.
    for obsolete in target.parent.glob(target.stem+'-group-*.html'):
        if obsolete.resolve().parent != target.parent.resolve():
            raise ValueError('Obsolete Q&A page outside the resource directory')
        obsolete.unlink()
    return target, title
