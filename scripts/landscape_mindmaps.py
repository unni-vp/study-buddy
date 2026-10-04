"""Landscape visual sheets: measured content, varied branch widths, useful diagrams."""
from html import escape
import xml.etree.ElementTree as ET
from functools import lru_cache
from mindmap_figures import figure, arrow, text
from visual_cell_biology_overview import visual_overview, BLUE, ORANGE, GREEN, PURPLE, TEAL, RED, GOLD, INK
from cell_biology_map_content import OVERVIEW
NS='http://www.w3.org/2000/svg'
ET.register_namespace('',NS)
COLORS=[BLUE,GREEN,PURPLE,ORANGE,TEAL,RED]

def tag(name):return '{'+NS+'}'+name

def landscape_overview(m,wrap):
    """Keep generous panel gutters and route relationships through empty space."""
    old=ET.fromstring(visual_overview(m,wrap))
    new=ET.Element(tag('svg'),{'width':'2400','height':'1500','viewBox':'0 0 4000 2500','role':'img','aria-labelledby':'title description'})
    for n in list(old):
        if n.tag in [tag('title'),tag('desc'),tag('defs')]:new.append(n)
    ET.SubElement(new,tag('rect'),{'width':'4000','height':'2500','fill':'#fffefa'})
    g=ET.SubElement(new,tag('g'),{'font-family':'Segoe UI, Arial, sans-serif','fill':INK})
    paths=[('M2420 980Q2280 975 2280 805H1190',BLUE),
           ('M2530 980V800Q2530 755 2370 720',ORANGE),
           ('M2380 1100H2205',GREEN),('M2680 1120H2820',PURPLE),
           ('M2380 1280Q2300 1310 2300 1555H1265',TEAL),
           ('M2530 1340V1670',RED),
           ('M2680 1280Q2710 1370 2780 1370H3100V1430',GOLD)]
    for d,c in paths:ET.SubElement(g,tag('path'),{'class':'relationship-path','d':d,'fill':'none','stroke':c,'stroke-width':'7','stroke-linecap':'round'})
    hub=ET.SubElement(g,tag('g'),{'class':'map-hub','data-bounds':'2380,980,300,360'})
    ET.SubElement(hub,tag('rect'),{'x':'2380','y':'980','width':'300','height':'360','rx':'85','fill':'#f1f7ff','stroke':INK,'stroke-width':'6'})
    for y,label,size in [(1120,'Cell',72),(1220,'biology',65)]:
        el=ET.SubElement(hub,tag('text'),{'x':'2530','y':str(y),'font-size':str(size),'text-anchor':'middle','font-weight':'700'});el.text=label
    layout={1:(40,40),2:(1310,40),3:(1370,850),4:(2820,40),5:(40,1140),6:(1390,1670),7:(2820,1430)}
    for sec in old.findall('.//'+tag('g')):
        if sec.get('class')!='map-section':continue
        n=int(sec.get('id').split('-')[-1]);x,y,w,h=map(float,sec.get('data-bounds').split(','));nx,ny=layout[n]
        sec.set('transform',f'translate({nx-x} {ny-y})');g.append(sec)
    labels=[(1790,788,'Compare structures',BLUE),(2530,867,'Adapt to a job',ORANGE),
            (2300,1062,'Observe',GREEN),(2750,1080,'Divide',PURPLE),
            (1810,1535,'Move substances',TEAL),(2530,1610,'Culture',RED),
            (3040,1352,'Measure changes',GOLD)]
    for x,y,label,c in labels:
        width=sum(v[2] for row in wrap('**'+label+'**',2000,30) for v in row)+32
        ET.SubElement(g,tag('rect'),{'x':str(x-width/2),'y':str(y-32),'width':str(width),'height':'45','rx':'9','fill':'#fffefa'})
        el=ET.SubElement(g,tag('text'),{'class':'relationship-label','x':str(x),'y':str(y),'font-size':'30','fill':c,'text-anchor':'middle','font-weight':'700'});el.text=label
    # Border/connector geometry grows; original text and scientific drawings retain
    # their font sizes and proportions, with additional inset and heading clearance.
    factor=1.10; vertical=1.16
    new.set('viewBox','0 0 4400 2900');new.set('height',str(2400*2900/4400))
    new.find(tag('rect')).set('width','4400');new.find(tag('rect')).set('height','2900')
    g.set('transform',f'scale({factor} {vertical})')
    for sec in list(g):
        if sec.get('class')!='map-section':continue
        n=int(sec.get('id').split('-')[-1]);ox,oy,w,h=map(float,sec.get('data-bounds').split(','));nx,ny=layout[n]
        children=list(sec);sec.clear()
        sec.attrib.update({'class':'map-section','id':f'section-{n}','data-bounds':f'0,0,{w},{h}','transform':f'translate({nx} {ny})'})
        for node in children[:2]:
            node.set('x','5' if node is children[0] else '0');node.set('y','7' if node is children[0] else '0');sec.append(node)
        heading=ET.SubElement(sec,tag('g'),{'class':'section-heading','transform':f'scale({1/factor} {1/vertical}) translate({-ox+40} {-oy+20})'})
        for node in children[2:6]:heading.append(node)
        body=ET.SubElement(sec,tag('g'),{'class':'section-body','transform':f'scale({1/factor} {1/vertical}) translate({-ox+40} {-oy+65})'})
        for node in children[6:]:body.append(node)
    return ET.tostring(new,encoding='unicode')

@lru_cache(None)
def anatomy(kind):
    """Reuse the approved anatomical artwork, with labels keyed to the notes."""
    from cell_biology_mindmaps import lines_for
    root=ET.fromstring(visual_overview(OVERVIEW,lines_for))
    sec=root.find('.//'+tag('g')+"[@id='section-1']")
    candidates=[n for n in list(sec) if n.tag==tag('g') and n.get('transform','').startswith('translate')]
    node=candidates[{'animal':0,'plant':1,'bacteria':2}[kind]]
    node.set('transform','translate(170 15) scale(1.05)')
    return ET.tostring(node,encoding='unicode')

def diagram(kind):
    """Return a labelled concept illustration, in a 600 × 240 coordinate system."""
    s=''
    if kind in ('animal','plant','bacteria'):
        s=anatomy(kind)
        if kind=='bacteria':
            s+=text(120,215,'Main DNA loop',22,PURPLE)+text(480,215,'Plasmid (some)',22,PURPLE)
            s+='<path d="M125 184L253 104M466 184L357 97" stroke="#8258b8" stroke-width="2" fill="none"/>'
    elif kind=='resolution':
        for x in [160,435]:s+=f'<circle cx="{x}" cy="92" r="72" fill="#eaf3fb" stroke="{BLUE}" stroke-width="3"/>'
        s+='<ellipse cx="160" cy="92" rx="46" ry="24" fill="#9ab6d0"/><circle cx="407" cy="92" r="18" fill="#1e67bc"/><circle cx="463" cy="92" r="18" fill="#1e67bc"/>'
        s+=text(160,200,'One blurred image',23)+text(435,200,'Two separate points',23)
    elif kind=='slide':
        s+='<path d="M85 161H495L532 182H122Z" fill="#dff3fa" stroke="#458caa" stroke-width="3"/><path d="M230 146h100l-11 17h-100Z" fill="#e6dfad" stroke="#927d35" stroke-width="3"/><path d="M329 155L260 38l133 21 69 118Z" fill="#e3f4fc" fill-opacity=".75" stroke="#438dab" stroke-width="3"/>'
        s+=text(120,76,'Thin sample',24)+text(420,30,'Angled coverslip',24)+arrow(144,89,234,146,GREEN)+text(300,225,'Lower gently → fewer trapped air bubbles',22)
    elif kind=='scale':
        for x,a in [(120,60),(335,120)]:
            s+=f'<rect x="{x}" y="35" width="{a}" height="{a}" fill="#e1eeda" stroke="{GREEN}" stroke-width="3"/>'
        s+=text(150,200,'Length ×1 / area ×1',22)+text(395,200,'Length ×2 / area ×4',22)
    elif kind=='zone':
        s=f'<circle cx="220" cy="110" r="98" fill="#e2efcf" stroke="{GREEN}" stroke-width="4"/><circle cx="220" cy="110" r="60" fill="#fffefa" stroke="{ORANGE}" stroke-width="3"/><circle cx="220" cy="110" r="12" fill="#bdd6ed" stroke="{BLUE}" stroke-width="3"/>'
        for x,y in [(150,59),(280,52),(148,151),(289,155),(220,28),(225,190)]:s+=f'<circle cx="{x}" cy="{y}" r="4" fill="{GREEN}"/>'
        s+='<path d="M160 105V115M160 110H280M280 105V115M220 115V122M220 120H280M280 115V125" fill="none" stroke="#bb5447" stroke-width="3"/>'
        s+=text(450,85,'Diameter = 12 mm',24,RED)+text(450,129,'Radius = 6 mm',24,RED)+text(450,178,'Area = π × 6²',24,RED)+text(450,220,'= 113 mm²',27,RED)
    elif kind=='water-cells':
        for x,turgid in [(110,True),(400,False)]:
            s+=f'<rect x="{x-65}" y="25" width="130" height="142" rx="14" fill="#eef4d9" stroke="{GREEN}" stroke-width="6"/>'
            xx=x-56 if turgid else x-35;ww=112 if turgid else 70
            s+=f'<rect x="{xx}" y="{34 if turgid else 55}" width="{ww}" height="{124 if turgid else 82}" rx="22" fill="#bee0ed" stroke="{BLUE}" stroke-width="3"/>'
        s+=arrow(212,72,186,72,BLUE)+arrow(476,112,529,112,BLUE)+text(110,211,'Water in: turgid',23)+text(425,211,'Water out: plasmolysed',23)
    elif kind=='osmosis-graph':
        s+='<path d="M95 20V192H515M95 100H515" fill="none" stroke="#173452" stroke-width="3"/><path d="M120 37Q245 75 282 100T490 166" fill="none" stroke="#168c98" stroke-width="5"/><circle cx="282" cy="100" r="7" fill="#168c98"/>'
        s+=text(300,230,'Increasing solution concentration →',22)+text(293,26,'Mean % mass change',23)+text(69,107,'0',23)+text(432,66,'No net change',22)+arrow(371,73,297,95,TEAL)
    elif kind=='vessels':
        s+='<rect x="90" y="20" width="80" height="156" rx="12" fill="#f4e3bd" stroke="#98683c" stroke-width="8"/><path d="M97 49h10M153 49h10M97 90h10M153 90h10M97 132h10M153 132h10" stroke="#98683c" stroke-width="6"/><rect x="350" y="20" width="70" height="156" rx="8" fill="#e0edc4" stroke="#668549" stroke-width="4"/><path d="M354 73h61M354 127h61" stroke="#668549" stroke-width="3"/><rect x="431" y="20" width="35" height="156" rx="6" fill="#cde1ad" stroke="#668549" stroke-width="3"/><circle cx="448" cy="95" r="11" fill="#916aa9"/>'
        s+=text(130,218,'Hollow xylem',23)+text(410,218,'Phloem + companion cell',22)
    elif kind=='nerve-muscle':
        s+='<path d="M100 67L60 30M100 67L48 76M100 67L68 112M100 67L112 18M119 67H246L277 34M246 67L287 77M246 67L276 106" fill="none" stroke="#8258b8" stroke-width="5"/><circle cx="101" cy="67" r="22" fill="#c7a3e1" stroke="#8258b8" stroke-width="3"/><path d="M330 98Q421 12 560 64Q462 155 330 98Z" fill="#e9a99a" stroke="#b25644" stroke-width="4"/>'
        for dy in [0,12,24]:s+=f'<path d="M357 {84+dy}Q454 {36+dy} 528 {61+dy}" fill="none" stroke="#b25644" stroke-width="3"/>'
        s+=text(153,184,'Long fibre + branches',22,PURPLE)+text(453,184,'Contractile proteins',22,ORANGE)
    elif kind=='gills':
        for x in [120,270,420]:
            s+=f'<path d="M{x} 42V153" stroke="{RED}" stroke-width="10"/>'
            for y in range(50,150,22):s+=f'<ellipse cx="{x}" cy="{y}" rx="48" ry="9" fill="#f3cbc7" stroke="{RED}" stroke-width="2"/>'
        s+=text(300,207,'Many thin lamellae → large exchange area',22)
    elif kind=='leaf':
        s+='<path d="M60 42H540V66H60ZM60 149H278V174H60ZM324 149H540V174H324Z" fill="#c9df9a" stroke="#5c8740" stroke-width="3"/>'
        for x,y in [(90,100),(175,115),(270,95),(379,112),(476,103)]:s+=f'<ellipse cx="{x}" cy="{y}" rx="30" ry="19" fill="#e0edbb" stroke="#5c8740" stroke-width="3"/>'
        s+=arrow(300,226,300,132,BLUE)+text(117,211,'Air spaces',23)+text(443,219,'CO₂ through stoma',22)
    elif kind=='sperm':
        s+='<ellipse cx="125" cy="95" rx="48" ry="27" fill="#c8dbec" stroke="#375b86" stroke-width="3"/><path d="M83 81Q102 55 126 70" fill="none" stroke="#8258b8" stroke-width="10"/><path d="M174 95H230Q280 40 332 95T475 95" fill="none" stroke="#375b86" stroke-width="5"/>'
        for x in [181,194,207,220]:s+=f'<ellipse cx="{x}" cy="{95}" rx="5" ry="11" fill="#d69e48"/>'
        s+=text(93,192,'Acrosome',22)+text(252,192,'Mitochondria',22)+text(461,192,'Tail',22)
        s+='<path d="M93 162V104M252 162L216 108M461 162V112" fill="none" stroke="#173452" stroke-width="2"/>'
    elif kind=='active':
        s=figure(kind).replace('y="157"','y="153"').replace('y="176"','y="194"').replace('y="202"','y="236"').replace('viewBox="0 0 600 205"','viewBox="0 0 600 250"')
    else:
        # Existing figures already show correct replication, separation and transport.
        s=f'<svg x="0" y="8" width="600" height="218" viewBox="0 0 600 205">{figure(kind)}</svg>'
    return f'<svg viewBox="0 0 600 240" width="100%" height="100%" font-family="Segoe UI, Arial, sans-serif">{s}</svg>'

# Each branch owns source panels exactly once; widths and groupings suit the topic.
# (title, panel indices, teaching diagram, relationship label)
PLANS={
 '01-cells':([1000,1290,1170],[1280,1330,850],[
  ('Animal cells',[0],'animal','share organelles'),('Plant cells',[1],'plant','add structures'),('Bacterial cells',[2],'bacteria','compare DNA'),
  ('Animal adaptations',[3,4],'sperm','adapt to a job'),('Plant adaptations',[5,6],'vessels','absorb & transport'),('Differentiation',[7],'differentiate','become specialised')]),
 '02-cell-processes':([1100,1280,1080],[1190,1210,1060],[
  ('Chromosomes & copying',[0,1],'dna-copy','copy instructions'),('Mitosis & division',[2,3],'cell-cycle','keep matching sets'),('Plant meristems',[7],'meristem','make plant clones'),
  ('Human stem cells',[4],'differentiate','form new cell types'),('Medical uses',[5],None,'replace damaged cells'),('Benefits, risks & ethics',[6],None,'weigh the evidence')]),
 '03-transport-processes':([1350,870,1240],[1000,1130,1330],[
  ('Diffusion & its rate',[0,1],'diffusion','down a gradient'),('Osmosis',[2],'osmosis','water through membrane'),('Active transport',[4,5],'active','against a gradient'),
  ('Cells gain or lose water',[3],'water-cells','change cell volume'),('Osmosis practical',[6],None,'measure mass'),('Interpreting results',[7],'osmosis-graph','calculate & explain')]),
 '04-exchange-surfaces':([1480,1000,980],[1050,1450,960],[
  ('Size & exchange needs',[0,1],'cubes','area relative to volume'),('Lung alveoli',[2],'alveolus','exchange with air'),('Small intestine',[3],'folds','absorb nutrients'),
  ('Fish gills',[4],'gills','exchange with water'),('Plants',[5,6],'root','absorb & diffuse'),('Efficient exchange',[7],None,'explain each adaptation')]),
 '05-microscopy':([1220,1320,920],[1170,1180,1110],[
  ('Magnification & resolution',[0,1],'resolution','see fine detail'),('Calculate size',[2,3],None,'image ↔ actual size'),('Units & standard form',[4],None,'convert first'),
  ('Scale & area',[5],'scale','compare measurements'),('Prepare a slide',[6],'slide','make structures visible'),('Focus & draw',[7],None,'record what you see')]),
 '06-culturing-microorganisms':([1020,1250,1190],[1180,1120,1160],[
  ('Binary fission',[0],'fission','cells divide'),('Grow a pure culture',[1,2],None,'prevent contamination'),('Test antimicrobial discs',[4,5],None,'make a fair comparison'),
  ('Handle plates safely',[3],'plate','control incubation'),('Measure inhibition',[6],'zone','measure the clear zone'),('Repeated doubling',[7],None,'calculate population')])}

class Branch:
    def __init__(self,title,indices,kind,label,width,m,color,wrap):
        self.title,self.indices,self.label,self.width,self.color=title,indices,label,width,color
        self.bits=[];self.wrap=wrap;self.y=170
        # Single useful illustration per branch; no filler icon for text-only concepts.
        if kind:
            fw=min(width-128,840);fh=fw*.40
            self.bits.append(f'<svg x="{(width-fw)/2}" y="{self.y}" width="{fw}" height="{fh}" viewBox="0 0 600 240">{diagram(kind)}</svg>')
            self.y+=fh+40
        for k,i in enumerate(indices):
            p=m['panels'][i]
            if len(indices)>1:
                if k:self.y+=23;self.bits.append(f'<path d="M64 {self.y-22}H{width-64}" stroke="{color}" opacity=".25" stroke-width="2"/>')
                self.y=self.para(p['title'].capitalize().replace('dna','DNA').replace('πr²','πr²'),self.y,width-128,32,True)+22
            for j,line in enumerate(p['lines']):
                if kind=='animal' and i==0 and j>0:line=str(j)+'. '+line
                if kind=='plant' and i==1 and 1<=j<=3:line=str(j+5)+'. '+line
                self.y=self.para(line,self.y,width-128,32)+16
        self.height=self.y+42
    def para(self,line,y,width,size,bold=False):
        for row in self.wrap('**'+line+'**' if bold else line,width,size):
            xx=64
            for word,b,w in row:
                b=b or bold
                if b:self.bits.append(f'<rect x="{xx-2}" y="{y-size+4}" width="{w}" height="{size+5}" rx="5" fill="{self.color}" opacity=".10"/>')
                self.bits.append(f'<text x="{xx}" y="{y}" font-size="{size}" fill="{self.color if bold else INK}" font-weight="{700 if b else 400}">{escape(word)}</text>');xx+=w
            y+=size+12
        return y
    def svg(self,x,y,n):
        c=self.color;w=self.width;h=self.height
        return f'<g class="map-section" id="section-{n}" data-bounds="0,0,{w},{h}" transform="translate({x} {y})"><rect x="5" y="7" width="{w}" height="{h}" rx="30" fill="{c}" opacity=".09"/><rect width="{w}" height="{h}" rx="30" fill="white" stroke="{c}" stroke-width="4"/><g class="section-heading"><circle cx="64" cy="60" r="26" fill="{c}"/><text x="64" y="71" font-size="31" text-anchor="middle" fill="white" font-weight="700">{n}</text><text x="108" y="74" font-size="38" fill="{c}" font-weight="700">{escape(self.title)}</text></g><g class="section-body">'+''.join(self.bits)+'</g></g>'

def landscape_detail(m,wrap):
    upper,lower,spec=PLANS[m['slug']]
    used=[i for _,ids,_,_ in spec for i in ids]
    assert sorted(used)==list(range(len(m['panels']))),f'Incomplete/duplicate source panels: {m["slug"]}'
    branches=[Branch(*s,w,m,c,wrap) for s,w,c in zip(spec,upper+lower,COLORS)]
    top=max(b.height for b in branches[:3]);bottom=max(b.height for b in branches[3:])
    # Compact central band: branches connect conceptually without a large empty centre.
    roomy=True
    long_title=m['slug']=='06-culturing-microorganisms'
    gap=100 if roomy else 40
    W=3460+2*gap+60
    middle=top+65;band=440 if long_title else 340
    H=max(top+bottom+band+90,2250)
    # Keep headings/paragraphs at the same size across maps; grow canvas if needed.
    s=[f'<svg xmlns="{NS}" width="2400" height="{2400*H/W:.1f}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title description"><title id="title">{escape(m["title"])}</title><desc id="description">'+escape(' '.join(p['title']+': '+' '.join(p['lines']).replace('**','') for p in m['panels']))+'</desc>',
       '<defs><radialGradient id="animalFill"><stop stop-color="#fff5de"/><stop offset="1" stop-color="#dceafd"/></radialGradient><radialGradient id="nucleusFill"><stop stop-color="#ddc7f4"/><stop offset="1" stop-color="#9b79c2"/></radialGradient><linearGradient id="leafFill" x2="0" y2="1"><stop stop-color="#edf7b8"/><stop offset="1" stop-color="#bfd882"/></linearGradient></defs>',f'<rect width="{W}" height="{H}" fill="#fffefa"/><g font-family="Segoe UI, Arial, sans-serif" fill="{INK}">']
    title=m['title'];hubw=1100 if roomy else (1000 if len(title)>20 else 820);hx=(W-hubw)/2;hy=middle+(85 if roomy else 25)
    hubh=270 if long_title else 160
    positions=[]
    for row,widths in enumerate([upper,lower]):
        x=30
        for j,w in enumerate(widths):
            b=branches[row*3+j];y=(top-b.height)/2+30 if row==0 else middle+band+(bottom-b.height)/2
            positions.append((x,y));cx=x+w/2
            start=hy if roomy and row==0 else hy+hubh if roomy else hy+50
            anchor=hx+140+j*(hubw-280)/2 if roomy else W/2
            end=y+b.height if row==0 else y
            lane=middle-10 if row==0 else middle+band-25
            route=f'M{anchor} {start}C{anchor} {lane} {cx} {start} {cx} {lane}L{cx} {end}'
            s.append(f'<path class="relationship-path" d="{route}" fill="none" stroke="{b.color}" stroke-width="6"/>')
            ly=middle+(25 if roomy else 5) if row==0 else middle+band-40 if roomy else middle+164
            # A paper-coloured label prevents a connector crossing the words.
            labelw=sum(v[2] for r in wrap(b.label,2000,26) for v in r)+28
            s.append(f'<rect x="{cx-labelw/2}" y="{ly-28}" width="{labelw}" height="36" rx="8" fill="#fffefa"/><text x="{cx}" y="{ly}" text-anchor="middle" font-size="26" fill="{b.color}" font-weight="700">{escape(b.label)}</text>')
            x+=w+gap
    s.append(f'<g class="map-hub" data-bounds="{hx},{hy},{hubw},{hubh}"><rect x="{hx}" y="{hy}" width="{hubw}" height="{hubh}" rx="55" fill="#edf5ff" stroke="{INK}" stroke-width="5"/>')
    if long_title:
        for yy,line in [(hy+105,'Culturing'),(hy+205,'microorganisms')]:
            s.append(f'<text x="{W/2}" y="{yy}" text-anchor="middle" font-size="64" font-weight="700">{line}</text>')
    else:s.append(f'<text x="{W/2}" y="{hy+102}" text-anchor="middle" font-size="53" font-weight="700">{escape(title)}</text>')
    s.append('</g>')
    for n,(b,(x,y)) in enumerate(zip(branches,positions),1):s.append(b.svg(x,y,n))
    s.append('</g></svg>');return ''.join(s)
