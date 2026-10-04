"""Partition an editable Markdown resource without losing or duplicating content."""
from dataclasses import dataclass
from html import escape
import json
import re
from html_utils import render_md
from mindmap_navigation import icon

@dataclass
class Block:
    level: int
    heading: str
    body: str

def outline(raw):
    headings=list(re.finditer(r'^(#{1,6}) (.+)$',raw,re.M))
    if not headings or raw[:headings[0].start()].strip():
        raise ValueError('Revision source must begin with a heading; introductory content cannot be dropped')
    return [Block(len(m[1]),m[2],raw[m.end():headings[i+1].start() if i+1<len(headings) else len(raw)].strip()) for i,m in enumerate(headings)]

def descendants(blocks, start):
    end=start+1
    while end<len(blocks) and blocks[end].level>blocks[start].level:
        end+=1
    return list(range(start,end))

def partition(raw, layout):
    blocks=outline(raw)
    pages=layout['groups']+layout.get('extras',[])
    ids=[p['id'] for p in pages]
    if len(ids)!=len(set(ids)): raise ValueError('Duplicate revision page IDs')
    used={}
    contents={}
    for page in pages:
        chosen=[]
        levels={}
        for selector in page['sections']:
            matches=[i for i,b in enumerate(blocks) if b.heading==selector['heading']]
            if len(matches)!=1: raise ValueError(f'Heading must be unique: {selector["heading"]}')
            indices=[matches[0]] if selector.get('intro_only') else descendants(blocks,matches[0])
            excluded=set()
            for name in selector.get('exclude',[]):
                hits=[i for i in indices if blocks[i].heading==name]
                if len(hits)!=1: raise ValueError(f'Excluded heading must exist in selection: {name}')
                excluded.update(descendants(blocks,hits[0]))
            chosen.extend(i for i in indices if i not in excluded)
            levels.update({i:blocks[i].level-blocks[matches[0]].level+2 for i in indices})
        chunks=['# '+page['title']]
        for n,i in enumerate(chosen):
            if i in used: raise ValueError(f'Content duplicated in {used[i]} and {page["id"]}: {blocks[i].heading}')
            used[i]=page['id']
            b=blocks[i]
            # Group pages retain the section headings as part of the same document.
            if n or 'icon' in page: chunks.append('#'*levels[i]+' '+re.sub(r'^\d+\. ','',b.heading))
            chunks.append(b.body)
        contents[page['id']]='\n\n'.join(chunks)
    for i,b in enumerate(blocks):
        if i not in used and b.heading!='Sources' and not (b.level==1 and not b.body):
            raise ValueError('Unassigned revision content: '+b.heading)
    return contents

def grouped_card(href, group):
    return f'<a class="revision-group" href="{escape(href,quote=True)}">{icon(group["icon"])}<span><strong>{escape(group["title"])}</strong><small>{escape(group["description"])}</small></span><span class="map-arrow" aria-hidden="true">→</span></a>'

def build_revision_pages(source, layout_path, target, subject, topic, topicpage, write, link, slug):
    layout=json.loads(layout_path.read_text(encoding='utf-8'))
    raw=source.read_text(encoding='utf-8')
    contents=partition(raw,layout)
    prefix=target.stem
    subjectpage=source.parents[2]/'index.html'
    crumbs=[(subject.split(' - ')[0],subjectpage),(topic,topicpage),('Revision notes',target)]
    groups=layout['groups']
    is_qa=source.parent.name=='Questions and Answers'
    label='Questions & answers' if is_qa else 'Revision notes'
    back='All Q&A' if is_qa else 'All revision notes'
    print_label='Print all Q&A' if is_qa else 'Print all notes'
    crumbs[-1]=(label,target)
    ordered=groups
    pages=ordered+layout.get('extras',[])
    targets={p['id']:target.with_name(prefix+('-group-' if p in groups else '-')+p['id']+'.html') for p in pages}
    full=target.with_name(prefix+'-all.html')

    def render(page, md):
        content=render_md(md)
        def relocate(m):
            url=m[2]
            if re.match(r'^(https?:|#|mailto:)',url): return m[0]
            from urllib.parse import unquote
            return m[1]+'="'+link(page,(source.parent/unquote(url)).resolve())+'"'
        return re.sub(r'(href|src)="([^"]+)"',relocate,content)

    cards=''.join(grouped_card(link(target,targets[g['id']]),g) for g in groups)
    utilities=''.join(f'<a href="{link(target,targets[p["id"]])}">{escape(p["title"])}</a>' for p in layout.get('extras',[]))
    write(target,topic+' '+label.lower(),f'<div class="reader-tools"><a href="{link(target,topicpage)}">← Back to topic</a><a href="{link(target,full)}">{print_label}</a></div><h1>{escape(topic)}</h1><div class="revision-grid">{cards}</div><nav class="revision-utilities" aria-label="Resource tools">{utilities}</nav>',crumbs[:-1],subject)
    for i,g in enumerate(groups):
        page=targets[g['id']]
        step_links=[]
        for direction,other in [('← Previous',groups[i-1] if i else None),('Next →',groups[i+1] if i+1<len(groups) else None)]:
            if other: step_links.append(f'<a href="{link(page,targets[other["id"]])}"><span>{direction}</span><strong>{escape(other["title"])}</strong></a>')
            else: step_links.append('<span></span>')
        navigation='<nav class="section-navigation" aria-label="Section navigation">'+''.join(step_links)+'</nav>'
        related=[]
        for map_name in g.get('maps',[]):
            map_image=source.parent.parent/'Mind Maps'/(map_name+'.png')
            if map_image.exists():
                map_page=target.parent/(slug(subject+'-'+topic)+'-'+map_name+'.html')
                title=map_name.split('-',1)[-1].replace('-',' ').capitalize()
                related.append(f'<a href="{link(page,map_page)}">{escape(title)} mind map</a>')
        for other in g.get('related',[]):
            item=next(p for p in pages if p['id']==other)
            related.append(f'<a href="{link(page,targets[other])}">{escape(item["title"])}</a>')
        if not is_qa and any(p.name.lower()!='readme.md' and p.suffix.lower() in {'.md','.html','.pdf'} for p in (source.parent.parent/'Questions and Answers').iterdir()):
            related.append(f'<a href="{link(page,topicpage)}">Questions &amp; answers</a>')
        extras='<nav class="revision-utilities" aria-label="Related resources">'+''.join(related)+'</nav>' if related else ''
        qa_class=' qa-reading' if is_qa else ''
        write(page,g['title'],f'<div class="reader-tools"><a href="{link(page,target)}">← {back}</a></div><article class="reading section-reading{qa_class}">{render(page,contents[g["id"]])}</article>{extras}{navigation}',crumbs,subject)
    for p in layout.get('extras',[]):
        page=targets[p['id']]
        write(page,p['title'],f'<div class="reader-tools"><a href="{link(page,target)}">← {back}</a></div><article class="reading">{render(page,contents[p["id"]])}</article>',crumbs,subject)
    qa_class=' qa-reading' if is_qa else ''
    write(full,topic+' — all '+label.lower(),f'<div class="reader-tools"><a href="{link(full,target)}">← {back}</a><button onclick="window.print()">{print_label}</button></div><article class="reading{qa_class}">{render(full,raw)}</article>',crumbs,subject)
    return target,topic+' '+label.lower()
