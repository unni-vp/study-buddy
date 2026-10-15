"""Generate readable Geography maps from each topic's maintained definitions."""
from pathlib import Path
import json,sys,subprocess
from html import escape
from biology_readable_mindmaps import build_map,text
ROOT=Path(__file__).resolve().parents[1]

def build(n):
 topic=next((ROOT/'Geography - OCR A').glob(f'{n:02d} - *'));items=json.loads((topic/'mindmap-content.json').read_text(encoding='utf-8'));folder=topic/'Mind Maps';folder.mkdir(exist_ok=True);paths=[];records=[]
 for item in items:
  svg,record=build_map(item['title'],item['slug'],item['panels'],columns=item.get('columns'),apply_biology_visuals=False);target=folder/(item['slug']+'.svg');target.write_text(svg,encoding='utf-8');paths.append(str(target));record.update(slug=item['slug'],title=item['title']);records.append(record)
  blocks=['# '+item['title']]
  for p in item['panels']:
   blocks.append('## '+p['title'])
   for g in p['groups']:
    if g.get('heading'):blocks.append('### '+g['heading'])
    blocks.extend('- '+line for line in g['lines'])
  target.with_suffix('.md').write_text('\n\n'.join(blocks)+'\n',encoding='utf-8')
 node=Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe';subprocess.run([str(node),str(ROOT/'scripts/render_mindmap_previews.cjs'),*paths],cwd=ROOT,check=True)
 (topic/'mindmap-layout-review.json').write_text(json.dumps(dict(reviewed='2026-10-15',generator='scripts/build_geography_maps.py',style='Content-sized panels, fixed readable fonts, black explanations, consistent coloured headings, inset dividers and no decorative hub',print=dict(width_mm=277,orientation='A4 landscape',body_pt=11.21),maps=records),ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print('Built',len(items),'Geography maps')
if __name__=='__main__':build(int(sys.argv[1]))
