"""Build only one Chemistry topic's maps using the shared A4 typography/layout."""
from chemistry_helpers import ROOT,SUBJECT,TOPICS
from chemistry_maps import MAPS
import a4_mindmaps as a4
import subprocess,sys,json
base_illustration=a4.illustration
def illustration(kind,w,h):
 if kind=='chem-ion':
  return a4.text(w*.25,32,'Na',27,anchor='middle')+a4.text(w*.75,32,'Na⁺',27,anchor='middle')+a4.text(w*.25,65,'11 electrons',15,anchor='middle',cls='diagram-label')+a4.text(w*.75,65,'10 electrons',15,anchor='middle',cls='diagram-label')+f'<path d="M{w*.4} 27H{w*.6}m-5-4 5 4-5 4" stroke="#2166ad" fill="none"/>'+a4.text(w/2,90,'Loses one electron',15,anchor='middle',cls='diagram-label')
 return base_illustration(kind,w,h)
a4.illustration=illustration
def build(n):
 p=ROOT/SUBJECT/TOPICS[n-1];f=p/'Mind Maps';f.mkdir(exist_ok=True);paths=[]
 for item in MAPS[n]:
  key='chem-'+str(n)+'-'+item['slug'];a4.COMPACT[key]=item['panels'];a4.PLANS[key]=([[0,1],[2,3],[4,5]],item['labels'],item['pics'])
  path=f/(item['slug']+'.svg');path.write_text(a4.build_a4(dict(item,slug=key)),encoding='utf-8');paths.append(str(path))
  path.with_suffix('.md').write_text('# '+item['title']+'\n\n'+'\n\n'.join('## '+p['title']+'\n\n'+'\n'.join('- '+x for x in p['lines']) for p in item['panels'])+'\n',encoding='utf-8')
 node=Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe'
 subprocess.run([str(node),str(ROOT/'scripts/render_mindmap_previews.cjs'),*paths],cwd=ROOT,check=True)
 d=json.loads((p/'resource-coverage.json').read_text());d['mindmaps']=[x['slug'] for x in MAPS[n]];(p/'resource-coverage.json').write_text(json.dumps(d,indent=2)+'\n')
from pathlib import Path
if __name__=='__main__':build(int(sys.argv[1]))
