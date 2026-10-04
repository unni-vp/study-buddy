"""Build panel-style revision maps as sharp SVGs plus PNG thumbnail exports."""
from pathlib import Path
from html import escape
import re, subprocess, shutil
from PIL import ImageFont
from cell_biology_map_content import MAP_CONTENT
from cell_biology_visuals import BASE

MAPS=[(m['slug'],m['title'],m['cue'],m['panels']) for m in MAP_CONTENT]
FONT='C:/Windows/Fonts/segoeui.ttf'
BOLD='C:/Windows/Fonts/segoeuib.ttf'

def tokens(line):
    result=[]
    for i,part in enumerate(re.split(r'\*\*(.*?)\*\*',line)):
        for word in part.split():
            # Keep punctuation attached when a bold span ends a sentence.
            if result and re.fullmatch(r'[.,:;!?)]+' ,word):
                previous,bold=result[-1];result[-1]=(previous+word,bold)
            else:result.append((word,i%2==1))
    return result

def lines_for(text,width,size):
    fonts={False:ImageFont.truetype(FONT,size),True:ImageFont.truetype(BOLD,size)}
    lines=[];row=[];used=0
    for word,bold in tokens(text):
        w=fonts[bold].getlength(word+' ')
        if row and used+w>width:lines.append(row);row=[];used=0
        row.append((word,bold,w));used+=w
    if row:lines.append(row)
    return lines

def rich(x,y,rows,size):
    result=[]
    for row in rows:
        xx=x
        for word,bold,width in row:
            if bold:result.append(f'<rect x="{xx-2:.1f}" y="{y-size+5}" width="{width:.1f}" height="{size+6}" rx="5" fill="#c8eee1"/>')
            result.append(f'<text x="{xx:.1f}" y="{y}" font-size="{size}" font-weight="{700 if bold else 400}">{escape(word)}</text>')
            xx+=width
        y+=size+10
    return ''.join(result),y

def build_svg(m):
    from landscape_mindmaps import landscape_overview, landscape_detail
    if m['slug']=='00-cell-biology-overview':
        return landscape_overview(m, lines_for)
    return landscape_detail(m, lines_for)


def build_maps(slugs=None):
    root=BASE.parents[1];folder=BASE/'Mind Maps';folder.mkdir(exist_ok=True)
    paths=[]
    for m in MAP_CONTENT:
        if slugs is not None and m['slug'] not in slugs:continue
        p=folder/(m['slug']+'.svg');p.write_text(build_svg(m),encoding='utf-8')
        md='# '+m['title']+'\n\n'+'\n\n'.join('## '+q['title'].capitalize()+'\n\n'+'\n'.join('- '+line for line in q['lines']) for q in m['panels'])+'\n'
        (folder/(m['slug']+'.md')).write_text(md,encoding='utf-8');paths.append(p.with_suffix('.png'))
    node=shutil.which('node') or str(Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe')
    subprocess.run([node,str(root/'scripts/render_mindmap_previews.cjs'),*[str(p.with_suffix('.svg')) for p in paths]],cwd=root,check=True)
    return paths

if __name__=='__main__':
    build_maps()
