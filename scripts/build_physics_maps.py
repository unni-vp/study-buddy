"""Build one Physics topic at fixed A4-readable typography."""
from physics_helpers import ROOT,SUBJECT,TOPICS
from physics_maps import MAPS
from pathlib import Path
import a4_mindmaps as a4
import subprocess,sys,json
from physics_map_figures import draw
base=a4.illustration

def illustration(kind,w,h):
 custom=draw(kind,w,h)
 if custom is not None:return custom
 if kind=='energy-share':
  b=f'<rect x="10" y="8" width="{w-20}" height="24" fill="#eee"/><rect x="10" y="8" width="{(w-20)*.6}" height="24" fill="#18837b"/><rect x="{10+(w-20)*.6}" y="8" width="{(w-20)*.4}" height="24" fill="#d39964"/>'
  return b+a4.text(w/2,57,'60 J useful + 40 J dissipated',15,anchor='middle',cls='diagram-label')
 if kind=='field-positive':
  x=w/2;y=34
  b=f'<circle cx="{x}" cy="{y}" r="15" fill="#fbe2cd" stroke="#b46d29"/>'+a4.text(x,y+6,'+',20,anchor='middle',cls='diagram-label')
  for sign in [-1,1]:
   start=x+sign*20;end=x+sign*85
   b+=f'<path d="M{start} {y}H{end}m{-sign*7} -5 {sign*7} 5 {-sign*7} 5" stroke="#2166ad" fill="none" stroke-width="2"/>'
  return b+a4.text(w/2,72,'Positive sphere: field points out',15,anchor='middle',cls='diagram-label')
 return base(kind,w,h)
a4.illustration=illustration

def build(n):
 topic=ROOT/SUBJECT/TOPICS[n-1];f=topic/'Mind Maps';f.mkdir(exist_ok=True);paths=[]
 for item in MAPS[n]:
  key=f'physics-{n}-'+item['slug'];a4.COMPACT[key]=item['panels'];a4.PLANS[key]=([[0,1],[2,3],[4,5]],item['labels'],item['pics'])
  out=f/(item['slug']+'.svg');out.write_text(a4.build_a4(dict(item,slug=key)),encoding='utf-8');paths.append(str(out))
  out.with_suffix('.md').write_text('# '+item['title']+'\n\n'+'\n\n'.join('## '+p['title']+'\n\n'+'\n'.join('- '+x for x in p['lines']) for p in item['panels'])+'\n',encoding='utf-8')
 node=Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe'
 subprocess.run([str(node),str(ROOT/'scripts/render_mindmap_previews.cjs'),*paths],cwd=ROOT,check=True)
 p=topic/'resource-coverage.json';d=json.loads(p.read_text());d['mindmaps']=[x['slug'] for x in MAPS[n]];p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
if __name__=='__main__':build(int(sys.argv[1]))
