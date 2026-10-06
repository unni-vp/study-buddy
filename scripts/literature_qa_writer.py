"""Combined Literature practice, with provenance kept on a separate source page."""
import json
from literature_helpers import ROOT,SUBJECT,TOPICS

def q(marks,prompt,answer,refs='Additional specification-based practice'):
 return dict(marks=marks,prompt=prompt,answer=answer,evidence=refs)

def write_bank(n,title,items,evidence):
 topic=ROOT/SUBJECT/TOPICS[n-1];dest=topic/'Questions and Answers';dest.mkdir(exist_ok=True)
 lines=['# '+title+' questions & answers'];last=None
 for number,item in enumerate(sorted(items,key=lambda x:x['marks']),1):
  if item['marks']!=last:last=item['marks'];lines.append('## '+str(last)+' marks')
  lines.extend([f'**{number}.** '+item['prompt'],'**Answer:** '+item['answer']]);item['number']=number
 lines+=['## Past-paper sources','Original practice questions and tutor-written model answers. The linked papers and mark schemes provide the official assessment examples.','### Resource directory','- [Eduqas English Literature](https://www.eduqas.co.uk/qualifications/english-literature-gcse/) — specification and assessment resources.\n- [Physics & Maths Tutor](https://www.physicsandmathstutor.com/past-papers/gcse-english-literature/) — public archive of board papers.\n- [Eduqas sample assessment materials](https://www.eduqas.co.uk/media/35mh4vb2/eduqas-gcse-english-literature-sams-from-2015.pdf) — sample tasks and assessment grids.','### Papers reviewed']
 for year in ['19','23','24']:
  base='../../00 - Past papers/Component 1/Eduqas-C720U10-1-'
  lines.append(f'- June 20{year}, Component 1: [question paper]({base}QP-JUN{year}.pdf) · [mark scheme]({base}MS-JUN{year}.pdf).')
 lines+=['### How the papers inform this practice',evidence]
 if n==1:lines.append('[Shakespeare text: Folger Shakespeare Library](https://www.folger.edu/explore/shakespeares-works/macbeth/read/). Extracts are from the public-domain play; punctuation can vary between editions.')
 else:lines.append('[Official anthology for first assessment in 2027](../../00 - Specification/Eduqas-poetry-anthology-first-assessment-2027.pdf). Page links in questions use PDF page numbers, not the contents list.')
 (dest/(title+' - Questions and Answers.md')).write_text('\n\n'.join(lines)+'\n',encoding='utf-8')
 (topic/'qa-evidence.json').write_text(json.dumps({'reviewed':'2026-10-06','specification':'Eduqas C720QS v4, Component 1; 2027 anthology where applicable','sample':'June 2019, 2023 and 2024 Component 1 question papers and mark schemes','question_status':'Original practice; not reproduced official tasks','evidence_summary':evidence,'questions':items},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 print(title,len(items),'questions')
