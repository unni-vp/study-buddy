"""Generate readable English Language maps from each topic's maintained definitions."""
from pathlib import Path
import json,sys,subprocess
from html import escape
from biology_readable_mindmaps import build_map,text
ROOT=Path(__file__).resolve().parents[1]
PURPOSES={'focus-shift':'Shows the selected practice passage moving from isolation through interruption to connection.','story-change':'Shows an event changing the character, rather than merely adding more incidents.','compare-views':'Links a shared issue to separate evidence and a meaningful comparison.','spoken-response':'Shows how a listening response develops from acknowledging the question to a justified answer.'}
ROUTES={'focus-shift':['Opening: isolation','Turning point: arrival','Ending: connection'],'story-change':['Starting belief','Choice under pressure','Changed understanding'],'compare-views':['Shared issue','Evidence from each text','Similarity or difference'],'spoken-response':['Listen to the question','Answer with a reason','Develop or qualify']}
def drawing(kind,width):
 out=[]
 for i,label in enumerate(ROUTES[kind]):
  y=i*48;out.append(f'<rect x="1" y="{y}" width="{width-2}" height="30" rx="5" fill="#f3f6fb" stroke="#77879a"/>');out.append(text(width/2,y+21,label,16,anchor='middle',cls='diagram-label'))
  if i<2:out.append(f'<path d="M{width/2} {y+33}v11m-4-4 4 4 4-4" stroke="#526e83" fill="none" stroke-width="1.5"/>')
 return '<g class="concept-illustration">'+''.join(out)+'</g>',130
def build(n):
 topic=next((ROOT/'English Language - Eduqas').glob(f'{n:02d} - *'));items=json.loads((topic/'mindmap-content.json').read_text(encoding='utf-8'));folder=topic/'Mind Maps';folder.mkdir(exist_ok=True);paths=[];records=[]
 for item in items:
  svg,record=build_map(item['title'],item['slug'],item['panels'],columns=item.get('columns'),drawing_provider=drawing,purpose_provider=PURPOSES,apply_biology_visuals=False);target=folder/(item['slug']+'.svg');target.write_text(svg,encoding='utf-8');paths.append(str(target));record.update(slug=item['slug'],title=item['title']);records.append(record)
  blocks=['# '+item['title']]
  for p in item['panels']:
   blocks.append('## '+p['title'])
   for g in p['groups']:
    if g.get('heading'):blocks.append('### '+g['heading'])
    blocks.extend('- '+line for line in g['lines'])
   if p.get('visual'):blocks.append(PURPOSES[p['visual']['kind']])
  target.with_suffix('.md').write_text('\n\n'.join(blocks)+'\n',encoding='utf-8')
 node=Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe';subprocess.run([str(node),str(ROOT/'scripts/render_mindmap_previews.cjs'),*paths],cwd=ROOT,check=True)
 (topic/'mindmap-layout-review.json').write_text(json.dumps(dict(reviewed='2026-10-14',generator='scripts/build_english_language_maps.py',style='Content-sized panels, fixed readable fonts, black explanations, consistent coloured headings, inset dividers and no decorative hub',print=dict(width_mm=277,orientation='A4 landscape',body_pt=11.21),maps=records),ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print('Built',len(items),'English Language maps')
if __name__=='__main__':build(int(sys.argv[1]))
