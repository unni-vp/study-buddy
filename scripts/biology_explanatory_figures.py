"""Mechanism diagrams for readable Biology maps; draw at final label size.

Every diagram has a specific learning purpose. No decorative branch icons.
Coordinates adapt to panel width; labels remain 16 units (11.2 pt on A4).
"""
from html import escape
import math

BLACK='#000000'; BLUE='#2366a0'; GREEN='#468133'; ORANGE='#b95619'; PURPLE='#7651a5'; RED='#b74650'

def label(x,y,value,anchor='start'):
    return f'<text class="diagram-label" x="{x}" y="{y}" font-size="16" fill="{BLACK}" text-anchor="{anchor}">{escape(value)}</text>'

def arrow(x1,y1,x2,y2,color=BLUE,thin=False):
    a=math.atan2(y2-y1,x2-x1); n=5
    return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" stroke-width="{1.3 if thin else 2.3}" fill="none"/><path d="M{x2-n*math.cos(a-.5)} {y2-n*math.sin(a-.5)}L{x2} {y2}L{x2-n*math.cos(a+.5)} {y2-n*math.sin(a+.5)}" stroke="{color}" stroke-width="2" fill="none"/>'

def leader(points):return f'<path d="{points}" stroke="#64747d" stroke-width="1.1" fill="none"/>'

def box(x,y,w,h,value,c=BLUE):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{c}" fill-opacity=".06" stroke="{c}" stroke-width="1.5"/>'+label(x+w/2,y+h/2+5,value,'middle')

def osmosis(w):
    mid=w/2
    s=label(w/4,16,'Dilute','middle')+label(w*3/4,16,'Concentrated','middle')
    s+=f'<rect x="2" y="25" width="{w-4}" height="66" rx="5" fill="#eef7fc" stroke="#94b4c6"/><path d="M{mid} 25V91" stroke="{GREEN}" stroke-width="2" stroke-dasharray="5 4"/>'
    # Equal compartments: concentration is a proportion, not a compartment-size effect.
    for side,waters,solutes in [(0,[(.12,37),(.29,37),(.46,38),(.65,37),(.17,56),(.40,59),(.15,79),(.41,79)],[(.64,78)]),(1,[(.17,40),(.72,57),(.39,78)],[(.44,36),(.68,38),(.17,61),(.42,60),(.63,79),(.84,79)])]:
        base=side*mid
        for x,y in waters:s+=f'<circle cx="{base+x*mid}" cy="{y}" r="3.5" fill="{BLUE}"/>'
        for x,y in solutes:s+=f'<rect x="{base+x*mid-4}" y="{y-4}" width="8" height="8" fill="{ORANGE}"/>'
    s+=arrow(mid-22,48,mid+22,48)+arrow(mid+22,73,mid-22,73,thin=True)
    s+=label(w/2,111,'Net water movement: dilute to concentrated','middle') if w>=330 else label(w/2,111,'Net water: dilute to concentrated','middle')
    s+=f'<circle cx="8" cy="130" r="4" fill="{BLUE}"/>'+label(18,135,'Water')+f'<rect x="95" y="126" width="8" height="8" fill="{ORANGE}"/>'+label(111,135,'Shown solute cannot cross')
    s+=label(w/2,160,'Dashed line: membrane','middle')
    return s,170

def cubes(w):
    s=''
    for x,a in [(w*.18,25),(w*.59,75)]:
        y=96-a;dx=a*.27;dy=a*.18
        s+=f'<path d="M{x} {y}l{dx} {-dy}h{a}l{-dx} {dy}Z" fill="#fff0d8" stroke="{ORANGE}"/><path d="M{x+a} {y}l{dx} {-dy}v{a}l{-dx} {dy}Z" fill="#efd1ad" stroke="{ORANGE}"/><rect x="{x}" y="{y}" width="{a}" height="{a}" fill="#fce8ce" stroke="{ORANGE}"/>'
        s+=label(x+a/2,118,'1 cm' if a==25 else '3 cm','middle')
        s+=label(x+a/2,140,'SA/V = 6' if a==25 else 'SA/V = 2','middle')
    return s,148

def fission(w):
    s=''
    centres=[w*.15,w*.5,w*.84]
    def cell(x,y,rx,ry,copies=1):
        out=f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#e8f4ed" stroke="{GREEN}" stroke-width="1.8"/>'
        for dx in ([0] if copies==1 else [-14,14]):out+=f'<ellipse cx="{x+dx}" cy="{y}" rx="9" ry="12" fill="none" stroke="{PURPLE}" stroke-width="2"/>'
        return out
    s+=cell(centres[0],42,28,20)+cell(centres[1],42,35,20,2)
    s+=cell(centres[2],23,24,15)+cell(centres[2],62,24,15)
    s+=arrow(centres[0]+32,42,centres[1]-39,42)+arrow(centres[1]+39,42,centres[2]-30,42)
    for x,value in zip(centres,['One cell','DNA copies','Two cells']):s+=label(x,100,value,'middle')
    s+=label(w/2,126,'Purple: DNA, not a nucleus','middle')
    return s,136

def enzyme(w):
    s='';step=w/3
    for i in range(3):
        x=step*(i+.5)
        s+=f'<path d="M{x-34} 62H{x-12}L{x} 80L{x+12} 62H{x+34}V103H{x-34}Z" fill="#e5effb" stroke="{BLUE}" stroke-width="1.5"/>'
        if i<2:
            y=28 if i==0 else 62
            s+=f'<path d="M{x-12} {y}H{x+12}L{x} {y+18}Z" fill="#f7d69e" stroke="{ORANGE}"/>'
            if i==0:s+=arrow(x,48,x,58,ORANGE)
        else:
            s+=f'<path d="M{x-23} 28H{x-11}V46Z M{x+11} 28H{x+23}L{x+11} 46Z" fill="#f7d69e" stroke="{ORANGE}"/>'
            s+=arrow(x,59,x,48,ORANGE)
        s+=label(x,16,['Substrate','Bound','Products'][i],'middle')
        if i<2:s+=arrow(x+38,86,x+step-38,86)
    s+=label(w/2,127,'Enzyme unchanged and reused','middle')
    return s,138

def circulation(w):
    # Two closed linked circuits: names and arrows show actual blood flow.
    left=65;right=w-65;mid=w/2;bw=122
    s=box(mid-43,0,86,27,'Body',RED)+box(mid-44,209,88,27,'Lungs',BLUE)
    for x,y,value,c in [(left,67,'Right atrium',BLUE),(left,117,'Right ventricle',BLUE),(right,67,'Left ventricle',RED),(right,117,'Left atrium',RED)]:s+=box(x-bw/2,y,bw,27,value,c)
    s+=f'<path d="M{mid-45} 13H115V50H{left}" stroke="{BLUE}" stroke-width="2.3" fill="none"/>'+arrow(left,50,left,61,BLUE)+label(4,43,'Vena cava')
    s+=arrow(left,96,left,113,BLUE)+f'<path d="M{left} 149V157H115V223" stroke="{BLUE}" stroke-width="2.3" fill="none"/>'+arrow(115,223,mid-49,223,BLUE)
    s+=label(4,171,'Pulmonary')+label(4,195,'artery')
    s+=arrow(mid+49,223,w-115,223,RED)+f'<path d="M{w-115} 223V157H{right}" stroke="{RED}" stroke-width="2.3" fill="none"/>'+arrow(right,157,right,150,RED)
    s+=label(w-4,171,'Pulmonary','end')+label(w-4,195,'vein','end')
    s+=arrow(right,115,right,99,RED)+arrow(right,62,right,13,RED)+arrow(right,13,mid+45,13,RED)+label(w-4,43,'Aorta','end')
    s+=f'<path d="M{left+46} 35H{right-46}" stroke="#aab9c2" stroke-width="1" stroke-dasharray="3 3"/>' if w>370 else ''
    s+=label(0,263,'Blue: lower oxygen')+label(w,263,'Red: higher oxygen','end')
    return s,274

def leaf(w):
    dw=116;tx=145;s=''
    s+=f'<rect x="2" y="12" width="{dw}" height="5" fill="#67994c"/><rect x="2" y="17" width="{dw}" height="20" fill="#eaf2d7" stroke="{GREEN}"/>'
    for x in [6,30,54,78,102]:
        s+=f'<rect x="{x}" y="40" width="18" height="43" rx="5" fill="#c2df8e" stroke="{GREEN}"/>'
        for y in [48,60,73]:s+=f'<ellipse cx="{x+9}" cy="{y}" rx="3" ry="4" fill="{GREEN}"/>'
    for x,y in [(14,101),(49,106),(20,130),(50,141)]:s+=f'<ellipse cx="{x}" cy="{y}" rx="13" ry="8" fill="#ddeac2" stroke="{GREEN}"/>'
    s+=f'<ellipse cx="90" cy="116" rx="22" ry="29" fill="#f5f6e3" stroke="{GREEN}"/><circle cx="90" cy="102" r="8" fill="#c5dff6" stroke="{BLUE}"/><circle cx="90" cy="130" r="8" fill="#f6d9a7" stroke="{ORANGE}"/>'
    s+=f'<path d="M2 156H43V170H2Z M76 156H118V170H76Z" fill="#eaf2d7" stroke="{GREEN}"/><ellipse cx="45" cy="163" rx="6" ry="11" fill="#badf90" stroke="{GREEN}"/><ellipse cx="73" cy="163" rx="6" ry="11" fill="#badf90" stroke="{GREEN}"/>'
    for y,value,px,py in [(17,'Cuticle',116,14),(41,'Epidermis',116,27),(65,'Palisade cells',116,61),(89,'Spongy cells',49,106),(113,'Xylem',98,102),(137,'Phloem',98,130),(161,'Guard cells',77,163)]:
        s+=leader(f'M{px} {py}L{tx-10} {y-5}H{tx-3}')+label(tx,y,value)
    s+=leader('M59 166V180')+label(59,198,'Stoma','middle')+label(tx,193,'Air spaces')+leader(f'M40 120L{tx-10} 187H{tx-3}')
    return s,207

def memory(w):
    s=label(0,16,'Antibody level');plot=(w-32)/2
    for i in range(2):
        x=8+i*(plot+16);end=x+plot
        s+=arrow(x,112,x,30,BLACK)+arrow(x,112,end,112,BLACK)
        curve=f'M{x+2} 110C{x+45} 110 {x+42} 80 {x+65} 80S{end-25} 105 {end-5} 108' if i==0 else f'M{x+2} 110C{x+18} 110 {x+18} 41 {x+45} 41S{end-26} 55 {end-5} 64'
        s+=f'<path d="{curve}" stroke="{BLUE if i==0 else GREEN}" stroke-width="2.5" fill="none"/>'
        s+=label(x+plot/2,136,'First exposure' if i==0 else 'Later exposure','middle')
    s+=label(w/2,160,'Time after exposure (same scale)','middle')
    return s,172

def hybridoma(w):
    x1=w*.24;x2=w*.76;mid=w/2
    s=label(x1,16,'Lymphocyte','middle')+label(x2,16,'Tumour cell','middle')
    for x,c in [(x1,PURPLE),(x2,ORANGE)]:s+=f'<circle cx="{x}" cy="45" r="18" fill="{c}" fill-opacity=".12" stroke="{c}" stroke-width="1.7"/><circle cx="{x-2}" cy="44" r="7" fill="{c}" fill-opacity=".5"/>'
    s+=label(x1,82,'Makes antibody','middle')+label(x2,82,'Divides','middle')
    s+=arrow(x1,93,mid-12,113,PURPLE)+arrow(x2,93,mid+12,113,ORANGE)
    s+=f'<ellipse cx="{mid}" cy="136" rx="25" ry="18" fill="#ecedf8" stroke="{BLUE}" stroke-width="1.7"/><circle cx="{mid}" cy="136" r="9" fill="#aa9aca"/>'
    s+=label(mid,178,'Hybridoma: divides + makes antibody','middle')
    return s,188

def limiting(w):
    s=label(0,16,'Photosynthesis rate')+arrow(15,135,15,29,BLACK)+arrow(15,135,w-3,135,BLACK)
    end=w-15
    s+=f'<path d="M19 132C55 115 70 93 120 93H{end}" stroke="{BLUE}" stroke-width="2.5" fill="none"/><path d="M19 132C55 115 80 54 160 54H{end}" stroke="{GREEN}" stroke-width="2.5" fill="none"/>'
    s+=label(end,46,'Higher CO₂','end')+label(end,85,'Lower CO₂','end')
    s+=label(w/2,160,'Light intensity','middle')+label(w/2,184,'Same temperature and chlorophyll','middle')
    return s,194

def pondweed(w):
    s=f'<rect x="6" y="87" width="30" height="48" rx="8" fill="#ffe5a7" stroke="#ac771f"/><path d="M36 89L107 71M36 110H107M36 131L107 166" stroke="#dba63a" fill="none"/>'+label(21,161,'Lamp','middle')
    s+=f'<path d="M105 54V179H214V54" stroke="#829caf" stroke-width="2" fill="none"/><path d="M106 95H213V177H106Z" fill="#e4f2fa"/>'
    # Inverted, initially water-filled collector; oxygen accumulates at its closed top.
    s+='<path d="M144 127V64Q156 59 168 64V127" stroke="#6c8d9e" stroke-width="1.7" fill="#eff8fb"/><path d="M145 64Q156 60 167 64V86H145Z" fill="#f5dd99"/>'
    s+='<path d="M132 150L148 129V122M164 122V129L180 150Z" fill="none" stroke="#63828d" stroke-width="1.6"/>'
    s+=f'<path d="M156 171V151M156 158L145 156M156 164L167 158" stroke="{GREEN}" stroke-width="3" fill="none"/>'
    s+='<circle cx="156" cy="119" r="2.5" fill="#9bc0d7"/><circle cx="156" cy="108" r="3" fill="#9bc0d7"/><path d="M195 92V158" stroke="#be4b55" stroke-width="3"/><circle cx="195" cy="160" r="5" fill="#be4b55"/>'
    s+=leader('M168 75H225')+label(230,80,'Oxygen')+leader('M195 96L225 113')+label(230,118,'Thermometer')
    s+=leader('M167 166L225 155')+label(230,160,'Pondweed')
    s+=label(w/2,205,'Sodium hydrogencarbonate solution','middle')
    return '<g transform="translate(0 -46)">'+s+'</g>',169

DRAWINGS={'osmosis':osmosis,'cubes':cubes,'fission':fission,'enzyme':enzyme,'circulation':circulation,'leaf':leaf,'memory':memory,'hybridoma':hybridoma,'limiting':limiting,'pondweed':pondweed}
MIN_WIDTH={'osmosis':322,'cubes':285,'fission':266,'enzyme':310,'circulation':310,'leaf':310,'memory':316,'hybridoma':330,'limiting':310,'pondweed':382}
PURPOSES={
'osmosis':'Equal compartments distinguish water from solute; bidirectional arrows show movement with a larger dilute-to-concentrated net movement.',
'cubes':'A 3 cm cube has three times the drawn side of a 1 cm cube, illustrating the falling surface area to volume ratio.',
'fission':'Bacterial DNA is copied before the cell divides into two; no nucleus or mitotic chromosomes are shown.',
'enzyme':'The substrate fits the active site, is split and leaves as products; the enzyme remains unchanged.',
'circulation':'The four heart chambers, named vessels, body and lungs form two linked circuits with actual flow directions.',
'leaf':'A leaf cross-section locates the tissues, air spaces, vascular bundle and guard cells around a stoma.',
'memory':'Matched schematic axes show the shorter delay and higher antibody response on later exposure.',
'hybridoma':'Fusion combines antibody production from a lymphocyte with repeated division from a tumour cell.',
'limiting':'Two schematic curves show the effect of increased carbon dioxide at fixed temperature and chlorophyll.',
'pondweed':'The lamp, submerged plant and funnel, inverted water-filled gas collector and thermometer clarify oxygen collection.'}

def drawing(kind,width):
    if width<MIN_WIDTH[kind]:raise ValueError('Diagram needs a wider panel: '+kind)
    body,height=DRAWINGS[kind](width)
    return '<g class="explanatory-diagram" data-diagram="'+kind+'"><title>'+escape(PURPOSES[kind])+'</title>'+body+'</g>',height

VISUALS={
'03-transport-processes':{2:('osmosis',0)},
'04-exchange-surfaces':{1:('cubes',0)},
'06-culturing-microorganisms':{0:('fission',0)},
'01-digestion-and-enzymes':{2:('enzyme',0)},
'02-circulation-and-health':{0:('circulation',0)},
'03-plant-tissues-and-transport':{0:('leaf',0)},
'02-defence-and-vaccination':{4:('memory',0)},
'03-medicines-and-antibodies':{4:('hybridoma',0)},
'01-photosynthesis-and-limiting-factors':{3:('limiting',0)},
'02-photosynthesis-practical':{2:('pondweed',0)},
}
