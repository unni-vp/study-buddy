from pathlib import Path
import json
root=Path('Chemistry - AQA'); total=0
for folder in sorted(root.iterdir()):
 if folder.is_dir() and folder.name[:2] in ['01','02','03','04','05']:
  data=json.loads((folder/'qa-evidence.json').read_text(encoding='utf-8'));n=len(data['questions']);total+=n
  if folder.name.startswith('05'):
   data['reviewed']='2026-10-06';(folder/'qa-evidence.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
  print(folder.name,':',n,'Q&A;',len(list((folder/'Mind Maps').glob('*.svg'))),'mindmaps')
print('Total Q&A:',total)
