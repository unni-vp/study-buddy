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
