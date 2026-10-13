"""Selective explanatory science figures, with readable final-size labels."""
from biology_explanatory_figures import label,arrow,BLUE,GREEN,ORANGE
from html import escape
import math

def line(x,y,x2,y2,color='#667781',width=1,dash=False):
    return f'<path d="M{x} {y}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{width}"'+(' stroke-dasharray="5 4"' if dash else '')+'/>'
def wave(w):
    if w<270:raise ValueError('Wave diagram requires 270 units')
    start=10;length=w-20;lam=length/2
    s=line(start,73,w-10,73,dash=True)
    points=[(start+i*length/100,73-30*math.sin(i*4*math.pi/100)) for i in range(101)]
    s+='<polyline points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in points)+'" fill="none" stroke="'+BLUE+'" stroke-width="3"/>'
    crest=start+lam/4
    s+=line(crest,26,crest+lam,26)+line(crest,21,crest,31)+line(crest+lam,21,crest+lam,31)
    s+=label(crest+lam/2,16,'Wavelength','middle')
    s+=line(crest,43,crest,73,ORANGE,2)+label(w/2,127,'Amplitude: rest to crest','middle')
    s+=label(w/2,152,'Dashed line: resting position','middle')
    return s,162
def refraction(w):
    if w<280:raise ValueError('Refraction requires 280 units')
    cx=w*.48
    s=f'<rect x="0" y="90" width="{w}" height="138" fill="#e1f0f4"/>'
    s+=line(0,90,w,90)+line(cx,24,cx,221,dash=True)
    s+=arrow(cx-78,27,cx,90,BLUE)+arrow(cx,90,cx+36,200,BLUE)
    s+=label(9,56,'Air')+label(9,139,'Glass')+label(cx+12,18,'Normal')
    s+=label(w/2,253,'Slower: bends towards normal','middle')
    s+=label(w/2,278,'Frequency stays the same','middle')
    return s,288
def convex(w):
    if w<300:raise ValueError('Lens diagram requires 300 units')
    cx=w/2;f=w*.16;ox=cx-2*f;ix=cx+2*f;axis=143;top=78;bottom=208
    s=line(5,axis,w-5,axis)
    s+=f'<path d="M{cx} 35Q{cx-27} 143 {cx} 238Q{cx+27} 143 {cx} 35Z" fill="#dff2f7" stroke="{BLUE}" stroke-width="2"/>'
    for x in (cx-f,cx+f):s+=line(x,axis-5,x,axis+5)+label(x,168,'F','middle')
    s+=arrow(ox,axis,ox,top,GREEN)+arrow(ix,axis,ix,bottom,ORANGE)
    s+=arrow(ox,top,cx,top,BLUE)+arrow(cx,top,ix,bottom,BLUE)
    s+=arrow(ox,top,ix,bottom,GREEN)
    s+=label(ox,57,'Object','middle')+label(ix,234,'Image','middle')
    s+=label(w/2,264,'Real, inverted image at 2F','middle')
    return s,274

def motor_force(w):
    if w<280:raise ValueError('Motor-effect figure needs 280 units')
    cx=w/2
    s=f'<rect x="5" y="45" width="48" height="64" rx="4" fill="#e7eff7" stroke="{BLUE}"/><rect x="{w-53}" y="45" width="48" height="64" rx="4" fill="#e7eff7" stroke="{BLUE}"/>'
    s+=label(29,83,'N','middle')+label(w-29,83,'S','middle')
    s+=arrow(60,48,w-60,48,BLUE)+label(cx,27,'Field: N to S','middle')
    s+=f'<circle cx="{cx}" cy="84" r="13" fill="white" stroke="{GREEN}" stroke-width="2"/>'+line(cx-6,78,cx+6,90,GREEN,2)+line(cx-6,90,cx+6,78,GREEN,2)
    s+=arrow(cx,105,cx,151,ORANGE)
    s+=label(cx,178,'Force downwards','middle')+label(cx,204,'×: current into the page','middle')
    return s,214
def transformer(w):
    if w<290:raise ValueError('Transformer figure needs 290 units')
    a=65;b=w-65
    s=f'<rect x="{a}" y="41" width="{b-a}" height="94" rx="14" fill="none" stroke="#b5c3cb" stroke-width="16"/>'
    for x,ys in [(a,[65,87,109]),(b,[54,68,82,96,110,124])]:
        for y in ys:s+=f'<ellipse cx="{x}" cy="{y}" rx="24" ry="7" fill="none" stroke="{BLUE}" stroke-width="2"/>'
    s+=label(a,24,'Primary','middle')+label(b,24,'Secondary','middle')
    s+=label(a,164,'AC input','middle')+label(b,164,'Induced AC','middle')
    s+=label(w/2,193,'Changing field in iron core','middle')
    s+=label(w/2,219,'More secondary turns: step-up','middle')
    return s,229

def bar_field(w):
    if w<280:raise ValueError('Field diagram needs 280 units')
    a=w*.32;b=w*.68;cx=w/2
    s=''
    for offset in (40,72):
        for sign in (-1,1):
            yy=94+sign*offset
            start_y=94+sign*(6 if offset==40 else 11)
            s+=f'<path d="M{a} {start_y}C{a-50} {start_y} {a-40} {yy} {cx} {yy}C{b+40} {yy} {b+50} {start_y} {b} {start_y}" fill="none" stroke="{BLUE}" stroke-width="2"/>'
            s+=arrow(cx-12,yy,cx+12,yy,BLUE)
    s+=f'<rect x="{a}" y="79" width="{b-a}" height="30" fill="#e7eff7" stroke="{BLUE}"/>'
    s+=label(a+18,100,'N','middle')+label(b-18,100,'S','middle')
    s+=label(cx,195,'Outside magnet: N to S','middle')
    s+=label(cx,219,'Compass follows field direction','middle')
    return s,229
def generator_graphs(w):
    if w<290:raise ValueError('Generator graphs need 290 units')
    s='';x0=19;span=w-32
    for row,name,rectified in [(0,'Alternator: AC',False),(1,'Dynamo: pulsing DC',True)]:
        y=52+row*125
        s+=label(0,y-36,name)+line(x0,y-27,x0,y+28)+line(x0,y,w-8,y)
        points=[]
        for i in range(121):
            value=math.sin(i*4*math.pi/120)
            if rectified:value=abs(value)
            points.append((x0+i*span/120,y-25*value))
        s+='<polyline points="'+' '.join(f'{x:.2f},{yy:.2f}' for x,yy in points)+'" fill="none" stroke="'+BLUE+'" stroke-width="2"/>'
        s+=label(x0-3,y+5,'0','end')+label(w-8,y+47,'Time','end')
    s+=label(w/2,249,'Vertical axes: potential difference','middle')
    return s,259

def star_life(w):
    if w<330:raise ValueError('Star routes require 330 units')
    cx=w/2;left=w*.25;right=w*.75
    s=label(cx,16,'Nebula','middle')+arrow(cx,25,cx,43)+label(cx,65,'Protostar','middle')+arrow(cx,74,cx,94)+label(cx,116,'Main sequence','middle')
    s+=arrow(cx-10,130,left,159)+arrow(cx+10,130,right,159)
    s+=label(left,182,'Red giant','middle')+label(right,182,'Red supergiant','middle')
    s+=arrow(left,192,left,211)+arrow(right,192,right,211)
    s+=label(left,235,'White dwarf','middle')+label(right,235,'Supernova','middle')
    s+=arrow(left,245,left,264)+arrow(right,245,right,264)
    s+=label(left,288,'Black dwarf','middle')+label(right,288,'Neutron star','middle')+label(right,312,'or black hole','middle')
    s+=label(left,345,'Sun-like route','middle')+label(right,345,'Massive route','middle')
    return s,357
def orbit(w):
    if w<290:raise ValueError('Orbit diagram requires 290 units')
    cx=w/2;cy=92;r=65
    s=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#9eb3c3" stroke-width="2"/><circle cx="{cx}" cy="{cy}" r="19" fill="#edf2fa" stroke="{BLUE}"/><circle cx="{cx+r}" cy="{cy}" r="6" fill="{ORANGE}"/>'
    s+=arrow(cx+r-10,cy,cx+25,cy,ORANGE)+arrow(cx+r,cy-10,cx+r,cy-66,GREEN)
    s+=label(cx,98,'Earth','middle')+label(cx,181,'Gravity acts towards the centre','middle')+label(cx,205,'Velocity is tangent to the orbit','middle')
    s+=label(w/2,230,'Speed constant, direction changes','middle')
    return s,240
def redshift(w):
    if w<290:raise ValueError('Spectrum comparison needs 290 units')
    s=label(0,16,'Laboratory pattern')+label(0,114,'Distant galaxy pattern')
    for y,shift in [(28,0),(128,w*.15)]:
        s+=f'<rect x="7" y="{y}" width="{w-14}" height="44" fill="#f2f5f8" stroke="#9eb3c3"/>'
        for ratio in (.23,.42,.61):s+=line(w*ratio+shift,y,w*ratio+shift,y+44,BLUE,3)
    s+=label(w/2,203,'Matching lines at longer wavelength','middle')+label(w/2,231,'Wavelength increases left to right','middle')
    return s,241

def tangent(w):
    if w<300:raise ValueError('Tangent figure needs 300 units')
    x0=23;span=w-49
    s=label(0,16,'Distance (m)')+line(x0,26,x0,163)+line(x0,163,w-5,163)
    points=[(x0+span*i/100,160-120*(i/100)**2) for i in range(101)]
    s+='<polyline points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in points)+'" fill="none" stroke="'+BLUE+'" stroke-width="2"/>'
    def ty(u):return 116.8-144*(u-.6)
    s+=line(x0+span*.35,ty(.35),x0+span*.95,ty(.95),ORANGE,2)
    s+=line(x0+span*.35,ty(.35),x0+span*.85,ty(.35),GREEN)+line(x0+span*.85,ty(.35),x0+span*.85,ty(.85),GREEN)
    s+=f'<circle cx="{x0+span*.6}" cy="116.8" r="4" fill="{ORANGE}"/>'
    s+=label(w/2,187,'Time (s)','middle')+label(w/2,213,'Tangent gradient: speed at that instant','middle')
    return s,223

RAW={'remaining-wave':wave,'remaining-refraction':refraction,'remaining-convex':convex,'remaining-motor-force':motor_force,'remaining-transformer':transformer,'remaining-bar-field':bar_field,'remaining-generators':generator_graphs,'remaining-star-life':star_life,'remaining-orbit':orbit,'remaining-redshift':redshift,'remaining-tangent':tangent}
PURPOSES={
 'remaining-wave':'Distinguishes rest-to-crest amplitude from the distance between successive crests.',
 'remaining-refraction':'Shows light changing speed and bending towards the normal as it enters glass obliquely.',
 'remaining-convex':'Traces two rays from an object at twice the focal length to an inverted real image of equal size.',
 'remaining-motor-force':'Shows mutually perpendicular field, current and force with explicit into-page current notation.',
 'remaining-transformer':'Shows separate coils linked by an iron core and distinguishes alternating input from induced output.',
 'remaining-bar-field':'Shows curved field lines outside a bar magnet pointing from north to south, matching compass direction.',
 'remaining-generators':'Compares alternating potential difference crossing zero with a dynamo’s output that pulses in one direction.',
 'remaining-star-life':'Separates the Sun-like and much-more-massive star routes after their common main-sequence stage.',
 'remaining-orbit':'Distinguishes an inward gravitational force from a tangent velocity in circular orbital motion.',
 'remaining-redshift':'Compares the same spectral-line pattern at increasing wavelengths, rather than treating red-shift as an object simply appearing red.',
 'remaining-tangent':'Shows a tangent at a point on a curved distance–time graph and a large gradient triangle for instantaneous speed.'}
def wrap(kind):
    def draw(width):
        svg,height=RAW[kind](width)
        return '<g class="concept-illustration"><title>'+escape(PURPOSES[kind])+'</title>'+svg+'</g>',height
    return draw
FIGURES={kind:wrap(kind) for kind in RAW}

from remaining_biology_figures import FIGURES as BIOLOGY_FIGURES,PURPOSES as BIOLOGY_PURPOSES
FIGURES.update(BIOLOGY_FIGURES)
PURPOSES.update(BIOLOGY_PURPOSES)
