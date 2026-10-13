"""Verify anthology evidence, note coverage and the combined Literature readers."""
from pathlib import Path
import hashlib
import json
import re
from pypdf import PdfReader
from literature_poetry_enrichment import DETAILS, missing_quotes, normalize

ROOT = Path(__file__).resolve().parents[1]
subject = ROOT / 'English Literature - Eduqas'
topic = subject / '02 - Poetry anthology - assessment from 2027'
items = json.loads((topic / 'qa-evidence.json').read_text(encoding='utf-8'))['questions']
extended = [item for item in items if item['marks'] >= 15]
singles = [item for item in extended if item['marks'] == 15]
assert len(DETAILS) == len(singles) == 15
pdf = PdfReader(subject / '00 - Specification/Eduqas-poetry-anthology-first-assessment-2027.pdf')
starts = {}
for item in extended:
    match = re.search(r'Read \[([^]]+)\]\([^)]*#page=(\d+)\)', item['prompt'])
    assert match, item['number']
    title, page = match[1], int(match[2])
    assert title.lower() in ' '.join(pdf.pages[page-1].extract_text().split()).lower(), (title, page)
    if item['marks'] == 15:
        starts[title] = page
    assert len(item['answer'].split()) >= 190, item['number']
    for poem in item['poems']:
        detail = next(d for heading, d in DETAILS.items() if heading.split(' — ')[0] == poem)
        assert not missing_quotes(detail, item['answer']), (item['number'], poem)

notes_source = topic / 'Revision Notes/Poetry anthology - Revision Notes.md'
notes = notes_source.read_text(encoding='utf-8')
sections = dict((part.split('\n', 1)[0], part.split('\n', 1)[1])
                for part in re.split(r'^## ', notes, flags=re.M)[1:])
required = ['Poet context', 'Poem context', 'The poem content', 'Key quotations',
            'Language and imagery', 'Form and structure', 'Example quotation analysis']
ordered_pages = sorted(starts.values())
anchor_count = 0
for heading, detail in DETAILS.items():
    assert all('### ' + label in sections[heading] for label in required), heading
    assert 5 <= len(detail['quotes']) <= 6, heading
    title = heading.split(' — ')[0]
    start = starts[title]
    end = next((p-1 for p in ordered_pages if p > start), len(pdf.pages))
    poem_text = normalize(' '.join(pdf.pages[p-1].extract_text() for p in range(start, end+1)))
    for quote, explanation in detail['quotes']:
        assert normalize(quote) in poem_text, (title, quote)
        assert explanation.strip()
        anchor_count += 1
    bank = sections[heading].split('### Key quotations', 1)[1].split('### Language and imagery', 1)[0]
    assert len(re.findall(r'^- \*\*“', bank, re.M)) == len(detail['quotes']), heading

for folder in ['01 - Macbeth', '02 - Poetry anthology - assessment from 2027']:
    source = next((subject / folder / 'Questions and Answers').glob('* - Questions and Answers.md'))
    key = hashlib.sha1(str(source.relative_to(ROOT)).encode()).hexdigest()[:12]
    reader = (ROOT / 'library/resources' / (key + '.html')).read_text(encoding='utf-8')
    bank = json.loads((source.parent.parent / 'qa-evidence.json').read_text(encoding='utf-8'))['questions']
    assert reader.count('class="qa-answer"') == len(bank), folder
    assert 'class="qa-answer" open' not in reader, folder
    assert '.pdf%23' not in reader, folder
    if folder.startswith('02'):
        assert reader.count('.pdf#page=') == len(extended)
    else:
        assert reader.count('class="verse-extract"') >= 3 and '<br>' in reader
        for name in ['Banquo', 'Macduff', 'witches', 'violence', 'gender', 'appearance']:
            assert any(name.lower() in q['prompt'].lower() for q in bank if q['marks'] == 25), name
print(f'PASS: 15 complete poem notes; {anchor_count} verified quotation anchors; '
      f'{len(extended)} extended poetry models; intact combined Literature readers')
