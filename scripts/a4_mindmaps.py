"""A4 landscape maps. Fixed physical type size; layout adapts, type never shrinks."""
from html import escape
import xml.etree.ElementTree as ET
from a4_mindmap_content import COMPACT
from cell_biology_mindmaps import lines_for
from mindmap_figures import figure
from landscape_mindmaps import anatomy, diagram, NS

W,H=1120,768
BODY=16 # 11.22 pt at 277 mm printed width
LEADING=22
COLORS=['#2166ad','#7750a1','#18837b']
INK='#18344a'
# Each column groups related ideas. Widths are solved from its actual content.
PLANS={
 '00-cell-biology-overview':([[(0,1),3],[(5,2),4],[6,7]],['Structure & observation','Making new cells','Movement & exchange'],{5:('cell-cycle',90)}),
 '01-cells':([[0,1],[2,3,4],[5,6,7]],['Eukaryotic cells','Compare & specialise','Plant adaptations'],{0:('animal',95),1:('plant',95),3:('sperm',75),5:('root',75)}),
 '02-cell-processes':([[0,1],[2,3,4],[5,6,7]],['Copy the instructions','Divide & differentiate','Use stem cells'],{1:('dna-copy',80),2:('cell-cycle',90)}),
 '03-transport-processes':([[0,1,2],[(4,5),3],[6,7]],['Down a gradient','Energy & cell changes','Investigate osmosis'],{2:('osmosis',85),4:('active',105)}),
 '04-exchange-surfaces':([[0,1,7],[2,3,4],[5,6]],['Why adaptations matter','Animal exchange','Plant exchange'],{1:('cubes',80),2:('alveolus',95),6:('leaf',75)}),
 '05-microscopy':([[0,1,5],[2,3,4],[6,7]],['See & compare','Calculate size','Observe & record'],{0:('resolution',90),6:('slide',90)}),
 '06-culturing-microorganisms':([[0,7],[(1,2),3],[(4,5),6]],['Grow & calculate','Prevent contamination','Compare inhibition'],{0:('fission',80),6:('zone',95)})}

def text(x,y,value,size=BODY,c=INK,bold=False,anchor='start',cls=''):
 return f'<text class="{cls}" x="{x:.2f}" y="{y:.2f}" font-size="{size}" fill="{c}" font-weight="{700 if bold else 400}" text-anchor="{anchor}">{escape(str(value))}</text>'

def wrap(s,width,size=BODY):return lines_for(s,width,int(size))

def words(s,x,y,width,c):
 out=[]
 for row in wrap(s,width):
  xx=x
  for word,bold,w in row:
   if bold:out.append(f'<rect x="{xx-1:.2f}" y="{y-13:.2f}" width="{w:.2f}" height="18" rx="2" fill="{c}" opacity=".08"/>')
   out.append(text(xx,y,word,bold=bold,cls='body-text'));xx+=w
  y+=LEADING
 return ''.join(out),y

def illustration(kind,width,height):
 """Keep the useful artwork; redraw labels at physical print sizes, never scaled down."""
 out=[]
 if kind=='course-memory':
  half=width/2
  out.append(text(width/2,16,'Antibody level over time',15,anchor='middle',cls='diagram-label'))
  for j,label in enumerate(['First exposure','Later exposure']):
   x=8+j*half
   out.append(f'<path d="M{x} 86V29M{x} 86H{x+half-22}" fill="none" stroke="#617480"/>')
   curve=f'M{x+3} 85Q{x+25} 84 {x+42} 63T{x+half-26} 83' if j==0 else f'M{x+3} 85Q{x+12} 25 {x+45} 31T{x+half-26} 46'
   out.append(f'<path d="{curve}" fill="none" stroke="#2166ad" stroke-width="3"/>')
   out.append(text(x+half/2-10,109,label,15,anchor='middle',cls='diagram-label'))
  return ''.join(out)
 if kind=='course-chlorosis':
  for x,c,label in [(width*.25,'#8bbc55','Healthy'),(width*.75,'#ebd365','Chlorosis')]:
   out.append(f'<path d="M{x} 51Q{x-35} 22 {x+8} 5Q{x+35} 41 {x} 51M{x} 56L{x+8} 12" fill="{c}" stroke="#57794a" stroke-width="2"/>')
   out.append(text(x,78,label,15,anchor='middle',cls='diagram-label'))
  return ''.join(out)
 if kind=='course-hybridoma':
  cx=width/2
  out.append(text(5,20,'Lymphocyte',15,cls='diagram-label')+text(width-5,20,'Tumour cell',15,anchor='end',cls='diagram-label'))
  out.append(f'<path d="M45 30L{cx} 49L{width-45} 30M{cx} 49V65m-4-5 4 5 4-5" fill="none" stroke="#2166ad" stroke-width="2"/>')
  out.append(text(cx,84,'Hybridoma → clone',15,anchor='middle',cls='diagram-label'))
  return ''.join(out)
 if kind=='course-heart':
  for y,left,right in [(10,'Right heart','Lungs'),(52,'Left heart','Body')]:
   out.append(f'<rect x="5" y="{y}" width="110" height="28" rx="6" fill="#e9f3ff" stroke="#2166ad"/><rect x="{width-100}" y="{y}" width="95" height="28" rx="6" fill="#e9f3ff" stroke="#2166ad"/>')
   out.append(text(60,y+20,left,15,anchor='middle',cls='diagram-label')+text(width-52,y+20,right,15,anchor='middle',cls='diagram-label'))
   out.append(f'<path d="M120 {y+14}H{width-105}m-6-4 6 4-6 4" fill="none" stroke="#2166ad" stroke-width="2"/>')
  return ''.join(out)
 if kind=='course-enzyme':
  cx=width/2
  out.append(f'<path d="M{cx-70} 46H{cx-18}L{cx} 68L{cx+18} 46H{cx+70}V78H{cx-70}Z" fill="#e1effb" stroke="#2166ad" stroke-width="2"/><path d="M{cx-18} 14H{cx+18}L{cx} 36Z" fill="#f5cb87" stroke="#ac6a21"/>')
  out.append(text(5,28,'Substrate',15,cls='diagram-label')+text(width-5,66,'Enzyme',15,anchor='end',cls='diagram-label'))
  return ''.join(out)
 if kind=='alveolus':
  cx=width/2
  return (f'<ellipse cx="{cx}" cy="22" rx="85" ry="20" fill="#e5f2ff" stroke="#2166ad" stroke-width="1.5"/>'
    + f'<rect x="{cx-115}" y="50" width="230" height="22" rx="8" fill="#ffe2e5" stroke="#ba5066"/>'
    + f'<path d="M{cx-60} 32V61m-3-5 3 5 3-5M{cx+60} 61V32m-3 5 3-5 3 5" fill="none" stroke="#2166ad" stroke-width="1.5"/>'
    + text(cx,26,'Alveolar air',15,anchor='middle',cls='diagram-label')
    + text(cx,66,'Blood',15,anchor='middle',cls='diagram-label')
    + text(cx-98,47,'O₂',15,anchor='middle',cls='diagram-label')
    + text(cx+98,47,'CO₂',15,anchor='middle',cls='diagram-label')
    + text(cx,height-6,'O₂: air → blood; CO₂: reverse',15,anchor='middle',cls='diagram-label'))
 if kind in ('animal','plant'):
  root=ET.fromstring(anatomy(kind))
  root.set('transform',f'translate({width/2-58} 0) scale(.47)')
  for n in root.iter():
   if n.tag.endswith('text'):n.set('font-size','32');n.set('y',str(float(n.get('y'))+3))
   if n.tag.endswith('circle') and n.get('r')=='16':n.set('r','21')
  out.append(ET.tostring(root,encoding='unicode'))
  return ''.join(out)
 custom=kind in ['resolution','slide','zone','leaf']
 root=ET.fromstring(diagram(kind) if custom else figure(kind))
 # Remove inherited captions: re-add only compact, readable labels below.
 for parent in root.iter():
  for n in list(parent):
   if n.tag.endswith('text'):parent.remove(n)
 if kind=='resolution':vb='55 15 465 160';labels=[(.25,'Blurred'),(.75,'Separate points')]
 elif kind=='slide':vb='60 25 510 165';labels=[(.50,'Lower coverslip at an angle')]
 elif kind=='zone':vb='105 0 235 215';labels=[(.50,'Diameter → halve → radius')]
 elif kind=='leaf':vb='40 30 520 210';labels=[(.50,'CO₂ enters through a stoma')]
 elif kind=='cell-cycle':vb='0 10 600 110';labels=[(.08,'Before'),(.31,'Copy'),(.57,'Separate'),(.87,'2 cells')]
 elif kind=='dna-copy':vb='35 20 530 135';labels=[(.22,'Before copying'),(.79,'Joined copies')]
 elif kind=='osmosis':vb='40 10 520 135';labels=[(.5,'● water   ■ solute   ┆ membrane')]
 elif kind=='active':vb='40 10 520 140';labels=[(.50,'Low → high; respiration energy')]
 elif kind=='cubes':vb='70 10 430 140';labels=[(.22,'1 cm: 6:1'),(.74,'3 cm: 2:1')]
 elif kind=='alveolus':vb='60 15 480 180';labels=[(.5,'O₂: air → blood; CO₂: reverse')]
 elif kind=='fission':vb='65 10 445 150';labels=[(.5,'One bacterium → two')]
 elif kind=='root':vb='140 15 410 150';labels=[(.5,'Extension → large surface area')]
 elif kind=='sperm':vb='130 45 360 85';labels=[(.5,'Tail → movement')]
 else:raise ValueError(kind)
 root.set('viewBox',vb);root.set('width',str(width));root.set('height',str(height-(44 if kind=='active' else 24)));root.set('x','0');root.set('y','0')
 out.append(ET.tostring(root,encoding='unicode'))
 for fraction,label in labels:out.append(text(width*fraction,height-(26 if kind=='active' else 6),label,15,anchor='middle',cls='diagram-label'))
 if kind=='active':
  out.append(text(width/2,height-6,'● solute   │ membrane   ▣ protein',15,anchor='middle',cls='diagram-label'))
 # Explicit particle keys remain coloured like the particle models.
 if kind=='osmosis':
  out[-1]=''
  for x,value,col in [(width*.19,'● water','#286daa'),(width*.49,'■ solute','#c07432'),(width*.79,'┆ membrane','#25836d')]:out.append(text(x,height-6,value,15,col,anchor='middle',cls='diagram-label'))
 return ''.join(out)

class Panel:
 def __init__(self,slug,i,width,picture):
  self.indices=list(i) if isinstance(i,tuple) else [i]
  self.i=self.indices[0];self.width=width;self.data=dict(COMPACT[slug][self.i]);self.picture=picture
  if len(self.indices)>1:
   self.data['title']={(0,1):'Cells & specialisation',(5,2):'Division & stem cells',(1,2):'Grow an uncontaminated culture',(4,5):'Compare antimicrobial discs'}[i]
   if slug=='03-transport-processes':self.data['title']='Active transport & its uses'
   self.data['lines']=[line for n in self.indices for line in COMPACT[slug][n]['lines']]
  self.heading=wrap('**'+self.data['title']+'**',width-46,18)
  self.body_y=30+len(self.heading)*24+18 # heading baseline + clear gap to text
  self.lines=list(self.data['lines'])
  if picture and picture[0] in ('cell-cycle','dna-copy'):
   self.lines.insert(0,'Example shown: **two chromosomes**.')
  if slug=='01-cells' and i==0:
   for j in range(len(self.lines)):
    for n,term in enumerate(['Nucleus','Cytoplasm','Membrane','Mitochondria','Ribosomes'],1):self.lines[j]=self.lines[j].replace('**'+term+'**','**'+str(n)+'. '+term+'**').replace('**'+term+':**','**'+str(n)+'. '+term+':**')
  if slug=='01-cells' and i==1:
   for j in range(len(self.lines)):
    for n,term in [(6,'Cellulose wall'),(7,'Permanent vacuole'),(8,'Chloroplasts')]:self.lines[j]=self.lines[j].replace('**'+term+':**','**'+str(n)+'. '+term+':**')
  self.height=self.body_y+sum(len(wrap(line,width-28))*LEADING+4 for line in self.lines)-8+(picture[1]+8 if picture else 0)
 def svg(self,x,y,c,number):
  w,h=self.width,self.height
  out=[f'<g class="map-section" id="section-{number}" data-source-panel="{",".join(map(str,self.indices))}" data-bounds="0,0,{w},{h}" transform="translate({x} {y})"><rect width="{w}" height="{h}" rx="10" fill="white" stroke="{c}" stroke-width="1.5"/><g class="section-heading">',f'<circle cx="19" cy="23" r="10" fill="{c}"/>',text(19,28,number,15,'white',True,'middle')]
  yy=29
  for row in self.heading:
   out.append(text(35,yy,' '.join(v[0] for v in row),18,c,True));yy+=24
  out.append('</g><g class="section-body">');yy=self.body_y
  if self.picture:
   kind,hh=self.picture
   out.append(f'<g class="concept-illustration" transform="translate(14 {yy-13})">'+illustration(kind,w-28,hh)+'</g>');yy+=hh+8
  for line in self.lines:
   chunk,yy=words(line,14,yy,w-28,c);out.append(chunk);yy+=4
  out.append('</g></g>');return ''.join(out)

def build_a4(m):
 slug=m['slug'];groups,labels,pics=PLANS[slug]
 assert sorted(n for group in groups for i in group for n in (i if isinstance(i,tuple) else [i]))==list(range(len(COMPACT[slug])))
 # Search widths, not font sizes, to balance the actual height of related content.
 cache={}
 def column(col,w):
  key=(col,w)
  if key not in cache:
   panels=[Panel(slug,i,w,pics.get(i[0] if isinstance(i,tuple) else i)) for i in groups[col]]
   cache[key]=(panels,sum(p.height for p in panels)+12*(len(panels)-1))
  return cache[key]
 best=None
 for a in range(290,451,10):
  for b in range(290,451,10):
   c=W-40-a-b
   if not 290<=c<=450:continue
   heights=[column(k,w)[1] for k,w in enumerate([a,b,c])]
   score=(max(heights),sum(abs(w-360) for w in [a,b,c]))
   if best is None or score<best[0]:best=(score,[a,b,c],heights)
 _,widths,heights=best
 if max(heights)>H-83:raise ValueError(f'{slug}: needs {max(heights):.0f} px; widths {widths}; content must be reorganised, never shrink type')
 title=m['title'].replace(' overview','')
 header_width=max(280,sum(v[2] for row in wrap('**'+title+'**',2000,26) for v in row)+50)
 out=[f'<svg xmlns="{NS}" width="2400" height="{2400*H/W}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title description" data-print-width-mm="277" data-body-size="16"><title id="title">{escape(m["title"])}</title><desc id="description">'+escape(' '.join(p['title']+': '+' '.join(p['lines']).replace('**','') for p in COMPACT[slug]))+'</desc>',
 '<defs><radialGradient id="animalFill"><stop stop-color="#fff5de"/><stop offset="1" stop-color="#dceafd"/></radialGradient><radialGradient id="nucleusFill"><stop stop-color="#ddc7f4"/><stop offset="1" stop-color="#9b79c2"/></radialGradient><linearGradient id="leafFill" x2="0" y2="1"><stop stop-color="#edf7b8"/><stop offset="1" stop-color="#bfd882"/></linearGradient></defs>',f'<rect width="{W}" height="{H}" fill="#fffefa"/><g font-family="Segoe UI, Arial, sans-serif" fill="{INK}">']
 x=0;number=0
 for k,w in enumerate(widths):
  cx=x+w/2;c=COLORS[k]
  start=f'M{(W-header_width)/2} 25' if k==0 else (f'M{(W+header_width)/2} 25' if k==2 else 'M560 52')
  out.append(f'<path class="relationship-path" d="{start}Q{cx} {55 if k==1 else 25} {cx} 55V78" stroke="{c}" stroke-width="2" fill="none"/>')
  labelw=sum(v[2] for row in wrap('**'+labels[k]+'**',500,15) for v in row)+16
  out.append(f'<rect x="{cx-labelw/2}" y="51" width="{labelw}" height="22" rx="5" fill="#fffefa"/>'+text(cx,67,labels[k],15,c,True,'middle','diagram-label'))
  y=79
  for panel in column(k,w)[0]:
   number+=1;out.append(panel.svg(x,y,c,number));y+=panel.height+12
  x+=w+20
 out.append(f'<g class="map-hub" data-bounds="{(W-header_width)/2},0,{header_width},52"><rect x="{(W-header_width)/2}" width="{header_width}" height="52" rx="18" fill="#edf5ff" stroke="{INK}" stroke-width="1.7"/>'+text(W/2,35,title,24,INK,True,'middle')+'</g></g></svg>')
 print(slug,'widths',widths,'column heights',heights,'body 11.22 pt on A4')
 return ''.join(out)
