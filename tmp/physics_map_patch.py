from pathlib import Path
p=Path('scripts/physics_diagrams.py');s=p.read_text(encoding='utf-8-sig').replace('H850V280H120V90M260','H850V280M120 90V280H345M260');p.write_text(s,encoding='utf-8')
p=Path('scripts/build_physics_maps.py');s=p.read_text(encoding='utf-8-sig');needle=" return base(kind,w,h)";addition=''' if kind=='field-positive':
  x=w/2;y=34
  b=f'<circle cx="{x}" cy="{y}" r="15" fill="#fbe2cd" stroke="#b46d29"/>'+a4.text(x,y+6,'+',20,anchor='middle',cls='diagram-label')
  for sign in [-1,1]:
   start=x+sign*20;end=x+sign*85
   b+=f'<path d="M{start} {y}H{end}m{-sign*7} -5 {sign*7} 5 {-sign*7} 5" stroke="#2166ad" fill="none" stroke-width="2"/>'
  return b+a4.text(w/2,72,'Positive sphere: field points out',15,anchor='middle',cls='diagram-label')
''';assert needle in s;s=s.replace(needle,addition+needle);p.write_text(s,encoding='utf-8')
