from pathlib import Path
p=Path('scripts/literature_01_notes.py');s=p.read_text(encoding='utf-8-sig').replace('Out, damned spot!','Out, damned spot').replace('; no single literary word earns credit by itself.','.');p.write_text(s,encoding='utf-8')
