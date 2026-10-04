"""Standalone map pages use the same modal as the main offline website."""
from pathlib import Path
from urllib.parse import quote
from html import escape
import os, json
from cell_biology_map_content import MAP_CONTENT
from cell_biology_visuals import BASE
from mindmap_navigation import card
from mindmap_viewer import viewer_markup
from html_utils import render_md

def link(page,target):return quote(os.path.relpath(target,page.parent).replace('\\','/'),safe='/')
def build_standalone_pages(paths=None):
    root=BASE.parents[1];folder=BASE/'Mind Maps';index=folder/'Cell Biology - Mind Maps.html'
    site_title=json.loads((root/'project-config.json').read_text(encoding='utf-8'))['site_title']
    catalog=[{'title':m['title'],'image':folder/(m['slug']+'.svg'),'thumbnail':folder/(m['slug']+'.png'),'page':folder/(m['slug']+'.html')} for m in MAP_CONTENT]
    def write(page,title,body):
        styles=''.join(f'<link rel="stylesheet" href="{link(page,root/"library"/name)}">' for name in ['style.css','mindmaps.css'])
        script=f'<script defer src="{link(page,root/"library/mindmaps.js")}"></script>'
        page.write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+escape(title)+" · "+escape(site_title)+"</title>"+styles+script+'</head><body><main style="max-width:1200px;margin:auto">'+body+'</main>'+viewer_markup(page,catalog,link)+'</body></html>',encoding='utf-8')
    cards=''.join(card(link(index,m['page']),m['title'],link(index,m['thumbnail']),i) for i,m in enumerate(catalog))
    write(index,'Cell biology mind maps','<h1>Cell biology mind maps</h1><div class="mindmap-grid">'+cards+'</div>')
    for i,m in enumerate(catalog):
        page=m['page'];title=escape(m['title'])
        text=render_md(m['image'].with_suffix('.md').read_text(encoding='utf-8'))
        body=f'<div class="reader-tools"><a href="{link(page,index)}">← Back to mind maps</a></div><h1>{title}</h1><button type="button" class="mindmap-open" data-mindmap-index="{i}">Open full screen</button><figure class="mindmap-view"><img src="{link(page,m["image"])}" alt="{title} revision map"></figure><details class="mindmap-text" id="text-version"><summary>Text version</summary><article class="reading">{text}</article></details>'
        write(page,m['title']+' mind map',body)
if __name__=='__main__':build_standalone_pages()
