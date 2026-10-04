"""Small code-drawn memory cues for the main mind-map branches."""
from PIL import Image, ImageDraw
from cell_biology_visuals import cell, icon, BLUE, GREEN, PURPLE, ORANGE

BRANCH_ICONS = {
    '01-cells': ['animal', 'plant', 'bacteria', 'sperm'],
    '02-cell-processes': ['dna-copy', 'daughter-cells', 'differentiate', 'stem-cells'],
    '03-transport-processes': ['diffusion', 'osmosis', 'active', 'compare'],
    '04-exchange-surfaces': ['folds', 'thin', 'refresh-blood', 'cubes'],
}

def arrow(d, a, b, colour, width=5):
    import math
    d.line([a, b], fill=colour, width=width)
    angle = math.atan2(b[1]-a[1], b[0]-a[0])
    d.polygon([b, (b[0]-14*math.cos(angle-.5), b[1]-14*math.sin(angle-.5)),
               (b[0]-14*math.cos(angle+.5), b[1]-14*math.sin(angle+.5))], fill=colour)

def drop(d, x, y, colour, size=1):
    points=[(x,y-45*size),(x-27*size,y),(x-25*size,y+18*size),
            (x-14*size,y+30*size),(x+14*size,y+30*size),
            (x+25*size,y+18*size),(x+27*size,y)]
    d.polygon(points,fill=colour)
    d.line((x-12*size,y,x-13*size,y+13*size),fill='white',width=4)

def nucleus_cell(d, box, joined=False):
    d.ellipse(box,fill='#eaf3f0',outline=GREEN,width=4)
    x=(box[0]+box[2])/2;y=(box[1]+box[3])/2
    d.ellipse((x-21,y-27,x+21,y+27),fill='#f2eafb',outline=PURPLE,width=2)
    for dx,colour in [(-10,PURPLE),(10,ORANGE)]:
        d.line((x+dx,y-12,x+dx,y+12),fill=colour,width=5)

def cube(d, x, y, side, colour):
    dx=side*.4;dy=side*.2
    front=[(x,y),(x+side,y),(x+side,y+side),(x,y+side)]
    top=[(x,y),(x+dx,y-dy),(x+side+dx,y-dy),(x+side,y)]
    right=[(x+side,y),(x+side+dx,y-dy),(x+side+dx,y+side-dy),(x+side,y+side)]
    for points,fill in [(front,'#f9e9d9'),(top,'#fff3e6'),(right,'#eed2b3')]:
        d.polygon(points,fill=fill,outline=colour,width=3)

def branch_icon(kind, colour):
    canvas=Image.new('RGBA',(210,180),(255,253,248,0));d=ImageDraw.Draw(canvas)
    if kind in ['animal','plant','bacteria']:
        cell(d,105,90,kind,.68)
    elif kind=='sperm':
        icon(d,100,90,'sperm')
    elif kind=='dna-copy':
        # One chromosome becomes two joined copies, not two chromosomes.
        d.line((42,65,42,119),fill=PURPLE,width=8)
        arrow(d,(67,92),(121,92),colour,4)
        d.line((150,64,178,120),fill=PURPLE,width=7)
        d.line((178,64,150,120),fill=PURPLE,width=7)
    elif kind=='daughter-cells':
        # Matching complete sets in both daughters.
        nucleus_cell(d,(20,50,95,136));nucleus_cell(d,(115,50,190,136))
    elif kind=='differentiate':
        # A human cell becomes specialised; no human-to-plant arrow.
        d.ellipse((14,65,62,115),fill='#e4d8f3',outline=PURPLE,width=4)
        d.ellipse((30,81,47,99),fill=PURPLE)
        arrow(d,(70,90),(114,90),colour,4)
        d.ellipse((120,72,151,108),fill='#e4d8f3',outline=PURPLE,width=3)
        d.line((151,90,184,90),fill=PURPLE,width=5)
        for dy in [-24,0,24]:
            d.line((133,80,110,65+dy),fill=PURPLE,width=3)
            d.line((184,90,201,90+dy),fill=PURPLE,width=3)
    elif kind=='stem-cells':
        # Human-cell and plant-meristem cues are separate, never linked.
        d.ellipse((22,70,85,133),fill='#e4d8f3',outline=PURPLE,width=4)
        d.ellipse((44,91,65,112),fill=PURPLE)
        d.line((150,133,150,72),fill=GREEN,width=5)
        d.ellipse((119,65,150,95),fill='#d7ecd3',outline=GREEN,width=3)
        d.ellipse((151,55,184,85),fill='#d7ecd3',outline=GREEN,width=3)
        d.ellipse((143,45,157,63),fill=GREEN)
    elif kind=='diffusion':
        for x,y in [(28,58),(57,59),(30,89),(59,90),(28,120),(57,121),(166,72),(180,113)]:
            d.ellipse((x-8,y-8,x+8,y+8),fill=BLUE)
        arrow(d,(82,90),(144,90),BLUE,5)
    elif kind=='osmosis':
        drop(d,58,94,BLUE,.8)
        for y in range(44,140,18):d.line((119,y,119,y+9),fill=GREEN,width=4)
        arrow(d,(77,103),(173,103),BLUE,5)
    elif kind=='active':
        # Energy and an uphill direction are memory cues; the text states respiration.
        d.polygon([(55,45),(28,95),(52,95),(40,135),(85,78),(62,78),(76,45)],fill=ORANGE)
        d.line([(96,137),(96,114),(125,114),(125,88),(151,88),(151,63),(182,63)],fill=colour,width=4)
        arrow(d,(104,132),(172,54),colour,4)
    elif kind=='compare':
        arrow(d,(60,53),(60,128),BLUE,6)
        arrow(d,(149,128),(149,53),PURPLE,6)
        d.line((96,61,113,61),fill=colour,width=4)
        d.line((96,116,113,116),fill=colour,width=4)
    elif kind=='folds':
        points=[(23,130),(23,68),(35,46),(47,68),(47,113),(63,113),(63,68),
                (75,46),(87,68),(87,113),(103,113),(103,68),(115,46),(127,68),
                (127,113),(143,113),(143,68),(155,46),(167,68),(167,130)]
        d.line(points,fill=colour,width=6)
        d.line((23,140,167,140),fill=colour,width=3)
    elif kind=='thin':
        d.line((91,44,91,139),fill=colour,width=5)
        d.line((109,44,109,139),fill=colour,width=5)
        arrow(d,(56,90),(148,90),BLUE,5)
    elif kind=='refresh-blood':
        drop(d,105,96,'#bb4853',.85)
        d.arc((42,35,169,151),205,350,fill=colour,width=5)
        d.arc((42,35,169,151),25,170,fill=colour,width=5)
        arrow(d,(163,81),(169,97),colour,4)
        arrow(d,(47,107),(41,89),colour,4)
    elif kind=='cubes':
        # Both cubes are 3D and drawn with a 1:3 linear scale ratio.
        cube(d,29,100,22,colour);cube(d,95,67,66,colour)
    else:
        raise ValueError('Unknown branch icon: '+kind)
    return canvas.resize((116,100),Image.Resampling.LANCZOS)

def place_branch_icon(image, x, y, kind, colour):
    cue=branch_icon(kind,colour)
    image.paste(cue,(round(x-58),round(y-50)),cue)
