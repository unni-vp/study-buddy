from biology_explanatory_figures import box,arrow,BLUE,GREEN,ORANGE

def inspector_cycle(w):
    s=box(0,0,w,32,'Investigation exposes harm',BLUE)
    s+=arrow(w/2,35,w/2,49,BLUE)
    s+=box(0,52,w,32,'Doubts produce relief',ORANGE)
    s+=arrow(w/2,87,w/2,101,ORANGE)
    s+=box(0,104,w,32,'Final call renews pressure',GREEN)
    return s,146

DRAWINGS={'lit-inspector-cycle':inspector_cycle}
MIN_WIDTH={'lit-inspector-cycle':258}
PURPOSES={'lit-inspector-cycle':'Shows the cyclical ending: investigation, apparent escape and renewed pressure, making the moral lesson distinct from fear of punishment.'}
