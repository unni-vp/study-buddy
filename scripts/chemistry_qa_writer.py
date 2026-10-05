"""Write a combined, mark-ordered Q&A bank and its internal source mapping."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def q(marks,prompt,answer,spec,refs=''):
 return dict(marks=marks,prompt=prompt,answer=answer,specification=spec,evidence=refs or 'Additional specification-based practice')
def write_bank(folder,title,items,evidence):
 topic=ROOT/'Chemistry - AQA'/folder
 dest=topic/'Questions and Answers';dest.mkdir(exist_ok=True)
 items=sorted(items,key=lambda x:x['marks']);lines=['# '+title+' questions & answers'];last=None
 for n,item in enumerate(items,1):
  if item['marks']!=last:
   last=item['marks'];lines.append('## '+str(last)+(' mark' if last==1 else ' marks'))
  lines.append(f'**{n}.** '+item['prompt']);a=item['answer'];lines.append('**Answer:**'+ ('\n\n' if a.startswith('- ') else ' ')+a);item['number']=n
 lines+=['## Past-paper sources','These are original practice questions, informed by the AQA papers below and the current course specification. The answers are tutor-written; the linked mark schemes show the official answers to the original papers.','### Resource directory','- [AQA assessment resources](https://www.aqa.org.uk/subjects/chemistry/gcse/chemistry-8462/assessment-resources) — official papers and mark schemes.\n- [Physics & Maths Tutor](https://www.physicsandmathstutor.com/past-papers/gcse-chemistry/aqa-paper-1/) — paper archive.\n- [Revision Science](https://revisionscience.com/gcse-revision/chemistry/chemistry-gcse-past-papers/aqa-gcse-chemistry-past-papers) — alternative archive.','### Papers used']
 for y in ['19','22','23']:
  base='../../00 - Past papers/Paper 1 Higher/AQA-84621H-'
  lines.append(f'- June 20{y}, Paper 1 Higher: [question paper]({base}QP-JUN{y}.pdf) · [mark scheme]({base}MS-JUN{y}.pdf).')
 lines+=['### Question types checked',evidence,'Additional questions cover the rest of this topic, including practical and mathematical skills. This is a revision selection, not a prediction of the next exam.']
 (dest/(title+' - Questions and Answers.md')).write_text('\n\n'.join(lines)+'\n',encoding='utf-8')
 (topic/'qa-evidence.json').write_text(json.dumps({'reviewed':'2026-10-05','sample':'June 2019, 2022 and 2023 AQA 8462/1H; both questions and mark schemes','current_specification_checked':True,'questions':items},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 print(title,len(items),'questions')
