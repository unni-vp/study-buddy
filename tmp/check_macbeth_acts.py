from pathlib import Path
import re,json
s=Path('English Literature - Eduqas/01 - Macbeth/Revision Notes/Macbeth - Revision Notes.md').read_text(encoding='utf-8')
t=Path('tmp/macbeth-folger.txt').read_text(encoding='utf-8')
def norm(x): return re.sub(r'\s+',' ',x).replace('’',"'").replace('“','"').replace('”','"').lower()
parts=s.split('## Act ')[1:]
n=0
for part in parts:
 act=part[0]
 for line in part.split('## Macbeth:')[0].splitlines():
  if not line.startswith('| “'): continue
  for q in re.findall('“([^”]+)”',line.split('|')[1]):
   assert norm(q) in norm(t),(act,q)
   n+=1
print(f'PASS: {n} act-table quotation fragments occur in the primary text.')
layout=json.loads(Path('English Literature - Eduqas/01 - Macbeth/revision-layout.json').read_text())
assert [g['title'] for g in layout['groups']]==['Story / Acts','Characters','Themes and dramatic methods','Quotations and essay writing']
assert len(json.loads(Path('English Literature - Eduqas/01 - Macbeth/resource-coverage.json').read_text())['mindmaps'])==5
print('PASS: four direct reading groups; all five mind-map metadata entries retained.')
