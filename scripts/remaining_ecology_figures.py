"""Measured ecology relationships: arrows represent actual transfers."""
from biology_explanatory_figures import label,arrow,BLUE,GREEN,ORANGE
from html import escape

def carbon(w):
    if w<500:raise ValueError('Carbon-cycle notes figure needs 500 units')
    boxes=[(w/2,35,'Atmospheric CO₂'),(w*.22,170,'Plants'),(w*.78,170,'Animals'),(w/2,300,'Dead matter / waste')];s=''
    for x,y,t in boxes:s+=f'<rect x="{x-94}" y="{y-20}" width="188" height="40" rx="9" fill="#eff6ee" stroke="{GREEN}"/>'+label(x,y+5,t,'middle')
    s+=arrow(w/2-75,58,w*.22+14,147)+label(8,103,'Photosynthesis')
    s+=arrow(w*.22+98,170,w*.78-98,170)+label(w/2,156,'Feeding','middle')
    s+=arrow(w*.78-10,147,w/2+75,58)+label(w-5,102,'Respiration','end')
    s+=arrow(w*.22-16,147,w/2-100,58)+label(5,130,'Plant respiration')
    s+=arrow(w*.22+20,194,w/2-65,278)+arrow(w*.78-20,194,w/2+65,278)
    s+=label(6,249,'Death')+label(w-6,249,'Death / waste','end')
    s+=f'<path d="M{w/2+98} 300H{w-20}V35H{w/2+99}" fill="none" stroke="{BLUE}" stroke-width="2"/>'+arrow(w/2+122,35,w/2+98,35)
    s+=label(w/2,355,'Microbial decay and respiration return CO₂','middle')+label(w/2,383,'Burning fuels and biomass also releases CO₂','middle')
    return s,395

def sampling(w):
    if w<300:raise ValueError('Sampling plan needs 300 units')
    x=37;y=27;bw=w-65;bh=126;s=f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" fill="#f4f8ec" stroke="#829580"/>'
    for yy,t in [(27,'10'),(90,'5'),(153,'0')]:s+=label(28,yy+5,t,'end')
    s+=label(x,180,'0')+label(x+bw,180,'10','end')
    for fx,fy in ((.2,.2),(.65,.7),(.82,.15),(.35,.8)):
        xx=x+bw*fx;yy=y+bh*fy;s+=f'<rect x="{xx}" y="{yy}" width="21" height="21" fill="#c5dda9" stroke="{GREEN}"/>'
    s+=label(w/2,211,'Random coordinates select quadrats','middle')+label(w/2,239,'Axes: metres across the habitat','middle')
    return s,251

def biomass(w):
    if w<300:raise ValueError('Biomass bars need 300 units')
    # Common scale: exact 1000 : 100 : 10 mass relationship.
    scale=(w-34)/1000;s=''
    for mass,y,t in [(10,32,'Secondary: 10 kg'),(100,93,'Primary: 100 kg'),(1000,154,'Producers: 1000 kg')]:
        width=mass*scale;s+=f'<rect x="{(w-width)/2}" y="{y}" width="{width}" height="23" fill="{GREEN}" stroke="#65795d"/>'+label(w/2,y-8,t,'middle')
    s+=label(w/2,207,'All widths use the same mass scale','middle')+label(w/2,235,'Example: 10% transferred each time','middle')
    return s,247

RAW={'remaining-carbon-cycle':carbon,'remaining-sampling':sampling,'remaining-biomass':biomass}
PURPOSES={'remaining-carbon-cycle':'Shows carbon passing through photosynthesis, feeding, death and microbial respiration, with plant and animal respiration returning atmospheric carbon dioxide.','remaining-sampling':'Shows quadrat positions chosen by coordinates, distinguishing random habitat sampling from convenient placements.','remaining-biomass':'Draws mass-scaled biomass bars with producers at the base, avoiding a false equal-width pyramid.'}
def wrapper(kind):
    def draw(w):
        s,h=RAW[kind](w);return '<g class="concept-illustration"><title>'+escape(PURPOSES[kind])+'</title>'+s+'</g>',h
    return draw
FIGURES={k:wrapper(k) for k in RAW}
