from pathlib import Path
p=Path('scripts/literature_map_figures.py');s=p.read_text().replace("'lit-nature':[('Memory','Pleasure returns'),('Stored fruit','Pleasure decays')]","'lit-nature':[('Wordsworth','Pleasure returns'),('Heaney','Fruit decays')]");p.write_text(s,encoding='utf-8')
