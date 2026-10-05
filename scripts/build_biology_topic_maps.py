"""Generate current category only; full reading-site build remains separate."""
from pathlib import Path
import subprocess,sys
from biology_course_maps import MAPS
from a4_mindmaps import COMPACT,PLANS,build_a4
ROOT=Path(__file__).resolve().parents[1]
def build(topic):
 folder=ROOT/'Biology - AQA'/topic/'Mind Maps';folder.mkdir(exist_ok=True);files=[]
 for item in MAPS[topic]:
  key=topic[:2]+'-'+item['slug'];data=dict(item,slug=key)
  COMPACT[key]=item['panels'];PLANS[key]=([[0,1],[2,3],[4,5]],item['labels'],item['pics'])
  path=folder/(item['slug']+'.svg');path.write_text(build_a4(data),encoding='utf-8');files.append(str(path))
  path.with_suffix('.md').write_text('# '+item['title']+'\n\n'+'\n\n'.join('## '+p['title']+'\n\n'+'\n'.join('- '+x for x in p['lines']) for p in item['panels'])+'\n',encoding='utf-8')
 node=Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe'
 subprocess.run([str(node),str(ROOT/'scripts/render_mindmap_previews.cjs'),*files],cwd=ROOT,check=True)
if __name__=='__main__':build(sys.argv[1])
