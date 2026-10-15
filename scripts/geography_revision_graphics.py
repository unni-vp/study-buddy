"""Editable, original Geography learning diagrams; no copied guide artwork."""
from pathlib import Path
from html import escape
import textwrap,sys,json
ROOT=Path(__file__).resolve().parents[1] if Path(__file__).parent.name=='scripts' else Path('D:/Shreya/study-buddy')
INK='#172b3d';BLUE='#147db3';ORANGE='#b65c1a';GREEN='#367c40'
def txt(x,y,s,size=21,bold=False,anchor='start',color=INK):
 return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{700 if bold else 400}" text-anchor="{anchor}" fill="{color}">{escape(s)}</text>'
def paragraph(x,y,s,width=40,size=21):
 return ''.join(txt(x,y+i*29,line,size) for i,line in enumerate(textwrap.wrap(s,width)))
def box(x,y,w,h,fill='#f5f8fa',stroke='#81939f',r=10):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
def arrow(x1,y1,x2,y2,color=BLUE):return f'<path d="M{x1},{y1}L{x2},{y2}" fill="none" stroke="{color}" stroke-width="3" marker-end="url(#arrow)"/>'
def line(x1,y1,x2,y2,color='#687d8c'):return f'<path d="M{x1},{y1}L{x2},{y2}" stroke="{color}" fill="none" stroke-width="2"/>'
def document(title,desc,body,h=510):return f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{h}" viewBox="0 0 1200 {h}" role="img" aria-labelledby="title desc" font-family="Segoe UI,Arial,sans-serif"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="4" markerHeight="4" orient="auto-start-reverse"><path d="M1 1L9 5L1 9" stroke="{BLUE}" stroke-width="2" fill="none"/></marker></defs><rect width="1200" height="{h}" fill="white"/>'+txt(30,40,title,28,True)+body+'</svg>'
def waterfall():
 b=box(25,70,710,370,'#eef8ff')
 b+='<path d="M45 180H350V230Q310 300 400 340C430 395 490 395 530 340H710V420H45Z" fill="#d5ac75" stroke="#92724c" stroke-width="2"/><path d="M45 160H410V215H350V180H45Z" fill="#959da4" stroke="#57636e" stroke-width="2"/><path d="M400 337C430 390 490 390 530 337Z" fill="#2998cb"/><path d="M45 150H395Q422 150 422 180V297Q422 337 470 337H710" stroke="#2998cb" stroke-width="12" fill="none"/><path d="M410 360l18 19 21-13-9-18zM455 372l15-17 18 25z" fill="#727d85"/>'
 b+=txt(60,130,'River flow',21)+arrow(190,144,285,144)+txt(475,120,'Resistant rock',20)+line(480,128,375,190)+txt(65,300,'Less resistant rock',20)
 b+=txt(475,206,'Overhang',20)+line(465,211,405,211)+txt(515,305,'Plunge pool',20)+line(530,312,455,337)
 b+=txt(64,390,'Retreat upstream',20)+arrow(285,375,170,375)
 b+=paragraph(765,105,'1. Softer rock erodes faster.',34)+paragraph(765,175,'2. Undercutting leaves an unsupported overhang.',34)+paragraph(765,275,'3. Collapse adds rock to the plunge pool.',34)+paragraph(765,375,'4. Repetition leaves a gorge as the waterfall retreats.',34)
 return document('Waterfall retreat and gorge formation','A side view shows water crossing resistant rock, undercutting softer rock, an overhang and collapsed blocks in a plunge pool. The waterfall retreats upstream.',b)
def oxbow():
 b=''
 for i,title in enumerate(['1. Neck narrows','2. Flood cuts through','3. Old bend is isolated']):
  x=25+i*390;b+=box(x,75,370,335,'#eef4df')+txt(x+20,110,title,23,True)
  path=f'M{x+65} 145C{x+65} 210 {x+285} 120 {x+285} 240S{x+65} 275 {x+65} 355'
  if i<2:b+=f'<path d="{path}" stroke="#54acd0" stroke-width="32" fill="none"/>'
  if i==0:b+=txt(x+135,245,'Neck',20)+line(x+133,240,x+100,240)
  else:b+=f'<path d="M{x+65} 145V355" stroke="#54acd0" stroke-width="32"/>'
  if i==2:b+=f'<path d="M{x+150} 175C{x+340} 175 {x+340} 305 {x+150} 305" stroke="#54acd0" stroke-width="32" stroke-linecap="round" fill="none"/>'+box(x+100,160,30,30,'#ddbf78','#ddbf78',0)+box(x+100,290,30,30,'#ddbf78','#ddbf78',0)+txt(x+150,250,'Oxbow lake',20)
  b+=arrow(x+65,310,x+65,345)
 b+=paragraph(35,455,'Outer-bank erosion and inner-bank deposition enlarge bends. High flow can cut a shorter route. Deposition closes the entrances to the old bend.',94)
 return document('Meander cut-off and an oxbow lake','Three plan views show a meander with a narrowing neck, a flood cut-through, then a straighter channel and cut-off lake closed by sediment.',b,540)
def drift():
 b=box(25,75,1150,330,'#bfe7f4')+'<path d="M26 76H1174V240H26Z" fill="#f4d797"/>'+line(25,240,1175,240)
 b+=txt(50,115,'LAND / BEACH',23,True)+txt(50,370,'SEA',23,True)+txt(1030,230,'Shoreline',20)
 for x in [180,330,480,630]:b+=arrow(x,300,x+150,180)+arrow(x+150,180,x+150,300)
 b+=txt(90,445,'Swash: obliquely up the beach',22,True)+txt(620,445,'Backwash: straight downhill',22,True)
 b+=arrow(650,130,1030,130)+txt(715,112,'Net sediment movement',21)
 b+=arrow(65,340,150,275)+txt(40,397,'Waves approach',18)
 return document('Longshore drift: movement along a beach','A plan view shows swash travelling diagonally up the beach and gravity returning backwash at right angles to the shoreline. Repeated zigzags move sediment along the coast.',b)
def dtm():
 b='';bounds=[80,290,500,710,920,1130]
 for i in range(5):b+=box(bounds[i],85,210,310,'#f8f5eb',stroke='#d7d2c5',r=0)+txt(bounds[i]+105,120,f'Stage {i+1}',22,True,'middle')
 b+=line(80,395,1135,395)+line(80,395,80,150)
 birth='M80 180C160 170 220 190 290 180S430 180 500 190S650 285 710 310S850 330 920 330S1050 345 1130 353'
 death='M80 185C160 195 220 175 290 190S400 300 500 322S650 333 710 332S860 333 920 332S1060 325 1130 325'
 b+=f'<path d="{birth}" fill="none" stroke="{ORANGE}" stroke-width="5"/><path d="{death}" fill="none" stroke="{BLUE}" stroke-width="5"/>'
 b+=txt(85,65,'Birth / death rates: schematic, not measured country data',20)+txt(80,435,'Earlier development',20)+txt(1130,435,'Later development',20,anchor='end')+line(360,475,415,475,ORANGE)+txt(425,482,'Birth rate',21)+line(620,475,675,475,BLUE)+txt(685,482,'Death rate',21)
 b+=txt(300,155,'Deaths fall first',19,color=BLUE)+txt(530,265,'Births fall later',19,color=ORANGE)
 return document('Demographic Transition Model','Five stages show death rates falling before birth rates. The birth-death gap indicates natural population change. Migration is not included. Curves are a schematic model, not a dataset.',b,530)
def pyramid():
 vals=[(9,8),(10,10),(11,12),(13,14),(15,16),(14,16),(12,14),(8,11)]
 b=txt(315,92,'Male',23,True,'middle')+txt(840,92,'Female',23,True,'middle')
 for i,(m,f) in enumerate(reversed(vals)):
  y=120+i*36;age=['70+','60–69','50–59','40–49','30–39','20–29','10–19','0–9'][i]
  b+=box(520-m*19,y,m*19,28,'#7eafe0',stroke='white',r=0)+box(675,y,f*19,28,'#d1a0d9',stroke='white',r=0)+txt(598,y+22,age,20,anchor='middle')
 b+=txt(598,90,'Age',21,True,'middle')+txt(320,445,'Younger ages at the bottom',21,anchor='middle')+txt(840,445,'Older ages at the top',21,anchor='middle')
 b+=txt(600,492,'Bar length: share within each sex (illustrative values, not UK data)',21,anchor='middle')
 b+=paragraph(35,545,'Read age, sex and bar length together. A bulge is a large cohort; a broad upper section suggests a larger older population. The shape alone does not prove its causes.',105)
 return document('Reading a population pyramid','An illustrative pyramid uses horizontal bars by age, males left and females right. The example is not a real UK population dataset.',b,650)
def electricity():
 values=[('Renewables',50.4,GREEN),('Fossil fuels',31.8,ORANGE),('Nuclear',14.2,'#8155a4'),('Other fuels',3.6,'#73818a')]
 b=txt(35,80,'Share of UK electricity generated, 2024 (%) — DUKES 2025 publication',21)
 for tick in range(0,61,10):x=250+tick*13;b+=line(x,115,x,395,'#dce3e9')+txt(x,430,str(tick),20,anchor='middle')
 for i,(label,value,c) in enumerate(values):y=125+i*68;b+=txt(220,y+31,label,23,True,'end')+box(250,y,value*13,44,c,c,0)+txt(260+value*13,y+31,f'{value:.1f}%',22,True)
 b+=txt(250,470,'Electricity generation is not the same as total energy consumption.',22,True)
 return document('UK electricity generation mix: 2024','A zero-based bar chart shows renewables 50.4%, fossil fuels 31.8%, nuclear 14.2% and other fuels 3.6%, the remainder to 100 using published rounded shares. Source DUKES 2025.',b,510)
def digestion():
 b='';steps=[('Crops and slurry','Organic feedstock'),('Sealed digester','No oxygen: microbes act'),('Methane-rich biogas','Fuel for an engine'),('Heat and electricity','Local use / grid export')]
 for i,(head,desc) in enumerate(steps):x=25+i*295;b+=box(x,100,265,170,'#eff5e8')+paragraph(x+17,142,head,18,size=23)+paragraph(x+17,217,desc,21,size=19)
 for i in range(3):b+=arrow(292+i*295,185,315+i*295,185)
 b+=box(320,345,530,100,'#f7f0df')+txt(585,385,'Digestate: nutrients returned to fields',22,True,'middle')+txt(585,420,'Manage storage and spreading to avoid pollution',20,anchor='middle')
 b+=arrow(450,275,450,335)
 return document('Anaerobic digestion: energy and nutrient recovery','Feedstock enters an oxygen-free digester. Microbes produce methane-rich gas, used to generate heat and electricity. Digestate is returned to fields; it is not the material burned in the engine.',b)
def nutrients():
 b=box(65,110,320,110,'#e8f3df')+txt(225,155,'BIOMASS',25,True,'middle')+txt(225,190,'Largest nutrient store',21,anchor='middle')
 b+=box(815,110,320,110,'#f6ebd5')+txt(975,155,'LITTER',25,True,'middle')+txt(975,190,'Dead leaves and organisms',20,anchor='middle')
 b+=box(440,340,320,110,'#f3e3cf')+txt(600,383,'SOIL',25,True,'middle')+txt(600,420,'Small store: rapid uptake',20,anchor='middle')
 b+=arrow(400,165,800,165)+txt(600,140,'Leaf fall and death',21,anchor='middle')+arrow(950,230,770,368)+txt(1000,300,'Rapid decay',21,anchor='middle')+arrow(425,365,245,230)+txt(195,310,'Root uptake',21,anchor='middle')
 b+=txt(600,495,'Warmth and moisture speed decomposition. Heavy rain can leach exposed soil.',21,anchor='middle')
 return document('Tropical rainforest nutrient cycle','Nutrients move from biomass to litter through death, to soil through decomposition and back to vegetation through root uptake. The living biomass is the largest store.',b,540)
def coral():
 b=box(35,100,475,220,'#f7efdf')+txt(272,145,'CORAL ANIMAL',25,True,'middle')+paragraph(65,192,'Provides a protected home and nutrients from its wastes.',31)
 b+=box(690,100,475,220,'#e9f4dc')+txt(927,145,'ALGAE IN CORAL TISSUE',25,True,'middle')+paragraph(720,192,'Use sunlight to photosynthesise and pass food to the coral.',31)
 b+=arrow(520,190,680,190)+txt(600,170,'Shelter',19,anchor='middle')+arrow(680,275,520,275)+txt(600,252,'Food',19,anchor='middle')
 b+=box(120,375,960,105,'#eaf5fb')+txt(600,415,'Heat stress can cause algae to be expelled: coral becomes pale.',23,True,'middle')+txt(600,453,'Bleached coral may recover, but prolonged stress can kill it.',22,anchor='middle')
 return document('Coral and algae: a two-way partnership','Coral polyps house photosynthetic algae and supply nutrients. Algae provide food. Heat stress can break the partnership and cause bleaching, which is not always immediate death.',b,520)
def rostow():
 b='';names=['Traditional society','Preconditions','Take-off','Drive to maturity','High mass consumption']
 for i,name in enumerate(names):x=25+i*232;y=330-i*52;b+=box(x,y,215,100,'#eef2f8')+txt(x+15,y+32,str(i+1),24,True)+paragraph(x+15,y+63,name,19,size=20)
 for i in range(4):b+=arrow(210+i*232,315-i*52,260+i*232,265-i*52)
 b+=txt(40,500,'A model of development, not a measured graph or a guaranteed path for every country.',22,True)
 return document('Rostow’s five-stage model','Steps represent traditional society, preconditions, take-off, maturity and high mass consumption. Arrows show the sequence proposed by the model, not an inevitable path or measured country trend.',b,540)
def circulation():
 b='';xs=[80,245,410,600,790,955,1120];labels=['90°S','60°S','30°S','0°','30°N','60°N','90°N'];rising=[False,True,False,True,False,True,False]
 b+=line(65,370,1140,370)
 for x,label,up in zip(xs,labels,rising):
  b+=txt(x,410,label,23,True,'middle')+arrow(x,350 if up else 150,x,150 if up else 350)+txt(x,450,'LOW' if up else 'HIGH',21,True,'middle')
 for i in range(6):
  x1,x2=xs[i],xs[i+1];leftUp=rising[i]
  b+=arrow(x1+12 if leftUp else x2-12,145,x2-12 if leftUp else x1+12,145)+arrow(x2-12 if leftUp else x1+12,350,x1+12 if leftUp else x2-12,350)
 for x,name in [(160,'Polar'),(330,'Ferrel'),(500,'Hadley'),(700,'Hadley'),(870,'Ferrel'),(1040,'Polar')]:b+=txt(x,260,name,21,True,'middle')
 b+=txt(600,505,'Rising air: cooling, clouds and rain. Sinking air: warming and generally drier skies.',21,anchor='middle')
 return document('Global atmospheric circulation: a cross-section','Six schematic circulation cells show rising air and low pressure at the Equator and 60 degrees, sinking air and high pressure at 30 degrees and the poles. Surface winds also turn because of Earth’s rotation.',b,550)
def enso():
 b=''
 for i,(title,west,east) in enumerate([('Neutral conditions','Warm pool / wetter west','Cooler water / upwelling'),('El Niño tendency','Less rain in parts of Australia','Warming spreads east')]):
  y=80+i*235;b+=box(25,y,1150,215,'#eef7fc')+txt(45,y+35,title,24,True)+txt(65,y+80,'Australia / Indonesia (west)',21,True)+txt(815,y+80,'South America (east)',21,True)
  b+=box(70,y+105,1050,35,'#70c7e9',stroke='#70c7e9',r=0)+box(70,y+105,480 if i==0 else 900,35,'#f0a46a',stroke='#f0a46a',r=0)
  b+=arrow(1040,y+90,210 if i==0 else 650,y+90)+txt(600,y+65,'Easterly trade winds' if i==0 else 'Trade winds weaken',20,anchor='middle')
  b+=txt(75,y+180,west,21)+txt(780,y+180,east,21)
 b+=txt(600,595,'Patterns change probabilities. Not every drought is caused by El Niño.',22,True,'middle')
 return document('Pacific Ocean: neutral conditions and El Niño','Two schematic equatorial Pacific panels compare strong westward trade winds and a western warm pool with weaker winds and warm water extending east. Rainfall shifts east and drought risk can rise in parts of Australia.',b,630)
FIGURES={1:{'waterfall-retreat':waterfall,'oxbow-lake':oxbow,'longshore-drift':drift},2:{'demographic-transition':dtm,'population-pyramid':pyramid},3:{'uk-electricity-2024':electricity,'anaerobic-digestion':digestion},4:{'rainforest-nutrient-cycle':nutrients,'coral-symbiosis':coral},5:{'rostow-model':rostow},6:{'atmospheric-circulation':circulation,'enso-patterns':enso}}
def build(n):
 folder=next((ROOT/'Geography - OCR A').glob(f'{n:02d} - *'))/'Revision Notes'/'diagrams';folder.mkdir(exist_ok=True)
 for slug,fn in FIGURES[n].items():(folder/(slug+'.svg')).write_text(fn(),encoding='utf-8')
 print('Built',n,len(FIGURES[n]),'original diagrams')
if __name__=='__main__':build(int(sys.argv[1]))
