from pathlib import Path
import urllib.request, concurrent.futures
from pypdf import PdfReader
root=Path('Physics - AQA/00 - Past papers')
def fetch(item):
 paper,year,kind=item
 name=f'AQA-8463{paper}H-{kind}-JUN{year}.PDF'
 section='exam-papers' if kind=='QP' else 'sample-papers-and-mark-schemes'
 url=f'https://filestore.aqa.org.uk/{section}/20{year}/june/{name}'
 p=root/f'Paper {paper} Higher'/name;p.parent.mkdir(parents=True,exist_ok=True)
 if not p.exists():
  with urllib.request.urlopen(url,timeout=60) as response:p.write_bytes(response.read())
 reader=PdfReader(p)
 p.with_suffix('.txt').write_text('\n\n'.join(f'=== PDF page {i+1} ===\n'+page.extract_text() for i,page in enumerate(reader.pages)),encoding='utf-8')
 return f'{name}: {len(reader.pages)} pages'
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 for result in pool.map(fetch,[(p,y,k) for p in [1,2] for y in ['22','23'] for k in ['QP','MS']]):print(result)


