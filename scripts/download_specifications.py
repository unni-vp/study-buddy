from pathlib import Path
import urllib.request, concurrent.futures, hashlib, json
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
docs=[
('Computer Science - AQA','AQA-8525-specification-2027','https://www.aqa.org.uk/filestore/resource/updated-gcse-computer-science-spec.pdf'),
('English Language - Eduqas','Eduqas-C700QS-specification','https://www.eduqas.co.uk/media/10ea1en0/eduqas-gcse-english-language-from-2015-e.pdf'),
('English Literature - Eduqas','Eduqas-C720QS-specification','https://www.eduqas.co.uk/media/42ldm0wa/eduqas-gcse-english-literature-spec-from-2015.pdf'),
('English Literature - Eduqas','Eduqas-poetry-anthology-first-assessment-2027','https://www.eduqas.co.uk/media/szolurrz/new-poetry-anthology-for-first-examination-in-2027.pdf'),
('Maths - Edexcel','Edexcel-1MA1-specification','https://qualifications.pearson.com/content/dam/pdf/GCSE/mathematics/2015/specification-and-sample-assesment/gcse-maths-2015-specification.pdf'),
('Geography - OCR A','OCR-J383-specification','https://www.ocr.org.uk/Images/207306-specification-accredited-gcse-geography-a-j383.pdf'),
('French - AQA','AQA-8652-specification','https://cdn.sanity.io/files/p28bar15/green/5f30011c5678f09ec900e9ad0cd2db2a826d5f88.pdf'),
('Biology - AQA','AQA-8461-specification','https://cdn.sanity.io/files/p28bar15/green/510eb7c76df13be23292df4392de95eb32b0d30f.pdf'),
('Chemistry - AQA','AQA-8462-specification','https://cdn.sanity.io/files/p28bar15/green/4b1d5e819ad08a3b6d2ee6d8ed3514487c2255b4.pdf'),
('Physics - AQA','AQA-8463-specification','https://cdn.sanity.io/files/p28bar15/green/e96b2cef624c0970b0f90d9678a438580aed0f65.pdf')]
def download(doc):
 subject,name,url=doc
 folder=ROOT/subject/'00 - Specification'
 folder.mkdir(parents=True,exist_ok=True)
 target=folder/(name+'.pdf')
 if not target.exists():
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
  data=urllib.request.urlopen(req,timeout=60).read()
  if not data.startswith(b'%PDF-'):raise ValueError('Not a PDF: '+url)
  target.write_bytes(data)
 reader=PdfReader(target)
 text='\n\n'.join(f'=== PDF page {i+1} ===\n'+(page.extract_text() or '') for i,page in enumerate(reader.pages))
 target.with_suffix('.txt').write_text(text,encoding='utf-8')
 entry={'subject':subject,'file':str(target.relative_to(ROOT)),'url':url,'downloaded_on':'2026-10-04','bytes':target.stat().st_size,'pages':len(reader.pages),'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'cover_text':text[:1800]}
 print(f'{subject}: {len(reader.pages)} pages, {target.stat().st_size} bytes',flush=True)
 return entry
results=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
 futures={ex.submit(download,d):d for d in docs}
 for future in concurrent.futures.as_completed(futures):
  try:results.append(future.result())
  except Exception as e:print('FAILED',futures[future],repr(e),flush=True)
(ROOT/'specification-manifest.json').write_text(json.dumps(sorted(results,key=lambda d:d['subject']),indent=2),encoding='utf-8')
if len(results)!=len(docs):raise SystemExit('Some downloads failed')
