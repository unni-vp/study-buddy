"""Physics resource authoring; metadata is kept out of student reading pages."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
SUBJECT='Physics - AQA'
TOPICS=['01 - Energy','02 - Electricity','03 - Particle model of matter','04 - Atomic structure','05 - Forces']
TITLES=[t[5:] for t in TOPICS]
def notes(n,body,groups,coverage,practicals=()):
 p=ROOT/SUBJECT/TOPICS[n-1];f=p/'Revision Notes';f.mkdir(exist_ok=True)
 name=TITLES[n-1]+' - Revision Notes.md';(f/name).write_text('# '+TITLES[n-1]+'\n\n'+body.strip()+'\n',encoding='utf-8')
 (p/'revision-layout.json').write_text(json.dumps({'source':name,'groups':[dict(id=i,title=t,description=d,icon=icon,sections=[{'heading':h} for h in hs]) for i,t,d,icon,hs in groups]},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 target=p/'resource-coverage.json';data=json.loads(target.read_text()) if target.exists() else {}
 data.update(reviewed='2026-10-11',specification=f'AQA 8463 Higher, section 4.{n}, version 1.1 September 2019',source='../00 - Specification/AQA-8463-specification.pdf',coverage=coverage,practicals=list(practicals))
 target.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 print('Wrote',TITLES[n-1],'notes')
def q(marks,prompt,answer,spec,refs='Additional specification-based practice'):
 return dict(marks=marks,prompt=prompt,answer=answer,specification=spec,evidence=refs)
def write_bank(n,items,evidence):
 p=ROOT/SUBJECT/TOPICS[n-1];items=sorted(items,key=lambda x:x['marks']);lines=['# '+TITLES[n-1]+' questions & answers'];last=None
 for num,item in enumerate(items,1):
  if item['marks']!=last:
   last=item['marks'];lines.append('## '+str(last)+(' mark' if last==1 else ' marks'))
  lines.extend([f'**{num}.** '+item['prompt'],'**Answer:**'+ ('\n\n' if item['answer'].startswith('- ') else ' ')+item['answer']]);item['number']=num
 paper=2 if n==5 else 1
 lines+=['## Past-paper sources','Original practice questions with tutor-written answers. The linked AQA papers and mark schemes provide the assessment examples.','### Resource directory',f'- [AQA Physics assessment resources](https://www.aqa.org.uk/subjects/physics/gcse/physics-8463/assessment-resources)\n- [Physics & Maths Tutor paper archive](https://www.physicsandmathstutor.com/past-papers/gcse-physics/aqa-paper-{paper}/)\n- [Revision Science archive](https://revisionscience.com/gcse-revision/physics/physics-gcse-past-papers/aqa-gcse-physics-past-papers)','### Papers reviewed']
 for y in ['22','23']:
  base=f'../../00 - Past papers/Paper {paper} Higher/AQA-8463{paper}H-'
  lines.append(f'- June 20{y}, Paper {paper} Higher: [question paper]({base}QP-JUN{y}.PDF) · [mark scheme]({base}MS-JUN{y}.PDF).')
 lines+=['### Evidence and selection',evidence,'The two-paper sample illustrates question types; it is not a prediction. Additional questions cover the current specification, including Higher-tier and separate Physics content.']
 (p/'Questions and Answers'/(TITLES[n-1]+' - Questions and Answers.md')).write_text('\n\n'.join(lines)+'\n',encoding='utf-8')
 (p/'qa-evidence.json').write_text(json.dumps({'reviewed':'2026-10-11','sample':f'June 2022 and 2023 AQA 8463/{paper}H (2022 Paper 2 is 2HR)','selection':evidence,'questions':items},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 print(TITLES[n-1],len(items),'questions')
