"""Build an offline HTML library from the subject folders. No server required."""
from pathlib import Path
from urllib.parse import quote
from html import escape as esc
import hashlib, json, os, re
from html_utils import render_md
from mindmap_navigation import card as mindmap_card
from revision_navigation import build_revision_pages
from qa_navigation import build_qa_pages

ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'library'
READERS=SITE/'resources'
READERS.mkdir(parents=True,exist_ok=True)
config=json.loads((ROOT/'project-config.json').read_text(encoding='utf-8'))
SITE_TITLE=config['site_title']
subjects=config['subjects']
KINDS=[('Revision Notes','Revision notes'),('Mind Maps','Mind maps'),('Questions and Answers','Questions & answers')]
ICONS={
 'Computer Science':'<rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8M12 17v4M9 8l-3 3 3 3m6-6 3 3-3 3"/>',
 'English Language':'<path d="m15 3 6 6L8 22H2v-6ZM12 6l6 6M3 17l4 4"/>',
 'English Literature':'<path d="M12 5c-3-2-7-2-10-1v16c3-1 7-1 10 1 3-2 7-2 10-1V4c-3-1-7-1-10 1ZM12 5v16"/>',
 'Maths':'<rect x="4" y="2" width="16" height="20" rx="3"/><path d="M7 6h10M7 11h2m6 0h2M7 16h2m6 0h2M7 20h2m6 0h2"/>',
 'Geography':'<circle cx="12" cy="12" r="10"/><ellipse cx="12" cy="12" rx="4" ry="10"/><path d="M2 12h20M4 6h16M4 18h16"/>',
 'French':'<path d="M5 22V3m0 0c5-4 9 4 15 0v12c-6 4-10-4-15 0M10 3v11M15 5v11"/>',
 'Biology':'<path d="M3 20C1 8 7 2 21 3c0 14-6 20-18 17Zm0 0L17 7M8 15v-5m5 0h5"/>',
 'Chemistry':'<path d="M9 2h6M10 2v7L3 20c-1 2 2 2 2 2h14s3 0 2-2L14 9V2M6 15h12"/><circle cx="10" cy="18" r=".6"/>',
 'Physics':'<circle cx="12" cy="12" r="1.5"/><ellipse cx="12" cy="12" rx="11" ry="4"/><ellipse cx="12" cy="12" rx="11" ry="4" transform="rotate(60 12 12)"/><ellipse cx="12" cy="12" rx="11" ry="4" transform="rotate(120 12 12)"/>'}
def subject_icon(name):
 return '<span class="subject-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'+ICONS[name]+'</svg></span>'

def resource_icon(kind):
 paths={
  'Revision Notes':'<rect x="5" y="3" width="15" height="18" rx="2"/><path d="M9 7h7M9 11h7M9 15h5M3 7h4M3 12h4M3 17h4"/>',
  'Mind Maps':'<circle cx="12" cy="12" r="3"/><path d="M10 10 6 6m8 4 4-4m-8 8-4 4m8-4 4 4"/><circle cx="4" cy="4" r="2"/><circle cx="20" cy="4" r="2"/><circle cx="4" cy="20" r="2"/><circle cx="20" cy="20" r="2"/>',
  'Questions and Answers':'<path d="M16 11h3a2 2 0 0 1 2 2v5l-3-1h-6a2 2 0 0 1-2-2v-2M5 13l-3 2V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H5M7 6a2 2 0 0 1 4 0c0 1-2 1-2 2M9 10h.01"/>'
 }
 return '<svg class="resource-icon" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">'+paths[kind]+'</svg>'

def link(page,target):return quote(os.path.relpath(target,page.parent).replace('\\','/'),safe='/')
def slug(s):return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
def short(s):return s.split(' - ')[0]
def write(page,title,content,crumbs=[],subject=None):
 css=link(page,SITE/'style.css')
 side=''.join(f'<a class="{"selected" if s==subject else ""}" href="{link(page,ROOT/s/"index.html")}">{esc(short(s))}</a>' for s in subjects)
 breadcrumb='<a href="'+link(page,ROOT/'index.html')+'">Subjects</a>'+''.join(f'<span aria-hidden="true"> / </span><a href="{link(page,p)}">{esc(label)}</a>' for label,p in crumbs)
 breadcrumb_html='' if page.name=='index.html' and (page.parent==ROOT or page.parent.name in subjects) else '<nav class="breadcrumbs" aria-label="Breadcrumb">'+breadcrumb+'</nav>'
 page.parent.mkdir(parents=True,exist_ok=True)
 page_title=SITE_TITLE if page==ROOT/'index.html' else title+' · '+SITE_TITLE
 page_class='home-page' if page==ROOT/'index.html' else 'inner-page'
 page.write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{esc(page_title)}</title><link rel="stylesheet" href="{css}"></head><body class="{page_class}"><a class="skip" href="#main">Skip to content</a><header><a class="brand" href="{link(page,ROOT/'index.html')}"><span class="brand-mark">G</span><span class="brand-name">{esc(SITE_TITLE)}</span></a><span class="exam">Summer 2027</span></header><div class="layout"><aside><p class="eyebrow">YOUR SUBJECTS</p><nav aria-label="Subjects">{side}</nav><p class="side-note">Build understanding.<br>Practise precise answers.</p></aside><main id="main">{breadcrumb_html}{content}<footer>GCSE preparation · 2027 · Your personal revision library</footer></main></div></body></html>''',encoding='utf-8')

def resource_reader(source,subject,topic,topicpage):
 key=hashlib.sha1(str(source.relative_to(ROOT)).encode()).hexdigest()[:12]
 target=READERS/(key+'.html')
 title=source.stem.replace(' - School Fieldwork Account',' fieldwork').replace(' - Revision Notes',' revision notes')
 raw=source.read_text(encoding='utf-8')
 if source.parent.name=='Questions and Answers':
  return build_qa_pages(source,target,subject,topic,topicpage,write,link)
 layout_name={'Revision Notes':'revision-layout.json','Questions and Answers':'qa-layout.json'}.get(source.parent.name)
 layout_path=source.parent.parent/layout_name if layout_name else None
 if layout_path and layout_path.exists():
  layout=json.loads(layout_path.read_text(encoding='utf-8'))
  if layout['source']==source.name:
   return build_revision_pages(source,layout_path,target,subject,topic,topicpage,write,link,slug)
 content=render_md(raw)
 # Relative links written in Markdown are resolved from the original source directory.
 def fix(m):
  url=m.group(1)
  if re.match(r'^(https?:|#|mailto:)',url):return m.group(0)
  from urllib.parse import unquote
  return 'href="'+link(target,(source.parent/unquote(url)).resolve())+'"'
 content=re.sub(r'href="([^"]+)"',fix,content)
 content=re.sub(r'src="([^"]+)"',lambda m: 'src="'+link(target,(source.parent/__import__('urllib.parse',fromlist=['unquote']).unquote(m.group(1))).resolve())+'"',content)
 write(target,title,'<div class="reader-tools"><a href="'+link(target,topicpage)+'">← Back to topic</a><button onclick="window.print()">Print</button></div><article class="reading">'+content+'</article>',[(short(subject),ROOT/subject/'index.html'),(topic,topicpage)],subject)
 return target,title

def resources(folder,subject,topic,topicpage,kind):
 if kind=='Mind Maps':
  images=sorted(folder.glob('*.png'))
  if images:
   target=READERS/(slug(subject+'-'+topic)+'-mind-maps.html')
   cards=[]
   for p in images:
    title=p.stem.split('-',1)[-1].replace('-',' ').capitalize()
    mappage=READERS/(slug(subject+'-'+topic)+'-'+p.stem+'.html')
    write(mappage,title+' mind map',f'<div class="reader-tools"><a href="{link(mappage,target)}">← Back to mind maps</a><button onclick="window.print()">Print</button></div><h1>{esc(title)}</h1><figure class="mindmap-view"><img src="{link(mappage,p)}" alt="{esc(title)} mind map"></figure>',[(short(subject),ROOT/subject/'index.html'),(topic,topicpage),('Mind maps',target)],subject)
    cards.append(mindmap_card(link(target,mappage),title,link(target,p)))
   write(target,topic+' mind maps',f'<div class="reader-tools"><a href="{link(target,topicpage)}">← Back to topic</a></div><h1>{esc(topic)} mind maps</h1><div class="mindmap-grid">'+''.join(cards)+'</div>',[(short(subject),ROOT/subject/'index.html'),(topic,topicpage)],subject)
   return [(target,f'{len(images)} visual mind maps')]
 found=[]
 for f in sorted(folder.iterdir()):
  if not f.is_file() or f.name.lower()=='readme.md':continue
  if f.suffix.lower()=='.md':found.append(resource_reader(f,subject,topic,topicpage))
  elif f.suffix.lower() in ['.html','.pdf','.docx'] and not f.with_suffix('.md').exists():found.append((f,f.stem))
 return found

total_ready=0
for subject,course in subjects.items():
 subjectpage=ROOT/subject/'index.html'; rows=[]
 ready=0
 for i,topic in enumerate(course['topics'],1):
  title=topic['title']; folder=ROOT/subject/f'{i:02d} - {title}'; page=folder/'index.html'
  sections=[]; count=0
  for kind,label in KINDS:
   (folder/kind).mkdir(exist_ok=True)
   items=resources(folder/kind,subject,title,page,kind);count+=len(items)
   if items:
    target=items[0][0]
    if len(items)>1:
     target=READERS/(slug(subject+'-'+title+'-'+kind)+'-index.html')
     choices='<ul class="resources">'+''.join(f'<li><a href="{link(target,p)}">{esc(t)}</a></li>' for p,t in items)+'</ul>'
     write(target,title+' '+label.lower(),f'<div class="reader-tools"><a href="{link(target,page)}">← Back to topic</a></div><h1>{esc(label)}</h1>'+choices,[(short(subject),subjectpage),(title,page)],subject)
    sections.append(f'<a class="resource-button" href="{link(page,target)}">{resource_icon(kind)}<span>{esc(label)}</span></a>')
   else:sections.append(f'<button class="resource-button" disabled title="Not yet prepared">{resource_icon(kind)}<span>{esc(label)}</span></button>')
  write(page,title,f'<p class="eyebrow">{esc(short(subject))} · {esc(course["tier"])}</p><h1>{esc(title)}</h1><div class="resource-actions">'+''.join(sections)+'</div>',[(short(subject),subjectpage)],subject)
  ready+=bool(count)
  rows.append(f'<a class="topic-row topic-card" href="{link(subjectpage,page)}"><span class="topic-number">{i:02d}</span><strong>{esc(title)}</strong><div class="topic-card-footer"><span class="status {"ready" if count else ""}">{"Resources available" if count else "Not yet prepared"}</span><span aria-hidden="true">→</span></div></a>')
 total_ready+=ready
 specs=sorted((ROOT/subject/'00 - Specification').glob('*.pdf'))
 docs='<details class="sources"><summary>Official specifications & course references</summary><ul>'+''.join(f'<li><a href="{link(subjectpage,f)}">{esc(f.stem)}</a></li>' for f in specs)
 case=ROOT/subject/'CASE_STUDIES.md'
 if case.exists():
  target,label=resource_reader(case,subject,'Geography course references',subjectpage)
  docs+=f'<li><a href="{link(subjectpage,target)}">School case studies & fieldwork details</a></li>'
 docs+='</ul></details>'
 extra=''
 if subject=='English Literature - Eduqas':extra='<p class="course-detail">Macbeth · A Christmas Carol · An Inspector Calls · 2027 poetry anthology</p>'
 write(subjectpage,short(subject),f'<p class="eyebrow">{esc(subject.split(" - ")[-1])} · {esc(course["code"])} · {esc(course["tier"])}</p><h1>{esc(short(subject))}</h1>{extra}<div class="topic-list">'+''.join(rows)+'</div>'+docs,subject=subject)

home=ROOT/'index.html';cards=[]
colours=['#5264c8','#277d74','#936343','#497fb1','#8b579d','#d08c30','#378767','#b36377','#51888c']
for i,(subject,course) in enumerate(subjects.items()):
 cards.append(f'<a class="subject-card" style="--subject-colour:{colours[i]}" href="{link(home,ROOT/subject/"index.html")}"><div class="subject-card-top">{subject_icon(short(subject))}<span class="subject-code">{esc(course["code"])}</span></div><h2>{esc(short(subject))}</h2><p>{esc(subject.split(" - ")[-1])} · {esc(course["tier"])}</p><div><span>{len(course["topics"])} topics</span><span aria-hidden="true">→</span></div></a>')
write(home,'Subjects',f'<p class="intro">Follow each topic from clear explanations to visual mind maps and questions with answers.</p><div class="subject-grid">'+''.join(cards)+f'</div><p class="library-note">{len(subjects)} subjects · {sum(len(c["topics"]) for c in subjects.values())} topics · {total_ready} topics with resources available</p>')
print('Built offline subject index, 9 subject contents pages, 73 topic pages and resource readers.')
