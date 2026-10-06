"""Check current anthology coverage and working PDF page links in generated Q&A."""
from pathlib import Path
import json,re
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
topic=ROOT/'English Literature - Eduqas/02 - Poetry anthology - assessment from 2027'
items=json.loads((topic/'qa-evidence.json').read_text(encoding='utf-8'))['questions']
poems=json.loads((topic/'resource-coverage.json').read_text())['coverage']['poems']
assert len(poems)==15 and len(items)==23
assert [x['marks'] for x in items]==[15]*15+[25]*8
pdf=PdfReader(topic.parent/'00 - Specification/Eduqas-poetry-anthology-first-assessment-2027.pdf')
for item in items:
 m=re.search(r'Read \[([^]]+)\]\([^)]*#page=(\d+)\)',item['prompt']);assert m,item['number']
 title,page=m.group(1),int(m.group(2));assert 1<=page<=len(pdf.pages)
 actual=' '.join(pdf.pages[page-1].extract_text().split())
 assert title.lower() in actual.lower(),(title,page)
 assert len(item['answer'].split())>=190,(item['number'],'underdeveloped answer')
source=(ROOT/'library/resources/3e876e5719a7.html').read_text(encoding='utf-8')
assert source.count('.pdf#page=')==23 and '.pdf%23' not in source
assert source.count('class="qa-answer"')==23
for poem in poems:
 title=poem.split(' — ')[0]
 assert any(title in x['prompt'] for x in items[:15]),title
print('PASS: all 15 poems; 15 single-poem and 8 comparison answers; 23 correct PDF-page links')
