from pathlib import Path
p=Path('scripts/build_chemistry_maps.py');s=p.read_text();s=s.replace(" if kind=='chem-electrodes':",''' if kind=='chem-profile':
  out=f'<path d="M25 17V90H{w-15}" stroke="#617480" fill="none"/><path d="M35 48H70C100 48 105 12 140 12S190 78 {w-60} 78H{w-25}" stroke="#2166ad" stroke-width="3" fill="none"/>'
  out+=a4.text(48,40,'R',15,anchor='middle',cls='diagram-label')+a4.text(w-45,69,'P',15,anchor='middle',cls='diagram-label')
  return out+a4.text(w/2,114,'Exothermic: products (P) lower',15,anchor='middle',cls='diagram-label')
 if kind=='chem-electrodes':''');p.write_text(s,encoding='utf-8')
p=Path('scripts/chemistry_maps.py');s=p.read_text()+'\nMAPS[5][0]["pics"]={1:("chem-profile",125)}\nMAPS[5][1]["pics"]={3:("chem-profile",125)}\n';p.write_text(s,encoding='utf-8')
