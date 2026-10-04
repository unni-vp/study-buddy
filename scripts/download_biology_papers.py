"""Preserve the publicly released AQA papers used for the Cell biology audit."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib
import json
import urllib.request
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'Biology - AQA' / '00 - Past papers' / 'Paper 1 Higher'
SOURCES = {
    2018: ('https://pmt.physicsandmathstutor.com/download/Biology/GCSE/Past-Papers/AQA/Paper-1H/QP/June%202018%20QP.pdf', 'https://pmt.physicsandmathstutor.com/download/Biology/GCSE/Past-Papers/AQA/Paper-1H/MS/June%202018%20MS.pdf'),
    2019: ('https://pmt.physicsandmathstutor.com/download/Biology/GCSE/Past-Papers/AQA/Paper-1H/QP/June%202019%20QP.pdf', 'https://pmt.physicsandmathstutor.com/download/Biology/GCSE/Past-Papers/AQA/Paper-1H/MS/June%202019%20MS.pdf'),
    2022: ('https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-84611H-QP-JUN22.PDF', 'https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-84611H-MS-JUN22.PDF'),
    2023: ('https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2023/june/AQA-84611H-QP-JUN23.PDF', 'https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2023/june/AQA-84611H-MS-JUN23.PDF'),
    2024: ('https://cdn.sanity.io/files/p28bar15/green/45bce632101224bd077beea4b962c027353a7abc.pdf', 'https://cdn.sanity.io/files/p28bar15/green/8d711ebd0128dce40f21490bfc3ab7305e492fda.pdf'),
    2025: ('https://revisionscience.com/sites/default/files/revisionscience/documents/ABI253.PDF', 'https://revisionscience.com/sites/default/files/revisionscience/documents/ABI254.PDF'),
}

def preserve(item):
    year, kind, url = item
    name = f'AQA-84611H-{kind}-JUN{year % 100:02}.pdf'
    path = DEST / name
    if not path.exists():
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        data = urllib.request.urlopen(request, timeout=60).read()
        if not data.startswith(b'%PDF'): raise ValueError(f'Not a PDF: {url}')
        path.write_bytes(data)
    reader = PdfReader(path)
    raw = '\n\n'.join(f'=== PDF page {i+1} ===\n'+(p.extract_text() or '') for i,p in enumerate(reader.pages))
    path.with_suffix('.txt').write_text(raw, encoding='utf-8')
    if '8461' not in raw[:2000]: raise ValueError(f'Wrong qualification: {name}')
    print(f'{name}: {len(reader.pages)} pages', flush=True)
    return {'year': year, 'series': 'June', 'board': 'AQA', 'qualification': '8461', 'paper': '8461/1H', 'kind': kind, 'url': url, 'file': str(path.relative_to(ROOT)).replace('\\','/'), 'pages': len(reader.pages), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'checked': '2026-10-04'}

if __name__ == '__main__':
    DEST.mkdir(parents=True, exist_ok=True)
    items = [(y,k,u) for y,urls in SOURCES.items() for k,u in zip(('QP','MS'),urls)]
    with ThreadPoolExecutor(max_workers=4) as pool: records=list(pool.map(preserve,items))
    (DEST / 'source-manifest.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
