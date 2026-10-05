"""Editable SVG diagrams for the new Biology resources."""
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]
BLUE='#2166ad';GREEN='#20816c';INK='#18344a';PURPLE='#7950a1'
def text(x,y,value,size=21,anchor='start',colour=INK):
 return f'<text x="{x}" y="{y}" font-family="Segoe UI, Arial, sans-serif" font-size="{size}" text-anchor="{anchor}" fill="{colour}">{escape(value)}</text>'
def arrow(points,colour=BLUE):
 return f'<path d="{points}" fill="none" stroke="{colour}" stroke-width="3" marker-end="url(#arrow)"/>'
def box(x,y,w,h,label,colour=BLUE):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#f1f7ff" stroke="{colour}" stroke-width="2"/>'+text(x+w/2,y+h/2+7,label,21,'middle')
def save(folder,name,title,body,w=1000,h=460):
 folder.mkdir(exist_ok=True)
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0 0L7 3L0 6" fill="{BLUE}"/></marker></defs><rect width="{w}" height="{h}" fill="white"/>{body}</svg>'
 (folder/(name+'.svg')).write_text(svg,encoding='utf-8')
def organisation():
 folder=ROOT/'Biology - AQA/02 - Organisation/Diagrams'
 s=''
 for i,(x,heading) in enumerate([(25,'Substrate approaches'),(350,'Substrate binds'),(675,'Products leave')]):
  s+=text(x+145,40,heading,24,'middle')
  s+=f'<path d="M{x+25} 145Q{x+25} 125 {x+45} 125H{x+115}L{x+145} 165L{x+175} 125H{x+245}Q{x+265} 125 {x+265} 145V240Q{x+265} 260 {x+245} 260H{x+45}Q{x+25} 260 {x+25} 240Z" fill="#e1effb" stroke="{BLUE}" stroke-width="3"/>'
  if i<2:
   y=65 if i==0 else 125
   s+=f'<path d="M{x+115} {y}H{x+175}L{x+145} {y+40}Z" fill="#f5cb87" stroke="#ac6a21" stroke-width="2"/>'
  else:
   s+=f'<path d="M{x+95} 65H{x+125}V105Z M{x+160} 65H{x+190}L{x+160} 105Z" fill="#f5cb87" stroke="#ac6a21" stroke-width="2"/>'
  s+=text(x+145,300,'Enzyme',21,'middle')
  if i<2:s+=arrow(f'M{x+283} 192H{x+313}')
 s+=text(500,355,'A complementary active site gives specificity.',24,'middle')+text(500,393,'The enzyme is unchanged and can be used again.',24,'middle')
 save(folder,'enzyme-action','Enzyme action: binding and product release',s,h=430)
 s=box(365,20,270,52,'Body')+box(45,150,260,52,'Right atrium')+box(45,255,260,52,'Right ventricle')+box(365,390,270,52,'Lungs')+box(695,255,260,52,'Left atrium')+box(695,150,260,52,'Left ventricle')
 s+=arrow('M365 46H175V145')+text(180,107,'Vena cava')+arrow('M175 205V250')+text(190,234,'Valve',18)
 s+=arrow('M175 310V415H360')+text(10,351,'Pulmonary artery',19)
 s+=arrow('M640 415H825V312')+text(838,352,'Pulmonary vein',19)
 s+=arrow('M825 250V207')+text(842,234,'Valve',18)+arrow('M825 145V46H640')+text(736,107,'Aorta')
 s+=text(500,191,'Two linked circuits',26,'middle')+text(500,229,'Right heart → lungs',20,'middle')+text(500,263,'Left heart → body',20,'middle')+text(500,303,'Valves prevent backflow',19,'middle')
 save(folder,'double-circulation','Blood flow through the four heart chambers, lungs and body',s,h=465)
 s=f'<rect x="45" y="40" width="510" height="10" fill="#54965b"/><rect x="45" y="50" width="510" height="40" fill="#e9f3db" stroke="{GREEN}"/>'
 for x in range(55,550,40):
  s+=f'<rect x="{x}" y="100" width="30" height="112" rx="12" fill="#bbd982" stroke="{GREEN}"/>'
  for y in [119,148,180]:s+=f'<ellipse cx="{x+15}" cy="{y}" rx="5" ry="8" fill="#5b913e"/>'
 for x,y in [(80,255),(180,235),(290,273),(90,325),(230,337),(352,324),(340,239)]:s+=f'<ellipse cx="{x}" cy="{y}" rx="30" ry="17" fill="#dbeabd" stroke="{GREEN}"/>'
 s+='<ellipse cx="452" cy="280" rx="56" ry="43" fill="#eff1df" stroke="#7c9863"/><circle cx="452" cy="260" r="15" fill="#c4def6" stroke="#2166ad"/><circle cx="452" cy="300" r="15" fill="#f2d6ad" stroke="#b87c35"/>'
 s+=f'<path d="M45 368H260V400H45Z M315 368H555V400H315Z" fill="#e9f3db" stroke="{GREEN}"/><ellipse cx="261" cy="384" rx="14" ry="22" fill="#aad083"/><ellipse cx="315" cy="384" rx="14" ry="22" fill="#aad083"/>'
 for y,label,px,py in [(44,'Waxy cuticle',555,44),(81,'Upper epidermis',555,72),(153,'Palisade mesophyll',555,153),(235,'Spongy mesophyll',325,238),(276,'Xylem',470,260),(314,'Phloem',470,300),(357,'Air spaces',195,298),(400,'Lower epidermis',555,385)]:
  s+=f'<path d="M{px} {py}L615 {y-6}H640" fill="none" stroke="#71858a" stroke-width="1.5"/>'+text(650,y,label,21)
 s+=text(280,449,'Stoma between guard cells',21,'middle')
 save(folder,'leaf-tissues','Leaf tissue cross-section',s,h=475)

def infection():
 folder=ROOT/'Biology - AQA/03 - Infection and response/Diagrams'
 s=text(500,35,'The same antigen triggers a faster second response',25,'middle')
 for x,title,second in [(65,'First exposure',False),(555,'Later exposure',True)]:
  s+=arrow(f'M{x} 300V75')+arrow(f'M{x} 300H{x+360}')
  s+=text(x+180,355,title,23,'middle')+text(x+180,387,'Time after exposure',18,'middle')
  s+=text(x+18,82,'Antibody level',18)
  curve=f'M{x+5} 298C{x+45} 298 {x+48} 100 {x+120} 100S{x+260} 160 {x+345} 195' if second else f'M{x+5} 298C{x+130} 298 {x+125} 220 {x+185} 220S{x+260} 266 {x+345} 285'
  s+=f'<path d="{curve}" fill="none" stroke="{GREEN if second else BLUE}" stroke-width="5"/>'
 s+=text(500,435,'Schematic curves: compare the delay and size of the response.',18,'middle')
 save(folder,'immune-memory','Immune memory: slower primary and faster secondary antibody response',s,h=460)
 s=box(40,35,320,65,'Mouse lymphocyte')+box(640,35,320,65,'Tumour cell')
 s+=text(200,136,'Makes a specific antibody',20,'middle')+text(800,136,'Divides repeatedly',20,'middle')
 s+=arrow('M360 68H500V170')+arrow('M640 68H500')+text(525,151,'Fuse',20)
 s+=box(345,175,310,60,'Hybridoma')+text(500,269,'Select one making the required antibody',21,'middle')
 s+=arrow('M500 283V315')+box(260,320,480,60,'Clone → many identical hybridomas')
 s+=arrow('M500 385V425')+box(260,430,480,60,'Collect and purify the antibodies')
 save(folder,'hybridoma','Production of monoclonal antibodies',s,h=520)

if __name__=='__main__':
 import sys
 functions={'organisation':organisation,'infection':infection}
 functions[sys.argv[1] if len(sys.argv)>1 else 'organisation']()
