"""Scientific diagrams for the notes, generated separately from mind maps."""
from PIL import Image, ImageDraw
from cell_biology_visuals import BASE, f, arrow, BLUE, GREEN, ORANGE, PURPLE, INK
import math

FOLDER = BASE / 'Revision Notes' / 'Diagrams'
RED = '#bd4160'

def text(d, x, y, words, size=30, colour=INK, bold=False):
    lines = words.split('\n')
    for i, line in enumerate(lines):
        d.text((x, y + i * (size + 10)), line, font=f(size, bold), fill=colour, anchor='mm')

def sheet(title, height):
    im = Image.new('RGB', (1800, height), '#fafcfe')
    d = ImageDraw.Draw(im)
    text(d, 900, 60, title, 43, bold=True)
    return im, d

def thread(d, x, y, colour, copied=False, scale=1):
    # Two distinct parallel DNA copies, joined at their centre after replication.
    offsets = [-10, 10] if copied else [0]
    for dx in offsets:
        pts = [(x + dx + 9*scale*math.sin(i/6), y - 38*scale + i*scale) for i in range(77)]
        d.line(pts, fill=colour, width=max(5, round(6*scale)))
    if copied:
        d.line((x-12, y, x+12, y), fill=colour, width=5)

def chromatid(d, x, y, colour, toward):
    # Centromere leads each single copy towards its pole.
    tip = x + toward*15
    d.line([(x-toward*16, y-36), (tip, y), (x-toward*16, y+36)], fill=colour, width=8)

def outline(d, x, y, rx=170, ry=130, nucleus=True):
    d.ellipse((x-rx,y-ry,x+rx,y+ry), fill='#e9f2fb', outline=BLUE, width=5)
    if nucleus:
        d.ellipse((x-rx*.63,y-ry*.76,x+rx*.63,y+ry*.76), fill='#f5eff9', outline=PURPLE, width=3)

def mitosis():
    im,d = sheet('Copy each chromosome → separate the copies → divide', 1150)
    xs = [235, 680, 1120, 1570]
    for x, title in zip(xs, ['1  GROW', '2  COPY DNA', '3  MITOSIS', '4  TWO CELLS']):
        text(d,x,150,title,31,bold=True)
    for x in xs[:2]: outline(d,x,340)
    for x, copied in [(xs[0],False),(xs[1],True)]:
        thread(d,x-45,340,RED,copied)
        thread(d,x+45,340,BLUE,copied)
    outline(d,xs[2],340,nucleus=False)
    for yy,colour in [(295,RED),(385,BLUE)]:
        for xx,side in [(1045,-1),(1195,1)]:
            d.line((1120+side*140,340,xx+side*15,yy),fill='#b6c8d6',width=3)
            chromatid(d,xx,yy,colour,side)
        arrow(d,(1098,yy),(1070,yy),colour,4)
        arrow(d,(1142,yy),(1170,yy),colour,4)
    for yy in [260,440]:
        outline(d,1570,yy,140,78)
        thread(d,1535,yy,RED,scale=.6)
        thread(d,1605,yy,BLUE,scale=.6)
    for a,b in zip(xs,xs[1:]): arrow(d,(a+180,340),(b-180,340),GREEN)
    captions = [
        'Cell grows; more ribosomes\nand mitochondria.',
        'Each chromosome now has\ntwo joined, identical copies.',
        'Copies are pulled apart.\nOne full set goes to each end.',
        'Nuclei form; cytoplasm\nand membrane divide.'
    ]
    for x, words in zip(xs,captions): text(d,x,565,words,27)
    text(d,900,690,'Each daughter cell has the same chromosome number as the parent.',33,GREEN,True)
    d.line((80,745,1720,745),fill='#d7e3ec',width=3)
    # A true X close-up resolves the two joined copies, with pointers to each.
    d.line([(465,830),(510,920),(465,1010)],fill=RED,width=13)
    d.line([(555,830),(510,920),(555,1010)],fill=RED,width=13)
    d.ellipse((498,908,522,932),fill=INK)
    text(d,235,835,'One copy',29,RED,True)
    arrow(d,(330,850),(470,850),RED,3)
    text(d,775,835,'Identical copy',29,RED,True)
    arrow(d,(650,850),(550,850),RED,3)
    text(d,510,1060,'ONE copied chromosome',30,bold=True)
    text(d,1270,830,'At the start of mitosis, the DNA coils\ninto visible chromosomes like this.',29)
    text(d,1270,940,'The joined copies are sister chromatids.\nDNA amount doubles when copied;\nchromosome number has not doubled.',29,PURPLE)
    text(d,900,1120,'Two chromosomes are shown so you can follow each copy into both daughter cells.',26)
    im.save(FOLDER/'02-cell-cycle-stem-cells.png')

def dots(d,x,y,count,colour,water=False):
    for i in range(count):
        xx=x+(i%5)*43; yy=y+(i//5)*34
        r=7 if water else 10
        d.ellipse((xx-r,yy-r,xx+r,yy+r),fill=colour)

def transport():
    im,d=sheet('Transport: what moves, which way, and why?',1400)
    for i,(name,colour) in enumerate([('DIFFUSION',BLUE),('OSMOSIS',GREEN),('ACTIVE TRANSPORT',ORANGE)]):
        y=285+i*410
        text(d,245,y-30,name,31,colour,True)
        text(d,245,y+35,['Gas / dissolved\nparticles','Water molecules','Mineral ions\nor sugars'][i],27)
        # Identical-sized compartments make particle density interpretable.
        d.rectangle((600,y-100,1280,y+160),fill='#f0f6fb',outline='#bccedb',width=3)
        d.line((940,y-100,940,y+160),fill=PURPLE if i==1 else '#9daebc',width=7)
        dots(d,660,y-55,[15,20,5][i],colour,i==1)
        dots(d,1020,y-55,[5,15,15][i],colour,i==1)
        if i==1:
            for xx,yy in [(685,y+70),(815,y+70),(1010,y+40),(1095,y+40),(1180,y+40),(1030,y+70),(1120,y+70),(1200,y+70)]:
                d.rectangle((xx-13,yy-13,xx+13,yy+13),fill=PURPLE)
            d.ellipse((1358,y-72,1372,y-58),fill=GREEN)
            text(d,1430,y-65,'Water',28,GREEN)
            d.rectangle((1510,y-77,1534,y-53),fill=PURPLE)
            text(d,1600,y-65,'Solute',28,PURPLE)
            text(d,1520,y-5,'Membrane lets water through;\nthe solute shown stays put.',27)
            text(d,770,y-135,'Dilute solution',29,GREEN,True)
            text(d,1110,y-135,'Concentrated solution',29,GREEN,True)
        else:
            text(d,770,y-135,'Higher concentration' if i==0 else 'Lower concentration',29,colour,True)
            text(d,1110,y-135,'Lower concentration' if i==0 else 'Higher concentration',29,colour,True)
            text(d,1520,y-45,'No energy from\nrespiration needed' if i==0 else 'Energy from\nrespiration needed',29,colour,True)
        if i==2:
            d.rounded_rectangle((913,y+55,967,y+135),radius=13,fill='#efc78c',outline=ORANGE,width=4)
            text(d,940,y+200,'Membrane transport protein',27,ORANGE)
        arrow(d,(760,y+100),(1110,y+100),colour,8)
        if i<2: arrow(d,(1080,y+140),(810,y+140),colour,3)
        if i<2: text(d,940,y+200,'Thick arrow: NET movement; thin arrow: movement the other way.',25)
        text(d,940,y+240,['Example: oxygen diffuses into respiring cells.','Water moves from dilute to concentrated across a partially permeable membrane.','Example: root hair cells absorb mineral ions against the concentration gradient.'][i],26,colour)
        if i<2: d.line((70,y+257,1730,y+257),fill='#d7e3ec',width=2)
    im.save(FOLDER/'03-transport.png')

def cube(d,x,y,a):
    depth=a*.45
    top=[(x,y),(x+depth,y-depth),(x+a+depth,y-depth),(x+a,y)]
    side=[(x+a,y),(x+a+depth,y-depth),(x+a+depth,y+a-depth),(x+a,y+a)]
    d.polygon(top,fill='#d2e5f4',outline=BLUE,width=4)
    d.polygon(side,fill='#91b6d6',outline=BLUE,width=4)
    d.rectangle((x,y,x+a,y+a),fill='#e7f1f9',outline=BLUE,width=4)

def exchange():
    im,d=sheet('Exchange: surface area, distance and concentration gradient',1280)
    cube(d,230,235,75)
    cube(d,650,195,225)
    text(d,275,360,'1 cm side',29,bold=True)
    text(d,790,465,'3 cm side',29,bold=True)
    text(d,275,450,'Area: 6 cm²\nVolume: 1 cm³\nSA:V = 6:1',29,BLUE)
    text(d,790,535,'Area: 54 cm²\nVolume: 27 cm³\nSA:V = 2:1',29,BLUE)
    text(d,1360,235,'A larger cube has more total area,\nbut LESS area per unit of volume.',31,bold=True)
    text(d,1360,360,'Large organisms need specialised\nexchange surfaces and transport\nto supply their inner cells.',30)
    d.line((80,670,1720,670),fill='#d7e3ec',width=3)
    text(d,900,720,'Example: gas exchange in alveoli',34,bold=True)
    # Sacs at the end of an airway, rather than a whole-lung icon.
    d.line((245,795,245,850),fill=BLUE,width=20)
    for x,y in [(190,865),(285,865),(165,935),(250,960),(330,935)]:
        d.line((245,845,x,y),fill=BLUE,width=8)
        d.ellipse((x-42,y-42,x+42,y+42),fill='#e6f3fa',outline=BLUE,width=4)
    text(d,245,1040,'Many tiny sacs\n= large surface area',28,BLUE,True)
    arrow(d,(400,915),(455,915),GREEN,4)
    d.ellipse((475,785,825,1135),fill='#f7d8de',outline=RED,width=4)
    d.ellipse((500,810,800,1110),fill='#e6f3fa',outline=BLUE,width=4)
    text(d,635,935,'Air inside\none alveolus',27,BLUE)
    arrow(d,(715,870),(795,870),GREEN,6)
    text(d,915,825,'Oxygen',27,GREEN,True)
    arrow(d,(805,1020),(735,1020),ORANGE,6)
    text(d,920,1060,'Carbon dioxide',26,ORANGE,True)
    text(d,650,1180,'Blood capillary surrounds the sac',27,RED)
    text(d,1390,850,'THIN WALLS\nShort diffusion distance\nbetween air and blood.',29,BLUE,True)
    text(d,1390,1010,'STEEP GRADIENTS\nVentilation refreshes air.\nBlood flow brings CO₂\nand carries O₂ away.',29,GREEN,True)
    im.save(FOLDER/'04-exchange-surfaces.png')

def build_note_diagrams():
    FOLDER.mkdir(exist_ok=True)
    mitosis()
    transport()
    exchange()

if __name__ == '__main__':
    build_note_diagrams()
