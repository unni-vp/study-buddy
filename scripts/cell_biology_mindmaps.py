from PIL import Image, ImageDraw
from cell_biology_visuals import f, label, cell, icon, mito, BASE, BLUE, GREEN, PURPLE, ORANGE, INK
import textwrap
from mindmap_branch_icons import BRANCH_ICONS, place_branch_icon

MAPS=[
('01-cells','Cells','animal',[
 ('Animal cells',['Nucleus: DNA and control','Mitochondria: energy; ribosomes: proteins','Membrane: exchange; cytoplasm: reactions']),
 ('Plant cells',['Cellulose wall + usual cell structures','Photosynthetic cells: chloroplasts','Vacuole: cell sap and firmness']),
 ('Bacterial cells',['No nucleus: DNA loop; may have plasmids','Smaller; no mitochondria','Wall, membrane, cytoplasm, ribosomes']),
 ('Specialised cells',['Muscle / sperm: energy for movement','Root hair: large absorption area','Xylem: water; phloem: sugars'])]),
('02-cell-processes','Cell processes','animal',[
 ('Growth & DNA copying',['Cell grows; structures increase','DNA replicates before mitosis','Two copies of each chromosome']),
 ('Mitosis & division',['Separate copies; nucleus divides','Cytoplasm and membrane divide','Two identical cells: growth / repair']),
 ('Differentiation',['Cells develop specialised structures','Most animal cells: early in life','Many plant cells: throughout life']),
 ('Stem cells',['Undifferentiated; divide and specialise','Embryo / bone marrow / meristems','Tissue repair / clones; risks and ethics'])]),
('03-transport-processes','Transport processes','particles',[
 ('Diffusion',['Particles: net high → low concentration','No respiration energy needed','Oxygen / carbon dioxide / urea']),
 ('Osmosis',['Water: dilute → concentrated','Partially permeable membrane','Plant: gain → turgid; loss → flaccid']),
 ('Active transport',['Substances: low → high concentration','Energy from respiration needed','Root mineral ions; gut sugars']),
 ('Key comparisons',['Diffusion / osmosis: down gradient','Active transport: against gradient','Only osmosis is water-only'])]),
('04-exchange-surfaces','Exchange surfaces','lung',[
 ('Large area',['More particles cross at once','Alveoli / villi / gills','Root hairs']),
 ('Thin barrier',['Short diffusion distance','Faster exchange']),
 ('Maintain gradients',['Blood brings / removes substances','Ventilation refreshes air','Water flows over gills']),
 ('Why needed',['Large bodies: lower SA:V','Long distances to inner cells','Exchange + transport systems'])])]

def curve(d,a,b,c,width):
 dx=b[0]-a[0];pts=[]
 for i in range(51):
  t=i/50;u=1-t
  x=u**3*a[0]+3*u*u*t*(a[0]+dx*.55)+3*u*t*t*(b[0]-dx*.2)+t**3*b[0]
  y=u**3*a[1]+3*u*u*t*a[1]+3*u*t*t*b[1]+t**3*b[1]
  pts.append((x,y))
 d.line(pts,fill=c,width=width)

def wrapped(d,x,y,text,size=25,limit=25,c=INK,b=False):
 lines=textwrap.wrap(text,limit)
 label(d,(x,y-(len(lines)-1)*(size+9)/2),'\n'.join(lines),size,c,b)

def build_maps():
 paths=[]
 for slug,title,kind,branches in MAPS:
  im=Image.new('RGB',(1800,1350),'#fffdf8');d=ImageDraw.Draw(im)
  label(d,(900,55),title,42,b=True)
  cols=[BLUE,GREEN,PURPLE,ORANGE]
  positions=[(470,335,170,[200,345,490]),(1330,335,1630,[200,345,490]),(470,1010,170,[865,1010,1155]),(1330,1010,1630,[865,1010,1155])]
  for j,((head,leaves),(mx,my,lx,ys)) in enumerate(zip(branches,positions)):
   c=cols[j];left=mx<900
   curve(d,(760 if left else 1040,675),(mx+180 if left else mx-180,my+70),c,12)
   d.line((mx-140 if left else mx-180,my+70,mx+180 if left else mx+140,my+70),fill=c,width=6)
   place_branch_icon(im,mx,my-125,BRANCH_ICONS[slug][j],c)
   wrapped(d,mx,my-10,head,29,18,c,True)
   for k,text in enumerate(leaves):
    yy=ys[k] if len(leaves)>1 else my
    curve(d,(mx-140 if left else mx+140,my+70),(lx+145 if left else lx-145,yy+58),c,4)
    d.line((lx-140,yy+58,lx+140,yy+58),fill=c,width=3)
    wrapped(d,lx,yy,text,25,23,c)
  d.ellipse((730,505,1070,845),fill='#f0f3f2',outline='#ccd9d5',width=3)
  if kind in ['animal','plant','bacteria']:cell(d,900,620,kind,1)
  elif kind=='root':icon(d,875,620,kind)
  elif kind=='lung':icon(d,900,620,kind)
  else:
   for x,y in [(855,590),(890,565),(935,595),(870,635),(940,640)]:
    if kind=='water':d.ellipse((x-15,y-15,x+15,y+15),fill=GREEN)
    else:d.ellipse((x-12,y-12,x+12,y+12),fill=BLUE)
  wrapped(d,900,760,title,31,16,INK,True)
  p=BASE/'Mind Maps'/(slug+'.png');im.save(p);paths.append(p)
 return paths
