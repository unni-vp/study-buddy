"""Shared numbered blue-panel/yellow-centre mind-map layout."""
from html import escape
from PIL import ImageFont
from mindmap_figures import figure
import re

BOLD='C:/Windows/Fonts/segoeuib.ttf'
BLUE='#0754a2'
INK='#102c50'
W=2400


def numbered_map(m, wrap, rich):
    cw=754
    ch=820 if m['slug'].startswith('00-') else 700
    middle=ch+70;bottom=2*ch+120;height=3*ch+140
    cy=middle+ch/2+20;ry=ch/2-55
    positions=[(20,20),(823,20),(1626,20),(20,middle),(1626,middle),
               (20,bottom),(823,bottom),(1626,bottom)]
    desc=' '.join(p['title']+': '+' '.join(p['lines']).replace('**','') for p in m['panels'])
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height}" viewBox="0 0 {W} {height}" role="img" aria-labelledby="title description"><title id="title">{escape(m["title"])} mind map</title><desc id="description">{escape(desc)}</desc><rect width="2400" height="{height}" fill="#fffefa"/><g font-family="Segoe UI, Arial, sans-serif" fill="{INK}">']
    # Curves are behind panels: each is visibly connected to the central theme.
    paths=[f'M990 {cy-220} C820 {middle+80} 760 {ch+30} 630 {ch-60}',
           f'M1200 {cy-ry} C1170 {middle-10} 1200 {middle-20} 1200 {ch}',
           f'M1410 {cy-220} C1580 {middle+80} 1660 {ch+30} 1770 {ch-60}',
           f'M880 {cy-20} C830 {cy-80} 795 {cy-40} 730 {cy-20}',
           f'M1520 {cy-20} C1570 {cy-80} 1605 {cy-40} 1670 {cy-20}',
           f'M990 {cy+190} C820 {bottom-60} 720 {bottom} 600 {bottom+60}',
           f'M1200 {cy+ry} C1240 {bottom-60} 1200 {bottom} 1200 {bottom+60}',
           f'M1410 {cy+190} C1580 {bottom-60} 1700 {bottom} 1800 {bottom+60}']
    svg.extend(f'<path d="{d}" fill="none" stroke="{BLUE}" stroke-width="8" stroke-linecap="round"/>' for d in paths)
    # The circle and large title give the eye one clear starting point.
    svg.append(f'<ellipse cx="1200" cy="{cy}" rx="400" ry="{ry}" fill="#fff0a3" stroke="{BLUE}" stroke-width="9"/>')
    svg.append(f'<svg x="947" y="{cy-ry+55}" width="506" height="140" viewBox="0 0 600 205">{figure(m["cue"])}</svg>')
    title=m.get('centre_title',m['title'])
    size=82 if title=='Cell biology' else 72
    rows=wrap(title,620,size)
    if len(rows)>2:size=62;rows=wrap(title,620,size)
    y=cy-ry+55+140+size+20
    for row in rows:
        line=' '.join(w for w,_,_ in row)
        svg.append(f'<text x="1200" y="{y}" text-anchor="middle" font-size="{size}" font-weight="800">{escape(line)}</text>');y+=size+12
    y=max(y+28,cy+130)
    for row in wrap(m['subtitle'],660,32):
        line=' '.join(w for w,_,_ in row)
        svg.append(f'<text x="1200" y="{y}" text-anchor="middle" font-size="32">{escape(line)}</text>');y+=42
    for n,(p,(x,y)) in enumerate(zip(m['panels'],positions),1):
        svg.append(f'<rect x="{x}" y="{y+17}" width="{cw}" height="{ch-17}" rx="50" fill="white" stroke="{BLUE}" stroke-width="6"/>')
        svg.append(f'<rect x="{x+30}" y="{y}" width="{cw-40}" height="85" rx="42" fill="{BLUE}"/>')
        svg.append(f'<circle cx="{x+63}" cy="{y+42}" r="40" fill="#ffe366" stroke="{BLUE}" stroke-width="5"/><text x="{x+63}" y="{y+56}" text-anchor="middle" font-size="44" font-weight="800">{n}</text>')
        heading=re.sub(r'^\d+\.\s*','',p['title']).capitalize()
        heading=re.sub(r'\bdna\b','DNA',heading)
        hs=36
        while ImageFont.truetype(BOLD,hs).getlength(heading)>cw-150:hs-=1
        svg.append(f'<text x="{x+117}" y="{y+55}" font-size="{hs}" font-weight="700" fill="white">{escape(heading)}</text>')
        start=y+125
        # Illustrations sit beneath the related explanation, like the reference.
        icon_h=155 if p['cue'] else 0
        end=y+ch-icon_h-18
        size=30
        while True:
            groups=[wrap(line,cw-80,size) for line in p['lines']]
            needed=sum(len(rows)*(size+10)+10 for rows in groups)
            if start+needed<=end:break
            size-=1
            if size<24:raise ValueError('Crowded panel: '+m['slug']+' / '+p['title'])
        for rows in groups:
            svg.append(f'<circle cx="{x+29}" cy="{start-9}" r="4.5" fill="{BLUE}"/>')
            out,start=rich(x+45,start,rows,size);svg.append(out);start+=10
        if p['cue']:
            svg.append(f'<svg x="{x+42}" y="{y+ch-icon_h-8}" width="{cw-84}" height="{icon_h}" viewBox="0 0 600 205">{figure(p["cue"])}</svg>')
    svg.append('</g></svg>')
    return ''.join(svg)
