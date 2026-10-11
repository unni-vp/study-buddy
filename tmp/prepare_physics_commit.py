"""Prepare one already-reviewed Physics category for an isolated commit."""
from pathlib import Path
import sys,subprocess,json,hashlib
root=Path.cwd();sys.path.insert(0,str(root/'scripts'))
from physics_helpers import TOPICS,TITLES
n=int(sys.argv[1]);k=int(sys.argv[2]);kinds=['Revision Notes','Mind Maps','Questions and Answers'];topic=root/'Physics - AQA'/TOPICS[n-1]
assert not subprocess.check_output(['git','diff','--cached','--name-only']).strip(),'Index must be empty'
# Rebuild navigation using only categories included in this publication step.
build=root/'scripts/build_project_site.py';s=build.read_text(encoding='utf-8')
s=s.replace('def resources(folder,subject,topic,topicpage,kind):',f'''def resources(folder,subject,topic,topicpage,kind):
 if subject=='Physics - AQA' and int(folder.parent.name[:2])<=5:
  step=(int(folder.parent.name[:2])-1)*3+['Revision Notes','Mind Maps','Questions and Answers'].index(kind)
  if step>{(n-1)*3+k}:return []''')
exec(compile(s,str(build),'exec'),{'__file__':str(build),'__name__':'__main__'})
paths=[topic/kinds[k],topic/'index.html',root/'Physics - AQA/index.html',root/'index.html']
if k==0:
 paths += [topic/'revision-layout.json',topic/'resource-coverage.json',root/f'scripts/physics_{n:02d}_notes.py']
 paths += [p for p in (topic/'Diagrams').glob('*.svg') if not p.stem.endswith('-question')]
 if n==1:paths += [root/'scripts/physics_helpers.py',root/'scripts/physics_diagrams.py',root/'scripts/mindmap_navigation.py']
elif k==1:
 paths += [topic/'resource-coverage.json']
 if n==1:paths += [root/'scripts/physics_maps.py',root/'scripts/build_physics_maps.py',root/'scripts/physics_map_figures.py',root/'scripts/check_physics_modal.cjs']
else:
 paths += [topic/'qa-evidence.json',root/f'scripts/physics_{n:02d}_qa.py']
 paths += list((topic/'Diagrams').glob('*-question.svg'))
 if n==1:paths += [root/'Physics - AQA/00 - Past papers',root/'scripts/check_biology_qa.cjs']
 if n==5:paths += [root/'Physics - AQA/RESOURCE_REVIEW.md']
if k!=1:
 source=next((topic/kinds[k]).glob('*.md'));key=hashlib.sha1(str(source.relative_to(root)).encode()).hexdigest()[:12]
 paths+=list((root/'library/resources').glob(key+'*.html'))
else:
 import re
 prefix=re.sub(r'[^a-z0-9]+','-',('Physics - AQA-'+TITLES[n-1]).lower()).strip('-')
 paths+=list((root/'library/resources').glob(prefix+'-*.html'))
coverage=topic/'resource-coverage.json';original=coverage.read_bytes()
try:
 if k==0:
  d=json.loads(original);d.pop('mindmaps',None);coverage.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 subprocess.run(['git','add','--',*[str(p.relative_to(root)) for p in paths]],check=True)
finally:coverage.write_bytes(original)
print('Prepared',TITLES[n-1],kinds[k])
subprocess.run(['git','diff','--cached','--stat'],check=True)
