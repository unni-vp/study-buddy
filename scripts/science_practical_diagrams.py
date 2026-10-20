"""Editable, labelled apparatus diagrams; add them beside their practical methods.

Run with a subject and topic number. Shared assets live with the science topic,
and the practical-skills chapter reuses them rather than duplicating artwork.
"""
from pathlib import Path
from html import escape
import argparse, json, math, os, re

ROOT=Path(__file__).resolve().parents[1] if Path(__file__).parent.name=='scripts' else Path('D:/Shreya/study-buddy')
INK='#182c3b';BLUE='#17658c';TEAL='#147a70';ORANGE='#ad4c10';WATER='#d8effa'

class SVG:
 def __init__(self,title,h=560):
  self.title=title;self.h=h;self.parts=[]
 def text(self,x,y,value,size=22,color=INK,bold=False,anchor='start'):
  self.parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{700 if bold else 400}" text-anchor="{anchor}">{escape(str(value))}</text>')
 def lines(self,x,y,values,**kw):
  for i,v in enumerate(values):self.text(x,y+30*i,v,**kw)
 def path(self,d,color=INK,w=3,dash=False,fill='none'):
  self.parts.append(f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"'+(' stroke-dasharray="7 6"' if dash else '')+'/>')
 def rect(self,x,y,w,h,fill='white',stroke=INK,r=5):
  self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
 def circle(self,x,y,r,fill='white',stroke=INK):
  self.parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
 def arrow(self,x1,y1,x2,y2,color=BLUE):
  self.path(f'M{x1} {y1}L{x2} {y2}',color)
  a=math.atan2(y2-y1,x2-x1)
  self.path(f'M{x2-12*math.cos(a-.45)} {y2-12*math.sin(a-.45)}L{x2} {y2}L{x2-12*math.cos(a+.45)} {y2-12*math.sin(a+.45)}',color)
 def label(self,x,y,value,tx,ty,anchor='start'):
  self.text(x,y,value,anchor=anchor)
  start=x+len(value)*11+12 if tx>x else x-12
  self.path(f'M{start} {y-6}L{tx} {ty}',color='#65808c',w=1.5)
 def resistor(self,x,y,w=85):
  self.rect(x,y-15,w,30)
 def meter(self,x,y,letter):
  self.circle(x,y,25);self.text(x,y+8,letter,24,bold=True,anchor='middle')
 def junction(self,x,y):self.circle(x,y,4,INK,INK)
 def beaker(self,x,y,w=150,h=170,liquid=True):
  if liquid:self.rect(x+3,y+65,w-6,h-68,WATER,stroke='none',r=0)
  self.path(f'M{x} {y}V{y+h}H{x+w}V{y}');self.path(f'M{x} {y}h-10m{w+10} 0h10')
 def tube(self,x,y,h=160,color=WATER,level=60):
  self.path(f'M{x} {y}V{y+h-20}Q{x+22} {y+h+20} {x+44} {y+h-20}V{y}',fill='white')
  self.path(f'M{x+5} {y+level}V{y+h-20}Q{x+22} {y+h+8} {x+39} {y+h-20}V{y+level}Z',color=color,w=1,fill=color)
 def titleline(self):self.text(30,38,self.title,27,color=BLUE,bold=True)
 def output(self,description):
  return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 {self.h}" role="img" aria-labelledby="title desc"><title id="title">{escape(self.title)}</title><desc id="desc">{escape(description)}</desc><rect width="1000" height="{self.h}" fill="#fffefa"/><g font-family="Segoe UI, Arial, sans-serif">'+''.join(self.parts)+'</g></svg>'

def iv():
 s=SVG('Measuring an I–V characteristic',610);s.titleline()
 # A single series loop. Only the voltmeter bridges the test component.
 s.path('M100 130H140M190 130H240M300 130H470M580 130H900V390H720M560 390H295M245 390H100V130')
 s.path('M240 108V152M260 116V144M260 130H280M280 108V152M300 116V144')
 s.path('M140 130L180 110');s.text(85,85,'Switch',20)
 s.text(270,87,'Low-voltage DC',anchor='middle')
 s.resistor(470,130,110);s.arrow(475,165,575,94);s.text(525,208,'Variable resistor',anchor='middle')
 s.meter(270,390,'A');s.rect(560,370,160,40)
 s.text(640,448,'Test component',anchor='middle')
 s.path('M530 390V280H615M665 280H750V390');s.meter(640,280,'V')
 for x in (530,750):s.junction(x,390)
 s.text(270,448,'Ammeter in series',anchor='middle')
 s.text(640,245,'Voltmeter across component',anchor='middle')
 s.lines(40,510,['Swap the test component: fixed resistor, filament lamp or diode.',
 'Vary the potential difference; record paired current and voltage readings.',
 'For a diode, keep a protective resistor in series and limit the current.'])
 return s

def wire():
 s=SVG('Resistance of a wire: select a measured length',630);s.titleline()
 s.path('M100 130H140M190 130H240M300 130H490M580 130H900V430H700V360M420 360H295M245 360H100V130')
 s.path('M240 108V152M260 116V144M260 130H280M280 108V152M300 116V144')
 s.path('M140 130L180 110');s.text(85,85,'Switch',20)
 s.text(270,85,'Low-voltage DC',anchor='middle');s.resistor(490,130,90);s.arrow(490,160,580,98)
 s.text(535,205,'Current control',anchor='middle');s.meter(270,360,'A')
 s.path('M420 360H820',color=ORANGE,w=5)
 s.path('M420 360V260H535M585 260H700V360');s.meter(560,260,'V')
 s.junction(420,360);s.junction(700,360)
 s.label(45,470,'Fixed contact',420,360);s.label(755,310,'Movable contact',700,360)
 s.rect(420,475,400,35,'#fcf1d8')
 for i in range(11):
  x=420+40*i;s.path(f'M{x} 475v{18 if i%5==0 else 10}',w=1)
  if i%5==0:s.text(x,538,str(i*4)+' cm',19,anchor='middle')
 s.path('M420 445H700',BLUE,2);s.path('M420 437v16M700 437v16',BLUE,2)
 s.text(560,423,'Length in the circuit',20,anchor='middle')
 s.text(40,586,'Record V and I at each length. Switch off between readings to limit heating.')
 return s

def combinations():
 s=SVG('Measure total resistance: series and parallel',570);s.titleline()
 for x,title in [(40,'Series'),(530,'Parallel')]:
  s.text(x+200,100,title,25,bold=True,anchor='middle')
  s.path(f'M{x+25} 175H{x+175}M{x+215} 175H{x+400}V{x*0+405}H{x+25}V175')
  s.path(f'M{x+175} 153V197M{x+195} 161V189M{x+195} 175h20')
  # Remove underlying wire only where a component will be drawn using an opaque backing.
  s.rect(x+47,377,57,56,stroke='none');s.meter(x+75,405,'A')
  if title=='Series':
   s.resistor(x+145,405,70);s.resistor(x+280,405,70)
   s.path(f'M{x+125} 405V300H{x+225}M{x+275} 300H{x+375}V405');s.meter(x+250,300,'V')
   for a in (125,375):s.junction(x+a,405)
  else:
   # White gap separates the two junctions; current has two genuine branches.
   s.rect(x+125,378,250,54,stroke='none');s.path(f'M{x+125} 405V350H{x+375}V405M{x+125} 405V460H{x+375}V405')
   s.resistor(x+215,350,70);s.resistor(x+215,460,70)
   s.path(f'M{x+125} 350V270H{x+225}M{x+275} 270H{x+375}V350');s.meter(x+250,270,'V')
   for a in (125,375):s.junction(x+a,405);s.junction(x+a,350)
 s.lines(40,520,['In both circuits, measure the total V and I; calculate total R = V/I.'])
 return s

def heat_capacity():
 s=SVG('Specific heat capacity: heat an insulated block',570);s.titleline()
 s.rect(290,220,320,250,'#f1e8d6');s.rect(320,245,260,200,'#cbd8df')
 s.rect(365,155,30,220,'#e4c1a0');s.rect(500,120,22,255,'#fafafa');s.circle(511,370,13,'#cb5749')
 s.path('M370 155V95H145M390 155V130H145',BLUE)
 s.rect(35,75,110,80,'#e6f3f1');s.text(90,110,'Energy',20,anchor='middle');s.text(90,138,'meter',20,anchor='middle')
 s.label(650,155,'Temperature probe',520,230);s.label(650,255,'Heater',392,270)
 s.label(650,355,'Metal block',575,350);s.label(650,440,'Insulation',606,410)
 s.lines(35,515,['Measure block mass, electrical energy supplied and temperature rise.',
 'Good thermal contact and insulation reduce energy loss.'])
 return s

def insulation():
 s=SVG('Compare cooling: change one insulation factor',530);s.titleline()
 for x,label,fill in [(100,'Material A','#ead8bf'),(550,'Material B','#d7e3d6')]:
  s.rect(x,195,250,250,fill);s.beaker(x+35,190,180,220)
  s.rect(x+20,180,210,15,'#e2e4e5');s.rect(x+117,90,16,240,'white');s.circle(x+125,325,11,'#c65948')
  s.text(x+125,75,label,25,bold=True,anchor='middle')
 s.lines(35,485,['Same water mass, starting temperature, lid and insulation thickness.'])
 s.label(365,150,'Probe',233,180)
 return s

def density():
 s=SVG('Density of an irregular solid: volume by displacement',555);s.titleline()
 for x,label,level in [(120,'Before',285),(550,'After',220)]:
  s.text(x+75,100,label,25,bold=True,anchor='middle');s.beaker(x,145,150,290,False)
  s.rect(x+3,level,144,432-level,WATER,stroke='none',r=0);s.path(f'M{x} 145V435H{x+150}V145')
  for i in range(6):s.path(f'M{x+120} {180+i*40}h30',w=1)
  s.text(x+185,level+7,'V₁' if label=='Before' else 'V₂',25)
  s.path(f'M{x+150} {level}h25',BLUE)
  if label=='After':
   s.path(f'M{x+65} 360L{x+105} 350L{x+110} 403L{x+55} 405Z',fill='#abb7bf')
   s.path(f'M{x+80} 357V125',w=1);s.text(x+225,365,'Fully submerged',20)
 s.lines(35,490,['Volume of solid = V₂ − V₁. Remove trapped bubbles.',
 'Measure its mass separately on a balance. Density = mass / volume.'])
 return s

def spring():
 s=SVG('Force and extension: compare loaded and unloaded lengths',610);s.titleline()
 for x,label,end in [(90,'Unloaded',290),(545,'Loaded',380)]:
  s.text(x+130,90,label,24,bold=True,anchor='middle');s.path(f'M{x} 500V130H{x+200}',w=5)
  s.rect(x-35,500,140,20,'#d9e0e3');s.path(f'M{x+165} 130V160')
  pts=[(x+165,160)]+[(x+150+(i%2)*30,170+i*(end-180)/11) for i in range(12)]+[(x+165,end)]
  s.path('M'+'L'.join(f'{a} {b}' for a,b in pts),BLUE)
  s.rect(x+245,150,40,340,'#fbf1d4')
  for i in range(16):s.path(f'M{x+245} {160+i*20}h{22 if i%5==0 else 10}',w=1)
  s.path(f'M{x+165} {end}H{x+240}',ORANGE);s.text(x+300,end+8,'L₀' if label=='Unloaded' else 'L',24)
  if label=='Loaded':s.path(f'M{x+165} {end}v30');s.rect(x+120,end+30,90,60,'#aabcc6')
 s.lines(35,557,['Extension = L − L₀. Read the pointer at eye level after it settles.'])
 return s

def trolley():
 s=SVG('Acceleration: a trolley pulled by hanging masses',570);s.titleline()
 s.path('M60 355H780',w=6);s.rect(125,270,260,65,'#dbece6')
 for x in (175,330):s.circle(x,342,17,'#667887')
 for x in (160,215,270):s.rect(x,235,45,35,'#b7c7cf')
 s.path('M385 300H780Q810 300 810 330V440',BLUE);s.circle(790,328,22,'#e0e5e7')
 s.path('M790 306Q812 307 812 330V440',BLUE);s.rect(775,440,70,65,'#acbbc6')
 # Light-gate beam crosses the trolley interrupt card's route.
 s.rect(190,210,15,60,'#183b4d');s.path('M450 350V235H510V350M620 350V235H680V350',TEAL,w=5)
 s.text(450,200,'Light gates / timer',23);s.path('M480 215V235M650 215V235',w=1)
 s.label(35,150,'Trolley + masses',180,240);s.label(835,260,'Pulley',802,315)
 s.text(650,545,'Hanging masses',22);s.path('M790 520V503',w=1)
 s.lines(35,430,['Transfer masses from trolley to hanger',
 'to change force at constant total moving mass.',
 'Record acceleration before the hanger reaches the floor.'])
 return s

def waves():
 s=SVG('Wave speed: measure distance and frequency',640);s.titleline()
 s.text(30,90,'Ripple tank: plan view',25,bold=True);s.rect(40,120,400,250,WATER)
 s.rect(55,150,16,190,'#b3cbd3');s.text(65,410,'Vibrating dipper',21)
 for i in range(6):s.path(f'M{110+i*55} 140V345',BLUE,w=2)
 s.path('M110 335V365H385V335',ORANGE,w=2)
 s.text(245,450,'6 crests enclose 5 wavelengths',21,anchor='middle')
 s.text(520,90,'Stretched string',25,bold=True)
 s.rect(520,210,55,80,'#deebe5');s.path('M575 250C600 160 625 160 650 250S700 340 725 250S775 160 800 250H875',BLUE,w=4)
 s.circle(890,258,16,'#d7dfe4');s.path('M875 250Q906 238 906 268V370');s.rect(878,370,56,50,'#a8b9c2')
 for x in (575,650,725,800):s.circle(x,250,4,ORANGE,ORANGE)
 s.path('M650 275V315H725V275',ORANGE,w=2);s.text(687,350,'λ/2',23,anchor='middle')
 s.text(520,135,'Vibration generator',21);s.path('M548 150V210',w=1)
 s.text(522,465,'Adjacent nodes are half a wavelength apart.',21)
 s.lines(35,550,['Measure several spacings, then divide to find one wavelength.',
 'Use a measured / calibrated frequency. Wave speed v = fλ.'])
 return s

def rays():
 s=SVG('Ray practicals: trace rays and measure from the normal',590);s.titleline()
 s.text(50,95,'Reflection',25,bold=True);s.text(545,95,'Refraction',25,bold=True)
 s.path('M50 350H440',w=6);s.path('M245 140V440','#7e8d94',2,True)
 s.arrow(80,180,245,350);s.arrow(245,350,410,180)
 s.text(199,285,'i',24);s.text(280,285,'r',24);s.text(70,390,'Mirror',22)
 s.text(280,140,'Normal',21)
 s.rect(555,240,390,170,WATER);s.path('M675 120V470','#7e8d94',2,True);s.path('M755 240V510','#7e8d94',2,True)
 s.arrow(570,120,675,240);s.arrow(675,240,755,410);s.arrow(755,410,850,518)
 s.text(640,200,'i',24);s.text(690,300,'r',24);s.text(810,282,'Glass block',21)
 for x,y in [(580,132),(610,166),(817,480),(840,507)]:s.circle(x,y,4,ORANGE,ORANGE)
 s.lines(35,545,['Mark the surface and two points on each visible ray. Remove apparatus; join points.'])
 return s

def infrared():
 s=SVG('Infrared: separate emission from absorption',600);s.titleline()
 s.text(35,100,'Emission: Leslie cube',25,bold=True)
 s.path('M110 180L190 140L310 180V350L230 395L110 350Z',fill='#e4e8ea')
 s.path('M110 180L230 220L310 180M230 220V395');s.path('M112 184L228 223V390L112 348Z',fill='#344956')
 s.rect(375,260,70,55,'#d7e9e6');s.path('M370 287H255',ORANGE,2,True)
 s.text(295,375,'Same detector distance',20);s.text(295,405,'and angle for each face',20)
 s.label(45,470,'Hot water inside',184,174)
 s.text(530,100,'Absorption: matched samples',25,bold=True)
 s.rect(545,260,55,70,'#e9d1b2');s.path('M600 260L630 245V345L600 330Z',fill='#e7bf79')
 for y in (270,300,330):s.arrow(650,y,730,y,ORANGE)
 s.rect(760,175,35,220,'#344956');s.rect(875,175,35,220,'#d3dbe1')
 s.circle(777,300,12,'#c94d40');s.circle(892,300,12,'#c94d40')
 s.text(550,435,'IR lamp',21);s.text(747,145,'Black',21);s.text(865,145,'Shiny',21)
 s.lines(530,475,['Expose one sample at a time.',
 'Keep distance and time the same.',
 'Compare temperature rises.'])
 return s

def salt():
 s=SVG('Soluble salt crystals: remove solid, then remove some water',610);s.titleline()
 s.text(30,95,'1  Filter excess solid',24,bold=True)
 s.path('M75 160H285L195 280V345H165V280Z',fill='#f5f2e7');s.path('M105 175H255L180 265Z',fill='#e0d0b7')
 for x,y in [(145,195),(180,220),(205,190)]:s.circle(x,y,6,'#3f403c')
 s.beaker(85,355,190,135);s.text(320,220,'Residue:',22,bold=True);s.text(320,252,'excess solid',21)
 s.path('M310 260L202 218',w=1)
 s.text(320,395,'Filtrate:',22,bold=True);s.text(320,427,'salt solution',21);s.path('M310 438L250 450',w=1)
 s.text(550,95,'2  Concentrate, then cool',24,bold=True)
 s.beaker(620,285,230,200);s.path('M600 260Q735 360 870 260Z',fill='#b8deec')
 s.rect(595,485,285,25,'#e3b697');s.text(640,553,'Warm water bath',21)
 s.path('M685 225q-20-25 0-45m50 45q-20-25 0-45',ORANGE,2)
 s.lines(35,553,['Cool to crystallise. Separate, rinse with a little cold water, then dry.'],size=21)
 # Place instruction in separate footer, not on the bath label line.
 s.parts.pop();s.text(35,590,'Cool to crystallise. Separate, rinse with a little cold water, then dry.',21)
 return s

def calorimetry():
 s=SVG('Temperature changes: an insulated reaction cup',560);s.titleline()
 s.beaker(260,225,360,245,False);s.path('M300 215L325 455H555L580 215Z',fill='#eee9db')
 s.path('M315 320L328 450H552L565 320Z',fill=WATER)
 s.rect(285,200,310,18,'#dfded7');s.rect(405,90,22,280,'white');s.circle(416,367,12,'#c24e43')
 s.path('M515 125L505 385',TEAL,8)
 s.label(680,150,'Thermometer',428,230);s.label(680,250,'Lid with loose openings',590,210)
 s.label(680,350,'Insulated cup',560,390);s.label(35,400,'Supporting beaker',260,400)
 s.lines(35,512,['Measure starting temperature, add reactant, stir, then record the maximum / minimum.'])
 return s

def turbidity():
 s=SVG('Disappearing cross: keep the viewing depth constant',585);s.titleline()
 for x,label,color in [(70,'At the start',WATER),(555,'At the endpoint','#eee4b2')]:
  s.text(x+170,100,label,24,bold=True,anchor='middle')
  s.path(f'M{x+140} 145V205L{x+60} 380Q{x+170} 415 {x+280} 380L{x+200} 205V145Z',fill='white')
  s.path(f'M{x+106} 280H{x+234}L{x+280} 380Q{x+170} 415 {x+60} 380Z',fill=color,w=1)
  s.rect(x+30,410,285,65,'white');s.path(f'M{x+155} 425l30 35m-30 0 30-35',color=INK if x==70 else '#a7a184',w=5)
  s.arrow(x+170,125,x+170,250,BLUE)
  s.text(x+170,515,'Look down from above',21,anchor='middle')
 s.text(35,551,'Time until sulfur cloudiness hides the cross. Use the same flask, depth and endpoint.',20)
 return s

def chromatography():
 s=SVG('Paper chromatography: spots start above the solvent',560);s.titleline()
 s.beaker(260,125,400,340,False);s.rect(245,110,430,18,'#d7e1e5')
 s.rect(365,130,190,310,'#fcfbf3');s.rect(263,395,394,66,WATER,stroke='none',r=0)
 s.path('M365 350H555','#596b75',2,True)
 for x in (400,460,520):s.circle(x,350,6,'#873c6a')
 s.path('M365 230H555',BLUE,2,True)
 for x,y,c in [(400,280,'#b14049'),(460,255,'#4562a0'),(520,305,'#568846')]:s.circle(x,y,6,c)
 s.label(710,180,'Covered vessel',650,120);s.label(710,270,'Solvent front',555,230)
 s.label(710,350,'Pencil baseline',555,350);s.label(710,435,'Solvent',655,425)
 s.lines(35,515,['Keep the spots above the solvent. Mark the solvent front as soon as paper is removed.'])
 return s

def flame_test():
 s=SVG('Flame tests: place a clean sample loop in the blue flame',530);s.titleline()
 s.rect(180,405,200,28,'#b4c5ce');s.rect(255,290,50,115,'#c0cbd1')
 s.path('M258 290Q220 220 280 135Q340 220 302 290Z',fill='#9bd5ef',color=BLUE)
 s.path('M270 290Q255 255 280 218Q305 255 290 290Z',fill='#f8fcff',color=BLUE,w=2)
 s.path('M800 185L320 235',w=5);s.circle(308,237,13,'none')
 s.label(500,110,'Clean wire loop + sample',316,230)
 s.text(425,350,'Blue non-luminous flame',22)
 s.lines(35,490,['Clean the loop between samples. Compare the flame colour with known ions.'])
 return s

def microscopy():
 s=SVG('Prepare a slide: lower the coverslip at an angle',500);s.titleline()
 s.rect(80,335,720,22,'#e9f4fa');s.path('M350 332Q420 270 490 332Z',fill=WATER,color=BLUE)
 s.rect(405,315,85,15,'#d5e4b6');s.path('M330 330L570 175',BLUE,w=7)
 s.path('M650 205L425 270','#b88356',w=5)
 s.label(40,125,'Coverslip',470,235);s.label(710,185,'Mounted needle',580,225)
 s.label(680,285,'Thin specimen + stain',478,320);s.label(45,425,'Glass slide',240,349)
 s.text(35,480,'Lower gently to reduce air bubbles. Start viewing with the lowest-power objective.',21)
 return s

def agar():
 s=SVG('Antimicrobial discs: compare zones of inhibition',570);s.titleline()
 s.circle(300,285,180,'#eee5bd');s.circle(300,285,172,'#e2d6a4')
 s.circle(225,240,60,'#fffefa',BLUE);s.circle(365,330,38,'#fffefa',BLUE)
 for x,y,label in [(225,240,'A'),(365,330,'B'),(345,190,'C')]:s.circle(x,y,13,'#fffefa');s.text(x,y+6,label,16,anchor='middle')
 s.path('M165 240H285',ORANGE,2);s.path('M165 230v20M285 230v20',ORANGE,2)
 s.label(565,145,'Agar with bacterial lawn',400,170)
 s.label(565,235,'Clear zone: growth inhibited',269,210)
 s.label(565,330,'Equal-sized treated discs',366,330)
 s.text(565,405,'C: solvent-only control',22)
 s.lines(35,515,['Measure the full zone diameter consistently; radius = diameter ÷ 2.',
 'Keep the incubated plate closed. Compare replicate plates.'])
 return s

def osmosis():
 s=SVG('Potato osmosis: compare mass changes fairly',560);s.titleline()
 for x,label in [(45,'Water'),(355,'Dilute solution'),(665,'Concentrated solution')]:
  s.text(x+135,100,label,22,bold=True,anchor='middle');s.beaker(x+40,140,180,230)
  s.rect(x+100,235,45,105,'#e8d5a0');s.text(x+130,410,'Equal-sized tissue',20,anchor='middle')
 s.lines(35,475,['Weigh → immerse for the same time → blot consistently → reweigh.',
 'Use equal solution volumes and temperature; repeat at each concentration.'])
 return s

def food_tests():
 s=SVG('Food tests: use separate samples and compare positive results',600);s.titleline()
 tests=[('Reducing sugar','Benedict’s + hot water bath','#c76b2f','Brick-red precipitate'),('Starch','Iodine','#283047','Blue-black'),('Protein','Biuret reagent','#a478b8','Lilac / purple'),('Lipid','Sudan III','#efe1b0','Red-stained oil layer')]
 for i,(name,reagent,c,result) in enumerate(tests):
  x=30+i*245;s.text(x+110,100,name,22,bold=True,anchor='middle');s.tube(x+85,170,180,c)
  if i==3:s.rect(x+90,230,34,35,'#b53c38',stroke='none')
  s.text(x+110,410,result,18,anchor='middle')
  if i==0:
   for a,b in [(98,315),(112,330),(104,340),(120,312),(115,343)]:s.circle(x+a,b,3,'#9d3b21','#9d3b21')
  if i==0:s.lines(x+10,455,['Benedict’s solution','Warm in water bath'],size=20)
  else:s.text(x+110,455,reagent,20,anchor='middle')
 s.lines(35,550,['These show positive results. Include known positive and negative samples.',
 'Use clean equipment; colours identify substances, not exact concentrations.'],size=20)
 return s

def amylase():
 s=SVG('Amylase and pH: test fresh samples every 30 seconds',590);s.titleline()
 s.beaker(60,200,250,240);s.tube(125,125,240,color='#f7e8cf',level=170);s.text(40,490,'Constant-temperature water bath',21)
 s.lines(355,125,['Starch + amylase + pH buffer',
 'Start timing when they are mixed.'],size=22)
 s.arrow(190,200,460,250);s.text(330,300,'Fresh drop',21)
 s.rect(495,215,450,185,'#eef2ed')
 for i,(t,c) in enumerate([('0 s','#253046'),('30 s','#253046'),('60 s','#253046'),('90 s','#b87d33')]):
  x=550+i*110;s.circle(x,285,28,c);s.text(x,365,t,20,anchor='middle')
 s.lines(355,450,['Iodine stays blue-black while starch remains.',
 'First orange-brown sample: starch no longer detected.',
 'Illustrative endpoint only; actual times vary.'])
 s.text(35,555,'Never add iodine to the reaction tube. Repeat with a range of buffer pH values.',21)
 return s

def reaction():
 s=SVG('Ruler-drop reaction time: start zero at the finger gap',560);s.titleline()
 s.rect(440,95,95,370,'#f9e8b5')
 for i in range(16):
  y=435-i*21;s.path(f'M440 {y}h{35 if i%5==0 else 17}',w=1)
  if i%5==0:s.text(485,y+7,i,19)
 # Fingers on opposite sides of the ruler, open at the zero line.
 s.path('M140 455H350Q390 455 415 435Q390 415 350 415H255',fill='#ebcfb6')
 s.path('M815 455H620Q580 455 555 435Q580 415 620 415H705',fill='#ebcfb6')
 s.path('M355 435H620',ORANGE,2,True)
 s.label(45,175,'Release without warning',455,120)
 s.label(650,285,'Zero level with finger gap',530,435)
 s.text(575,120,'Distance (cm)',22)
 s.lines(35,515,['Catch the ruler. Record fall distance, then convert to time using a suitable table.'])
 return s

def seedling():
 s=SVG('Seedling practical: compare one-sided and all-round light',580);s.titleline()
 for x,title in [(55,'One-sided light'),(555,'All-round light control')]:
  s.text(x+180,100,title,23,bold=True,anchor='middle');s.rect(x+70,365,190,95,'#d6ccb6')
  s.path(f'M{x+165} 420V350Q{x+165} 270 {x+110 if x==55 else x+165} 230',TEAL,7)
  s.path(f'M{x+165} 360Q{x+200} 320 {x+215} 340Q{x+205} 370 {x+165} 360',TEAL,2,fill='#a5cba3')
  if x==55:s.arrow(x,190,x+100,190,ORANGE);s.arrow(x,235,x+85,235,ORANGE)
  else:
   s.arrow(x+35,180,x+120,220,ORANGE);s.arrow(x+290,180,x+205,220,ORANGE)
 s.lines(35,520,['Keep species, age, water, temperature and time the same.',
 'Record lengths and labelled drawings; compare several seedlings.'])
 return s

def transect():
 s=SVG('A line transect: sample at regular distances',545);s.titleline()
 s.rect(45,130,930,270,'#e4eedb');s.path('M85 275H915',BLUE,4)
 for i in range(5):
  x=100+i*190;s.rect(x,220,100,100,'none',TEAL,r=0);s.text(x+50,445,str(i*2)+' m',21,anchor='middle')
  for a,b in [(25,20),(70,75)]:s.circle(x+a,220+b,5,'#5b8750')
 s.text(50,100,'Shaded end',22);s.text(780,100,'Open / lighter end',22)
 s.lines(35,500,['At each quadrat, record abundance and the environmental factor. Repeat transects.'])
 return s

def milk():
 s=SVG('Milk decay: control temperature and measure pH change',560);s.titleline()
 s.beaker(90,215,350,245);s.tube(180,130,280,color='#f7e8cf',level=190);s.rect(300,105,20,250,'white');s.circle(310,350,11,'#c75246')
 s.label(575,145,'Temperature probe',312,230)
 s.lines(575,230,['Milk + sodium carbonate',
 '+ indicator; add lipase to start.',
 'Use the same volumes and',
 'concentrations for every run.'])
 s.label(570,430,'Controlled water bath',438,400)
 s.lines(35,510,['Time to the same pH endpoint. Repeat at each temperature; include a no-lipase control.'],size=21)
 return s

def potometer():
 s=SVG('Potometer: follow an air bubble in a water-filled capillary',595);s.titleline()
 s.beaker(50,260,155,220)
 s.rect(105,329,610,24,WATER);s.rect(690,185,25,155,WATER)
 s.rect(680,180,45,30,'#998975');s.path('M702 205V105',TEAL,8)
 s.path('M702 145Q625 95 620 155Q655 185 702 145M702 125Q775 75 790 130Q755 165 702 125',TEAL,2,fill='#b2d2a0')
 s.beaker(385,110,110,110);s.rect(432,218,18,112,WATER)
 s.rect(420,250,42,20,'#afbbc0');s.path('M440 250V235H470',w=3)
 s.rect(275,332,65,18,'white',stroke=BLUE,r=8)
 s.rect(220,390,420,35,'#f9efce')
 for i in range(15):s.path(f'M{235+i*27} 390v{18 if i%5==0 else 10}',w=1)
 s.arrow(280,465,395,465);s.text(420,474,'Bubble moves towards the shoot',21)
 s.label(45,155,'Air bubble',300,340);s.label(520,85,'Reservoir resets bubble',470,180)
 s.label(775,240,'Airtight seal',725,194);s.label(760,330,'Leafy shoot',704,160)
 s.text(35,545,'Measure bubble distance per unit time. Keep joins airtight and cut the shoot under water.',21)
 s.text(35,578,'Water uptake estimates transpiration; some absorbed water has other uses.',21)
 return s

DRAWINGS={k:v for k,v in globals().copy().items() if callable(v) and k in ['iv','wire','combinations','heat_capacity','insulation','density','spring','trolley','waves','rays','infrared','salt','calorimetry','turbidity','chromatography','flame_test','microscopy','agar','osmosis','food_tests','amylase','reaction','seedling','transect','milk','potometer']}

# subject, owning topic, filename, drawing function, explanatory text alternative.
ASSETS=[
 ('Physics',2,'wire-length-practical','wire','Ammeter in series; voltmeter across the selected wire length between fixed and movable contacts. A ruler measures that length.'),
 ('Physics',2,'resistor-combinations-practical','combinations','Series and parallel resistor circuits, each with an ammeter measuring total current and a voltmeter across the whole combination.'),
 ('Physics',2,'iv-practical','iv','Low-voltage supply, variable resistor, ammeter and test component in series; voltmeter across the component.'),
 ('Physics',1,'specific-heat-capacity-practical','heat_capacity','An insulated metal block contains a heater and temperature probe. A meter records electrical energy supplied.'),
 ('Physics',1,'thermal-insulation-practical','insulation','Identical lidded beakers have equal water masses, probes and equal thicknesses of different insulation.'),
 ('Physics',3,'density-displacement-practical','density','The water level rises from V₁ to V₂ when an irregular solid is fully submerged. Its volume is the difference.'),
 ('Physics',5,'spring-extension-practical','spring','Unloaded and loaded spring lengths are read against a ruler with an eye-level pointer. Extension is their difference.'),
 ('Physics',5,'trolley-acceleration-practical','trolley','A trolley carrying masses is pulled by a string over a pulley to a hanging mass. Light gates measure its motion.'),
 ('Physics',6,'wave-speed-practical','waves','A ripple tank plan shows six crests spanning five wavelengths. A vibrating string shows adjacent nodes separated by half a wavelength.'),
 ('Physics',6,'ray-tracing-practical','rays','Incident and reflected rays meet at a mirror. A separate parallel-sided block bends light towards the normal on entry and away on exit.'),
 ('Physics',6,'infrared-surfaces-practical','infrared','A detector compares emission from Leslie cube faces. Separately, an infrared lamp heats matched black and shiny samples.'),
 ('Chemistry',4,'salt-crystals-practical','salt','Filter excess insoluble solid, collect the salt solution, then concentrate it in an evaporating basin over a water bath and cool to crystallise.'),
 ('Chemistry',5,'reaction-temperature-practical','calorimetry','A supported insulated cup has a loose lid, thermometer bulb in the liquid and a stirrer.'),
 ('Chemistry',6,'disappearing-cross-practical','turbidity','Viewed from above, a cross under the flask becomes hidden as sulfur makes the liquid cloudy. Keep the viewing depth constant.'),
 ('Chemistry',8,'chromatography-setup','chromatography','Paper hangs in a covered vessel. The pencil baseline and sample spots are above the solvent; the solvent front is marked higher up the paper.'),
 ('Chemistry',8,'flame-test-practical','flame_test','A clean wire loop holds a sample in the blue non-luminous flame of a Bunsen burner.'),
 ('Biology',1,'microscope-slide-practical','microscopy','A coverslip is lowered at an angle onto a thin stained specimen on a glass slide, using a mounted needle.'),
 ('Biology',1,'agar-disc-practical','agar','Equal-sized antimicrobial discs sit on an inoculated agar plate. Clear zones differ in diameter; a solvent-only control has no clear zone.'),
 ('Biology',1,'potato-osmosis-practical','osmosis','Equal-sized potato cylinders are immersed in equal volumes of different concentrations, then blotted and reweighed.'),
 ('Biology',2,'food-tests-practical','food_tests','Positive food-test results: reducing sugar gives a coloured Benedict’s precipitate after warming, starch blue-black iodine, protein purple Biuret and lipid a Sudan-stained oil layer.'),
 ('Biology',2,'amylase-sampling-practical','amylase','Starch, amylase and buffer react in a controlled water bath. Fresh samples go into separate iodine wells every thirty seconds until starch is no longer detected.'),
 ('Biology',2,'potometer-practical','potometer','A leafy shoot is sealed into water-filled tubing. An air bubble moves along a capillary towards the shoot, and a reservoir allows it to be reset.'),
 ('Biology',5,'ruler-drop-practical','reaction','The ruler starts with zero level with the participant’s open thumb and finger. Record fall distance when caught and convert it to reaction time.'),
 ('Biology',5,'seedling-light-practical','seedling','Comparable seedlings receive one-sided or all-round light. The shoot bends towards one-sided light; record lengths and labelled drawings.'),
 ('Biology',7,'transect-practical','transect','Quadrats placed at regular distances along a transect sample an environmental gradient. Record abundance and the environmental factor at each site.'),
 ('Biology',7,'milk-decay-practical','milk','Milk, sodium carbonate and indicator equilibrate in a controlled water bath before lipase is added. Measure time to the same pH endpoint.'),
]

def topic_path(subject,n):return next((ROOT/(subject+' - AQA')).glob(f'{n:02d} - *'))
def item(subject,n,heading,assets):return dict(subject=subject,topic=n,heading=heading,assets=assets)
def a(subject,n,name):return (subject,n,name)

PLACEMENTS=[
 item('Physics',2,'Practical: resistance of a wire and resistor combinations',[a('Physics',2,'wire-length-practical'),a('Physics',2,'resistor-combinations-practical')]),
 item('Physics',2,'Practical: investigate I–V characteristics',[a('Physics',2,'iv-practical')]),
 item('Physics',1,'Practical: measure specific heat capacity',[a('Physics',1,'specific-heat-capacity-practical')]),
 item('Physics',1,'Practical: compare thermal insulators',[a('Physics',1,'thermal-insulation-practical')]),
 item('Physics',3,'Practical: measure density',[a('Physics',3,'density-displacement-practical')]),
 item('Physics',5,'Practical: force and extension',[a('Physics',5,'spring-extension-practical')]),
 item('Physics',5,'Practical: force, mass and acceleration',[a('Physics',5,'trolley-acceleration-practical')]),
 item('Physics',6,'Practical: measuring waves',[a('Physics',6,'wave-speed-practical')]),
 item('Physics',6,'Reflection, absorption and transmission',[a('Physics',6,'ray-tracing-practical')]),
 item('Physics',6,'Practical: infrared surfaces',[a('Physics',6,'infrared-surfaces-practical')]),
 item('Chemistry',4,'Required practical: pure dry salt crystals',[a('Chemistry',4,'salt-crystals-practical')]),
 item('Chemistry',4,'Required practical: aqueous electrolysis',[a('Chemistry',4,'electrolysis')]),
 item('Chemistry',5,'Required practical: temperature changes',[a('Chemistry',5,'reaction-temperature-practical')]),
 item('Chemistry',6,'Colour or turbidity rate practical',[a('Chemistry',6,'disappearing-cross-practical')]),
 item('Chemistry',8,'Chromatography practical and Rf',[a('Chemistry',8,'chromatography-setup')]),
 item('Chemistry',8,'Flame tests for metal ions',[a('Chemistry',8,'flame-test-practical')]),
 item('Chemistry',10,'Desalination and water analysis',[a('Chemistry',11,'water-distillation')]),
 item('Biology',1,'Required practical 1: observe, draw and label cells',[a('Biology',1,'microscope-slide-practical')]),
 item('Biology',1,'Required practical 2: antimicrobial substances',[a('Biology',1,'agar-disc-practical')]),
 item('Biology',1,'9. Required practical 3: osmosis in plant tissue',[a('Biology',1,'potato-osmosis-practical')]),
 item('Biology',2,'Food tests',[a('Biology',2,'food-tests-practical')]),
 item('Biology',2,'Investigating amylase and pH',[a('Biology',2,'amylase-sampling-practical')]),
 item('Biology',2,'Measuring water uptake',[a('Biology',2,'potometer-practical')]),
 item('Biology',5,'Practical: reaction time',[a('Biology',5,'ruler-drop-practical')]),
 item('Biology',5,'Practical: seedling growth responses',[a('Biology',5,'seedling-light-practical')]),
 item('Biology',7,'Transects: investigating distribution',[a('Biology',7,'transect-practical')]),
 item('Biology',7,'Milk-decay practical',[a('Biology',7,'milk-decay-practical')]),
]
# Reuse each apparatus diagram in the practical-skills revision page as well.
for subject,number,pairs in [
 ('Physics',9,[(1,'specific-heat-capacity-practical','Practical: specific heat capacity'),(1,'thermal-insulation-practical','Practical: thermal insulation'),(3,'density-displacement-practical','Practical: density'),(5,'spring-extension-practical','Practical: force and extension'),(5,'trolley-acceleration-practical','Practical: force, mass and acceleration'),(2,'wire-length-practical','Practical: resistance'),(2,'resistor-combinations-practical','Practical: resistance'),(2,'iv-practical','Practical: current–voltage characteristics'),(6,'wave-speed-practical','Practical: waves in water and solids'),(6,'ray-tracing-practical','Practical: reflection and refraction'),(6,'infrared-surfaces-practical','Practical: infrared absorption and emission')]),
 ('Chemistry',11,[(4,'salt-crystals-practical','Preparing a pure dry soluble salt'),(5,'reaction-temperature-practical','Temperature changes in reacting solutions'),(6,'disappearing-cross-practical','Concentration and rate: turbidity or colour'),(8,'chromatography-setup','Paper chromatography'),(8,'flame-test-practical','Identifying unknown ionic compounds')]),
 ('Biology',8,[(1,'microscope-slide-practical','Microscopy and biological drawings'),(1,'agar-disc-practical','Antibiotics and antiseptics on agar'),(1,'potato-osmosis-practical','Osmosis in plant tissue'),(2,'food-tests-practical','Food tests'),(2,'amylase-sampling-practical','Amylase and pH'),(5,'ruler-drop-practical','Human reaction time'),(5,'seedling-light-practical','Seedling responses to light or gravity'),(7,'transect-practical','Ecology sampling'),(7,'quadrat-sampling','Ecology sampling'),(7,'milk-decay-practical','Milk decay and temperature')])]:
 for owner,name,heading in pairs:PLACEMENTS.append(item(subject,number,heading,[a(subject,owner,name)]))

EXISTING_ALT={
 ('Chemistry',4,'electrolysis'):'An aqueous solution is electrolysed using a low-voltage DC supply and separate inert electrodes: positive anode and negative cathode.',
 ('Chemistry',11,'water-distillation'):'Water vapour travels from a heated flask through a water-cooled condenser into an open receiver. Cooling water stays in its separate jacket.',
 ('Biology',7,'quadrat-sampling'):'Random coordinates locate equal-sized quadrats across the habitat to estimate a population.',
}

def apply(subject,number):
 topic=topic_path(subject,number);notes=topic/'Revision Notes';source=notes/json.loads((topic/'revision-layout.json').read_text(encoding='utf-8'))['source']
 data=source.read_text(encoding='utf-8-sig');before=data
 for s,n,name,kind,alt in ASSETS:
  if (s,n)!=(subject,number):continue
  canvas=DRAWINGS[kind]();out=topic/'Diagrams'/(name+'.svg');out.parent.mkdir(exist_ok=True);out.write_text(canvas.output(alt),encoding='utf-8')
 audit=[]
 for entry in PLACEMENTS:
  if (entry['subject'],entry['topic'])!=(subject,number):continue
  heading=entry['heading']
  # One apparatus picture per reading group is sufficient. Move an existing
  # copy beside the method rather than repeating it in the theory above.
  groups=json.loads((topic/'revision-layout.json').read_text(encoding='utf-8'))['groups']
  peers=[h['heading'] for g in groups if any(h['heading']==heading for h in g['sections']) for h in g['sections'] if h['heading']!=heading]
  for s,n,name in entry['assets']:
   relative=Path(os.path.relpath(topic_path(s,n)/'Diagrams'/(name+'.svg'),source.parent)).as_posix()
   for peer in peers:
    pm=re.search(r'(?m)^#{2,3} '+re.escape(peer)+r'\s*$',data)
    if not pm:continue
    pe=re.search(r'(?m)^#{2,3} ',data[pm.end():]);stop=pm.end()+pe.start() if pe else len(data)
    content=data[pm.end():stop]
    cleaned=re.sub(r'!\[[^\]]*\]\('+re.escape(relative)+r'\)\s*','',content)
    if cleaned!=content:data=data[:pm.end()]+cleaned+data[stop:]
  if (subject,number,heading)==('Physics',9,'Practical: resistance'):
   data=re.sub(r'!\[[^\]]*\]\(../../02 - Electricity/Diagrams/resistance-circuit.svg\)\s*','',data)
  pattern=r'(?m)^#{2,3} '+re.escape(heading)+r'\s*$';match=re.search(pattern,data)
  assert match,(topic,heading)
  end=re.search(r'(?m)^#{2,3} ',data[match.end():]);stop=match.end()+end.start() if end else len(data)
  section=data[match.end():stop];images=[]
  for s,n,name in entry['assets']:
   path=topic_path(s,n)/'Diagrams'/(name+'.svg');assert path.exists(),path
   alt=next((x[4] for x in ASSETS if x[:3]==(s,n,name)),EXISTING_ALT.get((s,n,name)))
   assert alt,(s,n,name)
   relative=Path(os.path.relpath(path,source.parent)).as_posix()
   if relative not in section:images.append(f'![{alt}]({relative})')
   audit.append(dict(heading=heading,diagram=path.relative_to(ROOT).as_posix(),purpose=alt))
  if images:data=data[:match.end()]+'\n\n'+'\n\n'.join(images)+'\n'+data[match.end():]
 if data!=before:source.write_text(data,encoding='utf-8')
 (topic/'practical-diagram-review.json').write_text(json.dumps(dict(reviewed='2026-10-20',generator='scripts/science_practical_diagrams.py',scope='Apparatus and measurement diagrams beside practical methods; shared artwork reused in the practical-skills chapter.',placements=audit),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print('Updated',topic.name,':',len(audit),'diagram placements')

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('subject',choices=['Physics','Chemistry','Biology']);p.add_argument('topic',type=int);args=p.parse_args();apply(args.subject,args.topic)
