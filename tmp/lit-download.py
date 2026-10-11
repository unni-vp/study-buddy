from pathlib import Path
from urllib.request import Request,urlopen
from urllib.parse import quote
from pypdf import PdfReader
import json,hashlib
root=Path('English Literature - Eduqas/00 - Past papers/Component 1');manifest=[]
for year in ['2019','2023','2024']:
 for typ in ['QP','MS']:
  name=f'June {year} {typ} - Component 1 Eduqas English Literature GCSE.pdf'
  url='https://pmt.physicsandmathstutor.com/download/English-Literature/GCSE/Past-Papers/WJEC-England/Component-1/'+quote(name)
  try:
   data=urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35).read()
   assert data.startswith(b'%PDF')
   p=root/f'Eduqas-C720U10-1-{typ}-JUN{year[-2:]}.pdf';p.write_bytes(data);r=PdfReader(p)
   p.with_suffix('.txt').write_text('\n\n'.join('\n'.join(l.rstrip() for l in page.extract_text().splitlines()) for page in r.pages)+'\n',encoding='utf-8')
   manifest.append({'file':p.name,'source':url,'publisher':'WJEC/Eduqas, public PMT mirror','pages':len(r.pages),'sha256':hashlib.sha256(data).hexdigest()});print(p.name,len(r.pages))
  except Exception as e:print('FAILED',name,str(e))
(root/'source-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
