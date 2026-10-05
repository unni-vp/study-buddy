"""Chemistry SVG sources, with explicit particles, charges and labelled mechanisms."""
from chemistry_helpers import ROOT,TOPICS,SUBJECT
from biology_topic_diagrams import text,arrow,save,box
import math

def atomic():
 f=ROOT/SUBJECT/TOPICS[0]/'Diagrams';s=''
 for cx,counts,label in [(240,[2,8,1],'Na atom: 2,8,1'),(760,[2,8],'Na⁺ ion: 2,8')]:
  s+=text(cx,38,label,25,'middle')+f'<circle cx="{cx}" cy="205" r="30" fill="#f8d4ac" stroke="#ab762c"/>'+text(cx,212,'11p',19,'middle')
  for i,n in enumerate(counts):
   r=55+i*42;s+=f'<circle cx="{cx}" cy="205" r="{r}" fill="none" stroke="#819eaf"/>'
   for j in range(n):
    a=2*math.pi*j/n-math.pi/2;x=cx+r*math.cos(a);y=205+r*math.sin(a)
    s+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="#2166ad"/>'
  s+=text(cx,395,'Nucleus: 11 protons + 12 neutrons',19,'middle')
 s+=arrow('M415 200H590')+text(500,155,'Loses 1 electron',20,'middle')+text(500,448,'Blue dots = electrons. Shells are a simplified model, not to scale.',20,'middle')
 save(f,'sodium-ion','Sodium loses its outer electron; the nucleus stays unchanged',s,h=480)
 s=text(500,35,'Alpha-particle scattering: evidence for the nucleus',25,'middle')
 s+='<circle cx="480" cy="228" r="17" fill="#f6c39b" stroke="#ac6a21"/>'+text(480,234,'+',23,'middle')
 for y in [95,135,335]:s+=arrow(f'M55 {y}H925')
 s+=arrow('M55 195H360Q440 195 445 150L490 100')+arrow('M55 229H388Q433 229 397 258L290 300')
 s+=text(725,177,'Most pass straight through',20,'middle')+text(650,267,'Small positive nucleus',20)+text(570,75,'Some deflect',20)+text(160,320,'Very few return',20,'middle')
 s+=text(500,397,'Most of the atom is empty space; mass is concentrated in the nucleus.',21,'middle')
 save(f,'alpha-scattering','Schematic alpha paths showing straight, deflected and backward scattering',s,h=435)
if __name__=='__main__':atomic()

def bonding():
 f=ROOT/SUBJECT/TOPICS[1]/'Diagrams'
 s=text(500,35,'Sodium chloride: opposite ions attract',26,'middle')
 s+=text(250,160,'[ Na ]⁺',40,'middle')+text(700,160,'Cl',34,'middle')
 s+='<path d="M625 65H610V250H625M775 65H790V250H775" fill="none" stroke="#2166ad" stroke-width="3"/>'+text(806,75,'−',28)
 pts=[(680,90),(720,90),(650,140),(650,170),(680,225),(720,225),(750,140)]
 for x,y in pts:s+=f'<circle cx="{x}" cy="{y}" r="6" fill="#2166ad"/>'
 s+='<path d="M744 164L756 176M756 164L744 176" stroke="#b46f27" stroke-width="3"/>'
 s+=text(250,292,'2,8 electrons',23,'middle')+text(700,292,'2,8,8 electrons',23,'middle')+text(500,348,'● chlorine electron     × electron transferred from sodium',22,'middle')+text(500,387,'Only the chloride outer shell is drawn; ions form a giant lattice.',20,'middle')
 save(f,'ionic-bond','Na plus and Cl minus, showing seven original and one transferred chloride outer electrons',s,h=420)
 s=text(500,29,'Covalent molecules: outer electrons only',24,'middle')
 mols=[('H₂',['H','H'],[(80,110),(160,110)],[(0,1,1)],{}),('Cl₂',['Cl','Cl'],[(80,110),(160,110)],[(0,1,1)],{0:[(-1,0),(0,-1),(0,1)],1:[(1,0),(0,-1),(0,1)]}),('O₂',['O','O'],[(80,110),(160,110)],[(0,1,2)],{0:[(-1,0),(0,-1)],1:[(1,0),(0,1)]}),('N₂',['N','N'],[(80,110),(160,110)],[(0,1,3)],{0:[(-1,0)],1:[(1,0)]}),('HCl',['H','Cl'],[(80,110),(160,110)],[(0,1,1)],{1:[(1,0),(0,-1),(0,1)]}),('H₂O',['O','H','H'],[(120,110),(40,110),(120,190)],[(0,1,1),(0,2,1)],{0:[(1,0),(0,-1)]}),('NH₃',['N','H','H','H'],[(120,110),(40,110),(200,110),(120,190)],[(0,1,1),(0,2,1),(0,3,1)],{0:[(0,-1)]}),('CH₄',['C','H','H','H','H'],[(120,120),(40,120),(200,120),(120,40),(120,200)],[(0,1,1),(0,2,1),(0,3,1),(0,4,1)],{})]
 def electron(x,y,cross):
  return f'<path d="M{x-3} {y-3}L{x+3} {y+3}M{x+3} {y-3}L{x-3} {y+3}" stroke="#ac6a21" stroke-width="2"/>' if cross else f'<circle cx="{x}" cy="{y}" r="3.5" fill="#2166ad"/>'
 for i,(label,atoms,xy,bonds,lone) in enumerate(mols):
  ox=(i%4)*250;oy=55+(i//4)*300;s+=f'<g transform="translate({ox} {oy})"><rect x="5" y="0" width="240" height="287" rx="12" fill="#f7fafc" stroke="#a7bdce"/>'+text(125,274,label,24,'middle')
  for a,(x,y) in zip(atoms,xy):s+=text(x,y+8,a,27,'middle')
  for a,b,n in bonds:
   x1,y1=xy[a];x2,y2=xy[b];mx=(x1+x2)/2;my=(y1+y2)/2
   for j in range(n):
    d=(j-(n-1)/2)*15
    if y1==y2:s+=electron(mx-4,my+d,False)+electron(mx+4,my+d,True)
    else:s+=electron(mx+d,my-4,False)+electron(mx+d,my+4,True)
  for a,dirs in lone.items():
   x,y=xy[a]
   for dx,dy in dirs:
    px=x+dx*32;py=y+dy*32;s+=electron(px+(5 if dy else 0),py+(5 if dx else 0),bool(a%2))+electron(px-(5 if dy else 0),py-(5 if dx else 0),bool(a%2))
  s+='</g>'
 s+=text(500,690,'A pair between atoms = a bond. Dots and crosses track origin, not different electron types.',20,'middle')
 save(f,'covalent-molecules','Dot-and-cross examples of all eight specified simple molecules',s,h=715)
