from pathlib import Path
for n,func,title in [(1,'macbeth_quick','Macbeth'),(2,'poetry_quick','Poetry anthology')]:
 p=Path(f'scripts/literature_0{n}_qa.py')
 s=p.read_text(encoding='utf-8')
 s=s.replace('from literature_qa_writer import q,write_bank','from literature_qa_writer import q,write_bank\nfrom literature_quick_revision import '+func)
 s=s.replace(f"write_bank({n},'{title}',items,",f"write_bank({n},'{title}',{func}()+items,")
 # Keep practice-mark provenance in the separate sources page, not beside each answer.
 needle=f"write_bank({n},'{title}',{func}()+items,'"
 assert needle in s
 s=s.replace(needle,needle+'The 1- and 2-mark questions are original quick-revision practice, not Eduqas examination question formats. Their practice marks indicate the amount of recall or explanation expected. ')
 p.write_text(s,encoding='utf-8')
p=Path('scripts/literature_qa_writer.py');s=p.read_text()
s=s.replace("lines.append('## '+str(last)+' marks')","lines.append('## '+str(last)+(' mark' if last==1 else ' marks'))")
p.write_text(s,encoding='utf-8')
