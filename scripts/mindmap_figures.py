"""Small SVG illustrations; chromosome identity and net transport stay explicit."""
from html import escape
BLUE='#286daa'; GREEN='#25836d'; PURPLE='#8653ae'; ORANGE='#c07432'
def text(x,y,value,size=23,colour='#183b3a'):
    return f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" fill="{colour}">{escape(value)}</text>'
def arrow(x1,y1,x2,y2,c=BLUE):
    import math
    angle=math.atan2(y2-y1,x2-x1)
    a=(x2-13*math.cos(angle-.5),y2-13*math.sin(angle-.5));b=(x2-13*math.cos(angle+.5),y2-13*math.sin(angle+.5))
    return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{c}" stroke-width="5"/><path d="M{x2} {y2}L{a[0]} {a[1]}L{b[0]} {b[1]}Z" fill="{c}"/>'
def rod(x,y,c,joined=False):
    if joined:return f'<path d="M{x-8} {y-22}L{x+8} {y+22}M{x+8} {y-22}L{x-8} {y+22}" stroke="{c}" stroke-width="7" stroke-linecap="round"/>'
    return f'<path d="M{x} {y-22}V{y+22}" stroke="{c}" stroke-width="7" stroke-linecap="round"/>'
def basic_cell(x,kind='animal',joined=False):
    s=f'<ellipse cx="{x}" cy="83" rx="90" ry="56" fill="#e6f0ff" stroke="{BLUE}" stroke-width="4"/>'
    if kind=='chromosomes':return s+f'<ellipse cx="{x}" cy="83" rx="47" ry="38" fill="#f4e9ff" stroke="{PURPLE}" stroke-width="2"/>'+rod(x-18,83,PURPLE,joined)+rod(x+18,83,ORANGE,joined)
    if kind=='bacteria':return s+f'<path d="M{x-48} 82q10-28 40 0t40 0q-40 38-80 0" fill="none" stroke="{PURPLE}" stroke-width="4"/><circle cx="{x+55}" cy="110" r="9" fill="none" stroke="{PURPLE}" stroke-width="3"/>'+text(x,166,'DNA loop + plasmid')
    if kind=='plant':s=f'<rect x="{x-100}" y="15" width="200" height="137" rx="15" fill="#edf8dc" stroke="{GREEN}" stroke-width="6"/><rect x="{x-91}" y="24" width="182" height="119" rx="15" fill="none" stroke="{GREEN}" stroke-width="2"/><ellipse cx="{x+32}" cy="82" rx="40" ry="40" fill="#c9e8f5" stroke="{BLUE}" stroke-width="2"/>'
    s+=f'<circle cx="{x-42}" cy="78" r="24" fill="#dbc4ef" stroke="{PURPLE}" stroke-width="3"/>'
    if kind=='plant':
        for dx,dy in [(-70,40),(68,38),(60,125)]:s+=f'<ellipse cx="{x+dx}" cy="{dy}" rx="15" ry="7" fill="{GREEN}"/>'
    else:s+=f'<ellipse cx="{x+42}" cy="92" rx="28" ry="13" fill="#f8e2c8" stroke="{ORANGE}" stroke-width="3"/><path d="M{x+21} 92l9-6 9 12 9-12 9 6" fill="none" stroke="{ORANGE}" stroke-width="2"/>'
    for dx,dy in [(5,52),(-11,113),(-66,100)]:s+=f'<circle cx="{x+dx}" cy="{dy}" r="3" fill="{PURPLE}"/>'
    return s

def figure(kind):
    s=''
    if kind=='cell-types':
        s=basic_cell(110,'animal')+basic_cell(310,'plant')
        s+=basic_cell(510,'bacteria').replace('DNA loop + plasmid','').replace('rx="90"','rx="80"')
        s+=text(110,193,'Animal')+text(310,193,'Plant')+text(510,193,'Bacterium')
    elif kind=='cell-cycle':
        for x,rx in [(55,47),(185,47),(340,68),(480,35),(560,35)]:
            s+=f'<ellipse cx="{x}" cy="68" rx="{rx}" ry="47" fill="#e6f0ff" stroke="{BLUE}" stroke-width="3"/>'
            if x!=340:s+=f'<ellipse cx="{x}" cy="68" rx="28" ry="32" fill="#f4e9ff" stroke="{PURPLE}" stroke-width="2"/>'
        for x in [55,185,480,560]:s+=rod(x-11,68,PURPLE,x==185)+rod(x+11,68,ORANGE,x==185)
        for x in [303,377]:s+=rod(x-11,68,PURPLE)+rod(x+11,68,ORANGE)
        s+=arrow(105,68,132,68)+arrow(234,68,267,68)+arrow(412,68,440,68)
        s+=arrow(331,46,318,46)+arrow(348,93,362,93)
        for x,label in [(55,'Before'),(185,'DNA copied'),(340,'Mitosis'),(521,'Two cells')]:s+=text(x,148,label,22)
        s+=text(300,190,'Example: two chromosomes shown',21)
    elif kind in ('animal','plant','bacteria'):s=basic_cell(300,kind)
    elif kind=='meristem':
        s=f'<path d="M300 152V37" stroke="{GREEN}" stroke-width="7"/><ellipse cx="261" cy="87" rx="38" ry="19" fill="#d7ecd3" stroke="{GREEN}" stroke-width="4"/><ellipse cx="339" cy="67" rx="38" ry="19" fill="#d7ecd3" stroke="{GREEN}" stroke-width="4"/><circle cx="300" cy="34" r="13" fill="#bde9dc" stroke="{GREEN}" stroke-width="3"/>'+arrow(408,27,328,33,ORANGE)+text(300,188,'Growing tip → meristem')
    elif kind=='root':
        s=f'<path d="M180 30h145q15 0 15 15v28h180v24H340v39q0 15-15 15H180q-15 0-15-15V45q0-15 15-15Z" fill="#eef5db" stroke="{GREEN}" stroke-width="4"/><circle cx="200" cy="88" r="20" fill="#dbc4ef" stroke="{PURPLE}" stroke-width="3"/><ellipse cx="280" cy="90" rx="32" ry="43" fill="#c9e8f5" stroke="{BLUE}" stroke-width="2"/>'+text(300,186,'Long extension → large absorption area')
    elif kind in ('dna-copy','replication'):
        s=basic_cell(135,'chromosomes')+basic_cell(465,'chromosomes',True)+arrow(242,83,353,83)+text(135,174,'Before DNA copying')+text(465,174,'After DNA copying')+text(300,200,'Example: two chromosomes shown',18)
    elif kind=='separation':
        s=f'<ellipse cx="300" cy="80" rx="250" ry="61" fill="#e6f0ff" stroke="{BLUE}" stroke-width="4"/>'
        for x in [155,445]:s+=rod(x-20,80,PURPLE)+rod(x+20,80,ORANGE)
        s+=arrow(275,65,207,65)+arrow(325,100,397,100)+text(300,174,'One matching set moves to each end')
    elif kind=='daughter-cells':s=basic_cell(155,'chromosomes')+basic_cell(445,'chromosomes')+text(300,174,'Two identical cells; same chromosome number')
    elif kind=='diffusion':
        s='<rect x="56" y="18" width="488" height="119" rx="12" fill="#f2f8fd" stroke="#b5d4e3" stroke-width="3"/>'
        for x,y in [(90,42),(128,42),(166,42),(90,78),(128,78),(166,78),(90,114),(128,114),(166,114),(420,45),(465,80),(510,115)]:s+=f'<circle cx="{x}" cy="{y}" r="9" fill="{BLUE}"/>'
        s+=arrow(220,78,374,78)+text(300,174,'Higher → lower concentration; net movement')
    elif kind=='osmosis':
        s='<rect x="56" y="15" width="488" height="123" rx="10" fill="#f2f8fd" stroke="#b5d4e3" stroke-width="3"/>'+f'<path d="M300 15V138" stroke="{GREEN}" stroke-width="4" stroke-dasharray="8 7"/>'
        for x,y in [(88,40),(120,64),(158,43),(193,70),(230,43),(97,102),(160,110),(225,112),(399,40),(473,110)]:s+=f'<circle cx="{x}" cy="{y}" r="7" fill="{BLUE}"/>'
        for x,y in [(175,80),(366,45),(413,101),(457,50),(509,95)]:s+=f'<rect x="{x-7}" y="{y-7}" width="14" height="14" fill="{ORANGE}"/>'
        s+=arrow(255,76,343,76)+text(146,160,'Dilute')+text(456,160,'Concentrated')+text(300,191,'● water   ■ solute; dashed line = membrane',21)
    elif kind=='active':
        s=f'<path d="M288 16V140M312 16V140" stroke="{GREEN}" stroke-width="4"/><rect x="281" y="61" width="38" height="38" rx="8" fill="#dcc8f1" stroke="{PURPLE}" stroke-width="3"/>'
        for x,y in [(124,47),(185,112),(398,37),(435,73),(480,40),(406,114),(476,119),(525,85)]:s+=f'<circle cx="{x}" cy="{y}" r="9" fill="{BLUE}"/>'
        s+=arrow(215,81,366,81)+text(155,157,'Lower')+text(452,157,'Higher')+text(300,176,'● transported substance; lines = membrane',20)+text(300,202,'Energy from respiration',21)
    elif kind=='folds':s=f'<path d="M65 138V57q30-80 60 0v81h40V57q30-80 60 0v81h40V57q30-80 60 0v81h40V57q30-80 60 0v81h50" fill="#e4f5ed" stroke="{GREEN}" stroke-width="6"/>'+text(300,178,'Folds increase surface area')
    elif kind=='cubes':
        for x,y,a in [(100,85,33),(330,37,99)]:
            dx=a*.4;dy=a*.2
            s+=f'<path d="M{x} {y}l{dx} {-dy}h{a}l{-dx} {dy}Z" fill="#fff0d8" stroke="{ORANGE}" stroke-width="3"/><path d="M{x+a} {y}l{dx} {-dy}v{a}l{-dx} {dy}Z" fill="#ead2ad" stroke="{ORANGE}" stroke-width="3"/><rect x="{x}" y="{y}" width="{a}" height="{a}" fill="#fae8cc" stroke="{ORANGE}" stroke-width="3"/>'
        s+=text(132,174,'1 cm; SA:V 6:1')+text(399,174,'3 cm; SA:V 2:1')
    elif kind=='alveolus':
        s=f'<ellipse cx="300" cy="76" rx="160" ry="58" fill="#e5f2ff" stroke="{BLUE}" stroke-width="4"/><rect x="81" y="148" width="438" height="44" rx="18" fill="#ffe2e5" stroke="#ba5066" stroke-width="3"/>'+text(300,61,'Alveolar air')+text(300,181,'Blood')+arrow(202,108,202,168)+arrow(399,163,399,108,'#ba5066')+text(151,138,'O₂',20)+text(451,138,'CO₂',20)
    elif kind=='fission':
        for x,y,rx,ry in [(150,87,72,42),(430,48,63,29),(430,126,63,29)]:
            s+=f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#e6f0ff" stroke="{BLUE}" stroke-width="4"/><path d="M{x-25} {y}q15-24 45 0q-22 23-45 0" fill="none" stroke="{PURPLE}" stroke-width="3"/>'
        s+=arrow(250,87,325,87)+text(300,190,'Binary fission: one cell → two cells')
    elif kind in ('culture','plate'):
        s=f'<circle cx="300" cy="91" r="76" fill="#e9f5d8" stroke="{GREEN}" stroke-width="4"/>'
        for x,y,r in [(267,57,7),(326,58,6),(301,95,8),(255,112,6),(332,127,8)]:s+=f'<circle cx="{x}" cy="{y}" r="{r}" fill="{GREEN}"/>'
        if kind=='plate':
            s+='<rect x="226" y="75" width="24" height="19" rx="3" fill="#b9daf2"/><rect x="350" y="75" width="24" height="19" rx="3" fill="#b9daf2"/>'+text(300,191,'Tape at the edges; maximum 25°C',21)
        else:s+=text(300,191,'Colonies on nutrient agar',21)
    elif kind in ('petri','zone'):
        s=f'<ellipse cx="300" cy="90" rx="135" ry="76" fill="#e9f5d8" stroke="{GREEN}" stroke-width="4"/>'
        for x,y in [(194,84),(236,42),(238,133),(302,26),(330,151),(400,80),(352,41),(386,124)]:s+=f'<circle cx="{x}" cy="{y}" r="4" fill="{GREEN}"/>'
        s+=f'<circle cx="300" cy="90" r="48" fill="#fffdfa" stroke="{ORANGE}" stroke-width="2"/><circle cx="300" cy="90" r="12" fill="#c9dbef" stroke="{BLUE}" stroke-width="3"/>'+text(300,191,'Disc + clear zone of inhibition',21)
    elif kind=='microscope':
        s=f'<path d="M327 37q121 30 75 107h-129" fill="none" stroke="{GREEN}" stroke-width="15" stroke-linecap="round"/><path d="M244 13l39 20-43 79-39-20Z" fill="#e5f1ff" stroke="{BLUE}" stroke-width="5"/><path d="M180 128h164M280 150v28M184 178h228" stroke="{BLUE}" stroke-width="10" stroke-linecap="round"/><circle cx="352" cy="88" r="16" fill="#e4d5f1" stroke="{PURPLE}" stroke-width="4"/>'
    elif kind=='sperm':s=f'<ellipse cx="190" cy="87" rx="48" ry="26" fill="#e6f0ff" stroke="{BLUE}" stroke-width="4"/><path d="M238 87q50-45 100 0t120 0" fill="none" stroke="{BLUE}" stroke-width="5"/>'+text(300,168,'Tail → movement; mitochondria → energy')
    elif kind=='differentiate':s=basic_cell(130)+arrow(246,83,330,83)+f'<circle cx="405" cy="83" r="30" fill="#e4d5f1" stroke="{PURPLE}" stroke-width="4"/><path d="M435 83h96m0 0 29-29m-29 29 29 29M381 65l-33-26m33 26-5-43m1 83-28 26" stroke="{PURPLE}" stroke-width="4" fill="none"/>'+text(300,177,'Unspecialised → specialised nerve cell')
    elif kind=='stem-cells':s=basic_cell(300)+text(300,177,'Undifferentiated cells divide and specialise')
    elif kind=='refresh-blood':s=arrow(107,60,475,60,'#ba5066')+arrow(475,118,107,118,BLUE)+text(300,35,'Supply and remove substances')+text(300,165,'Keep a steep concentration gradient')
    return f'<svg x="0" y="0" width="100%" height="100%" viewBox="0 0 600 205" font-family="Segoe UI, Arial, sans-serif">{s}</svg>'
