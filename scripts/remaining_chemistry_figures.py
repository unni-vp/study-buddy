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

RAW={'remaining-chem-rate-curves':rates,'remaining-chem-tangent':tangent,'remaining-chem-equilibrium':equilibrium,'remaining-chem-gas':gas_collection}
PURPOSES={'remaining-chem-rate-curves':'Compares rates by slopes while both reactions approach the same limiting-reactant gas yield.','remaining-chem-tangent':'Shows an analytically correct tangent and large triangle for instantaneous gas-production rate.','remaining-chem-equilibrium':'Distinguishes initially unequal forward/reverse rates from equal nonzero rates at dynamic equilibrium.','remaining-chem-gas':'Shows a stoppered reaction flask connected to a graduated gas syringe, with an open moving plunger rather than a blocked collector.'}
def wrapper(kind):
    def draw(w):
        s,h=RAW[kind](w);return '<g class="concept-illustration"><title>'+escape(PURPOSES[kind])+'</title>'+s+'</g>',h
    return draw
FIGURES={k:wrapper(k) for k in RAW}
