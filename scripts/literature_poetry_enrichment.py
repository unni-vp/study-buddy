"""Shared poem detail for revision notes and evidence-rich model answers."""
from pathlib import Path
import json
import re
import unicodedata
from itertools import zip_longest

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / 'English Literature - Eduqas/02 - Poetry anthology - assessment from 2027/poem-details.json'
DETAILS = json.loads(DATA_PATH.read_text(encoding='utf-8'))
ANSWER_DATA = json.loads((DATA_PATH.parent / 'poetry-answer-enrichment.json').read_text(encoding='utf-8'))


def poem_detail(title):
    return next((heading, detail) for heading, detail in DETAILS.items() if heading.split(' — ')[0] == title)


def enrich_notes(body):
    for heading, detail in DETAILS.items():
        pattern = re.compile(r'^## ' + re.escape(heading) + r'\n\n(.*?)(?=^## |\Z)', re.M | re.S)
        match = pattern.search(body)
        if not match:
            raise ValueError('Missing poem: ' + heading)
        old = match[1]
        opening = old.split('\n\n')[0]
        retained = {}
        for label in ['Main argument', 'Form and structure', 'Compare', 'Must know']:
            row = re.search(r'^- \*\*' + label + r':\*\* (.+)$', old, re.M)
            if row:
                retained[label] = row[1]
        parts = ['## ' + heading, opening]
        if 'Main argument' in retained:
            parts.append('**Main idea:** ' + retained['Main argument'])
        parts += ['### Poet context', detail['poet_context'], '### Poem context', detail['poem_context'],
                  '### The poem content', '\n'.join('- ' + point for point in detail['content']),
                  '### Key quotations', '\n'.join('- **“' + quote + '”:** ' + analysis for quote, analysis in detail['quotes']),
                  '### Language and imagery', '\n'.join('- ' + point for point in detail['language'])]
        if 'Form and structure' in retained:
            parts += ['### Form and structure', retained['Form and structure']]
        parts += ['### Example quotation analysis', detail['example']]
        if 'Compare' in retained:
            parts.append('**Compare:** ' + retained['Compare'])
        if 'Must know' in retained:
            parts.append('**Remember:** ' + retained['Must know'])
        body = body[:match.start()] + '\n\n'.join(parts) + '\n\n' + body[match.end():]
    return body


def normalize(text):
    text = unicodedata.normalize('NFKC', text).replace('’', "'").replace('‘', "'")
    return re.sub(r'\s+', ' ', text).lower()


def missing_quotes(detail, answer):
    quoted = re.findall(r'[“"]([^”"]+)[”"]', answer)
    quoted += re.findall(r'‘(.+?)’(?=\W|$)', answer, re.S)
    return [(quote, analysis) for quote, analysis in detail['quotes']
            if not any(normalize(quote) in normalize(fragment) for fragment in quoted)]


def enrich_single_answer(title, answer):
    _, detail = poem_detail(title)
    additions = ANSWER_DATA['single'][title]
    paragraphs = answer.strip().split('\n\n')
    paragraphs.insert(1, additions['context'])
    paragraphs[-1:-1] = additions['evidence']
    result = '\n\n'.join(paragraphs)
    if missing_quotes(detail, result):
        raise ValueError('Incomplete quotation evidence: ' + title)
    return result


def enrich_comparison_answer(first, second, answer):
    paragraphs = answer.strip().split('\n\n')
    paragraphs = [p for p in paragraphs if not p.startswith('Their contexts support these choices.')]
    paragraphs.insert(1, ANSWER_DATA['single'][first]['context'] + ' ' + ANSWER_DATA['single'][second]['context'])
    paragraphs[-1:-1] = ANSWER_DATA['comparison'][first]
    result = '\n\n'.join(paragraphs)
    for title in [first, second]:
        if missing_quotes(poem_detail(title)[1], result):
            raise ValueError('Incomplete comparative quotation evidence: ' + title)
    return result
