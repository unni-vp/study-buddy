"""Editable vector diagrams for Physics notes and map memory cues."""
from pathlib import Path
from html import escape
from physics_helpers import ROOT,SUBJECT,TOPICS

def text(x,y,s,size=22,anchor='start',color='#18344a'):
 return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" fill="{color}">{escape(str(s))}</text>'
def path(d,color='#2166ad',width=3):return f'<path d="{d}" stroke="{color}" stroke-width="{width}" fill="none"/>'
def rect(x,y,w,h,fill='#e7f0fb'):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="#517386"/>'
def save(n,name,title,body,w=1000,h=370):
 p=ROOT/SUBJECT/TOPICS[n-1]/'Diagrams';p.mkdir(exist_ok=True)
 (p/(name+'.svg')).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><rect width="100%" height="100%" fill="#fffefa"/><g font-family="Segoe UI,Arial,sans-serif">'+body+'</g></svg>',encoding='utf-8')
def energy():
 b=text(35,40,'Follow the whole 100 J',27)+rect(45,100,280,100)+text(185,144,'Electrical input',23,'middle')+text(185,176,'100 J',23,'middle')
 b+=path('M325 150H430V105H570m-12-8 12 8-12 8')+path('M430 150V265H570m-12-8 12 8-12 8','#bc7132')
 b+=rect(580,60,375,100,'#e0f1e8')+text(767,100,'Useful lifting energy: 60 J',22,'middle')+text(767,134,'Gravitational potential store',20,'middle')
 b+=rect(580,215,375,100,'#fbe8d8')+text(767,255,'Unwanted heating: 40 J',22,'middle')+text(767,289,'Motor + surroundings',20,'middle')
 b+=text(45,344,'Efficiency = 60 / 100 = 0.60 = 60%; total output = total input.',21)
 save(1,'energy-budget','Energy is conserved: 100 J becomes 60 J useful and 40 J dissipated.',b)
def electricity():
 b=''
 labels=['Cell','Battery','Open switch','Resistor','Variable resistor','Lamp','Ammeter','Voltmeter','Diode','LED','Thermistor','LDR']
 for j,label in enumerate(labels):
  x=30+(j%4)*245;y=45+(j//4)*130
  if j in [0,1]:
   drawing=path('M0 0H70M70-25V25M85-13V13M85 0H180')
   if j==1:drawing=path('M0 0H55M55-25V25M70-13V13M70 0H100M100-25V25M115-13V13M115 0H180')
  elif j==2:drawing=path('M0 0H65M65 0L110-28M115 0H180')
  elif j in [3,4,10,11]:
   drawing=path('M0 0H55M125 0H180')+'<rect x="55" y="-15" width="70" height="30" fill="white" stroke="#2166ad" stroke-width="3"/>'
   if j==4:drawing+=path('M55 30L126-35m-14 3 14-3-4 14')
   if j==10:drawing+=path('M50 27H66L113-27')
   if j==11:drawing+='<circle cx="90" cy="0" r="46" fill="none" stroke="#2166ad" stroke-width="2"/>'+path('M37-49L65-22m-10-3 10 3-3-10M58-58L86-31m-10-3 10 3-3-10')
  elif j in [5,6,7]:
   drawing=path('M0 0H65M115 0H180')+'<circle cx="90" cy="0" r="25" fill="white" stroke="#2166ad" stroke-width="3"/>'
   drawing+=path('M73-17L107 17M73 17L107-17') if j==5 else text(90,8,'A' if j==6 else 'V',25,'middle')
  else:
   drawing=path('M0 0H70M110 0H180M110-22V22')+'<path d="M70-22V22L110 0Z" fill="none" stroke="#2166ad" stroke-width="3"/>'
   if j==9:drawing+=path('M100-30L126-56m-11 2 11-2-2 11M122-18L148-44m-11 2 11-2-2 11')
  b+=f'<g transform="translate({x} {y+25})">'+drawing+'</g>'+text(x+90,y+90,label,20,'middle')
 save(2,'circuit-symbols','Standard circuit symbols used in GCSE Physics.',b,h=410)
 b=path('M120 90H260M300 90H850V280M120 90V280H345M260 64V116M300 75V105')+text(280,40,'Low-voltage supply',22,'middle')
 b+=path('M280 280H345M395 280H525M665 280H850')+'<circle cx="370" cy="280" r="25" fill="white" stroke="#2166ad" stroke-width="3"/>'+text(370,288,'A',24,'middle')
 b+='<rect x="525" y="261" width="140" height="38" fill="white" stroke="#2166ad" stroke-width="3"/>'+text(595,333,'Test resistor',22,'middle')
 b+=path('M490 280V175H570M620 175H700V280')+'<circle cx="595" cy="175" r="25" fill="white" stroke="#2166ad" stroke-width="3"/>'+text(595,183,'V',24,'middle')
 for x in [490,700]:b+=f'<circle cx="{x}" cy="280" r="5" fill="#2166ad"/>'
 b+=text(45,385,'Ammeter: series',23)+text(470,385,'Voltmeter: parallel across test resistor',23)
 save(2,'resistance-circuit','Ammeter in series; voltmeter connected across the resistor.',b,h=420)
 b=''
 for j,label in enumerate(['Ohmic resistor','Filament lamp','Diode']):
  x=25+j*330;b+=text(x+150,35,label,24,'middle')+path(f'M{x+15} 185H{x+290}M{x+150} 320V65','#657580',2)+text(x+298,191,'V',18)+text(x+158,70,'I',18)
  if j==0:d=f'M{x+40} 290L{x+260} 80'
  elif j==1:d=f'M{x+25} 285C{x+120} 280 {x+115} 240 {x+150} 185S{x+175} 90 {x+275} 85'
  else:d=f'M{x+20} 187H{x+195}C{x+225} 187 {x+230} 160 {x+245} 80'
  b+=path(d,width=4)+text(x+150,356,['Constant temperature','Resistance rises as it heats','Forward conduction'][j],18,'middle')
 save(2,'iv-graphs','I against V: straight resistor graph, flattening lamp curve and one-way diode conduction.',b,h=385)
def particles():
 b=path('M85 70V345H940','#617480',2)+text(45,39,'Temperature',22)+text(800,390,'Energy supplied',22)
 b+=path('M110 320L260 260H400L580 145H760L900 70',width=5)
 for x,y,label in [(180,288,'Solid'),(318,244,'Melting'),(480,195,'Liquid'),(662,125,'Boiling'),(865,55,'Gas')]:b+=text(x,y,label,21,'middle')
 b+=text(280,435,'Flat sections: state changes, temperature stays constant.',22)
 save(3,'heating-curve','Heating curve: warming slopes alternate with melting and boiling plateaus. Schematic, not to scale.',b,h=470)
def atoms():
 import math
 b=path('M110 55V330H920','#617480',2)+text(35,32,'Source count rate (counts/s)',22)+text(800,391,'Time (hours)',22)
 for val in [0,50,100,200,400]:
  y=330-val*.6;b+=text(95,y+7,val,19,'end')+path(f'M105 {y}H920','#ddd',1)
 points=[]
 for i in range(81):
  t=i/10;x=110+t*95;y=330-400*(.5**(t/2))*.6;points.append(f'{x},{y}')
 b+=f'<polyline points="{" ".join(points)}" stroke="#2166ad" stroke-width="4" fill="none"/>'
 for t in [0,2,4,6,8]:
  x=110+t*95;y=330-400*(.5**(t/2))*.6
  b+=text(x,362,t,19,'middle')+f'<circle cx="{x}" cy="{y}" r="5" fill="#b46d29"/>'
 b+=text(160,431,'Equal two-hour intervals halve the count rate. Background already subtracted.',21)
 save(4,'half-life','Count rate halves every two hours: 400 to 200 to 100 to 50.',b,h=465)
 b=text(30,35,'Fission: a large nucleus splits',25)+text(530,35,'Fusion: light nuclei join',25)
 for x,y,r,c in [(135,150,45,'#d9c8ee'),(350,105,28,'#e1c4b1'),(350,230,28,'#c7e0c7'),(590,145,20,'#d3e8fa'),(590,245,24,'#dbd0ec'),(835,195,38,'#d6e8cc')]:
  b+=f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" stroke="#517386" stroke-width="2"/>'
 b+=f'<circle cx="40" cy="150" r="6" fill="#18344a"/>'+path('M50 150H80m-8-6 8 6-8 6')+text(35,115,'neutron',18)
 b+=path('M190 150L306 112m-11-3 11 3-7 9M190 155L306 222m-6-11 6 11-12-1')
 for x,y in [(450,125),(450,175),(450,225)]:b+=f'<circle cx="{x}" cy="{y}" r="6" fill="#18344a"/>'+path(f'M385 170L{x-12} {y}')
 b+=text(225,298,'2 smaller nuclei + neutrons',20,'middle')+text(225,328,'+ gamma + released energy',20,'middle')
 b+=path('M615 145L780 183m-8-8 8 8-12 3M621 245L780 207m-12-3 12 3-8 8')+text(750,298,'1 heavier nucleus + energy',20,'middle')
 b+=text(30,381,'Fission neutrons can trigger more fissions → chain reaction.',22)+text(30,415,'Schematic: shapes show splitting/joining, not individual nucleons or scale.',18)
 save(4,'fission-fusion','Fission splits a large nucleus and emits neutrons. Fusion joins light nuclei.',b,h=445)
def forces():
 b=text(35,35,'Two components, one resultant',26)+path('M100 490H400m-13-8 13 8-13 8','#18837b',4)+path('M400 490V90m-8 13 8-13 8 13','#7750a1',4)+path('M100 490L400 90m-15 5 15-5-1 16','#2166ad',4)
 b+=text(250,535,'3 N right',23,'middle')+text(430,290,'4 N upwards',23)+text(95,225,'5 N resultant',23)+text(560,415,'Tail → tip gives resultant.',23)+text(560,453,'Same scale on both axes.',23)
 save(5,'force-components','A true-scale 3–4–5 vector triangle: right and upward forces combine diagonally.',b,h=560)
 b=text(35,35,'Velocity (m/s)',23)+path('M90 70V340H850','#617480',2)
 b+='<path d="M90 340L490 100V340Z" fill="#dbeafa"/><path d="M490 100H790V340H490Z" fill="#deefdf"/>'+path('M90 340L490 100H790',width=4)
 b+=text(68,108,'8',20,'end')+text(68,348,'0',20,'end')+text(90,374,'0',20,'middle')+text(490,374,'4',20,'middle')+text(790,374,'7',20,'middle')+text(840,412,'Time (s)',21,'end')
 save(5,'velocity-time-question','Velocity increases from 0 to 8 m/s in 4 seconds, then remains constant until 7 seconds.',b,h=435)
 b+=text(300,291,'½ × 4 × 8 = 16 m',21,'middle')+text(640,230,'3 × 8 = 24 m',21,'middle')+text(100,447,'Slope first 4 s = 2 m/s². Total area = displacement = 40 m.',23)
 save(5,'velocity-time','Velocity rises uniformly to 8 m/s in four seconds then stays constant for three seconds.',b,h=480)

if __name__=='__main__':
 import sys
 [energy,electricity,particles,atoms,forces][int(sys.argv[1])-1]()
