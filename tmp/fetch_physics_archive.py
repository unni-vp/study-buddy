from pathlib import Path
import urllib.request, concurrent.futures, json
import re,html
from pypdf import PdfReader
root=Path('Physics - AQA/00 - Past papers');jobs=[]
for paper in [1,2]:
 for year in ['22','23']:
  for kind in ['QP','MS']:
   jobs.append((paper,year,kind,f'https://pmt.physicsandmathstutor.com/download/Physics/GCSE/Past-Papers/AQA/Paper-{paper}H/{kind}/June%2020{year}%20{kind}.PDF'))
def fetch(item):
 paper,year,kind,url=item
 url=url[:-3]+'pdf' if paper==2 and year=='23' and kind=='QP' else url
 p=root/f'Paper {paper} Higher'/f'AQA-8463{paper}H-{kind}-JUN{year}.PDF';p.parent.mkdir(exist_ok=True,parents=True)
 if not p.exists():p.write_bytes(urllib.request.urlopen(url,timeout=60).read())
 r=PdfReader(p);p.with_suffix('.txt').write_text('\n\n'.join(f'=== PDF page {i+1} ===\n'+page.extract_text() for i,page in enumerate(r.pages)),encoding='utf-8')
 return p.name
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 for result in pool.map(fetch,jobs):print(result)
(root/'download-sources.json').write_text(json.dumps(jobs,indent=2)+'\n')
assert len(jobs)==8,len(jobs)

