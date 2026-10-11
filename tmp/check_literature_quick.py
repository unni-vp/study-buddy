from pathlib import Path
import re,json,subprocess
s=Path('tmp/macbeth-folger.txt').read_text(encoding='utf-8')
def norm(x): return re.sub(r'\s+',' ',x).replace('’',"'").lower().strip(' .;:,!?')
full=norm(s)
qa=json.loads(Path('English Literature - Eduqas/01 - Macbeth/qa-evidence.json').read_text())
for item in qa['questions']:
 if item['marks']==25:
  qs=re.findall('“([^”]+)”',item['answer'])
  for quotation in qs:
   assert norm(quotation) in full,(item['number'],quotation)
  print('PASS: Macbeth essay',item['number'],len(qs),'quotation fragments verified')
old=subprocess.check_output(['git','show','HEAD:English Literature - Eduqas/01 - Macbeth/qa-evidence.json'],encoding='utf-8')
assert [x['answer'] for x in json.loads(old)['questions'] if x['marks']==15]==[x['answer'] for x in qa['questions'] if x['marks']==15]
for topic,count in [('01 - Macbeth',40),('02 - Poetry anthology - assessment from 2027',53)]:
 data=json.loads((Path('English Literature - Eduqas')/topic/'qa-evidence.json').read_text())
 items=data['questions']
 assert len(items)==count
 assert [i['number'] for i in items]==list(range(1,count+1))
 assert len([i for i in items if i['marks']==1])==15
 assert len([i for i in items if i['marks']==2])==15
 assert [i['marks'] for i in items]==sorted(i['marks'] for i in items)
 print('PASS:',topic,'counts, ordering and numbering')
