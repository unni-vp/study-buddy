"""Generate current category only; full reading-site build remains separate."""
from pathlib import Path
import subprocess,sys
from biology_course_maps import MAPS
from biology_readable_mindmaps import build_map,review
from biology_readable_course_content import course_panels
ROOT=Path(__file__).resolve().parents[1]
def build(topic):
 folder=ROOT/'Biology - AQA'/topic/'Mind Maps';folder.mkdir(exist_ok=True);files=[];records=[]
 for item in MAPS[topic]:
  artwork,record=build_map(item['title'],item['slug'],course_panels(topic,item))
  records.append(dict(slug=item['slug'],**record))
  path=folder/(item['slug']+'.svg');path.write_text(artwork,encoding='utf-8');files.append(str(path))
  path.with_suffix('.md').write_text('# '+item['title']+'\n\n'+'\n\n'.join('## '+p['title']+'\n\n'+'\n'.join('- '+x for x in p['lines']) for p in item['panels'])+'\n',encoding='utf-8')
 review(topic,records)
 node=Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe'
 subprocess.run([str(node),str(ROOT/'scripts/render_mindmap_previews.cjs'),*files],cwd=ROOT,check=True)
if __name__=='__main__':build(sys.argv[1])
