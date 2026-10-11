"""Small explanatory Physics drawings, at fixed readable label sizes."""
import a4_mindmaps as a4

def draw(kind,w,h):
 def label(x,y,s,anchor='middle'):
  return a4.text(x,y,s,15,anchor=anchor,cls='diagram-label')
 def line(d,c='#2166ad',width=2):
  return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{width}"/>'
 def arrow(x,y,x2,y2):
  import math
  a=math.atan2(y2-y,x2-x)
  return line(f'M{x} {y}L{x2} {y2}M{x2-7*math.cos(a-.6)} {y2-7*math.sin(a-.6)}L{x2} {y2}L{x2-7*math.cos(a+.6)} {y2-7*math.sin(a+.6)}')
 if kind=='ph-particles':
  b=''
  for j,name in enumerate(['Solid','Liquid','Gas']):
   x=(j+.5)*w/3
   coords=[(-18,18),(0,18),(18,18),(-18,36),(0,36),(18,36)] if j==0 else ([(-20,22),(-3,15),(16,23),(-15,39),(5,36),(23,43)] if j==1 else [(-27,9),(28,44),(0,31)])
   b+=f'<rect x="{x-w/6+3}" y="0" width="{w/3-6}" height="60" rx="5" fill="#f0f6fc" stroke="#8aa4b8"/>'
   for dx,y in coords:b+=f'<circle cx="{x+dx}" cy="{y}" r="5" fill="#2166ad"/>'
   b+=label(x,83,name)
  return b
 if kind=='ph-specific':
  b=label(5,15,'Temperature rise',anchor='start')+line(f'M15 25V85H{w-10}','#6e7d89')
  b+=line(f'M17 83L{w-30} 30',width=3)+line(f'M17 83L{w-30} 62','#18837b',3)
  return b+label(w-25,27,'Lower c','end')+label(w-25,59,'Higher c','end')+label(w/2,109,'Energy supplied → (same mass)')
 if kind=='ph-heat':
  b=label(6,15,'Temperature',anchor='start')+line(f'M12 25V85H{w-10}','#6e7d89')
  b+=line(f'M20 78L{w*.25} 58H{w*.47}L{w*.68} 32H{w-16}',width=3)
  return b+label(w/2,109,'Energy supplied →')
 if kind=='ph-spring':
  b=label(5,15,'Force',anchor='start')+line(f'M15 25V85H{w-10}','#6e7d89')
  b+=f'<path d="M17 83L{w-35} 30V83Z" fill="#deecfa"/>'+line(f'M17 83L{w-35} 30',width=3)
  return b+label(w*.66,73,'Area = ½ke²')+label(w/2,109,'Extension →')
 if kind=='ph-circuit':
  b=line(f'M20 34V12H65M20 53V100H{w-20}V12H{w/2+22}M65 12H{w/2-22}M65 12V65H{w/2-22}M{w/2+22} 65H{w-20}M10 34H30M14 53H26')
  for y in [12,65]:b+=f'<rect x="{w/2-22}" y="{y-7}" width="44" height="14" fill="#fffefa" stroke="#2166ad" stroke-width="2"/>'
  return b+label(w/2,125,'Parallel paths share the same pd')
 if kind=='ph-half-life':
  b=''
  for j,(v,t) in enumerate([(400,0),(200,2),(100,4)]):
   x=(j+.5)*w/3
   b+=f'<rect x="{x-17}" y="{70-v/8}" width="34" height="{v/8}" fill="#689acc"/>'+label(x,90,f'{t} h')+label(x,15,str(v))
  return b+label(w/2,113,'Count rate halves every 2 h')
 if kind=='ph-scatter':
  cx=w*.67;b=f'<circle cx="{cx}" cy="45" r="9" fill="#c77240"/>'+label(cx,51,'+')
  b+=arrow(10,15,w-12,15)+arrow(10,77,w-12,77)
  b+=line(f'M10 43H{cx-32}Q{cx-12} 43 {cx-32} 58H{cx-60}')
  b+=arrow(cx-32,58,cx-62,58)
  return b+label(w/2,105,'Most pass; very few turn back')
 if kind=='ph-vector':
  x=w/2-45;b=arrow(x,75,x+60,75)+arrow(x+60,75,x+60,15)+arrow(x,75,x+60,15)
  return b+label(w/2,105,'Tip-to-tail: diagonal is resultant')
 if kind=='ph-lever':
  b=line(f'M15 30H{w-15}',width=5)+f'<path d="M{w*.4} 32l-14 28h28Z" fill="#d4dfeb" stroke="#2166ad"/>'
  b+=arrow(30,5,30,27)+arrow(w-30,5,w-30,27)
  return b+label(w/2,87,'Opposite moments about pivot')
 if kind=='ph-motion':
  b=label(5,15,'Velocity',anchor='start')+line(f'M15 25V85H{w-10}','#6e7d89')
  b+=f'<path d="M17 83L{w*.55} 32H{w-20}V83Z" fill="#deecfa"/>'+line(f'M17 83L{w*.55} 32H{w-20}',width=3)
  return b+label(w*.65,74,'Area = displacement')+label(w/2,109,'Time →')
 if kind=='ph-terminal':
  b=f'<circle cx="{w/2}" cy="45" r="13" fill="#dcecf9" stroke="#2166ad"/>'
  b+=arrow(w/2,30,w/2,2)+arrow(w/2,60,w/2,88)
  return b+label(w/2+20,17,'Drag',anchor='start')+label(w/2+20,83,'Weight',anchor='start')+label(w/2,114,'Balanced forces → constant velocity')
 return None
