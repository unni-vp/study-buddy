from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
subjects={
'Computer Science - AQA':('8525','Untiered',[
('3.1','Fundamentals of algorithms'),('3.2','Programming'),('3.3','Fundamentals of data representation'),('3.4','Computer systems'),('3.5','Fundamentals of computer networks'),('3.6','Cyber security'),('3.7','Relational databases and SQL'),('3.8','Ethical legal and environmental impacts')]),
'English Language - Eduqas':('C700QS','Untiered',[
('Component 1 Reading','20th-century fiction reading'),('Component 1 Writing','Creative prose writing'),('Component 2 Reading','19th and 21st-century non-fiction reading'),('Component 2 Writing','Transactional and persuasive writing'),('Spoken language','Speaking listening and discussion')]),
'English Literature - Eduqas':('C720QS','Untiered',[
('Component 1 Section A','Macbeth'),('Component 1 Section B','Poetry anthology - assessment from 2027'),('Component 2 Section A','An Inspector Calls'),('Component 2 Section B','A Christmas Carol'),('Component 2 Section C','Unseen poetry')]),
'Maths - Edexcel':('1MA1','Higher',[
('1','Number'),('2','Algebra'),('3','Ratio proportion and rates of change'),('4','Geometry and measures'),('5','Probability'),('6','Statistics')]),
'Geography - OCR A':('J383','Untiered',[
('1.1','Landscapes of the UK'),('1.2','People of the UK'),('1.3','UK environmental challenges'),('2.1','Ecosystems of the planet'),('2.2','People of the planet'),('2.3','Environmental threats to our planet'),('J383-03','Geographical skills'),('Fieldwork','Physical and human fieldwork')]),
'French - AQA':('8652','Higher',[
('3.1.1','People and lifestyle'),('3.1.2','Popular culture'),('3.1.3','Communication and the world around us'),('3.2','Grammar'),('3.3 and Appendix 2','Vocabulary'),('Appendix 1','Phonics and sound symbol correspondences'),('Paper 1','Listening and dictation'),('Paper 2','Speaking and reading aloud'),('Paper 3','Reading and translation into English'),('Paper 4','Writing and translation into French')]),
'Biology - AQA':('8461','Higher',[(f'4.{i}',x) for i,x in enumerate(['Cell biology','Organisation','Infection and response','Bioenergetics','Homeostasis and response','Inheritance variation and evolution','Ecology'],1)]+[('3 and 8','Working scientifically and required practicals'),('7','Mathematical requirements')]),
'Chemistry - AQA':('8462','Higher',[(f'4.{i}',x) for i,x in enumerate(['Atomic structure and the periodic table','Bonding structure and properties of matter','Quantitative chemistry','Chemical changes','Energy changes','Rate and extent of chemical change','Organic chemistry','Chemical analysis','Chemistry of the atmosphere','Using resources'],1)]+[('3 and 8','Working scientifically and required practicals'),('7 and Appendix A','Mathematical requirements and periodic table')]),
'Physics - AQA':('8463','Higher',[(f'4.{i}',x) for i,x in enumerate(['Energy','Electricity','Particle model of matter','Atomic structure','Forces','Waves','Magnetism and electromagnetism','Space physics'],1)]+[('3 and 8','Working scientifically and required practicals'),('7 and Appendix A','Mathematical requirements and equations')])}
manifest=json.loads((ROOT/'specification-manifest.json').read_text(encoding='utf-8'))
for subject,(code,tier,topics) in subjects.items():
 folder=ROOT/subject
 lines=[f'# {subject}',f'\n**Exam year:** 2027 | **Code:** {code} | **Tier:** {tier}', '\n## Official sources\n']
 for doc in manifest:
  if doc['subject']==subject:
   name=Path(doc['file']).name
   lines.append(f'- [{name}](00%20-%20Specification/{name}) | [Official download]({doc["url"]}) | {doc["pages"]} pages')
 lines+=['\nThe PDF is the source of truth. The matching .txt file is a searchable convenience copy; tables and symbols may extract imperfectly. Downloaded and checked on 4 October 2026.','\n## Main topics\n']
 for i,(ref,title) in enumerate(topics,1):
  topic=folder/f'{i:02d} - {title}'
  topic.mkdir(parents=True,exist_ok=True)
  for kind in ['Revision Notes','Mind Maps','Questions and Answers']:(topic/kind).mkdir(exist_ok=True)
  (topic/'README.md').write_text(f'# {title}\n\n**Specification reference:** {ref}\n\n**Course:** {code} | **Exam year:** 2027 | **Tier:** {tier}\n\nUse the full official specification in ../00 - Specification. Match every resource to the exact sub-section and applicable tier.\n\n- Revision Notes: plain English explanations, everyday analogies and must-know facts.\n- Mind Maps: links between ideas in large or complex topics.\n- Questions and Answers: one combined document with each question, its answer and marking points together.\n\nResources have not yet been authored. Follow the project AGENTS.md and RESOURCE_GUIDELINES.md.\n',encoding='utf-8')
  lines.append(f'- {i:02d} - {title} (specification: {ref})')
 if subject=='English Literature - Eduqas':lines.append('\n## Course choices\n\nConfirmed: Macbeth, A Christmas Carol and An Inspector Calls. Use the new 15-poem anthology assessed from 2027.')
 if subject=='Geography - OCR A':lines.append('\n## School-specific details\n\nThe confirmed case studies are listed in CASE_STUDIES.md. Human fieldwork: Liverpool city. Physical fieldwork: River Alyn. Liverpool methods are recorded in CASE_STUDIES.md. Liverpool enquiry and qualitative findings are recorded in the fieldwork topic. Both Liverpool and River Alyn enquiries and qualitative findings are recorded. Numerical data, precise procedures and evaluation remain to be supplied.')
 if subject=='Computer Science - AQA':lines.append('\n## Course version\n\nUse the revised specification with first exams in 2027. Confirmed programming language: Python. Use pseudocode for algorithm descriptions, following AQA conventions where applicable.')
 (folder/'README.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
config={'exam_year':2027,'target_grades':[7,8],'subjects':{s:{'code':c,'tier':t,'topics':[{'reference':r,'title':n} for r,n in ts]} for s,(c,t,ts) in subjects.items()},'literature_texts':{'shakespeare':'Macbeth','nineteenth_century':'A Christmas Carol','post_1914':'An Inspector Calls','poetry':'Eduqas anthology for first assessment 2027'},'pending':['School Geography case studies and fieldwork investigations','Computer Science programming language']}
existing_path=ROOT/'project-config.json'
if existing_path.exists():
 existing=json.loads(existing_path.read_text(encoding='utf-8'))
 for key in ['computer_science','geography','pending','literature_texts']:
  if key in existing: config[key]=existing[key]
(ROOT/'project-config.json').write_text(json.dumps(config,indent=2),encoding='utf-8')
print('Created',len(subjects),'subject folders and',sum(len(v[2]) for v in subjects.values()),'topic folders')
