from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import html, re, textwrap, json

ROOT=Path(__file__).resolve().parents[1]
SITE_TITLE=html.escape(json.loads((ROOT/'project-config.json').read_text(encoding='utf-8'))['site_title'])
TOPIC=ROOT/'Biology - AQA'/'01 - Cell biology'
MAPS=TOPIC/'Mind Maps'
fontpath=Path('C:/Windows/Fonts')
def font(size,bold=False):
 return ImageFont.truetype(str(fontpath/('segoeuib.ttf' if bold else 'segoeui.ttf')),size)

from cell_biology_mindmaps import MAPS as maps, build_maps
from reviewed_cell_diagrams import build_note_diagrams
paths=build_maps()
build_note_diagrams()

from html_utils import render_md
from mindmap_navigation import card as mindmap_card, CSS as mindmap_css

css='''body{font-family:Segoe UI,Arial,sans-serif;color:#20334a;background:#f4f7fb;margin:0;line-height:1.65}main{max-width:950px;margin:auto;background:white;padding:45px 55px}h1{font-size:44px;color:#142d4e;margin:0}h2{color:#2458a6;border-bottom:2px solid #dce5f0;padding-bottom:8px;margin-top:45px}h3{color:#197262;margin-top:26px}strong{color:#142d4e}table{border-collapse:collapse;width:100%;font-size:15px;margin:18px 0}th,td{text-align:left;padding:12px;border-bottom:1px solid #dce5f0;vertical-align:top}th{background:#eaf0f8}li{margin:7px 0}img{width:100%;height:auto}a{color:#2458a6}nav{margin:20px 0;padding:15px;background:#eaf0f8}figure{margin:30px 0}figcaption{font-weight:bold} @media(max-width:650px){main{padding:22px}h1{font-size:34px}table{font-size:13px}td,th{padding:6px}}@media print{body{background:white}main{max-width:none;padding:0}h2,h3{break-after:avoid}tr,figure{break-inside:avoid}nav{display:none}a{color:inherit}}'''
source=TOPIC/'Revision Notes'/'Cell Biology - Revision Notes.md'
body=render_md(source.read_text(encoding='utf-8'))
page=f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Cell biology revision notes · {SITE_TITLE}</title><style>{css}</style></head><body><main>{body}</main></body></html>'
(source.with_suffix('.html')).write_text(page,encoding='utf-8')
map_index='Cell Biology - Mind Maps.html'
gallery='<h1>Cell biology mind maps</h1><div class="mindmap-grid">'+''.join(mindmap_card(p.stem+'.html',m[1],p.name) for m,p in zip(maps,paths))+'</div>'
(MAPS/map_index).write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Cell biology mind maps · {SITE_TITLE}</title><style>{css}{mindmap_css}</style></head><body><main>{gallery}</main></body></html>',encoding='utf-8')
for m,p in zip(maps,paths):
 title=html.escape(m[1])
 content=f'<nav><a href="Cell%20Biology%20-%20Mind%20Maps.html">← Back to mind maps</a></nav><h1>{title}</h1><figure class="mindmap-view"><img src="{p.name}" alt="{title} mind map"></figure>'
 (MAPS/(p.stem+'.html')).write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} mind map · {SITE_TITLE}</title><style>{css}{mindmap_css}</style></head><body><main>{content}</main></body></html>',encoding='utf-8')
p=TOPIC/'README.md'; t=p.read_text(encoding='utf-8').replace('Resources have not yet been authored. Follow the project AGENTS.md and RESOURCE_GUIDELINES.md.','## Available resources\n\n- [Printable revision notes with mind maps](Revision%20Notes/Cell%20Biology%20-%20Revision%20Notes.html)\n- [Editable revision notes](Revision%20Notes/Cell%20Biology%20-%20Revision%20Notes.md)\n- [Focused visual mind maps](Mind%20Maps/Cell%20Biology%20-%20Mind%20Maps.html)\n\nCovers 4.1.1.1–4.1.3.3 and required practicals 1–3.');p.write_text(t,encoding='utf-8')
print('Created printable HTML notes, editable Markdown notes and four grouped branching mind maps.')
