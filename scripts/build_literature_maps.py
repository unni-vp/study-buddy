"""Build Literature maps with the established readable A4 layout."""
from literature_helpers import ROOT,SUBJECT,TOPICS
from literature_maps import MAPS
from pathlib import Path
import a4_mindmaps as a4
import literature_map_figures
import subprocess,json,sys

def build(n):
 topic=ROOT/SUBJECT/TOPICS[n-1];folder=topic/'Mind Maps';folder.mkdir(exist_ok=True);paths=[]
 for item in MAPS[n]:
  key='literature-'+str(n)+'-'+item['slug'];a4.COMPACT[key]=item['panels'];a4.PLANS[key]=([[0,1],[2,3],[4,5]],item['labels'],item['pics'])
  path=folder/(item['slug']+'.svg');path.write_text(a4.build_a4(dict(item,slug=key)),encoding='utf-8');paths.append(str(path))
  path.with_suffix('.md').write_text('# '+item['title']+'\n\n'+'\n\n'.join('## '+p['title']+'\n\n'+'\n'.join('- '+x for x in p['lines']) for p in item['panels'])+'\n',encoding='utf-8')
 node=Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe'
 subprocess.run([str(node),str(ROOT/'scripts/render_mindmap_previews.cjs'),*paths],cwd=ROOT,check=True)
 p=topic/'resource-coverage.json';d=json.loads(p.read_text());d['mindmaps']=[x['slug'] for x in MAPS[n]];p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
if __name__=='__main__':build(int(sys.argv[1]))
