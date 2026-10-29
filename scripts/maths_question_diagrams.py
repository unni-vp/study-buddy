"""Editable, mathematically scaled diagrams for the original Maths questions."""
from pathlib import Path
from html import escape
import math

def txt(x,y,s,anchor='middle',size=16):
 return f'<text x="{x:g}" y="{y:g}" text-anchor="{anchor}" font-size="{size}">{escape(str(s))}</text>'
def line(x1,y1,x2,y2,colour='#274d85',dash=False):
 return f'<path d="M{x1:g},{y1:g} L{x2:g},{y2:g}" fill="none" stroke="{colour}" stroke-width="2"'+(' stroke-dasharray="6 4"' if dash else '')+'/>'
def poly(points,fill='none',colour='#274d85'):
 return f'<polygon points="'+ ' '.join(f'{x:g},{y:g}' for x,y in points)+f'" fill="{fill}" stroke="{colour}" stroke-width="2"/>'
def rect(x,y,w,h,fill='#deebfa'):
 return f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" fill="{fill}" stroke="#274d85" stroke-width="2"/>'
def circle(x,y,r,fill='none'):
 return f'<circle cx="{x:g}" cy="{y:g}" r="{r:g}" fill="{fill}" stroke="#274d85" stroke-width="2"/>'
def dot(x,y):return circle(x,y,3,'#274d85')
def axes(xmax,ymax,xlabel,ylabel,xtick,ytick):
 # 600 × 390 view; proportional plot with generous label margins.
 X=lambda x:75+450*x/xmax;Y=lambda y:315-240*y/ymax
 s=''
 for i in range(int(xmax/xtick)+1):
  x=i*xtick;s+=line(X(x),75,X(x),315,'#d9e1ec')+txt(X(x),338,f'{x:g}',size=14)
 for i in range(int(ymax/ytick)+1):
  y=i*ytick;s+=line(75,Y(y),525,Y(y),'#d9e1ec')+txt(62,Y(y)+5,f'{y:g}','end',14)
 s+=line(75,315,540,315)+line(75,315,75,62)+txt(300,375,xlabel,size=16)+txt(75,35,ylabel,'start',16)
 return s,X,Y

def diagrams():
 d={}
 s,X,Y=axes(16,16,'Time (s)','Velocity (m/s)',2,4)
 s+=poly([(X(x),Y(y)) for x,y in [(0,0),(4,12),(10,12),(14,0)]],'#e2effd')
 d['velocity-graph']=('Velocity against time',s,390)
 s,X,Y=axes(6,6,'x','y',1,1)
 s+=poly([(X(x),Y(y)) for x,y in [(1,0),(5,0),(1,4)]],'#d9f0e8')
 s+=line(X(1),Y(0),X(1),Y(6))+line(X(0),Y(5),X(5),Y(0))+txt(X(3.7),Y(2.2),'x + y = 5',size=14)
 d['inequality-region']=('Included triangular region',s,390)
 pts=[(270+140*math.cos(math.radians(a)),185-140*math.sin(math.radians(a))) for a in [200,268,336,88]]
 s=circle(270,185,140)+poly(pts)
 for (x,y),a in zip(pts,'ABCD'):
  dx=x-270;dy=y-185;s+=txt(x+dx*.17,y+dy*.17+5,a)
 s+=txt(265,291,'112°')+txt(270,82,'?')
 d['cyclic-quadrilateral']=('Cyclic quadrilateral ABCD',s,380)
 s=txt(300,32,'Plan: each number is a stack height')
 for row,values in enumerate([[3,1],[1,2]]):
  for col,v in enumerate(values):s+=rect(210+col*90,60+row*90,90,90)+txt(255+col*90,113+row*90,v)
 s+=txt(300,279,'FRONT EDGE')+line(300,323,300,290)+poly([(300,284),(295,296),(305,296)],'#274d85')+txt(300,350,'View from here')
 d['cube-plan']=('Plan of four stacks of unit cubes',s,375)
 s=txt(300,35,'Front elevation')
 for col,h in enumerate([3,2]):
  for k in range(h):s+=rect(220+col*70,290-(k+1)*70,70,70)
 s+=txt(300,330,'Left                         Right')
 d['cube-elevation']=('Front elevation: heights three and two',s,350)
 s=line(140,180,460,180)+dot(140,180)+dot(460,180)+txt(140,211,'A')+txt(460,211,'B')
 # Radius 200; centres separated by 320; intersections are (300,60),(300,300).
 s+='<path d="M260,20 A200,200 0 0 1 260,340 M340,20 A200,200 0 0 0 340,340" fill="none" stroke="#8e64b0" stroke-width="2"/>'
 s+=line(300,35,300,325)+rect(300,168,12,12,'#fff')+txt(330,355,'Perpendicular bisector')
 d['perpendicular-bisector']=('Equal-radius construction arcs',s,380)
 s=poly([(170,60),(170,300),(240,300)],'#edf4fd')+txt(145,185,'Wall','middle')+txt(250,185,'5 m')+txt(205,330,'1.4 m')+rect(170,286,14,14,'#fff')+txt(220,286,'θ')+txt(120,90,'? m')+line(140,300,450,300)
 d['ladder']=('Ladder against a vertical wall',s,355)
 o=(180,180);r=100;p=(180+r/math.cos(math.radians(64)),180);a=(180+r*math.cos(math.radians(64)),180-r*math.sin(math.radians(64)));b=(a[0],360-a[1])
 s=circle(*o,r)+poly([o,a,p,b])+txt(160,185,'O')+txt(a[0]-3,a[1]-15,'A')+txt(b[0]-3,b[1]+26,'B')+txt(p[0]+20,p[1]+5,'P')+txt(p[0]-59,185,'52°')
 for pt in [a,b]:
  ux,uy=(o[0]-pt[0])/r,(o[1]-pt[1])/r;length=math.dist(pt,p);vx,vy=(p[0]-pt[0])/length,(p[1]-pt[1])/length
  c1=(pt[0]+12*ux,pt[1]+12*uy);c2=(c1[0]+12*vx,c1[1]+12*vy);c3=(pt[0]+12*vx,pt[1]+12*vy)
  s+=line(*c1,*c2)+line(*c2,*c3)
 d['two-tangents']=('Two tangents from P to a circle',s,355)
 s=line(80,90,520,90)+poly([(300,90),(150,285),(460,285)])
 s+=txt(300,65,'A')+txt(140,311,'B')+txt(470,311,'C')+txt(195,269,'β')+txt(420,269,'γ')+txt(252,123,'β')+txt(350,123,'γ')+txt(303,147,'α')+txt(304,348,'The line through A is parallel to BC.')
 d['triangle-angle-proof']=('Alternate angles in a triangle proof',s,380)
 s=circle(260,205,150)
 a=(260,55);b=(260+150*math.cos(math.radians(30)),205-75)
 s+=f'<path d="M{a[0]},{a[1]} A150,150 0 0 1 {b[0]},{b[1]} Z" fill="#f7dba2" stroke="#274d85" stroke-width="2"/>'
 s+=line(260,205,*a)+line(260,205,*b)+txt(245,226,'O')+txt(235,47,'A')+txt(b[0]+15,b[1],'B')+txt(237,135,'6 cm','end')+txt(292,169,'60°')+txt(416,60,'Minor segment','start')+line(416,67,338,91)
 d['circle-segment']=('Minor circular segment shaded',s,380)
 s=circle(270,210,150)+poly([(120,210),(420,210),(345,80.096)],'#f0f5fc')+line(270,210,345,80.096)+txt(103,231,'A')+txt(439,231,'B')+txt(351,64,'C')+txt(270,233,'O')+txt(167,193,'α')+txt(377,193,'β')
 d['semicircle-proof']=('Diameter AB and radius OC for a circle proof',s,380)
 s=rect(55,45,490,280,'#fff')+circle(240,185,100,'#e4effc')+circle(360,185,100,'#fff5d8')+circle(240,185,100)+txt(178,71,'A')+txt(422,71,'B')+txt(195,191,'6')+txt(300,191,'4')+txt(405,191,'8')+txt(500,294,'2')+txt(82,72,'ξ')
 d['venn-counts']=('Venn diagram of twenty people',s,355)
 def tree(root,leftlabel,rightlabel,branches,prob=False):
  s=txt(65,191,root,size=15)
  for y,label,leaves in [(105,leftlabel,branches[0]),(275,rightlabel,branches[1])]:
   s+=line(95,185,230,y)+txt(160,105 if y==105 else 285,label,size=15)
   for dy,leaf in [(-45,leaves[0]),(45,leaves[1])]:
    s+=line(230,y,460,y+dy)+txt(357,y+dy/2-22,leaf,size=15)
  return s
 s=tree('Start','Red: 5/8','Blue: 3/8',[['Red: 4/7','Blue: 3/7'],['Red: 5/7','Blue: 2/7']])+txt(300,30,'Two draws without replacement')
 d['counter-tree']=('Counter probabilities on each branch',s,365)
 s=tree('200','Gym: 120','No gym: 80',[['Swim: 75','No swim: 45'],['Swim: 20','No swim: 60']])
 d['frequency-tree']=('Frequency tree: gym use and swimming',s,365)
 s,X,Y=axes(40,2.5,'Journey time (minutes)','Frequency density (journeys per minute)',10,.5)
 for a,b,h in [(0,10,1),(10,20,2),(20,40,1)]:s+=rect(X(a),Y(h),X(b)-X(a),Y(0)-Y(h))
 d['histogram']=('Histogram with unequal class widths',s,390)
 s=txt(300,30,'Test scores for two groups')
 X=lambda x:80+7*x
 for y,values,label in [(105,[10,20,30,40,50],'A'),(205,[20,30,35,40,55],'B')]:
  lo,q1,med,q3,hi=map(X,values);s+=txt(45,y+5,label)+line(lo,y,hi,y)+line(lo,y-15,lo,y+15)+line(hi,y-15,hi,y+15)+rect(q1,y-25,q3-q1,50)+line(med,y-25,med,y+25)
 s+=line(X(0),280,X(60),280)
 for n in range(0,61,5):s+=line(X(n),275,X(n),285)+txt(X(n),307,n,size=14)
 s+=txt(300,350,'Test score')
 d['box-plots']=('Box plots on the same score scale',s,375)
 s,X,Y=axes(6,100,'Practice time (hours)','Test score (out of 100)',1,20)
 for x,y in [(1,40),(1.5,45),(2,50),(2.5,55),(3,60),(3.5,66),(4,70),(5,79)]:s+=line(X(x)-4,Y(y)-4,X(x)+4,Y(y)+4)+line(X(x)-4,Y(y)+4,X(x)+4,Y(y)-4)
 d['scatter']=('Eight students: practice time and test score',s,390)
 s,X,Y=axes(50,80,'Journey time (minutes)','Cumulative frequency',5,10)
 pts=[(0,0),(10,10),(20,30),(30,50),(40,70),(50,80)]
 for (x1,y1),(x2,y2) in zip(pts,pts[1:]):s+=line(X(x1),Y(y1),X(x2),Y(y2))
 for x,y in pts:s+=dot(X(x),Y(y))
 d['cumulative-frequency']=('Grouped journey times for eighty journeys',s,390)
 return d

def write_diagrams(folder,keys):
 folder=Path(folder);folder.mkdir(parents=True,exist_ok=True);catalog=diagrams()
 for key in keys:
  title,body,height=catalog[key]
  svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="600" height="{height}" viewBox="0 0 600 {height}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><rect width="600" height="{height}" fill="white"/><g font-family="Arial, sans-serif" fill="#161e2d">{body}</g></svg>'
  (folder/(key+'.svg')).write_text(svg,encoding='utf-8')
