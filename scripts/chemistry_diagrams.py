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

def quantitative():
 f=ROOT/SUBJECT/TOPICS[2]/'Diagrams';s=text(500,36,'Reacting masses: use moles to cross the equation',25,'middle')
 for x,title,content in [(25,'Mass of Mg','6.0 g'),(350,'Moles of Mg','0.25 mol'),(675,'Moles of MgO','0.25 mol')]:
  s+=f'<rect x="{x}" y="85" width="280" height="105" rx="15" fill="#edf5ff" stroke="#2166ad"/>'+text(x+140,120,title,22,'middle')+text(x+140,164,content,25,'middle')
 s+=arrow('M308 139H344')+arrow('M633 139H669')+text(165,234,'÷ 24 g/mol',22,'middle')+text(490,234,'Mg : MgO = 2 : 2',22,'middle')
 s+=arrow('M815 198V277')+text(700,269,'× 40 g/mol',20,'end')
 s+='<rect x="675" y="285" width="280" height="100" rx="15" fill="#e4f4eb" stroke="#18837b"/>'+text(815,325,'Mass of MgO',22,'middle')+text(815,365,'10 g',25,'middle')
 s+=text(340,325,'2Mg + O₂ → 2MgO',28,'middle')+text(340,367,'Oxygen is in excess.',21,'middle')
 save(f,'mole-route','Magnesium mass divided by molar mass, mole ratio, then product moles multiplied by molar mass',s,h=415)

def changes():
 f=ROOT/SUBJECT/TOPICS[3]/'Diagrams'
 s=text(500,32,'Titration: measure the acid volume at the endpoint',25,'middle')
 s+='<path d="M360 65V275H390V65" fill="none" stroke="#2166ad" stroke-width="3"/><path d="M360 130Q375 141 390 130V275H360Z" fill="#e0f2fe" stroke="#2166ad"/><path d="M375 276V318M350 286H400" stroke="#425968" stroke-width="4"/>'
 for y in range(80,270,15):s+=f'<path d="M360 {y}H370" stroke="#2166ad"/>'
 s+='<path d="M351 342V366L285 474Q275 489 298 489H452Q475 489 465 474L399 366V342" fill="none" stroke="#425968" stroke-width="3"/><path d="M313 432H438L462 474H288Z" fill="#f1c7dc"/><rect x="270" y="500" width="212" height="16" fill="white" stroke="#738893"/>'
 s+=text(570,105,'Burette: acid of known concentration',21)+arrow('M550 112H398')+text(570,171,'Read meniscus at eye level',21)+arrow('M550 177L398 133')+text(570,290,'Tap controls drops near endpoint',21)+arrow('M550 295H410')
 s+=text(560,396,'Conical flask: measured alkali',21)+text(560,427,'volume + a few drops of indicator',21)+arrow('M545 437H453')+text(565,510,'White tile: see colour change',21)+arrow('M550 513H495')
 save(f,'titration','Labelled burette, tap, measured alkali and indicator in conical flask, white tile',s,h=550)
 s=text(500,32,'Electrolysis: ions carry charge in the liquid',25,'middle')
 s+='<rect x="355" y="65" width="290" height="65" rx="10" fill="#edf5ff" stroke="#2166ad"/>'+text(500,105,'DC power supply',23,'middle')
 s+='<path d="M355 95H205V175M645 95H795V175" fill="none" stroke="#425968" stroke-width="3"/><path d="M95 205V430H905V205" fill="none" stroke="#738893" stroke-width="3"/><rect x="97" y="250" width="806" height="178" fill="#e5f3f8"/><rect x="190" y="175" width="30" height="190" fill="#526573"/><rect x="780" y="175" width="30" height="190" fill="#526573"/>'
 s+=text(105,158,'− cathode',23,'middle')+text(895,158,'+ anode',23,'middle')
 s+='<circle cx="375" cy="300" r="26" fill="#dae7fb" stroke="#2166ad"/><circle cx="625" cy="300" r="26" fill="#ffe3ce" stroke="#b96821"/>'+text(375,308,'+',27,'middle')+text(625,308,'−',27,'middle')
 s+=arrow('M340 300H232')+arrow('M660 300H768')+text(375,380,'Positive ions',20,'middle')+text(625,380,'Negative ions',20,'middle')
 s+=text(245,474,'Gain electrons → reduction',22,'middle')+text(755,474,'Lose electrons → oxidation',22,'middle')+text(500,525,'Electrolyte: molten ionic compound or aqueous solution',22,'middle')
 save(f,'electrolysis','Positive ions move to negative cathode and gain electrons; negative ions move to positive anode and lose electrons',s,h=555)

def energy():
 f=ROOT/SUBJECT/TOPICS[4]/'Diagrams';s=''
 for x,exo in [(0,True),(500,False)]:
  yr=220 if exo else 350;yp=350 if exo else 220
  s+=text(x+250,32,'Exothermic' if exo else 'Endothermic',27,'middle')
  s+=f'<path d="M{x+55} 400V68M{x+55} 400H{x+465}" stroke="#526573" stroke-width="2" fill="none"/>'+text(x+60,62,'Energy',20)+text(x+255,442,'Progress of reaction →',20,'middle')
  s+=f'<path d="M{x+80} {yr}H{x+145}C{x+190} {yr} {x+192} 100 {x+245} 100S{x+310} {yp} {x+360} {yp}H{x+425}" fill="none" stroke="{ "#2166ad" if exo else "#b76a22"}" stroke-width="4"/>'
  s+=f'<path d="M{x+145} {yr}H{x+460}M{x+245} 100H{x+280}" stroke="#adbcc6" stroke-dasharray="5 5"/>'
  s+=arrow(f'M{x+270} {yr}V105')+text(x+330,145,'Activation',19)+text(x+330,170,'energy',19)
  s+=arrow(f'M{x+448} {yr}V{yp}')+text(x+112,yr-14,'Reactants',20,'middle')+text(x+370,yp+28,'Products',20,'middle')
  s+=text(x+250,480,'Products lower: energy out' if exo else 'Products higher: energy in',21,'middle')
 s+=text(500,518,'Right-hand vertical arrows: overall energy change between the two levels.',20,'middle')
 save(f,'reaction-profiles','Two profiles: activation energy from reactants to peak; overall change between reactants and products',s,h=550)
 s=text(500,32,'Hydrogen fuel cell with an acidic electrolyte',25,'middle')
 s+='<rect x="420" y="215" width="160" height="255" fill="#eadff5" stroke="#7750a1"/><rect x="285" y="210" width="35" height="260" fill="#526573"/><rect x="680" y="210" width="35" height="260" fill="#526573"/>'
 s+='<path d="M302 210V95H410M590 95H697V210" fill="none" stroke="#2166ad" stroke-width="3"/><rect x="410" y="70" width="180" height="50" rx="8" fill="#fff1cc" stroke="#aa7e22"/>'+text(500,102,'Electrical load',21,'middle')
 s+=arrow('M332 95H396')+arrow('M600 95H660')+text(500,153,'Electrons through the external circuit →',21,'middle')
 s+=text(150,190,'Hydrogen electrode (−)',20,'middle')+text(850,190,'Oxygen electrode (+)',20,'middle')
 s+=text(117,283,'H₂ in',24,'middle')+arrow('M170 277H276')+text(881,283,'O₂ in',24,'middle')+arrow('M830 277H725')
 s+=text(399,343,'H⁺',26,'middle')+arrow('M425 337H660')+text(500,405,'H⁺ crosses',20,'middle')+text(500,432,'electrolyte',20,'middle')
 s+=arrow('M725 409H828')+text(884,414,'H₂O out',23,'middle')
 s+=text(220,510,'H₂ loses electrons',22,'middle')+text(780,510,'O₂ gains electrons',22,'middle')+text(500,555,'Overall: 2H₂ + O₂ → 2H₂O',26,'middle')
 save(f,'hydrogen-fuel-cell','Acidic fuel cell: hydrogen oxidised; electrons pass through load while protons cross electrolyte; oxygen reduced to water',s,h=585)

if __name__=='__main__':
 import sys
 {1:atomic,2:bonding,3:quantitative,4:changes,5:energy}[int(sys.argv[1])]()
