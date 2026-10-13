"""Physics mechanisms and graphs with final-size 16-unit black labels."""
from biology_explanatory_figures import label,arrow,leader,BLUE,GREEN,ORANGE,PURPLE
import math

def path(d,color=BLUE,width=2):return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}"/>'

def energy(w):
    s=label(w/2,16,'100 J supplied','middle')
    s+=f'<rect y="30" width="{w*.6}" height="26" fill="#b3ded4"/><rect x="{w*.6}" y="30" width="{w*.4}" height="26" fill="#edc4a5"/>'
    s+=label(w*.3,81,'60 J useful','middle')+label(w*.8,81,'40 J dissipated','middle')
    s+=label(w/2,111,'100 J = 60 J + 40 J','middle')+label(w/2,137,'Total energy is conserved','middle')
    return s,147

def spring(w):
    s=label(0,16,'Force (N)')+path(f'M18 30V126H{w-4}','#667781',1)
    s+=f'<path d="M20 124L{w-24} 43V124Z" fill="#e2eef9"/>'+path(f'M20 124L{w-24} 43',BLUE,3)
    s+=label(w*.61,109,'Area = ½ke²','middle')+label(w/2,150,'Extension (m)','middle')
    s+=label(w/2,175,'Within proportional limit','middle')
    return s,185

def specific(w):
    s=label(0,16,'Temperature rise (°C)')+path(f'M18 31V130H{w-4}','#667781',1)
    s+=path(f'M20 128L{w-20} 48',BLUE,3)+path(f'M20 128L{w-20} 102',GREEN,3)
    s+=label(w-20,38,'Lower c','end')+label(w-20,93,'Higher c','end')
    s+=label(w/2,154,'Energy supplied (J)','middle')+label(w/2,178,'Same mass; no state change','middle')
    return s,188

def circuit(w):
    cx=w/2
    s=path(f'M22 35V14H67M22 56V114H{w-18}V14H{cx+23}M67 14H{cx-23}M67 14V68H{cx-23}M{cx+23} 68H{w-18}M10 35H34M15 56H29')
    for y in [14,68]:s+=f'<rect x="{cx-23}" y="{y-8}" width="46" height="16" fill="white" stroke="{BLUE}" stroke-width="2"/>'
    for x in [67,w-18]:s+=f'<circle cx="{x}" cy="14" r="3" fill="{BLUE}"/><circle cx="{x}" cy="68" r="3" fill="{BLUE}"/>'
    s+=label(w/2,153,'Parallel branches have the same pd','middle')
    return s,163

def field(w):
    x=w/2;y=77
    s=f'<circle cx="{x}" cy="{y}" r="16" fill="#f9e6d8" stroke="{ORANGE}"/>'+label(x,y+5,'+','middle')
    for k in range(8):
        a=k*math.pi/4;s+=arrow(x+22*math.cos(a),y+22*math.sin(a),x+70*math.cos(a),y+70*math.sin(a))
    s+=label(w/2,175,'Positive sphere: field points outwards','middle')
    return s,185

def particles(w):
    s=''
    for j,name in enumerate(['Solid','Liquid','Gas']):
        x=(j+.5)*w/3
        s+=f'<rect x="{j*w/3+3}" y="0" width="{w/3-6}" height="87" rx="5" fill="#eff6fc" stroke="#8ba6bc"/>'
        points=[(-12,36),(0,36),(12,36),(-12,48),(0,48),(12,48)] if j==0 else [(-15,36),(-4,31),(8,33),(-14,48),(-2,47),(10,45)] if j==1 else [(-27,14),(28,68),(0,41)]
        for dx,y in points:s+=f'<circle cx="{x+dx}" cy="{y}" r="5" fill="{BLUE}"/>'
        s+=label(x,110,name,'middle')
    s+=label(w/2,137,'Symbols show particle arrangement','middle')
    return s,147

def heat(w):
    s=label(0,16,'Temperature (°C)')+path(f'M15 31V140H{w-3}','#667781',1)
    s+=path(f'M20 133L{w*.25} 104H{w*.45}L{w*.67} 65H{w*.86}L{w-7} 33',BLUE,3)
    s+=label(w*.35,130,'Melting','middle')+label(w*.76,91,'Boiling','middle')
    s+=label(w/2,164,'Energy supplied (J)','middle')
    return s,174

def half_life(w):
    s=label(0,16,'Source count rate (counts/s)')+path(f'M40 31V145H{w-4}','#667781',1)
    for v in [400,200,100]:
        y=145-.24*v;s+=label(33,y+5,str(v),'end')+path(f'M40 {y}H{w-5}','#bdcbd4',.6)
    points=[]
    for j in range(81):
        t=4*j/80;x=50+(w-60)*t/4;y=145-.24*400*2**(-t/2);points.append(f'{x},{y}')
    s+=f'<polyline points="{" ".join(points)}" fill="none" stroke="{BLUE}" stroke-width="2.5"/>'
    for t,v in [(0,400),(2,200),(4,100)]:
        x=50+(w-60)*t/4;y=145-.24*v
        s+=f'<circle cx="{x}" cy="{y}" r="3.5" fill="{BLUE}"/>'+label(x,166,str(t),'middle')
    s+=label(w/2,193,'Time (h)','middle')+label(w/2,217,'Example: half-life = 2 h','middle')
    return s,227

def scatter(w):
    x=w*.64
    s=f'<circle cx="{x}" cy="53" r="12" fill="#f3d3b7" stroke="{ORANGE}"/>'+label(x,58,'+','middle')
    s+=label(x+20,58,'Nucleus')
    s+=arrow(2,17,w-3,17)+arrow(2,98,w-3,98)
    s+=path(f'M2 51H{x-33}Q{x-6} 51 {x-33} 74H{x-64}')+arrow(x-33,74,x-64,74)
    s+=label(w/2,128,'Arrows: alpha particles','middle')+label(w/2,152,'Most pass; very few turn back','middle')
    s+=label(w/2,176,'Nucleus and paths not to scale','middle')
    return s,186

def lever(w):
    left=27;pivot=w*.35;right=pivot+2*(pivot-left)
    s=path(f'M8 61H{w-8}',BLUE,5)+f'<path d="M{pivot} 64l-14 25h28Z" fill="#dae6f2" stroke="{BLUE}"/>'
    s+=label(left,16,'30 N','middle')+arrow(left,23,left,58)+label(right,36,'15 N','middle')+arrow(right,42,right,58)
    for x in [left,pivot,right]:s+=path(f'M{x} 94V113','#667781',1)
    s+=path(f'M{left} 105H{right}','#667781',1)
    s+=label((left+pivot)/2,133,'0.20 m','middle')+label((pivot+right)/2,133,'0.40 m','middle')
    s+=label(w/2,160,'30 × 0.20 = 15 × 0.40 = 6 Nm','middle')
    return s,170

def motion(w):
    s=label(0,16,'Velocity (m/s)')+path(f'M18 31V126H{w-4}','#667781',1)
    s+=f'<path d="M20 124L{w*.56} 48H{w-12}V124Z" fill="#e1edf8"/>'+path(f'M20 124L{w*.56} 48H{w-12}',BLUE,3)
    s+=label(w/2,150,'Time (s)','middle')+label(w/2,175,'Shaded area: displacement','middle')
    return s,185

def terminal(w):
    x=w/2
    s=f'<circle cx="{x}" cy="57" r="13" fill="#dfecf8" stroke="{BLUE}"/>'
    s+=arrow(x,41,x,4)+arrow(x,73,x,110)
    s+=label(x+20,20,'Drag')+label(x+20,106,'Weight')
    s+=label(w/2,139,'Drag = weight','middle')+label(w/2,163,'Constant downward velocity','middle')
    return s,173

DRAWINGS={'ph-energy':energy,'ph-spring':spring,'ph-specific':specific,'ph-circuit':circuit,'ph-field':field,'ph-particles':particles,'ph-heat':heat,'ph-half-life':half_life,'ph-scatter':scatter,'ph-lever':lever,'ph-motion':motion,'ph-terminal':terminal}
MIN_WIDTH={'ph-energy':284,'ph-spring':270,'ph-specific':280,'ph-circuit':284,'ph-field':286,'ph-particles':268,'ph-heat':270,'ph-half-life':270,'ph-scatter':298,'ph-lever':280,'ph-motion':270,'ph-terminal':270}
PURPOSES={
 'ph-energy':'Shows that useful and dissipated outputs still add up to the supplied energy.',
 'ph-spring':'Shows that elastic energy is the triangular area under a proportional force–extension graph.',
 'ph-specific':'Compares temperature rises for equal masses with different heat capacities.',
 'ph-circuit':'Shows two genuine parallel branches connected across the same cell.',
 'ph-field':'Shows a radial field and its direction around an isolated positive sphere.',
 'ph-particles':'Compares fixed, irregular and widely spaced particle arrangements.',
 'ph-heat':'Shows energy continuing to enter during constant-temperature changes of state.',
 'ph-half-life':'Shows equal time intervals halving a background-corrected source count rate.',
 'ph-scatter':'Shows straight-through and rare turned-back alpha paths around a small positive nucleus.',
 'ph-lever':'Shows perpendicular lever arms and opposite, equal moments with properly scaled distances.',
 'ph-motion':'Shows the signed area represented by a positive velocity–time graph.',
 'ph-terminal':'Shows equal and opposite drag and weight at terminal velocity.',
}
