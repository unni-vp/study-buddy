"""Small conceptual diagrams for Literature mind maps, with A4-readable labels."""
import a4_mindmaps as a4
_original=a4.illustration

def illustration(kind,width,height):
 if not kind.startswith('lit-'): return _original(kind,width,height)
 t=a4.text;out=[]
 if kind=='lit-partnership':
  for y,left,right,color in [(20,'Shared plan','Macbeth alone','#2166ad'),(72,'Her control','Her isolation','#7750a1')]:
   out += [t(0,y,left,15,color,cls='diagram-label'),t(width,y,right,15,color,anchor='end',cls='diagram-label'),f'<path d="M8 {y+12}H{width-8}m-6-4 6 4-6 4" stroke="{color}" stroke-width="2" fill="none"/>']
 elif kind=='lit-downfall':
  labels=['Defender','Killer','Tyrant'];xs=[width*.14,width*.50,width*.86];ys=[20,50,80]
  out.append(f'<path d="M{xs[0]} 29L{xs[1]} 59L{xs[2]} 89" stroke="#2166ad" stroke-width="3" fill="none"/>')
  for x,y,label in zip(xs,ys,labels):out.append(t(x,y,label,15,anchor='middle',cls='diagram-label'))
  out.append(t(width/2,117,'Violence changes its purpose',15,anchor='middle',cls='diagram-label'))
 elif kind=='lit-guilt':
  for x,fill,label in [(width*.24,'#b74551','Blood on hands'),(width*.76,'#f8e0e3','Stain in the mind')]:
   out.append(f'<path d="M{x} 3Q{x-24} 32 {x-18} 43Q{x} 67 {x+18} 43Q{x+24} 32 {x} 3Z" fill="{fill}" stroke="#b74551" stroke-width="2"/>')
   out.append(t(x,83,label,15,anchor='middle',cls='diagram-label'))
  out.append(f'<path d="M{width*.4} 35H{width*.6}m-6-4 6 4-6 4" stroke="#b74551" stroke-width="2" fill="none"/>')
 elif kind=='lit-irony':
  for y,label,color in [(22,'Duncan: trusts the welcome','#18837b'),(60,'Audience: knows the plot','#b74551')]:
   out.append(f'<rect x="0" y="{y-20}" width="{width}" height="31" rx="6" fill="{color}" opacity=".08"/>')
   out.append(t(width/2,y,label,15,color,anchor='middle',cls='diagram-label'))
  out.append(t(width/2,100,'Unequal knowledge → tension',15,anchor='middle',cls='diagram-label'))
 else:raise ValueError(kind)
 return ''.join(out)

a4.illustration=illustration
