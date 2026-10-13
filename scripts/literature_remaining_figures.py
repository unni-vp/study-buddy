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

def spirit_sequence(w):
    s=box(0,0,w,32,'Past: regret and reflection',BLUE)
    s+=arrow(w/2,35,w/2,49,BLUE)
    s+=box(0,52,w,32,'Present: empathy for others',GREEN)
    s+=arrow(w/2,87,w/2,101,GREEN)
    s+=box(0,104,w,32,'Future: urgency to change',ORANGE)
    return s,146

DRAWINGS['lit-spirit-sequence']=spirit_sequence
MIN_WIDTH['lit-spirit-sequence']=252
PURPOSES['lit-spirit-sequence']='Shows how the ordered visits build regret, empathy and urgency; avoids presenting Scrooge’s redemption as only fear of death.'

def unseen_contrast(w):
    half=(w-12)/2
    s=box(0,0,half,32,'Waiting',BLUE)+box(half+12,0,half,32,'Departure',GREEN)
    s+=box(0,45,half,32,'Attachment',BLUE)+box(half+12,45,half,32,'Independence',GREEN)
    s+=box(0,90,half,32,'Unresolved',BLUE)+box(half+12,90,half,32,'Chosen space',GREEN)
    return s,132

DRAWINGS['lit-unseen-contrast']=unseen_contrast
MIN_WIDTH['lit-unseen-contrast']=278
PURPOSES['lit-unseen-contrast']='Compares the two original practice poems by attitude and ending; similar absence is experienced as unresolved attachment or chosen independence.'
