from urllib.request import urlopen
from pathlib import Path
from pypdf import PdfReader
Path('tmp/macbeth-folger.txt').write_bytes(urlopen('https://folger-main-site-assets.s3.amazonaws.com/uploads/2022/11/macbeth_TXT_FolgerShakespeare.txt').read())
root=Path('English Literature - Eduqas/00 - Past papers/Component 1')
for y in ['19','23','24']:
 print('YEAR',y,'QUESTION:')
 print(PdfReader(root/f'Eduqas-C720U10-1-QP-JUN{y}.pdf').pages[3].extract_text())
 r=PdfReader(root/f'Eduqas-C720U10-1-MS-JUN{y}.pdf')
 for i,p in enumerate(r.pages):
  t=p.extract_text()
  if ('Macbeth' in t and ('2 1' in t or '2 2' in t or '2.1' in t or '2.2' in t)):
   print('MS PAGE',i+1,t[:5000])
