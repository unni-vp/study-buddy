from pathlib import Path
p=Path('scripts/literature_maps.py');s=p.read_text();s+='\nfrom literature_poetry_maps import MAPS as POETRY_MAPS\nMAPS[2]=POETRY_MAPS\n';p.write_text(s,encoding='utf-8')
p=Path('scripts/literature_map_figures.py');s=p.read_text(encoding='utf-8-sig');needle=" if kind=='lit-partnership':";new=''' if kind in ('lit-camera','lit-nature','lit-absence','lit-bond','lit-return','lit-home'):
  pairs={
   'lit-camera':[('Human suffering','Selected image'),('Selected image','Viewer response')],
   'lit-nature':[('Memory','Pleasure returns'),('Stored fruit','Pleasure decays')],
   'lit-absence':[('Sonnet 29','Imagined release'),('Dusting the Phone','Unresolved wait')],
   'lit-bond':[('Birth','Physical separation'),('Growing up','Emotional bond')],
   'lit-return':[('Returns alive','Family falls silent'),('Survival','Social exclusion')],
   'lit-home':[('Remembered home','Future promise'),('Present pain','Hoped-for relief')]}[kind]
  for i,(left,right) in enumerate(pairs):
   y=18+i*48
   out += [t(0,y,left,15,'#2166ad',cls='diagram-label'),t(width,y,right,15,'#7750a1',anchor='end',cls='diagram-label'),f'<path d="M5 {y+12}H{width-5}m-6-4 6 4-6 4" stroke="#18837b" stroke-width="2" fill="none"/>']
 elif kind=='lit-partnership':''';s=s.replace(needle,new);p.write_text(s,encoding='utf-8')
