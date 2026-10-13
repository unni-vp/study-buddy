"""The approved illustrated A4 Cell Biology overview and shared mitosis drawing."""
from pathlib import Path
from html import escape
from PIL import ImageFont
import json

ROOT = Path(__file__).resolve().parents[1] if Path(__file__).parent.name == 'scripts' else Path(r'D:\Shreya\study-buddy')
FOLDER = ROOT / 'Biology - AQA/01 - Cell biology/Mind Maps'
SLUG = '00-cell-biology-overview'
W, H = 1120, 768
SUBHEADING_SIZE = 16  # Match Compare discs; about 11.2 pt on A4.
INK = '#000000'
BLUE, ORANGE, PURPLE, TEAL, GREEN = '#2366a0', '#b95619', '#7651a5', '#167d87', '#468133'
FONT = {False: ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 16), True: ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 16)}


def text(x, y, value, size=16, color=INK, bold=False, anchor='start', cls='body-text'):
    size=max(size,16)  # Keep at least 11.2 pt at the fixed A4 print width.
    parts=value.split('**')
    if len(parts)%2 != 1:
        raise ValueError(f'Unpaired bold markers: {value}')
    content=''.join(f'<tspan class="keyword" font-weight="700">{escape(part)}</tspan>' if i%2 else escape(part) for i,part in enumerate(parts))
    # Only genuine movement/sequence arrows remain in the text and diagrams.
    content=content.replace('→', '<tspan class="relationship-arrow" font-weight="700">→</tspan>')
    weight=400 if len(parts)>1 else (700 if bold else 400)
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}" class="{cls}">{content}</text>'


def lines(x, y, values, size=16, color=INK, bold=False, gap=21, cls='body-text'):
    return ''.join(text(x, y+i*gap, s, size, color, bold, cls=cls) for i, s in enumerate(values))


def paragraph(x, y, value, width, color=INK, bold=False, gap=21):
    font=FONT[bold]; result=[]; row=''
    for word in value.split():
        test=(row+' '+word).strip()
        if row and font.getlength(test)>width:
            result.append(row);row=word
        else:row=test
    if row:result.append(row)
    return lines(x,y,result,color=color,bold=bold,gap=gap),y+len(result)*gap



def divider(y, width, color):
    """A light rule between content groups, with the same inset as the text."""
    return f'<path class="section-divider" d="M18 {y}H{width-18}" fill="none" stroke="{color}" stroke-opacity=".25" stroke-width="1"/>'


def arrow(x1, y1, x2, y2, color=TEAL, width=2.5):
    return f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{width}" marker-end="url(#arrow-{color[1:]})"/>'


def chromosome(x,y,copy=False,color=PURPLE):
    path='M-5-12L5 12M5-12L-5 12' if copy else 'M0-12V12'
    return f'<path d="{path}" transform="translate({x} {y})" stroke="{color}" stroke-width="4.5" stroke-linecap="round"/>'


def division():
    """Four visible stages; compact artwork, full-size labels."""
    out=[]
    for cx in [41,114]:
        out.append(f'<circle cx="{cx}" cy="109" r="23" fill="#ebf2fc" stroke="#5079a4" stroke-width="2"/><circle cx="{cx}" cy="109" r="17" fill="#f1e8f7" stroke="#a386b7" stroke-width="1.2"/>')
    out += [chromosome(34,109),chromosome(48,109,color=ORANGE),chromosome(106,109,True),chromosome(121,109,True,ORANGE)]
    out.append('<ellipse cx="205" cy="109" rx="41" ry="25" fill="#edf4fc" stroke="#5079a4" stroke-width="2"/>')
    for cx in [184,224]:
        out.extend([chromosome(cx-5,109),chromosome(cx+7,109,color=ORANGE)])
    out += [arrow(194,94,179,94,PURPLE,1.5),arrow(215,124,231,124,ORANGE,1.5)]
    for cx in [284,322]:
        out.append(f'<circle cx="{cx}" cy="109" r="16" fill="#ebf2fc" stroke="#5079a4" stroke-width="2"/><circle cx="{cx}" cy="109" r="12" fill="#f1e8f7" stroke="#a386b7"/>')
        for offset,color in [(-4,PURPLE),(4,ORANGE)]:
            out.append(f'<path d="M{cx+offset} 101V117" stroke="{color}" stroke-width="3" stroke-linecap="round"/>')
    out += [arrow(67,109,85,109,BLUE),arrow(140,109,159,109,BLUE),arrow(250,109,265,109,BLUE)]
    for xx,label in [(41,'Grow'),(114,'Copy DNA'),(205,'Mitosis'),(303,'Divide')]:
        out.append(text(xx,152,label,16,anchor='middle',cls='diagram-label'))
    return ''.join(out)


def panel(number,title,x,y,w,h,color,body):
    # Insets and heading gaps are explicit so print/layout audits can check them.
    heading=text(29,32,str(number),16,'white',True,'middle','diagram-label')+text(50,34,title,20,color,True,cls='panel-title')
    return f'<g class="map-section" style="--panel-accent:{color}" id="illustrated-{number}" transform="translate({x} {y})" data-bounds="0,0,{w},{h}"><rect width="{w}" height="{h}" rx="16" fill="white" stroke="{color}" stroke-width="1.9"/><rect x="9" y="9" width="{w-18}" height="36" rx="11" fill="{color}" opacity=".09"/><g class="section-heading"><circle cx="29" cy="27" r="12" fill="{color}"/>{heading}</g><g class="section-body">{body}</g></g>'


def build_svg():
    defs=''.join(f'<marker id="arrow-{c[1:]}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="4" markerHeight="4" orient="auto-start-reverse"><path d="M1 1L9 5L1 9" fill="none" stroke="{c}" stroke-width="2" stroke-linejoin="round"/></marker>' for c in [BLUE,ORANGE,PURPLE,TEAL,GREEN])
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="2400" height="{2400*H/W:.3f}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="map-title map-description" font-family="Segoe UI,Arial,sans-serif"><title id="map-title">Cell biology overview</title><desc id="map-description">Six clearly divided sections explain cell structures, specialised cells, microscopy, division and stem cells, culturing, and transport with exchange. Mitosis is the only diagram. Bold labels with colons introduce explanations. A complete text counterpart is also available.</desc><defs>{defs}</defs><style>.relationship-arrow{{fill:var(--panel-accent,#2366a0)}}.keyword{{fill:inherit}}</style><rect width="1120" height="768" fill="#fffdf8"/>']

    # Cell types have their own subsections, rather than picture-led columns.
    body=text(18,75,'Animal + plant cells (eukaryotic)',SUBHEADING_SIZE,BLUE,True)
    body+=lines(18,99,[
        '**Nucleus:** stores DNA and controls the cell.',
        '**Cytoplasm:** chemical reactions happen here.',
        '**Membrane:** controls what enters and leaves.',
        '**Mitochondria:** aerobic respiration.',
        '**Ribosomes:** make proteins.',
    ])
    body+=divider(189.5,362,BLUE)
    body+=text(18,209,'Plant cell extras',SUBHEADING_SIZE,GREEN,True)
    body+=lines(18,231,[
        '**Cellulose wall:** strengthens the cell.',
        '**Vacuole:** contains cell sap.',
        '**Chloroplasts:** photosynthesis.',
        'Found in photosynthetic plant cells.',
    ])
    body+=divider(301.5,362,BLUE)
    body+=text(18,322,'Bacteria (prokaryotic)',SUBHEADING_SIZE,PURPLE,True)
    body+=lines(18,347,[
        '**No nucleus:** main DNA is a circular loop.',
        'Much smaller than animal and plant cells.',
        'Some have small DNA rings called **plasmids**.',
    ])
    out.append(panel(1,'Cell structures',18,18,362,405,BLUE,body))

    # One adaptation/function pair per cell, with full words and no icons.
    facts=[
        ['**Sperm:** the tail helps it swim.', 'Many mitochondria release energy.'],
        ['**Nerve:** a long axon carries impulses.', 'Branches connect to other cells.'],
        ['**Muscle:** contracts to move the body.', 'Many mitochondria release energy.'],
        ['**Root hair:** large area for absorption.', 'Takes in water and mineral ions.'],
        ['**Xylem:** hollow tubes carry water.', '**Lignin:** strengthens the cell walls.'],
        ['**Phloem:** sieve tubes transport sugars.', 'Companion cells provide energy.'],
    ]
    body=''.join(lines(18,75+i*44,paragraphs) for i,paragraphs in enumerate(facts))
    body+=divider(323.5,364,ORANGE)
    body+=lines(18,344,[
        '**Differentiation:** becoming specialised.',
        'Most animal cells do this early in life.',
        'Many plant cells can do this for life.',
    ],gap=22)
    out.append(panel(2,'Specialised cells',396,18,364,405,ORANGE,body))

    body=lines(18,73,[
        '**Magnification:** image enlargement.',
        '**Resolution:** tell two close points apart.',
        'Electron microscopes show finer detail.',
    ])
    body+=divider(130,326,GREEN)
    body+=lines(18,152,[
        '**Magnification = image ÷ actual**',
        'Use the same units for both sizes.',
        '**Practical:** stain, focus, draw + scale.',
        '1 mm = 1,000 µm.',
    ])
    out.append(panel(3,'Microscopy',776,18,326,241,GREEN,body))

    # Preserve the existing four-stage chromosome illustration unchanged.
    body=division()+text(18,73,'Two chromosomes shown before copying',16,INK,True,cls='diagram-label')
    body+=text(18,178,'2 genetically identical daughter cells',16,bold=True)
    body+=text(18,201,'Same chromosome number as the parent.',16)
    body+=divider(208.5,362,PURPLE)
    body+=text(18,229,'**Stem cells:** unspecialised, able to divide.',16)
    body+=lines(18,251,[
        '**Embryonic:** most human cell types.',
        '**Bone marrow:** some types, including blood.',
        '**Meristems:** any plant cell type.',
    ],gap=22)
    out.append(panel(4,'Division & stem cells',18,439,362,311,PURPLE,body))

    body=text(18,75,'Diffusion',SUBHEADING_SIZE,TEAL,True)
    body+=lines(18,99,[
        'Net particle movement from high to low',
        'concentration.',
        'No energy from respiration is needed.',
    ],gap=22)
    body+=divider(152,326,TEAL)
    body+=text(18,174,'Osmosis',SUBHEADING_SIZE,TEAL,True)
    body+=lines(18,198,[
        'Water moves from a dilute solution',
        'to a concentrated solution through a',
        '**partially permeable membrane**.',
        'No energy is needed.',
    ])
    body+=divider(269,326,TEAL)
    body+=text(18,290,'Active transport',SUBHEADING_SIZE,TEAL,True)
    body+=lines(18,314,[
        'Moves particles **against the gradient**,',
        'from low to high concentration.',
        'Requires **energy from respiration**.',
    ])
    body+=divider(364,326,TEAL)
    body+=text(18,385,'Exchange surfaces',SUBHEADING_SIZE,TEAL,True)
    body+=lines(18,409,[
        '**Large area** and **thin barrier** aid diffusion.',
        'Blood and ventilation keep gradients.',
        'Large organisms have a lower **SA/V**.',
    ])
    out.append(panel(5,'Transport & exchange',776,275,326,475,TEAL,body))

    # Practical methods, treatment comparison and maths are distinct groups.
    body=text(18,75,'Aseptic technique',SUBHEADING_SIZE,ORANGE,True)
    body+=lines(18,99,[
        'Sterilise agar and',
        'the dish and loop.',
        'Let the loop cool.',
        'Tape lid edges only.',
        'Store upside down.',
        'Incubate at ≤25°C.',
    ])
    body+=text(190,75,'Compare discs',SUBHEADING_SIZE,ORANGE,True)
    body+=lines(190,99,[
        'Antibiotic or',
        'antiseptic discs.',
        'Larger clear zones',
        'mean less growth.',
        'Keep conditions equal.',
        'Repeat each test.',
    ])
    body+=divider(217,364,ORANGE)
    body+=text(18,240,'Calculations',SUBHEADING_SIZE,ORANGE,True)
    body+=text(18,266,'Area = πr²',16,INK,True)
    body+=text(18,288,'r = diameter ÷ 2',16,INK)
    body+=text(170,266,'Cells = start × 2ⁿ',16,INK)
    body+=text(170,288,'n = time ÷ division time',16,INK)
    out.append(panel(6,'Culturing microorganisms',396,439,364,311,ORANGE,body))

    out.append('</svg>')
    return ''.join(out)


def build():
    FOLDER.mkdir(exist_ok=True)
    (FOLDER/(SLUG+'.svg')).write_text(build_svg(),encoding='utf-8')
    from cell_biology_map_content import MAP_CONTENT
    source=next(m for m in MAP_CONTENT if m['slug']==SLUG)
    md='# '+source['title']+'\n\n'+'\n\n'.join('## '+p['title'].capitalize()+'\n\n'+'\n'.join('- '+line for line in p['lines']) for p in source['panels'])+'\n'
    (FOLDER/(SLUG+'.md')).write_text(md,encoding='utf-8')
    review={
        'reviewed':'2026-10-13',
        'type':'Main one-page text-led overview with the existing mitosis diagram and complete overview text counterpart',
        'source':'scripts/cell_biology_illustrated_overview.py',
        'specification':'AQA 8461 4.1, local specification PDF pages 15–23',
        'scope':['cell structures','six specialised cells','differentiation','microscopy','mitosis and stem cells','culturing and calculations','diffusion, osmosis, active transport and exchange'],
        'detail_preservation':'The approved illustrated artwork replaces the older overview. Detailed maps and the complete overview text counterpart are retained.',
        'print':{'width_mm':277,'orientation':'landscape','smallest_text_pt':round(16/1120*277/25.4*72,2)},
        'layout_preferences':['Mitosis is the only diagram','No central heading panel','Clear subsections and fuller explanations','Bold keyword and colon labels','Black body text and keywords beneath coloured headings','Consistent 16-unit bold subsection headings; explanations on separate body lines','Compact 16-unit outer gutters with preserved inner padding','Light panel-colour dividers between natural content groups','Single overview, followed by six detailed maps'],
        'scientific_review':['Existing chromosome identities, copies, separation and daughter sets preserved','No nucleus around separating chromatids','Plant chloroplast qualification retained','Bacterial plasmid qualification retained','Osmosis describes water, solutions and partially permeable membrane','Active transport states against-gradient direction and respiration energy','Clear-zone area and repeated-doubling calculations retained','School incubation limit and practical comparison retained'],
    }
    (FOLDER.parent/'illustrated-overview-review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(FOLDER/(SLUG+'.svg'))


if __name__=='__main__':
    build()
