"""Accurate, selective Biology mechanisms and identification diagrams."""
from biology_explanatory_figures import label,arrow,leader,BLUE,GREEN,ORANGE,PURPLE
from html import escape

def line(x,y,x2,y2,color='#667781',width=1):return f'<path d="M{x} {y}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{width}"/>'
def eye(w):
    if w<540:raise ValueError('Eye identification needs a wide notes figure')
    cx=w/2;cy=155
    s=f'<ellipse cx="{cx}" cy="{cy}" rx="110" ry="94" fill="#f4f9fb" stroke="#657b88" stroke-width="5"/>'
    s+=f'<path d="M{cx-98} 113Q{cx-134} 155 {cx-98} 197" fill="#e2f3fa" stroke="{BLUE}" stroke-width="3"/>'
    s+=f'<path d="M{cx+4} 68Q{cx+103} 69 {cx+103} 155Q{cx+103} 241 {cx+4} 242" fill="none" stroke="{ORANGE}" stroke-width="4"/>'
    s+=f'<ellipse cx="{cx-62}" cy="155" rx="17" ry="42" fill="#dcecf7" stroke="{BLUE}" stroke-width="2"/>'
    s+=line(cx-89,115,cx-89,139,GREEN,6)+line(cx-89,171,cx-89,195,GREEN,6)
    for y,end in [(105,116),(205,194)]:
        s+=f'<circle cx="{cx-83}" cy="{y}" r="8" fill="#c8a5d8" stroke="{PURPLE}"/>'+line(cx-77,y,cx-59,end,PURPLE,2)
    s+=f'<path d="M{cx+108} 144L{cx+148} 151L{cx+146} 169L{cx+108} 164Z" fill="#c9d9a6" stroke="{GREEN}"/>'
    for text,x,y,tx,ty,anchor in [
      ('Ciliary muscles',5,34,cx-83,105,'start'),('Cornea',5,124,cx-116,155,'start'),
      ('Pupil',5,157,cx-89,155,'start'),('Iris',5,190,cx-89,183,'start'),
      ('Lens',5,229,cx-62,180,'start'),('Suspensory ligaments',5,276,cx-68,200,'start'),
      ('Sclera',w-5,35,cx+69,82,'end'),('Retina',w-5,113,cx+101,132,'end'),
      ('Optic nerve',w-5,218,cx+136,159,'end')]:
        s+=label(x,y,text,anchor)
        lx=145 if anchor=='start' else w-112
        s+=line(lx,y-5,tx,ty)
    return s,288
def brain(w):
    if w<500:raise ValueError('Brain identification needs a wide notes figure')
    cx=w*.43
    s=f'<path d="M{cx-140} 122C{cx-160} 69 {cx-116} 38 {cx-59} 42C{cx-37} 9 {cx+43} 16 {cx+64} 44C{cx+139} 44 {cx+150} 105 {cx+107} 145C{cx+59} 169 {cx-84} 177 {cx-140} 122Z" fill="#ede6f5" stroke="{PURPLE}" stroke-width="4"/>'
    s+=f'<path d="M{cx+29} 146Q{cx+34} 197 {cx+12} 225L{cx+34} 232Q{cx+61} 184 {cx+54} 147Z" fill="#e6e0bd" stroke="{ORANGE}" stroke-width="2"/>'
    s+=f'<ellipse cx="{cx+94}" cy="171" rx="49" ry="31" fill="#d5e9d0" stroke="{GREEN}" stroke-width="2"/>'
    for y in (158,170,182):s+=f'<path d="M{cx+59} {y}Q{cx+95} {y-12} {cx+126} {y}" fill="none" stroke="{GREEN}"/>'
    for a in (-80,-35,10,55):s+=f'<path d="M{cx+a} 60q-21 23 4 35q26 15 8 36" fill="none" stroke="#b199c8" stroke-width="2"/>'
    for text,y,tx,ty in [('Cerebral cortex',28,cx+66,45),('Cerebellum',152,cx+110,165),('Medulla',249,cx+28,216)]:
        s+=label(w-5,y,text,'end')+line(w-154,y-5,tx,ty)
    s+=label(w/2,281,'Side view: three key regions','middle')
    return s,293
def endocrine(w):
    if w<580:raise ValueError('Gland positions need wide notes figure')
    a=w*.30;b=w*.77;s=''
    for x in (a,b):
        s+=f'<circle cx="{x}" cy="30" r="24" fill="#f6f7fb" stroke="#87979e"/><path d="M{x-13} 53V67L{x-44} 77L{x-57} 133L{x-42} 138L{x-28} 100V176L{x-30} 226H{x-13}L{x} 183L{x+13} 226H{x+30}L{x+28} 176V100L{x+42} 138L{x+57} 133L{x+44} 77L{x+13} 67V53" fill="#f6f7fb" stroke="#87979e" stroke-width="2"/>'
    points=[('Pituitary',a,35,24),('Thyroid',a,73,81),('Pancreas',a+3,114,119),('Adrenal glands',a-16,128,156)]
    for x in (a-16,a+16):s+=f'<ellipse cx="{x}" cy="143" rx="7" ry="11" fill="#d7e2e7" stroke="#87979e"/>'
    for name,x,y,ly in points:
        s+=f'<circle cx="{x}" cy="{y}" r="5" fill="{PURPLE}"/>'
        if name=='Adrenal glands':s+=f'<circle cx="{a+16}" cy="{y}" r="5" fill="{PURPLE}"/>'
        s+=label(w*.47,ly,name)+line(w*.46,ly-5,x+7,y)
    for x in (a-13,a+13):s+=f'<ellipse cx="{x}" cy="166" rx="6" ry="4" fill="{ORANGE}"/>'
    for x in (b-5,b+5):s+=f'<ellipse cx="{x}" cy="207" rx="5" ry="7" fill="{ORANGE}"/>'
    s+=label(a,256,'Ovaries: inside pelvis','middle')+line(a,240,a+13,170)
    s+=label(b,256,'Testes: in scrotum','middle')+line(b,240,b,210)
    s+=label(a,284,'Female','middle')+label(b,284,'Male','middle')
    s+=label(w/2,316,'Both have the common glands labelled on the left','middle')
    return s,328
def reflex(w):
    if w<330:raise ValueError('Reflex route needs 330 units')
    a=35;b=w-48
    s=f'<rect x="{b-23}" y="45" width="46" height="136" rx="12" fill="#ede6f5" stroke="{PURPLE}"/>'
    s+=label(a,22,'Receptor')+label(w/2,52,'Sensory neurone','middle')+arrow(a,70,b-7,70,BLUE)
    s+=arrow(b,82,b,156,PURPLE)+label(w/2,122,'Relay in spinal cord','middle')
    s+=arrow(b-7,171,a,171,GREEN)+label(w/2,195,'Motor neurone','middle')
    s+=label(a,222,'Muscle contracts')+label(w/2,250,'Synapses use chemical signals','middle')
    return s,262
def insulin(w):
    if w<280:raise ValueError('Insulin sequence needs 280 units')
    cx=w/2;s=label(cx,16,'High blood glucose','middle')+label(cx,43,'Pancreas releases insulin','middle')
    s+=arrow(cx,55,cx,78)+label(cx,101,'Cells take up glucose','middle')+label(cx,127,'Glucose stored as glycogen','middle')
    s+=arrow(cx,139,cx,163)+label(cx,188,'Blood glucose falls','middle')+label(cx,215,'Insulin release reduces','middle')
    return s,227
def adh(w):
    if w<300:raise ValueError('ADH sequence needs 300 units')
    cx=w/2;s=label(cx,16,'Concentrated blood','middle')+arrow(cx,28,cx,50)
    for y,text in [(75,'Pituitary releases more ADH'),(102,'Tubules become more permeable'),(129,'More water is reabsorbed')]:s+=label(cx,y,text,'middle')
    s+=arrow(cx,142,cx,162)+label(cx,186,'Small, concentrated urine volume','middle')+label(cx,213,'Blood becomes less concentrated','middle')+label(cx,240,'ADH release then reduces','middle')
    return s,252
def phototropism(w):
    if w<300:raise ValueError('Shoot growth figure needs 300 units')
    cx=w*.57
    s=arrow(18,31,102,31,ORANGE)+label(10,60,'Light')
    shape=f'M{cx-11} 173Q{cx-15} 104 {cx-40} 77L{cx-20} 61Q{cx+18} 107 {cx+11} 173Z'
    s+=f'<defs><clipPath id="shoot-cell-marks"><path d="{shape}"/></clipPath></defs><path d="{shape}" fill="#e0ecd6" stroke="{GREEN}" stroke-width="2"/><g clip-path="url(#shoot-cell-marks)">'
    for y in (107,134,158):s+=line(cx+1,y,cx+10,y,GREEN)
    for y in (120,143,162):s+=line(cx-11,y,cx,y,GREEN)
    s+='</g>'
    s+=label(w/2,205,'Shaded side: more auxin','middle')+label(w/2,232,'More cell elongation on shaded side','middle')+label(w/2,259,'Shoot bends towards light','middle')
    return s,272

def corrected_eyes(w):
    if w<580:raise ValueError('Eyesight rays need a wide notes figure')
    xg=w*.20;xe=w*.45;xr=w*.83;s=''
    for cy,short in [(95,True),(300,False)]:
        s+=label(5,cy-79,'Short-sighted: concave correction' if short else 'Long-sighted: convex correction')
        s+=label(xe,cy-63,'Eye lens','middle')+label(xg,cy+79,'Concave' if short else 'Convex','middle')+label(xr,cy+79,'Retina','middle')
        s+=line(xr,cy-56,xr,cy+56,ORANGE,3)
        s+=f'<ellipse cx="{xe}" cy="{cy}" rx="12" ry="54" fill="#e5f2f8" stroke="{BLUE}"/>'
        if short:s+=f'<path d="M{xg-12} {cy-54}Q{xg+6} {cy} {xg-12} {cy+54}H{xg+12}Q{xg-6} {cy} {xg+12} {cy-54}Z" fill="#e5f2f8" stroke="{BLUE}"/>'
        else:s+=f'<ellipse cx="{xg}" cy="{cy}" rx="16" ry="54" fill="#e5f2f8" stroke="{BLUE}"/>'
        original_h=24 if short else 54
        corrected_h=42.03 if short else 39.84
        xf=w*.68 if short else w*.95
        for sign in (-1,1):
            y_at_retina=cy+sign*original_h*(1-(xr-xe)/(xf-xe))
            extra=f'L{xr} {y_at_retina}' if short else ''
            s+=f'<path d="M{xg} {cy+sign*24}L{xe} {cy+sign*original_h}L{xf} {cy}{extra}" fill="none" stroke="#87979e" stroke-width="1.6" stroke-dasharray="5 4"/>'
            start_x=12 if short else 0
            start_y=cy+sign*24 if short else cy
            s+=f'<path d="M{start_x} {start_y}L{xg} {cy+sign*24}L{xe} {cy+sign*corrected_h}L{xr} {cy}" fill="none" stroke="{BLUE}" stroke-width="2"/>'
    s+=label(w/2,421,'Grey dashed rays: without correction','middle')+label(w/2,447,'Blue rays: correction focuses light on the retina','middle')
    return s,459

RAW={'remaining-eye':eye,'remaining-brain':brain,'remaining-endocrine':endocrine,'remaining-reflex':reflex,'remaining-insulin':insulin,'remaining-adh':adh,'remaining-phototropism':phototropism,'remaining-eye-correction':corrected_eyes}
PURPOSES={
 'remaining-eye':'Identifies eye structures in cross-section with leaders ending on the named tissue or opening.',
 'remaining-brain':'Identifies cortex, cerebellum and medulla in a simplified side view, supporting structure/function recall.',
 'remaining-endocrine':'Locates common endocrine glands and separates ovaries in the pelvis from testes in the scrotum.',
 'remaining-reflex':'Shows sensory, relay and motor routing through the spinal cord rather than a conscious decision path.',
 'remaining-insulin':'Connects high glucose, insulin release, cellular uptake/storage and reduced hormone release in negative feedback.',
 'remaining-adh':'Connects concentrated blood to increased ADH, water permeability/reabsorption and the resulting urine changes.',
 'remaining-phototropism':'Shows asymmetric shoot elongation bending towards one-sided light, with shaded-side auxin explicitly identified.',
 'remaining-eye-correction':'Compares uncorrected rays with concave correction for myopia and convex correction for hyperopia, moving the focus to the retina.'}
def wrap(kind):
    def draw(width):
        svg,height=RAW[kind](width)
        return '<g class="concept-illustration"><title>'+escape(PURPOSES[kind])+'</title>'+svg+'</g>',height
    return draw
FIGURES={kind:wrap(kind) for kind in RAW}
