"""Shared Chemistry authoring helpers; build only the requested category."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
SUBJECT='Chemistry - AQA'
TOPICS=['01 - Atomic structure and the periodic table','02 - Bonding structure and properties of matter','03 - Quantitative chemistry','04 - Chemical changes','05 - Energy changes']
def notes(n,title,body,groups,coverage,practicals=None):
 p=ROOT/SUBJECT/TOPICS[n-1];f=p/'Revision Notes';f.mkdir(exist_ok=True)
 name=title+' - Revision Notes.md';(f/name).write_text('# '+title+'\n\n'+body.strip()+'\n',encoding='utf-8')
 (p/'revision-layout.json').write_text(json.dumps({'source':name,'groups':[dict(id=i,title=t,description=d,icon=icon,sections=[{'heading':h} for h in hs]) for i,t,d,icon,hs in groups]},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 (p/'resource-coverage.json').write_text(json.dumps({'reviewed':'2026-10-05','specification':f'AQA 8462 4.{n}, version 1.2 January 2026','source':'../00 - Specification/AQA-8462-specification.pdf','coverage':coverage,'practicals':practicals or []},indent=2)+'\n',encoding='utf-8')
 print('Wrote',title,'notes')
