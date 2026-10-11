from pathlib import Path
p=Path('scripts/physics_map_figures.py');s=p.read_text(encoding='utf-8-sig');a=s.index(" if kind=='ph-circuit':");b=s.index(" if kind=='ph-half-life':",a)
s=s[:a]+''' if kind=='ph-circuit':
  b=line(f'M20 34V12H{w/2-22}M{w/2+22} 12H{w-20}V85H{w/2+22}M{w/2-22} 85H20V53M10 34H30M14 53H26')
  for y in [12,85]:b+=f'<rect x="{w/2-22}" y="{y-7}" width="44" height="14" fill="#fffefa" stroke="#2166ad" stroke-width="2"/>'
  # A third branch connects directly across the cell terminals via the outer nodes.
  b=line(f'M20 34V12H{w/2-22}M{w/2+22} 12H{w-20}V85H20V53M10 34H30M14 53H26M20 85V105H{w-20}V85') if False else b
  # This drawing is a series loop. Use explicit separate parallel branch nodes instead.
  b=line(f'M20 34V12H65M20 53V100H{w-20}V12H{w/2+22}M65 12H{w/2-22}M65 12V65H{w/2-22}M{w/2+22} 65H{w-20}M10 34H30M14 53H26')
  for y in [12,65]:b+=f'<rect x="{w/2-22}" y="{y-7}" width="44" height="14" fill="#fffefa" stroke="#2166ad" stroke-width="2"/>'
  return b+label(w/2,125,'Parallel paths share the same pd')
''' +s[b:]
# Actual parallel branches must not have a bottom return connecting supply bottom to branch-left: current geometry correct (left top splits, right common returns to bottom).
a=s.index(" if kind=='ph-impact':");b=s.index(' return None',a);s=s[:a]+s[b:];p.write_text(s,encoding='utf-8')
p=Path('scripts/build_physics_maps.py');s=p.read_text(encoding='utf-8-sig').replace('base=a4.illustration','from physics_map_figures import draw\nbase=a4.illustration').replace('def illustration(kind,w,h):','def illustration(kind,w,h):\n custom=draw(kind,w,h)\n if custom is not None:return custom');p.write_text(s,encoding='utf-8')
p=Path('scripts/physics_maps.py');s=p.read_text(encoding='utf-8-sig');s+='''
# Explanatory drawings occupy reserved panel space; typography stays fixed.
FIGURES={
 1:{1:(3,'ph-spring',120),2:(0,'ph-heat',120)},
 2:{1:(3,'ph-circuit',140),2:(3,'ph-circuit',140)},
 3:{0:(0,'ph-particles',95),1:(0,'ph-particles',95),2:(2,'ph-heat',120)},
 4:{0:(3,'ph-half-life',125),1:(2,'ph-scatter',115),2:(2,'ph-half-life',125),3:(0,'ph-scatter',115)},
 5:{0:(3,'ph-motion',120),1:(5,'ph-spring',120),2:(0,'ph-lever',100),3:(5,'ph-motion',120),4:(2,'ph-terminal',125)}
}
# Scattering illustrates the atom-model map only, not exposure routes.
FIGURES[4].pop(3)
for n,entries in FIGURES.items():
 for index,(panel,kind,height) in entries.items():MAPS[n][index]['pics'][panel]=(kind,height)
''';p.write_text(s,encoding='utf-8')
