"""Author complete resources for previously empty science topics."""
from pathlib import Path
from datetime import date
import json,re,subprocess
from copy import deepcopy
from biology_readable_mindmaps import prepare_panels,build_map
from subject_explanatory_figures import drawing as existing_drawing,PURPOSES as existing_purposes
from science_remaining_figures import FIGURES,PURPOSES

ROOT=Path(__file__).resolve().parents[1]
def q(marks,prompt,answer,spec,evidence='Additional specification-based practice'):
    return dict(marks=marks,prompt=prompt,answer=answer,specification=spec,evidence=evidence)
def p(title,*lines,visual=None):
    value=dict(title=title,lines=list(lines))
    if visual:value['visual']=visual
    return value
def m(slug,title,*panels):return dict(slug=slug,title=title,panels=list(panels))
def drawing(kind,width):
    return FIGURES[kind](width) if kind in FIGURES else existing_drawing(kind,width)
def write(subject,n,data):
    config=json.loads((ROOT/'project-config.json').read_text(encoding='utf-8'))
    title=config['subjects'][subject]['topics'][n-1]['title']
    topic=ROOT/subject/f'{n:02d} - {title}'
    for category in ('Revision Notes','Mind Maps','Questions and Answers','Flash Cards','Diagrams'):
        (topic/category).mkdir(parents=True,exist_ok=True)
    notes_name=f'{title} - Revision Notes.md'
    notes='# '+title+'\n\n'+data['notes'].strip()+'\n'
    (topic/'Revision Notes'/notes_name).write_text(notes,encoding='utf-8')
    groups=[dict(id=i,title=t,description=d,icon=icon,sections=[dict(heading=h) for h in hs]) for i,t,d,icon,hs in data['groups']]
    (topic/'revision-layout.json').write_text(json.dumps(dict(source=notes_name,groups=groups),indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    items=sorted(deepcopy(data['questions']),key=lambda x:x['marks'])
    bank=['# '+title+' questions & answers'];last=None
    for number,item in enumerate(items,1):
        if item['marks']!=last:
            last=item['marks'];bank.append('## '+str(last)+(' mark' if last==1 else ' marks'))
        bank.extend([f'**{number}.** '+item['prompt'],'**Answer:**'+ ('\n\n' if item['answer'].startswith('- ') else ' ')+item['answer']])
        item['number']=number
    code=config['subjects'][subject]['code'];paper=data.get('paper',2)
    bank+=['## Past-paper sources','### Resource directory',f'- [AQA assessment resources](https://www.aqa.org.uk/subjects/{subject.split(" - ")[0].lower()}/gcse/{subject.split(" - ")[0].lower()}-{code}/assessment-resources)']
    bank+=data.get('source_links',[])
    bank+=['### Question selection',data['evidence'],'These are original practice questions and tutor-written answers, informed by the linked papers. Mark allocations are practice allocations.']
    for y in ('22','23'):
        folder=ROOT/subject/f'00 - Past papers/Paper {paper} Higher'
        if folder.exists():
            paths={kind:next(iter(sorted(folder.glob(f'AQA-{code}{paper}H-{kind}-JUN{y}.*'))),None) for kind in ('QP','MS')}
            if all(paths.values()):
                bank.append(f'- June 20{y}, Paper {paper} Higher: '+ ' · '.join(f'[{label}](../../00 - Past papers/Paper {paper} Higher/{paths[kind].name})' for kind,label in [('QP','question paper'),('MS','mark scheme')])+'.')
    qa_name=f'{title} - Questions and Answers.md'
    qa='\n\n'.join(bank)+'\n';(topic/'Questions and Answers'/qa_name).write_text(qa,encoding='utf-8')
    (topic/'qa-evidence.json').write_text(json.dumps(dict(reviewed=date.today().isoformat(),sample=data['evidence'],questions=items),indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    records=[];paths=[]
    for item in data['maps']:
        panels=prepare_panels(item['panels'])
        for panel,source in zip(panels,item['panels']):
            panel['text_reserve']=12
            # Keep adjacent related facts together: dividers mark groups, not every fact.
            groups=panel['groups']
            panel['groups']=[dict(lines=[line for g in groups[i:i+2] for line in g['lines']]) for i in range(0,len(groups),2)]
            if source.get('visual'):
                panel['visual']={**source['visual'],'after':source['visual']['after']//2}
        svg,record=build_map(item['title'],item['slug'],panels,columns=item.get('columns'),drawing_provider=drawing,purpose_provider={**existing_purposes,**PURPOSES},apply_biology_visuals=False)
        path=topic/'Mind Maps'/(item['slug']+'.svg');path.write_text(svg,encoding='utf-8');paths.append(str(path))
        text=['# '+item['title']]
        for panel in item['panels']:text.extend(['## '+panel['title'],*panel['lines']])
        (path.with_suffix('.md')).write_text('\n\n'.join(text)+'\n',encoding='utf-8')
        record.update(slug=item['slug'],title=item['title']);records.append(record)
    for name,kind,width in data.get('diagrams',[]):
        content,height=drawing(kind,width)
        svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" font-family="Segoe UI, Arial, sans-serif"><title>{PURPOSES.get(kind,existing_purposes.get(kind,kind))}</title><rect width="100%" height="100%" fill="white"/>{content}</svg>'
        (topic/'Diagrams'/(name+'.svg')).write_text(svg,encoding='utf-8')
    node=Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe'
    subprocess.run([str(node),str(ROOT/'scripts/render_mindmap_previews.cjs'),*paths],cwd=ROOT,check=True)
    (topic/'mindmap-layout-review.json').write_text(json.dumps(dict(reviewed=date.today().isoformat(),generator='scripts/science_completion.py',style='Approved readable panels, black text, consistent headings, dividers, content-measured layout',print=dict(orientation='A4 landscape',width_mm=277,body_pt=11.21),maps=records),indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    if data.get('cards'):
        cards=[dict(category=c,front=f,back=b if isinstance(b,list) else [b]) for c,f,b in data['cards']]
    else:
        from flashcards_from_qa import parse_cards
        cards=parse_cards(qa)
    deck_name=f'{title} - Flash Cards.json'
    (topic/'Flash Cards'/deck_name).write_text(json.dumps(dict(title=title+' flash cards',cards=cards),indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    coverage=dict(reviewed=date.today().isoformat(),specification=f'AQA {code}, Higher tier',source=f'../00 - Specification/AQA-{code}-specification.pdf',coverage=data['coverage'],coverage_checklist=data.get('checklist',{}),practicals=data.get('practicals',[]),mindmaps=[x['slug'] for x in data['maps']],flashcards=dict(reviewed=date.today().isoformat(),source='Questions and Answers/'+qa_name,deck='Flash Cards/'+deck_name,count=len(cards),categories=list(dict.fromkeys(c['category'] for c in cards))))
    (topic/'resource-coverage.json').write_text(json.dumps(coverage,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    readme=topic/'README.md';text=readme.read_text(encoding='utf-8')
    placeholder='Resources have not yet been authored. Follow the project AGENTS.md and RESOURCE_GUIDELINES.md.'
    text=text.replace(placeholder,'## Available resources\n\nRevision notes, mind maps, combined questions and answers, and interactive flash cards are available from the topic page.')
    readme.write_text(text,encoding='utf-8')
    print(f'Wrote {subject} / {title}: {len(items)} questions, {len(cards)} cards, {len(records)} maps')
