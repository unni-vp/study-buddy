"""Build only one Chemistry topic's maps using the shared A4 typography/layout."""
from chemistry_helpers import ROOT,SUBJECT,TOPICS
from chemistry_maps import MAPS
import a4_mindmaps as a4
import subprocess,sys,json
base_illustration=a4.illustration
def illustration(kind,w,h):
 if kind=='chem-electrodes':
  out=a4.text(32,22,'−',24,anchor='middle')+a4.text(w-32,22,'+',24,anchor='middle')
  out+=a4.text(32,70,'Cathode',15,anchor='middle',cls='diagram-label')+a4.text(w-32,70,'Anode',15,anchor='middle',cls='diagram-label')
  for x,label,end in [(w*.38,'+',57),(w*.62,'−',w-57)]:
   out+=f'<circle cx="{x}" cy="35" r="12" fill="#dceafa" stroke="#2166ad"/>'+a4.text(x,40,label,16,anchor='middle',cls='diagram-label')
   start=x-15 if label=='+' else x+15;d=5 if label=='+' else -5
   out+=f'<path d="M{start} 35H{end}m{d} -4 {-d} 4 {d} 4" stroke="#2166ad" fill="none"/>'
  return out
 if kind in ('chem-route','chem-titration'):
  out=''
  for j,label in enumerate(['c × V' if kind=='chem-titration' else 'mass','moles','ratio']):
   x=10+j*(w-20)/3;bw=(w-35)/3
   out+=f'<rect x="{x}" y="10" width="{bw}" height="32" rx="6" fill="#e2eefb" stroke="#2166ad"/>'+a4.text(x+bw/2,31,label,15,anchor='middle',cls='diagram-label')
  return out+a4.text(w/2,70,'Convert → compare → convert back',15,anchor='middle',cls='diagram-label')
 if kind=='chem-layers':
  out=''
  for row in range(3):
   y=12+row*24
   out+=f'<path d="M25 {y}H{w-25}" stroke="#18837b" stroke-width="3"/>'
   for col in range(6):out+=f'<circle cx="{w/2+(col-2.5)*30}" cy="{y}" r="6" fill="#c5e6df" stroke="#18837b"/>'
  return out+a4.text(w/2,89,'Layers can slide past each other',15,anchor='middle',cls='diagram-label')
 if kind=='chem-lattice':
  out=''
  for row in range(2):
   for col in range(6):
    x=w/2+(col-2.5)*32;y=17+row*32;positive=(row+col)%2==0
    out+=f'<circle cx="{x}" cy="{y}" r="13" fill="{"#dceafa" if positive else "#ffe4ce"}" stroke="#52758b"/>'+a4.text(x,y+5,'+' if positive else '−',16,anchor='middle',cls='diagram-label')
  return out+a4.text(w/2,84,'Opposite ions; 2D slice of lattice',15,anchor='middle',cls='diagram-label')
 if kind=='chem-pairs':
  out=a4.text(w/2-53,32,'H',26,anchor='middle')+a4.text(w/2+53,32,'H',26,anchor='middle')
  out+=f'<circle cx="{w/2-8}" cy="23" r="4" fill="#2166ad"/><path d="M{w/2+4} 19l8 8m0-8-8 8" stroke="#b96120" stroke-width="2"/>'
  return out+a4.text(w/2,66,'One shared pair → one bond',15,anchor='middle',cls='diagram-label')
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
