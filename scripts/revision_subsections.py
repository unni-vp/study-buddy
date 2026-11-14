"""Opt-in, focused subsection pages beneath an existing revision-section menu."""
from html import escape
import json,re
from html_utils import render_md,is_reference_heading,is_revision_checklist_heading

def split_section(raw,definitions):
    from revision_navigation import outline,descendants
    blocks=outline(raw)
    hidden=set()
    for i,b in enumerate(blocks):
        if is_reference_heading(b.heading) or is_revision_checklist_heading(b.heading):
            hidden.update(descendants(blocks,i))
    used={};result={}
    ids=[p['id'] for p in definitions]
    if len(ids)!=len(set(ids)):raise ValueError('Duplicate subsection IDs')
    for page in definitions:
        chunks=['# '+page['title']];first=True
        for selector in page['sections']:
            hits=[i for i,b in enumerate(blocks) if b.level>1 and b.heading==selector['heading']]
            if len(hits)!=1:raise ValueError('Subsection heading must be unique: '+selector['heading'])
            root=hits[0]
            heading_key=lambda value:re.sub(r'\W+',' ',value.casefold().replace('&',' and ')).strip()
            root_is_title=first and (len(page['sections'])==1 or selector.get('intro_only') or heading_key(blocks[root].heading)==heading_key(page['title']))
            indices=[root] if selector.get('intro_only') else descendants(blocks,root)
            for i in indices:
                if i in hidden:continue
                if i in used:raise ValueError(f'Content repeated in {used[i]} and {page["id"]}: {blocks[i].heading}')
                used[i]=page['id'];b=blocks[i]
                # The first selected heading becomes the page title, not a duplicate heading.
                if not (root_is_title and i==root):
                    chunks.append('#'*(b.level-blocks[root].level+(1 if root_is_title else 2))+' '+b.heading)
                if b.body:chunks.append(b.body)
                first=False
        if len(chunks)==1:raise ValueError('Empty subsection: '+page['id'])
        result[page['id']]='\n\n'.join(chunks)
    missing=[b.heading for i,b in enumerate(blocks) if i not in used and i not in hidden and b.body]
    if missing:raise ValueError('Unassigned subsection content: '+', '.join(missing))
    return result

def build_subsection_pages(source,layout,target,subject,topic,topicpage,write,link,slug):
    from revision_navigation import partition,grouped_card,revision_sidebar
    if source.parent.name!='Revision Notes':raise ValueError('Subsection navigation applies only to revision notes')
    raw=source.read_text(encoding='utf-8');contents=partition(raw,layout)
    groups=layout['groups'];prefix=target.stem;full=target.with_name(prefix+'-all.html')
    parent_targets={g['id']:target.with_name(prefix+'-group-'+g['id']+'.html') for g in groups}
    extra_targets={p['id']:target.with_name(prefix+'-'+p['id']+'.html') for p in layout.get('extras',[])}
    targets=dict(parent_targets);targets.update(extra_targets);tree=[];leaves=[]
    for g in groups:
        definitions=g['subsections'];texts=split_section(contents[g['id']],definitions);children=[]
        for i,sub in enumerate(definitions):
            key=g['id']+'--'+sub['id']
            page=parent_targets[g['id']] if i==0 else target.with_name(prefix+'-group-'+key+'.html')
            targets[key]=page;children.append(dict(id=key,title=sub['title']))
            leaves.append(dict(id=key,title=sub['title'],parent=g,text=texts[sub['id']],page=page))
        tree.append(dict(id=g['id'],title=g['title'],subsections=children))
    crumbs=[(subject.split(' - ')[0],source.parents[2]/'index.html'),(topic,topicpage),('Revision notes',target)]
    def publish(page,title,content,current='menu',parent=None):
        trail=crumbs[:-1] if page==target else crumbs+([(parent['title'],parent_targets[parent['id']])] if parent else [])
        write(page,title,content,trail,subject,revision_sidebar=revision_sidebar(page,topic,tree,targets,target,full,current,link))
    def render(page,text):
        def relocate(match):
            url=match[2]
            if re.match(r'^(https?:|#|mailto:)',url):return match[0]
            from urllib.parse import unquote,urlsplit,urlunsplit
            parts=urlsplit(url);href=link(page,(source.parent/unquote(parts.path)).resolve())
            return match[1]+'="'+urlunsplit(('', '',href,parts.query,parts.fragment))+'"'
        return re.sub(r'(href|src)="([^"]+)"',relocate,render_md(text))
    cards=''.join(grouped_card(link(target,parent_targets[g['id']]),g) for g in groups)
    utilities=''.join(f'<a href="{link(target,extra_targets[p["id"]])}">{escape(p["title"])}</a>' for p in layout.get('extras',[]) if not is_reference_heading(p['title']) and not is_revision_checklist_heading(p['title']))
    publish(target,topic+' revision notes',f'<div class="reader-tools"><a href="{link(target,topicpage)}">← Back to topic</a><a href="{link(target,full)}">Print all notes</a></div><h1>{escape(topic)}</h1><div class="revision-grid">{cards}</div><nav class="revision-utilities" aria-label="Resource tools">{utilities}</nav>')
    for i,item in enumerate(leaves):
        page=item['page'];g=item['parent'];steps=[]
        for label,other in [('← Previous',leaves[i-1] if i else None),('Next →',leaves[i+1] if i+1<len(leaves) else None)]:
            if other:
                title=other['title'] if other['parent']['id']==g['id'] else other['parent']['title']+': '+other['title']
                steps.append(f'<a href="{link(page,other["page"])}"><span>{label}</span><strong>{escape(title)}</strong></a>')
            else:steps.append('<span></span>')
        navigation='<nav class="section-navigation" aria-label="Subsection navigation">'+''.join(steps)+'</nav>'
        related=[]
        for name in g.get('maps',[]):
            if (source.parent.parent/'Mind Maps'/(name+'.png')).exists():
                related.append(f'<a href="{link(page,target.parent/(slug(subject+"-"+topic)+"-"+name+".html"))}">{escape(name.split("-",1)[-1].replace("-"," ").capitalize())} mind map</a>')
        for key in g.get('related',[]):
            other=next(p for p in groups+layout.get('extras',[]) if p['id']==key)
            related.append(f'<a href="{link(page,targets[key])}">{escape(other["title"])}</a>')
        if any(p.name.lower()!='readme.md' and p.suffix.lower() in {'.md','.html','.pdf'} for p in (source.parent.parent/'Questions and Answers').iterdir()):
            related.append(f'<a href="{link(page,topicpage)}">Questions &amp; answers</a>')
        extra='<nav class="revision-utilities" aria-label="Related resources">'+''.join(related)+'</nav>' if related else ''
        body=f'<div class="reader-tools"><a href="{link(page,target)}">← All revision notes</a></div><article class="reading section-reading"><p class="revision-parent-title">{escape(g["title"])}</p>{render(page,item["text"])}</article>{extra}{navigation}'
        publish(page,item['title']+' · '+g['title'],body,current=item['id'],parent=g)
    for p in layout.get('extras',[]):
        page=extra_targets[p['id']]
        publish(page,p['title'],f'<div class="reader-tools"><a href="{link(page,target)}">← All revision notes</a></div><article class="reading">{render(page,contents[p["id"]])}</article>',current=p['id'])
    publish(full,topic+' — all revision notes',f'<div class="reader-tools"><a href="{link(full,target)}">← All revision notes</a><button onclick="window.print()">Print all notes</button></div><article class="reading">{render(full,raw)}</article>',current='all')
    return target,topic+' revision notes'
