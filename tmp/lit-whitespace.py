from pathlib import Path
p=Path('scripts/literature_01_qa.py');s=p.read_text(encoding='utf-8-sig').replace("'> '+line+'  '","'> '+line");p.write_text(s,encoding='utf-8')
