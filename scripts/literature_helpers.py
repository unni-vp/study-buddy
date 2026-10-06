"""Author Literature resources with shared subject navigation and internal coverage."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
SUBJECT='English Literature - Eduqas'
TOPICS=['01 - Macbeth','02 - Poetry anthology - assessment from 2027']
def notes(n,title,body,groups,coverage):
 p=ROOT/SUBJECT/TOPICS[n-1];f=p/'Revision Notes';f.mkdir(parents=True,exist_ok=True)
 name=title+' - Revision Notes.md';(f/name).write_text('# '+title+'\n\n'+body.strip()+'\n',encoding='utf-8')
 (p/'revision-layout.json').write_text(json.dumps({'source':name,'groups':[dict(id=i,title=t,description=d,icon=icon,sections=[{'heading':h} for h in hs]) for i,t,d,icon,hs in groups]},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 metadata_path=p/'resource-coverage.json'
 metadata=json.loads(metadata_path.read_text(encoding='utf-8')) if metadata_path.exists() else {}
 metadata.update({'reviewed':'2026-10-06','specification':'Eduqas C720QS v4 August 2024, assessment 2027','coverage':coverage,'sources':['https://www.eduqas.co.uk/media/42ldm0wa/eduqas-gcse-english-literature-spec-from-2015.pdf']})
 metadata_path.write_text(json.dumps(metadata,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 print('Wrote',title,'notes')
