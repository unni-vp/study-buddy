"""Selective explanatory diagrams drawn at their final readable A4 label size."""
from biology_explanatory_figures import label, arrow, leader, box, BLUE, GREEN, ORANGE, PURPLE
from html import escape
import math

def ion(w):
    s=label(w*.22,28,'Na','middle')+label(w*.77,28,'Na⁺','middle')
    s+=arrow(w*.39,21,w*.59,21)
    s+=label(w*.22,56,'2,8,1','middle')+label(w*.77,56,'2,8','middle')
    s+=label(w*.22,80,'11 electrons','middle')+label(w*.77,80,'10 electrons','middle')
    s+=label(w/2,110,'One electron lost; 11 protons remain','middle')
    return s,120

def pairs(w):
    x=w/2
    s=label(x-55,34,'H','middle')+label(x+55,34,'H','middle')
    s+=f'<ellipse cx="{x-26}" cy="28" rx="46" ry="26" fill="none" stroke="{BLUE}"/><ellipse cx="{x+26}" cy="28" rx="46" ry="26" fill="none" stroke="{ORANGE}"/>'
    s+=f'<circle cx="{x-7}" cy="28" r="4" fill="{BLUE}"/><path d="M{x+3} 24l8 8m0-8-8 8" stroke="{ORANGE}" stroke-width="2"/>'
    s+=label(x,78,'H₂: one shared electron pair','middle')
    s+=label(x,102,'Dot and cross: electron origins','middle')
    return s,112

def lattice(w):
    s=''
    for row in range(3):
        for col in range(6):
            x=w/2+(col-2.5)*34;y=18+row*34;pos=(row+col)%2==0
            s+=f'<circle cx="{x}" cy="{y}" r="14" fill="{"#e4eefb" if pos else "#fff0dc"}" stroke="#5c7287"/>'+label(x,y+5,'+' if pos else '−','middle')
    s+=label(w/2,123,'2D slice of a repeating 3D lattice','middle')
    return s,133

def alloy(w):
    s=label(w*.25,16,'Pure metal','middle')+label(w*.75,16,'Alloy','middle')
    for side in range(2):
        for row in range(2):
            for col in range(4):
                x=w*(.25+side*.5)+(col-1.5)*27;y=39+row*28
                large=side==1 and row==0 and col==2
                if side and row==1:x+=6
                s+=f'<circle cx="{x}" cy="{y}" r="{13 if large else 9}" fill="{"#edccb0" if large else "#dceaf7"}" stroke="{ORANGE if large else BLUE}"/>'
    s+=label(w/2,104,'Different-sized atoms disrupt layers','middle')
    s+=label(w/2,128,'Layers slide less easily in an alloy','middle')
    return s,138

def graphite(w):
    s=''
    # Finite fragment of hexagonal sheets; the network continues beyond this view.
    for row in range(2):
        cy=27+row*65
        for j in range(3):
            cx=w/2+(j-1)*math.sqrt(3)*24
            points=[(cx+24*math.cos(math.pi/6+math.pi/3*k),cy+24*math.sin(math.pi/6+math.pi/3*k)) for k in range(6)]
            s+=f'<polygon points="{" ".join(f"{x},{y}" for x,y in points)}" fill="none" stroke="{GREEN}" stroke-width="2"/>'
    s+=f'<path d="M{w/2} 51V68M{w/2-42} 51V68M{w/2+42} 51V68" stroke="{GREEN}" stroke-dasharray="3 4" fill="none"/>'
    s+=arrow(w-32,53,w-9,53,GREEN)
    s+=label(w/2,140,'Strong bonds within each layer','middle')+label(w/2,164,'Dashed: weak forces between layers','middle')
    s+=label(w/2,188,'Fragment: network continues','middle')
    return s,198

def limiting(w):
    s=label(0,18,'Before:','start')+label(0,83,'After:','start')
    # 3 Mg atoms with one O₂ molecule; after reaction two MgO units and excess Mg.
    for x in [100,137,174]:s+=f'<circle cx="{x}" cy="13" r="9" fill="#bdc8d5" stroke="{BLUE}"/>'
    for x in [w-35,w-18]:s+=f'<circle cx="{x}" cy="13" r="7" fill="#e7a9a8" stroke="#b74650"/>'
    s+=arrow(w/2,34,w/2,55)
    for x in [100,155]:
        s+=f'<circle cx="{x}" cy="78" r="9" fill="#bdc8d5" stroke="{BLUE}"/><circle cx="{x+16}" cy="78" r="7" fill="#e7a9a8" stroke="#b74650"/>'
    s+=f'<circle cx="{w-25}" cy="78" r="9" fill="#bdc8d5" stroke="{BLUE}"/>'
    s+=label(w/2,110,'Grey: Mg    Red: O','middle')+label(w/2,134,'O₂ runs out; one Mg atom remains','middle')
    return s,144

def electrodes(w):
    left=39;right=w-39
    s=label(left,17,'Cathode −','middle')+label(right,17,'Anode +','middle')
    s+=f'<path d="M3 42V117H{w-3}V42" fill="#edf6fa" stroke="#7f9cb1"/><rect x="{left-5}" y="30" width="10" height="66" fill="#7d8792"/><rect x="{right-5}" y="30" width="10" height="66" fill="#7d8792"/>'
    s+=label(w*.37,60,'Pb²⁺','middle')+label(w*.63,92,'Br⁻','middle')
    s+=arrow(w*.37-19,63,left+8,63)+arrow(w*.63+16,93,right-8,93)
    s+=label(w/2,142,'Molten lead bromide: ions move','middle')
    return s,152

def titration(w):
    s=f'<path d="M35 5V108H53V5M39 9H49" fill="none" stroke="{BLUE}" stroke-width="2"/><path d="M35 39Q44 46 53 39" fill="none" stroke="{BLUE}"/><path d="M29 99H59M44 109V120" stroke="#4f6775" stroke-width="2"/><path d="M32 124V138L10 176Q44 192 78 176L56 138V124" fill="#f7f1f8" stroke="{PURPLE}" stroke-width="2"/><path d="M24 156H64L74 176Q44 186 14 176Z" fill="#edc4d9"/>'
    s+=label(90,23,'Burette: acid')+leader('M83 18H57')
    s+=label(90,67,'Read bottom of')+label(90,89,'meniscus at eye level')+leader('M82 66L52 42')
    s+=label(90,140,'Flask: alkali')+label(90,162,'and indicator')+leader('M83 143H62')
    return s,197

def profile(w,endo=False):
    # Reaction progress is not time. Eₐ always starts at the reactant level.
    ry=76 if not endo else 105;py=105 if not endo else 68
    s=label(w/2,16,'Endothermic' if endo else 'Exothermic','middle')
    s+=f'<path d="M28 30V124H{w-12}" stroke="#607583" fill="none"/>'
    s+=label(0,43,'E')
    s+=f'<path d="M37 {ry}H70C94 {ry} 107 35 144 35S190 {py} {w-69} {py}H{w-20}" fill="none" stroke="{BLUE}" stroke-width="2.5"/>'
    s+=label(48,ry-9,'R')+label(w-42,py-9,'P')
    s+=arrow(111,ry,111,35,ORANGE)+label(89,54,'Eₐ')
    s+=label(w/2,148,'Reaction progress','middle')
    s+=label(w/2,172,'E: energy    R: reactants    P: products','middle')
    return s,182

def profiles(w):
    s='';half=(w-12)/2
    for side in range(2):
        ry=88 if side==0 else 111;py=111 if side==0 else 88
        a=label(half/2,18,'Exothermic' if side==0 else 'Endothermic','middle')
        a+=f'<path d="M20 32V127H{half-2}" stroke="#607583" fill="none"/>'
        a+=label(0,51,'E')
        a+=f'<path d="M27 {ry}H43C57 {ry} 59 46 {half*.52} 46S{half*.71} {py} {half-38} {py}H{half-5}" stroke="{BLUE}" stroke-width="2.5" fill="none"/>'
        a+=label(28,ry-8,'R')+label(half-24,py-8,'P')
        a+=arrow(60,ry,60,46,ORANGE)+label(45,42,'Eₐ')
        a+=label(half/2,150,'Progress','middle')
        s+=f'<g transform="translate({side*(half+12)} 0)">{a}</g>'
    s+=label(w/2,175,'E: energy    R: reactants    P: products','middle')
    return s,185

DRAWINGS={'chem-ion':ion,'chem-pairs':pairs,'chem-lattice':lattice,'chem-alloy':alloy,'chem-graphite':graphite,'chem-limiting':limiting,'chem-electrodes':electrodes,'chem-titration':titration,'chem-profile':profile,'chem-profiles':profiles}
MIN_WIDTH={'chem-ion':266,'chem-pairs':250,'chem-lattice':266,'chem-alloy':294,'chem-graphite':266,'chem-limiting':266,'chem-electrodes':266,'chem-titration':276,'chem-profile':300,'chem-profiles':330}
PURPOSES={
 'chem-ion':'Shows electron loss while proton number stays unchanged.',
 'chem-pairs':'Shows the shared pair and the origins of electrons in a covalent bond.',
 'chem-lattice':'Shows the repeating alternation of oppositely charged ions, rather than separate molecules.',
 'chem-alloy':'Compares regular metal layers with layers distorted by different-sized atoms.',
 'chem-graphite':'Distinguishes bonds within carbon sheets from weak forces between them.',
 'chem-limiting':'Makes the limiting reactant and leftover excess visible in a particle model.',
 'chem-electrodes':'Shows positive and negative ions moving to oppositely charged electrodes.',
 'chem-titration':'Shows the apparatus, meniscus and placement of reagents.',
 'chem-profile':'Shows reactant/product energy levels and the starting point of activation energy.',
 'chem-profiles':'Compares the energy levels in exothermic and endothermic profiles.',
}

def word_card(x,y,w,lines,color=BLUE):
    h=16+24*len(lines)
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{color}" fill-opacity=".06" stroke="{color}"/>'
    for i,line in enumerate(lines):s+=label(x+w/2,y+24+i*24,line,'middle')
    return s,h

def downfall(w):
    s='';cw=(w-24)/3
    for j,lines in enumerate([['Defender','Protects','Scotland'],['Regicide','Kills','Duncan'],['Tyrant','Attacks','innocents']]):
        x=j*(cw+12);a,h=word_card(x,0,cw,lines,BLUE if j==0 else ORANGE);s+=a
        if j<2:s+=arrow(x+cw+2,44,x+cw+10,44)
    return s,98

def partnership(w):
    s=label(0,16,'Early:')+label(w/2+8,16,'Later:')
    a,h=word_card(0,29,w/2-8,['Shared plot','Her direction'],PURPLE);s+=a
    b,k=word_card(w/2+8,29,w/2-8,['His secret plans','Her isolation'],ORANGE);s+=b
    s+=label(w/2,125,'Power and knowledge become unequal','middle')
    return s,135

def guilt(w):
    s=label(0,16,'Act 2:')+label(w/2+8,16,'Act 5:')
    a,h=word_card(0,30,w/2-8,['Physical blood','“A little water”'],ORANGE);s+=a
    b,k=word_card(w/2+8,30,w/2-8,['Imagined stain','“damned spot”'],PURPLE);s+=b
    s+=label(w/2,124,'Confidence is reversed by lasting guilt','middle')
    return s,134

def irony(w):
    a,h=word_card(0,0,w,['Duncan: trusts the welcome'],BLUE)
    b,k=word_card(0,h+12,w,['Audience: knows the murder plan'],ORANGE)
    return a+b+label(w/2,h+k+42,'Unequal knowledge creates tension','middle'),h+k+52

def photographer(w):
    s='';cw=(w-24)/3
    stages=[['Witness','Painful','events'],['Editor','Selects','images'],['Audience','Brief','response']]
    for j,lines in enumerate(stages):
        x=j*(cw+12);a,h=word_card(x,0,cw,lines,[BLUE,PURPLE,ORANGE][j]);s+=a
        if j<2:s+=arrow(x+cw+2,44,x+cw+10,44)
    return s,98

def nature(w):
    a,h=word_card(0,0,w/2-7,['Wordsworth','Memory recalls','lasting pleasure'],GREEN)
    b,k=word_card(w/2+7,0,w/2-7,['Heaney','Stored fruit','cannot last'],ORANGE)
    return a+b,98

def absence(w):
    a,h=word_card(0,0,w/2-7,['Browning','Imagines release','through closeness'],GREEN)
    b,k=word_card(w/2+7,0,w/2-7,['Kay','Keeps waiting','without resolution'],PURPLE)
    return a+b,98

def catrin(w):
    a,h=word_card(0,0,w/2-7,['Childbirth','Physical cord'],BLUE)
    b,k=word_card(w/2+7,0,w/2-7,['Later conflict','Metaphorical bond'],PURPLE)
    return a+b+label(w/2,96,'Connection survives the wish to separate','middle'),106

def rejection(w):
    a,h=word_card(0,0,w,['Pilot returns alive'],GREEN)
    b,k=word_card(0,60,w,['Family learns silence'],PURPLE)
    return a+arrow(w/2,44,w/2,57)+b,110

def home(w):
    a,h=word_card(0,0,w,['Remembered homeland'],BLUE)
    b,k=word_card(0,60,w,['Return is hoped for, not shown'],GREEN)
    return a+arrow(w/2,44,w/2,57)+b,110

DRAWINGS.update({'lit-downfall':downfall,'lit-partnership':partnership,'lit-guilt':guilt,'lit-irony':irony,'lit-camera':photographer,'lit-nature':nature,'lit-absence':absence,'lit-bond':catrin,'lit-return':rejection,'lit-home':home})
MIN_WIDTH.update({'lit-downfall':260,'lit-partnership':298,'lit-guilt':298,'lit-irony':282,'lit-camera':260,'lit-nature':298,'lit-absence':298,'lit-bond':312,'lit-return':260,'lit-home':270})
PURPOSES.update({
 'lit-downfall':'Tracks the changing purpose of Macbeth’s violence through his character arc.',
 'lit-partnership':'Compares the couple’s early shared knowledge with later secrecy and isolation.',
 'lit-guilt':'Places the early dismissal of guilt beside its later reversal in the washing motif.',
 'lit-irony':'Makes the unequal knowledge of Duncan and the audience explicit.',
 'lit-camera':'Tracks how witnessed suffering is selected and received in War Photographer.',
 'lit-nature':'Compares the different outcomes of remembering nature and trying to preserve fruit.',
 'lit-absence':'Compares imagined release with unresolved waiting rather than treating both love poems as identical.',
 'lit-bond':'Compares the literal birth cord with the continuing metaphorical bond in Catrin.',
 'lit-return':'Shows survival followed by exclusion, rather than equating return with recovery.',
 'lit-home':'Distinguishes remembered homeland from a hoped-for return that the poem does not show happening.',
})

def drawing(kind,width):
    if width<MIN_WIDTH[kind]:raise ValueError('Diagram requires a wider panel: '+kind)
    svg,height=DRAWINGS[kind](width)
    return '<g class="concept-illustration"><title>'+escape(PURPOSES[kind])+'</title>'+svg+'</g>',height

from physics_readable_figures import DRAWINGS as PHYSICS_DRAWINGS,MIN_WIDTH as PHYSICS_WIDTHS,PURPOSES as PHYSICS_PURPOSES
DRAWINGS.update(PHYSICS_DRAWINGS)
MIN_WIDTH.update(PHYSICS_WIDTHS)
PURPOSES.update(PHYSICS_PURPOSES)
