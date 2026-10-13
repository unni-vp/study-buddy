"""Chemistry relationships drawn at the final readable label size."""
from biology_explanatory_figures import label,arrow,BLUE,GREEN,ORANGE
from html import escape
import math

def rates(w):
    if w<320:raise ValueError('Rate curves need 320 units')
    s=label(0,16,'Gas volume (cm³)');x0=25;y0=160;span=w-44
    s+=f'<path d="M{x0} 29V{y0}H{w-3}" fill="none" stroke="#596d77"/>'
    for finish,c in [(.52,BLUE),(.95,ORANGE)]:
        pts=[(x0+span*i/100,y0-111*(1-(1-min(i/100/finish,1))**3)) for i in range(101)]
        s+='<polyline points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in pts)+'" fill="none" stroke="'+c+'" stroke-width="2"/>'
    s+=label(w/2,188,'Time (s)','middle')+label(w/2,216,'Blue: faster, with same final amount','middle')+label(w/2,244,'Orange: slower reaction','middle')
    # Both profiles are modelled approaching the same limiting-reactant yield.
    return s,256

def tangent(w):
    if w<330:raise ValueError('Rate tangent needs 330 units')
    x0=25;span=w-44;y0=164;k=3.5;a=113;u=.4
    s=label(0,16,'Gas volume (cm³)')+f'<path d="M{x0} 29V{y0}H{w-3}" fill="none" stroke="#596d77"/>'
    pts=[(x0+span*i/100,y0-a*(1-math.exp(-k*i/100))) for i in range(101)]
    s+='<polyline points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in pts)+'" fill="none" stroke="'+BLUE+'" stroke-width="2"/>'
    yu=y0-a*(1-math.exp(-k*u));grad=-a*k*math.exp(-k*u)
    def yy(t):return yu+grad*(t-u)
    lo=.15;hi=.82
    s+=f'<path d="M{x0+span*lo} {yy(lo)}L{x0+span*hi} {yy(hi)}" stroke="{ORANGE}" stroke-width="2"/>'
    s+=f'<path d="M{x0+span*lo} {yy(lo)}H{x0+span*hi}V{yy(hi)}" fill="none" stroke="{GREEN}"/>'
    s+=f'<circle cx="{x0+span*u}" cy="{yu}" r="4" fill="{ORANGE}"/>'+label(w/2,192,'Time (s)','middle')+label(w/2,220,'Tangent at the marked instant','middle')+label(w/2,248,'Gradient = volume change / time change','middle')
    return s,260

def equilibrium(w):
    if w<340:raise ValueError('Equilibrium rates need 340 units')
    x0=23;span=w-42;s=label(0,16,'Reaction rate')+f'<path d="M{x0} 29V166H{w-3}" fill="none" stroke="#596d77"/>'
    for first,c in [(True,BLUE),(False,ORANGE)]:
        pts=[(x0+span*i/100,100+(-65 if first else 65)*math.exp(-6*i/100)) for i in range(101)]
        s+='<polyline points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in pts)+'" fill="none" stroke="'+c+'" stroke-width="2"/>'
    s+=label(w/2,193,'Time','middle')+label(w/2,221,'Blue: forward. Orange: reverse.','middle')+label(w/2,249,'Equal rates, both reactions continue','middle')
    return s,261

def gas_collection(w):
    if w<540:raise ValueError('Gas apparatus requires notes width 540')
    s='<path d="M79 87V113L40 192Q36 207 58 211H147Q169 207 163 192L124 113V87Z" fill="#eef5f8" stroke="#668392" stroke-width="2"/><path d="M60 174H143L158 201H45Z" fill="#b5dce9"/><rect x="77" y="77" width="50" height="14" fill="#91837b"/>'
    s+='<path d="M104 77V38H282V82H307" fill="none" stroke="#6e8995" stroke-width="4"/>'
    s+='<rect x="307" y="62" width="180" height="42" fill="#f4f7fa" stroke="#6e8995" stroke-width="2"/><path d="M401 62V104M401 83H525M525 56V110" fill="none" stroke="#6e8995" stroke-width="3"/>'
    for x in range(317,397,16):s+=f'<path d="M{x} 62V73" stroke="#59717d"/>'
    s+=label(10,241,'Reactants in flask')+label(178,26,'Gas-tight delivery tube')+label(396,139,'Gas syringe','middle')+label(w/2,278,'Read volume at measured time intervals','middle')
    return s,290

def molecule(n,x,y,spacing=52,double=False,sub=None):
    """A straight carbon chain, with every H and single/double bond visible."""
    sub=sub or {};s=''
    def bond(a,b,c,d,two=False):
        z=f'<path d="M{a} {b}L{c} {d}" fill="none" stroke="#566b77"/>'
        if two:z+=f'<path d="M{a} {b+5}L{c} {d+5}" fill="none" stroke="#566b77"/>'
        return z
    for i in range(n):
        cx=x+i*spacing;s+=label(cx,y+5,'C','middle')
        if i<n-1:s+=bond(cx+11,y,x+(i+1)*spacing-11,y,double and i==0)
        for key,dx,dy in [('top',0,-32),('bottom',0,32)]:
            # First two carbons in an alkene have one fewer hydrogen each.
            if double and i<2 and key=='bottom':continue
            text=sub.get((i,key),'H');tx=cx+dx;ty=y+dy
            s+=bond(cx,y+(-11 if dy<0 else 11),tx,ty+(11 if dy<0 else -11))+label(tx,ty+5,text,'middle')
        if i==0:s+=bond(cx-11,y,cx-25,y)+label(cx-34,y+5,sub.get((i,'left'),'H'),'middle')
        if i==n-1:
            if sub.get((i,'right'))=='O–H':
                s+=bond(cx+11,y,cx+23,y)+label(cx+34,y+5,'O','middle')+bond(cx+45,y,cx+57,y)+label(cx+68,y+5,'H','middle')
            else:s+=bond(cx+11,y,cx+25,y)+label(cx+34,y+5,sub.get((i,'right'),'H'),'middle')
    return s

def alkenes(w):
    if w<580:raise ValueError('Displayed alkene series needs notes width')
    s=''
    for i,(n,name,formula) in enumerate([(2,'Ethene','C₂H₄'),(3,'Propene','C₃H₆'),(4,'But-1-ene','C₄H₈'),(5,'Pent-1-ene','C₅H₁₀')]):
        y=58+i*110;s+=label(8,y,name)+label(8,y+26,formula)+molecule(n,235,y,double=True)
    s+=label(w/2,453,'Each carbon has four bonds in total','middle')
    return s,465

def additions(w):
    if w<640:raise ValueError('Displayed addition products need notes width')
    s=''
    for i,(agent,name,subs) in enumerate([('H₂ / Ni catalyst','Ethane',{}),('Steam / acid catalyst','Ethanol',{(1,'right'):'O–H'}),('Br₂','1,2-dibromoethane',{(0,'bottom'):'Br',(1,'bottom'):'Br'})]):
        y=65+i*137;s+=molecule(2,52,y,double=True)+arrow(142,y,330,y)+label(235,y-23,agent,'middle')+molecule(2,385,y,sub=subs)+label(480,y+59,name,'middle')
    s+=label(w/2,459,'C=C becomes C–C as atoms add across it','middle')
    return s,471

def addition_polymer(w):
    if w<350:raise ValueError('Addition unit needs 350 units')
    # Ethene to a repeating unit: external bonds pass through brackets.
    s=molecule(2,w/2-26,45,double=True)+label(w/2,102,'Ethene monomer','middle')+arrow(w/2,115,w/2,151)
    a=w/2-26;b=w/2+26;y=207
    s+=label(a,y+5,'C','middle')+label(b,y+5,'C','middle')
    s+=f'<path d="M{a-75} {y}H{a-12}M{a+12} {y}H{b-12}M{b+12} {y}H{b+75}" fill="none" stroke="#566b77"/>'
    for x in (a,b):
        for dy in (-32,32):s+=f'<path d="M{x} {y+(-11 if dy<0 else 11)}V{y+dy+(11 if dy<0 else -11)}" stroke="#566b77"/>'+label(x,y+dy+5,'H','middle')
    s+=f'<path d="M{a-48} 165H{a-60}V250H{a-48}M{b+48} 165H{b+60}V250H{b+48}" fill="none" stroke="{BLUE}" stroke-width="2"/>'+label(b+66,258,'n')
    s+=label(w/2,291,'Poly(ethene) repeating unit','middle')+label(w/2,319,'Same atoms, no small by-product','middle')
    return s,331

def chromatogram(w):
    if w<350:raise ValueError('Chromatogram needs 350 units')
    s=label(w/2,16,'Solvent front: dashed line','middle')+f'<rect x="22" y="34" width="{w-44}" height="180" fill="#f7f9f6" stroke="#a7b8ae"/><path d="M22 55H{w-22}" stroke="{BLUE}" stroke-dasharray="5 4"/><path d="M22 185H{w-22}" stroke="#666"/>'
    xs=[w*.2,w*.5,w*.8]
    for x,ys in zip(xs,[(107,),(143,),(107,143)]):
        for y in ys:s+=f'<circle cx="{x}" cy="{y}" r="7" fill="{BLUE if y==107 else ORANGE}"/>'
    for x,t in zip(xs,'ABC'):s+=label(x,236,t,'middle')
    s+=label(w/2,265,'Baseline: solid starting line','middle')+label(w/2,293,'A’s Rf = 78 / 130 = 0.60','middle')+label(w/2,321,'C contains spots matching A and B','middle')
    return s,333

def greenhouse(w):
    if w<360:raise ValueError('Radiation routes require 360 units')
    s=label(40,18,'Sun','middle')+label(w*.5,18,'Space','middle')+f'<circle cx="40" cy="51" r="17" fill="#ffe1a0" stroke="{ORANGE}"/><rect x="15" y="76" width="{w-30}" height="97" rx="10" fill="#dcecf5" fill-opacity=".6" stroke="#adc4d1" stroke-dasharray="5 4"/><path d="M15 227H{w-15}" stroke="{GREEN}" stroke-width="5"/>'
    s+=arrow(57,65,w*.28,223,ORANGE)+arrow(w*.5,220,w*.5,36,BLUE)
    s+=f'<path d="M{w*.75} 220l-5 -13l10 -13l-10 -13l10 -13l-5 -13V141" fill="none" stroke="#b94b57" stroke-width="2"/>'+arrow(w*.75,150,w*.75,140,'#b94b57')
    s+=f'<circle cx="{w*.75}" cy="129" r="7" fill="#b94b57"/>'+arrow(w*.78,142,w*.93,222,'#b94b57')+arrow(w*.78,118,w*.92,88,'#b94b57')
    s+=label(w*.78,64,'Re-emission','middle')+label(20,201,'Surface')
    s+=label(w/2,258,'Orange: incoming short-wave radiation','middle')+label(w/2,285,'Blue/red: outgoing long-wave infrared','middle')+label(w/2,312,'Some escapes, some is absorbed by gases','middle')+label(w/2,339,'Re-emission towards surface warms it','middle')
    return s,351

RAW={'remaining-chem-rate-curves':rates,'remaining-chem-tangent':tangent,'remaining-chem-equilibrium':equilibrium,'remaining-chem-gas':gas_collection,'remaining-chem-alkenes':alkenes,'remaining-chem-additions':additions,'remaining-chem-polymer':addition_polymer,'remaining-chem-chromatogram':chromatogram,'remaining-chem-greenhouse':greenhouse}
PURPOSES={'remaining-chem-rate-curves':'Compares rates by slopes while both reactions approach the same limiting-reactant gas yield.','remaining-chem-tangent':'Shows an analytically correct tangent and large triangle for instantaneous gas-production rate.','remaining-chem-equilibrium':'Distinguishes initially unequal forward/reverse rates from equal nonzero rates at dynamic equilibrium.','remaining-chem-gas':'Shows a stoppered reaction flask connected to a graduated gas syringe, with an open moving plunger rather than a blocked collector.'}
PURPOSES.update({'remaining-chem-alkenes':'Displays every atom and bond in straight-chain representatives of the first four alkenes, keeping carbon valency four.','remaining-chem-additions':'Shows hydrogen, water and bromine adding across ethene’s double bond with the new atoms attached to the correct carbons.','remaining-chem-polymer':'Changes ethene C=C into a single-bond repeating unit with two external chain bonds, brackets and n, preserving all atoms.'})
PURPOSES['remaining-chem-chromatogram']='Shows separated reference/sample spots with a distinct common baseline and solvent front; the dimensionless Rf is calculated from two distances measured from that baseline.'
PURPOSES['remaining-chem-greenhouse']='Distinguishes incoming short-wavelength radiation, outgoing infrared escape and absorption/re-emission by greenhouse gases, without depicting a reflecting solid blanket or implying all radiation is trapped.'
def wrapper(kind):
    def draw(w):
        s,h=RAW[kind](w);return '<g class="concept-illustration"><title>'+escape(PURPOSES[kind])+'</title>'+s+'</g>',h
    return draw
FIGURES={k:wrapper(k) for k in RAW}
