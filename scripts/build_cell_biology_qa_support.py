"""Build navigation, original SVG diagrams and provenance around the editable Q&A."""
from pathlib import Path
from html import escape
import json
import re
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
TOPIC=ROOT/'Biology - AQA'/'01 - Cell biology'
SOURCE=TOPIC/'Questions and Answers'/'Cell Biology - Questions and Answers.md'
DIAGRAMS=SOURCE.parent/'Diagrams'
PAPERS=ROOT/'Biology - AQA'/'00 - Past papers'/'Paper 1 Higher'

def svg(name,width,height,body,title):
    raw=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><rect width="100%" height="100%" rx="18" fill="#fafcfb"/><g font-family="Segoe UI, Arial, sans-serif" fill="#203b40">{body}</g></svg>'
    ET.fromstring(raw)
    (DIAGRAMS/name).write_text(raw,encoding='utf-8')

def text(x,y,s,size=20,anchor='middle',colour='#203b40'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="{colour}">{escape(s)}</text>'

def osmosis():
    body=text(140,36,'A · Inside the cell')+text(420,36,'B · Outside the cell')
    body+=text(140,65,'More dilute',19)+text(420,65,'More concentrated',19)
    for start,solutes in [(25,4),(305,8)]:
        body+=f'<rect x="{start}" y="88" width="230" height="145" rx="12" fill="#eaf5fa" stroke="#b9d3dd"/>'
        for i in range(16):
            x=start+35+(i%4)*52;y=110+(i//4)*32
            if i in ([0,5,10,15] if solutes==4 else [0,2,5,7,8,10,13,15]):
                body+=f'<rect x="{x-7}" y="{y-7}" width="14" height="14" rx="2" fill="#8655b5"/>'
            else:body+=f'<circle cx="{x}" cy="{y}" r="7" fill="#278eaf"/>'
    body+='<path d="M280 88 V233" stroke="#426d65" stroke-width="7" stroke-dasharray="10 6"/>'
    body+=text(280,265,'Partially permeable membrane',20)
    body+='<circle cx="103" cy="302" r="7" fill="#278eaf"/>'+text(119,308,'Water',19,'start')
    body+='<rect x="319" y="295" width="14" height="14" rx="2" fill="#8655b5"/>'+text(344,308,'Solute',19,'start')
    svg('osmosis-question.svg',560,333,body,'Water and solute on either side of a partially permeable cell membrane')

def rod(x,y,c,length=38):
    return f'<path d="M{x} {y-length/2} V{y+length/2}" fill="none" stroke="{c}" stroke-width="9" stroke-linecap="round"/>'

def copied(x,y,c):
    return f'<path d="M{x-12} {y-22} L{x+12} {y+22} M{x+12} {y-22} L{x-12} {y+22}" stroke="{c}" stroke-width="8" stroke-linecap="round"/><circle cx="{x}" cy="{y}" r="5" fill="{c}"/>'

def mitosis():
    colours=['#8a53b4','#dc8336']
    body=''
    for x,y,title in [(140,40,'1 · Before copying'),(420,40,'2 · DNA copied'),(140,315,'3 · Copies separate'),(420,315,'4 · Two cells')]:
        body+=text(x,y,title,20)
    # Stages 1 and 2: a nucleus is present and the replicated pair remains joined.
    for x in [140,420]:
        body+=f'<ellipse cx="{x}" cy="146" rx="112" ry="80" fill="#eaf5ee" stroke="#428778" stroke-width="3"/><ellipse cx="{x}" cy="146" rx="70" ry="57" fill="#f5f0fa" stroke="#a497ad" stroke-width="2"/>'
    body+=rod(111,146,colours[0])+rod(169,146,colours[1])
    body+=copied(391,146,colours[0])+copied(449,146,colours[1])
    body+=text(140,249,'One of each chromosome',18)
    body+=text(420,249,'Two joined copies of each',18)
    # Stage 3: no intact nuclear envelope around separating chromosome copies.
    body+='<ellipse cx="140" cy="415" rx="117" ry="80" fill="#eaf5ee" stroke="#428778" stroke-width="3"/>'
    for x in [77,203]:
        body+=rod(x,390,colours[0],30)+rod(x,440,colours[1],30)
    body+='<path d="M127 390 H99 M127 440 H99 M153 390 H181 M153 440 H181" fill="none" stroke="#52716c" stroke-width="2"/><path d="M99 385 L91 390 L99 395 M99 435 L91 440 L99 445 M181 385 L189 390 L181 395 M181 435 L189 440 L181 445" fill="none" stroke="#52716c" stroke-width="2"/>'
    body+=text(140,524,'One full set at each end',18)
    for x in [358,482]:
        body+=f'<ellipse cx="{x}" cy="415" rx="55" ry="70" fill="#eaf5ee" stroke="#428778" stroke-width="3"/><ellipse cx="{x}" cy="415" rx="42" ry="47" fill="#f5f0fa" stroke="#a497ad" stroke-width="2"/>'
        body+=rod(x-16,415,colours[0],30)+rod(x+16,415,colours[1],30)
    body+=text(420,524,'Matching complete sets',18)
    body+=text(280,569,'Simplified: two chromosomes are tracked',18)
    svg('mitosis-question.svg',560,590,body,'DNA copying, visible chromosome-copy separation and two matching daughter cells')

def graph():
    x=lambda v: 85+v/0.6*400
    y=lambda v: 195-v/12*135
    body=''
    for n in range(7):
        xx=x(n/10)
        body+=f'<path d="M{xx} 60 V330" stroke="#dbe5e1"/>'+text(xx,356,f'{n/10:.1f}',18)
    for v in range(-12,13,4):
        yy=y(v)
        body+=f'<path d="M85 {yy} H485" stroke="#dbe5e1"/>'+text(70,yy+6,str(v),18,'end')
    body+='<path d="M85 55 V330 H495 M85 195 H495" stroke="#44645b" stroke-width="2" fill="none"/>'
    body+=f'<path d="M{x(0)} {y(12)} L{x(.6)} {y(-12)}" stroke="#337d99" stroke-width="3"/>'
    for xx,yy in [(0,12),(.1,8),(.2,4),(.4,-4),(.5,-8),(.6,-12)]:
        body+=f'<circle cx="{x(xx)}" cy="{y(yy)}" r="6" fill="#337d99"/>'
    body+=f'<circle cx="{x(.3)}" cy="{y(0)}" r="8" fill="#fff" stroke="#bc6d32" stroke-width="3"/>'
    body+=text(300,164,'0.30 mol/dm³',20,'start','#a85925')
    body+=text(285,391,'Sugar concentration (mol/dm³)',20)
    body+='<text x="25" y="195" text-anchor="middle" font-size="19" transform="rotate(-90 25 195)">Mean change in mass (%)</text>'
    svg('osmosis-answer-graph.svg',560,418,body,'Correctly plotted original osmosis results with the zero-change concentration at 0.30 mol per cubic decimetre')

# Each entry is checked against the current specification, independently of a
# mark scheme's printed content code. All items are original/adapted practice.
# The tuples are references to the source question TYPE, not copied questions.
MAP={
 1:('cells',['4.1.1.2'],[(2019,'01.1')]),
 2:('cells',['4.1.1.2'],[(2022,'01.2')]),
 3:('cell-processes',['4.1.2.3'],[(2023,'01.2'),(2024,'04.1')]),
 4:('cells',['4.1.1.4'],[(2022,'04.5')]),
 5:('cell-processes',['4.1.2.2'],[(2024,'08.1')]),
 6:('transport',['4.1.3.1'],[(2025,'06.1')]),
 7:('transport',['4.1.3.2','4.1.3.3'],[(2025,'03.3')]),
 8:('practical-investigations',['4.1.3.2','RPA3'],[(2022,'01.5')]),
 9:('practical-investigations',['4.1.1.6','RPA2'],[(2023,'03.5')]),
 10:('practical-investigations',['4.1.1.6','WS'],[(2018,'01.8')]),
 11:('cells',['4.1.1.1','4.1.1.2'],[(2025,'08.2'),(2023,'05.2')]),
 12:('cells',['4.1.1.5'],[(2019,'01.6'),(2022,'03.5')]),
 13:('cells',['4.1.1.5','RPA1'],[]),
 14:('cell-processes',['4.1.2.3'],[(2025,'07.1')]),
 15:('cell-processes',['4.1.2.2'],[(2024,'08.4')]),
 16:('transport',['4.1.3.1'],[(2022,'06.3')]),
 17:('practical-investigations',['4.1.3.2','RPA3'],[(2018,'04.2'),(2022,'01.6')]),
 18:('practical-investigations',['4.1.3.2','RPA3'],[(2022,'01.4')]),
 19:('cells',['4.1.1.2'],[(2022,'01.1'),(2018,'06.2')]),
 20:('cells',['4.1.1.3'],[]),
 21:('cells',['4.1.1.5'],[(2019,'01.5')]),
 22:('transport',['4.1.3.2'],[(2022,'01.9'),(2024,'05.2')]),
 23:('transport',['4.1.3.3','4.1.1.3'],[(2018,'04.5'),(2024,'04.5')]),
 24:('transport',['4.1.3.1'],[]),
 25:('practical-investigations',['4.1.1.5','RPA1'],[(2022,'03.2')]),
 26:('practical-investigations',['4.1.1.6','RPA2'],[(2023,'03.4')]),
 27:('practical-investigations',['4.1.1.6'],[(2018,'01.7'),(2023,'03.7')]),
 28:('practical-investigations',['4.1.1.6'],[(2022,'02.3')]),
 29:('cell-processes',['4.1.2.3'],[]),
 30:('cell-processes',['4.1.2.2'],[(2022,'04.4'),(2023,'05.6')]),
 31:('transport',['4.1.3.1'],[(2024,'02.4'),(2022,'06.5')]),
 32:('transport',['4.1.3.1'],[(2025,'06.2')]),
 33:('transport',['4.1.3.1'],[(2022,'06.1'),(2022,'06.2')]),
 34:('practical-investigations',['4.1.3.2','RPA3','MS4'],[(2022,'01.7'),(2022,'01.8'),(2018,'04.4')]),
 35:('cells',['4.1.1.5'],[(2022,'03.3'),(2025,'05.2')]),
 36:('transport',['4.1.3.1','4.1.3.3','4.1.1.2'],[(2019,'06.5')]),
 37:('cells',['4.1.1.5','MS'],[(2024,'08.3')]),
 38:('cell-processes',['4.1.2.3','WS1.3'],[(2018,'06.7'),(2018,'06.8'),(2025,'07.1'),(2025,'07.2')]),
 39:('practical-investigations',['4.1.1.2','4.1.1.5','RPA1'],[(2022,'03.1'),(2022,'03.2'),(2022,'03.4')]),
 40:('practical-investigations',['4.1.3.2','RPA3'],[(2024,'05.1')]),
 41:('practical-investigations',['4.1.3.2','RPA3','WS'],[(2025,'03.1')]),
 42:('practical-investigations',['4.1.1.6','RPA2'],[(2023,'03.3'),(2023,'03.4'),(2023,'03.5'),(2023,'03.7')]),
}

PATTERNS={
 'Cell structures and comparisons':{2018:['06.1','06.2'],2019:['01.1','01.2','01.3','01.4'],2022:['01.1','01.2','01.3','02.1'],2023:['05.2'],2024:['02.1','04.2','04.4','04.6'],2025:['08.1','08.2']},
 'Osmosis in different contexts':{2018:['04.1','04.2','04.3','04.4'],2019:['06.4'],2022:['01.4','01.5','01.6','01.7','01.8','01.9'],2023:['03.9'],2024:['05.1','05.2','05.3'],2025:['03.1','03.2']},
 'Stem cells and differentiation':{2018:['06.7','06.8'],2019:['07.5','07.6'],2022:['04.5'],2023:['01.2'],2024:['04.1','04.6'],2025:['07.1','07.2']},
 'Microscopy and magnification':{2019:['01.5','01.6'],2022:['03.1','03.2','03.3','03.4','03.5'],2024:['08.3'],2025:['05.2']},
 'Exchange surfaces and their adaptations':{2019:['06.5','07.4'],2022:['06.3','06.5'],2024:['02.4'],2025:['06.2']},
 'Osmosis practical methods or data':{2018:['04.1','04.2','04.4'],2022:['01.4','01.5','01.6','01.7','01.8'],2024:['05.1','05.2','05.3'],2025:['03.1']},
 'Bacterial culture investigations or data':{2018:['01.6','01.7','01.8','01.9'],2023:['03.3','03.4','03.5','03.6','03.7'],2024:['06.2'],2025:['08.3','08.4']},
 'Mitosis and the cell cycle':{2022:['04.4'],2023:['05.5','05.6'],2024:['08.1','08.2','08.4']},
}

def build():
    DIAGRAMS.mkdir(exist_ok=True)
    osmosis();mitosis();graph()
    raw=SOURCE.read_text(encoding='utf-8')
    from qa_navigation import parse_qa
    _,mark_groups,_=parse_qa(raw)
    questions=[(n,m.marks,text) for m in mark_groups for n,text in m.questions]
    assert len(questions)==42
    groups=[{'id':g.id,'title':g.title,'marks':g.marks,'questions':[f'Q{n:02}' for n,_ in g.questions]} for g in mark_groups]
    layout={'source':SOURCE.name,'mode':'combined-by-marks','groups':groups,'sources_heading':'Past-paper sources'}
    (TOPIC/'qa-layout.json').write_text(json.dumps(layout,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    sources=json.loads((PAPERS/'source-manifest.json').read_text(encoding='utf-8'))
    lookup={(p['year'],p['kind']):p for p in sources}
    records=[]
    for n,m,text in questions:
        group,spec,refs=MAP[n]
        evidence=[]
        for year,question in refs:
            paper=lookup[year,'QP'];scheme=lookup[year,'MS']
            evidence.append({'year':year,'series':'June','board':'AQA','qualification':'8461','paper':'8461/1H','question':question,'question_paper':paper['file'],'question_paper_url':paper['url'],'mark_scheme':scheme['file'],'mark_scheme_url':scheme['url']})
        records.append({'id':f'Q{n:02}','prompt':text.split('\n\n')[0].split('** ',1)[1],'marks':m,'mark_group':f'marks-{m}','theme':group,'type':'adapted practice' if refs else 'original specification practice','specification':spec,'current_specification_relevant':True,'evidence':evidence,'marking':'suggested marking points; linked explanation for extended responses' if n in [38,39,40,41,42] else 'suggested marking points'})
    audit={'checked':'2026-10-04','exam_year':2027,'board':'AQA','qualification':'8461','tier':'Higher','source':str(SOURCE.relative_to(ROOT)).replace('\\','/'),'specification_pdf':'Biology - AQA/00 - Specification/AQA-8461-specification.pdf','current_specification_url':'https://www.aqa.org.uk/subjects/biology/gcse/biology-8461/specification/subject-content/cell-biology','sample':[2018,2019,2022,2023,2024,2025],'sample_definition':'Six publicly released June 8461/1H papers, spanning the first assessment and four recent summer series; 2020/2021 emergency autumn series and specimens excluded. No claim of an exhaustive frequency ranking or prediction. Count each type once per paper; overlapping types are allowed.','patterns':[{'type':name,'papers':len(refs),'denominator':6,'references':refs} for name,refs in PATTERNS.items()],'questions':records,'review_notes':['All questions use new wording or contexts/data and proposed marks; none is presented as a verbatim official question or mark scheme.','Q28 is specification-based bacterial doubling practice; June 2022 Q02.3 supports the transferable time/division calculation, but concerns fungal cells and does not ask exponential bacterial growth.','Q38 extends short-answer stem-cell evidence into an original evaluation task. Q39 and Q42 assemble required-practical methods; their six-mark allocations are original.','The June 2025 mark scheme prints 4.1.3.2 beside Q07.1/Q07.2. Their actual content is stem cells, correctly mapped here to 4.1.2.3.','Current online AQA wording says a maximum of 25 degrees C; the local older PDF says generally 25 degrees C. The current maximum is used.','Excluded clinical drug-testing procedures, immune responses, digestion detail, cancer biology and inheritance mechanisms beyond the Cell biology focus. Application questions supply the necessary context.','This is a focused question bank, not full curriculum coverage. Xylem/phloem and nerve/muscle examples remain available in revision notes.','Six-mark methods and evaluations are read as complete linked answers, not as a universal one-bullet-equals-one-mark rule.']}
    (TOPIC/'QA_SOURCE_AUDIT.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'Built {len(records)} question references, {len(groups)} groups and 3 SVG diagrams.')

if __name__=='__main__':build()
