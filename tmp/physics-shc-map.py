from pathlib import Path
p=Path('scripts/physics_map_figures.py');s=p.read_text(encoding='utf-8');s=s.replace(" if kind=='ph-heat':",''' if kind=='ph-specific':
  b=label(5,15,'Temperature rise',anchor='start')+line(f'M15 25V85H{w-10}','#6e7d89')
  b+=line(f'M17 83L{w-30} 30',width=3)+line(f'M17 83L{w-30} 62','#18837b',3)
  return b+label(w-25,27,'Lower c','end')+label(w-25,59,'Higher c','end')+label(w/2,109,'Energy supplied → (same mass)')
 if kind=='ph-heat':''');p.write_text(s,encoding='utf-8')
p=Path('scripts/physics_maps.py');s=p.read_text(encoding='utf-8').replace("2:(0,'ph-heat',120)","2:(0,'ph-specific',120)");p.write_text(s,encoding='utf-8')
