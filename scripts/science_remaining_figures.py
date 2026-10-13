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

RAW={'remaining-wave':wave,'remaining-refraction':refraction,'remaining-convex':convex}
PURPOSES={
 'remaining-wave':'Distinguishes rest-to-crest amplitude from the distance between successive crests.',
 'remaining-refraction':'Shows light changing speed and bending towards the normal as it enters glass obliquely.',
 'remaining-convex':'Traces two rays from an object at twice the focal length to an inverted real image of equal size.'}
def wrap(kind):
    def draw(width):
        svg,height=RAW[kind](width)
        return '<g class="concept-illustration"><title>'+escape(PURPOSES[kind])+'</title>'+svg+'</g>',height
    return draw
FIGURES={kind:wrap(kind) for kind in RAW}
