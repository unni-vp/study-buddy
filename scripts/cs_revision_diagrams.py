"""Editable teaching diagrams for the expanded Computer Science revision notes."""
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1] if Path(__file__).parent.name=='scripts' else Path('D:/Shreya/study-buddy')

class Diagram:
 def __init__(self,w,h,title):self.w=w;self.h=h;self.title=title;self.parts=[]
 def text(self,x,y,s,size=23,bold=False):self.parts.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" font-weight="{700 if bold else 400}">{escape(s)}</text>')
 def path(self,d,arrow=True):self.parts.append(f'<path d="{d}" fill="none" stroke="#243b64" stroke-width="2.5"'+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
 def box(self,x,y,w,h,lines,kind='rect'):
  if kind=='diamond':shape=f'<path d="M{x+w/2} {y}L{x+w} {y+h/2}L{x+w/2} {y+h}L{x} {y+h/2}Z"'
  elif kind=='io':shape=f'<path d="M{x+20} {y}H{x+w}L{x+w-20} {y+h}H{x}Z"'
  else:shape=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2 if kind=="terminal" else 8}"'
  self.parts.append(shape+' fill="#e8eef6" stroke="#243b64" stroke-width="2"/>')
  for i,line in enumerate(lines):self.text(x+w/2,y+h/2+8+(i-(len(lines)-1)/2)*28,line)
 def save(self,n,name,desc):
  p=next((ROOT/'Computer Science - AQA').glob(f'{n:02d} - *'))/'Diagrams';p.mkdir(exist_ok=True)
  svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" role="img" aria-labelledby="title desc"><title id="title">{escape(self.title)}</title><desc id="desc">{escape(desc)}</desc><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0 0L7 3L0 6Z" fill="#243b64"/></marker></defs><rect width="100%" height="100%" fill="#fffefa"/><g font-family="Segoe UI, Arial, sans-serif" fill="#182c3b">'+''.join(self.parts)+'</g></svg>'
  (p/(name+'.svg')).write_text(svg,encoding='utf-8')

def algorithms():
 d=Diagram(700,700,'A temperature decision flowchart')
 d.path('M350 105V140');d.path('M350 210V260');d.path('M200 300H150V420');d.path('M500 300H550V420');d.path('M150 490V560H350',False);d.path('M550 490V560H350V610')
 d.box(290,55,120,50,['Start'],'terminal');d.box(220,140,260,70,['Input temperature'],'io');d.box(200,260,300,80,['temperature < 0?'],'diamond');d.box(30,420,240,70,['Output','Freezing'],'io');d.box(430,420,240,70,['Output','Not freezing'],'io');d.box(290,610,120,50,['Stop'],'terminal')
 d.text(155,280,'Yes',22,True);d.text(545,280,'No',22,True)
 d.save(1,'temperature-flowchart','Start, input temperature, test whether temperature is below zero. Yes leads to output Freezing; No leads to output Not freezing. Both branches join and stop.')
 d=Diagram(900,550,'Merge sort: splitting and ordered merging')
 for path in ['M450 105L230 155','M450 105L670 155','M230 205L120 255','M230 205L340 255','M670 205L560 255','M670 205L780 255','M120 305L230 355','M340 305L230 355','M560 305L670 355','M780 305L670 355','M230 405L450 455','M670 405L450 455']:d.path(path)
 for x,y,w,content in [(325,55,250,'8, 3, 6, 1'),(145,155,170,'8, 3'),(585,155,170,'6, 1'),(85,255,70,'8'),(305,255,70,'3'),(525,255,70,'6'),(745,255,70,'1'),(145,355,170,'3, 8'),(585,355,170,'1, 6'),(325,455,250,'1, 3, 6, 8')]:d.box(x,y,w,50,[content])
 d.text(450,190,'Split',22,True);d.text(450,390,'Merge in order',22,True)
 d.save(1,'merge-sort-stages','Split 8, 3, 6, 1 into pairs and then individual items. Merge to 3, 8 and 1, 6, then merge those ordered lists to 1, 3, 6, 8.')

def systems():
 def gate(d,x,y,kind):
  if kind=='AND':shape=f'M{x} {y}H{x+50}C{x+117} {y} {x+117} {y+70} {x+50} {y+70}H{x}Z'
  elif kind in ('OR','XOR'):shape=f'M{x} {y}Q{x+32} {y+35} {x} {y+70}Q{x+65} {y+75} {x+100} {y+35}Q{x+65} {y-5} {x} {y}Z'
  else:shape=f'M{x} {y}L{x+80} {y+35}L{x} {y+70}Z'
  d.parts.append(f'<path d="{shape}" fill="#e8eef6" stroke="#243b64" stroke-width="2.5"/>')
  if kind=='XOR':d.path(f'M{x-12} {y}Q{x+20} {y+35} {x-12} {y+70}',False)
  if kind=='NOT':d.parts.append(f'<circle cx="{x+87}" cy="{y+35}" r="7" fill="#fffefa" stroke="#243b64" stroke-width="2.5"/>')
 d=Diagram(940,225,'Logic gate symbols: AND, OR, XOR and NOT')
 for i,k in enumerate(['AND','OR','XOR','NOT']):
  x=45+i*235;gate(d,x,65,k);d.text(x+50,35,k,23,True)
  if k=='NOT':d.path(f'M{x-25} 100H{x}',False)
  else:
   for yy in [85,115]:d.path(f'M{x-25} {yy}H{x+(13 if k in ("OR","XOR") else 0)}',False)
  d.path(f'M{x+(94 if k=="NOT" else 100)} 100H{x+135}',False)
 d.text(470,193,'Inputs enter from the left. Each gate produces one output on the right.',22)
 d.save(4,'logic-gate-symbols','The standard AND, OR, XOR and NOT gate symbols. NOT has one input and an inversion circle; the other gates have two inputs. XOR has an extra curved line before the OR shape.')
 d=Diagram(850,330,'A combined circuit for (A AND B) OR (NOT C)')
 gate(d,240,35,'AND');gate(d,240,180,'NOT');gate(d,560,100,'OR')
 for label,y in [('A',55),('B',85),('C',215)]:d.text(65,y+7,label,24,True);d.path(f'M90 {y}H240',False)
 d.path('M340 70H470V120H573',False);d.path('M334 215H470V150H573',False);d.path('M660 135H750',False)
 d.text(780,143,'Q',24,True);d.text(400,50,'X',23,True);d.text(400,245,'Y',23,True)
 d.text(200,298,'X = A AND B',23,True);d.text(425,298,'Y = NOT C',23,True);d.text(650,298,'Q = X OR Y',23,True)
 d.save(4,'combined-logic-circuit','A and B enter an AND gate to produce X. C enters a NOT gate to produce Y. X and Y enter an OR gate to produce Q. Therefore Q is (A AND B) OR (NOT C).')

def networks():
 d=Diagram(1000,680,'Communication between two devices through the four TCP/IP layers')
 d.text(220,38,'Sending device',27,True);d.text(780,38,'Receiving device',27,True)
 rows=[('Application','HTTPS','Browser prepares a web request.','Web service reads the request.'),('Transport','TCP','Manages reliable delivery.','Checks and reassembles data.'),('Internet','IP','Addresses data for its destination.','Processes the IP addressing.'),('Link','NIC and drivers','Sends using local network hardware.','Receives using network hardware.')]
 for i,(name,protocol,left,right) in enumerate(rows):
  y=65+i*115
  for x,desc in [(40,left),(600,right)]:
   d.parts.append(f'<rect x="{x}" y="{y}" width="360" height="90" rx="10" fill="{["#eaf1fa","#eaf6f0","#fff4dd","#f1eafb"][i]}" stroke="#243b64" stroke-width="2"/>')
   d.text(x+180,y+32,name+' · '+protocol,24,True);d.text(x+180,y+65,desc,19)
  if i<3:
   d.path(f'M220 {y+90}V{y+115}');d.path(f'M780 {y+115}V{y+90}')
 d.path('M220 500V610H345');d.path('M655 610H780V500')
 d.box(345,565,310,90,['Network path','may include routers'])
 d.text(500,110,'Data passes down',22,True);d.text(500,140,'the sender’s layers.',20)
 d.text(500,270,'Data passes up',22,True);d.text(500,300,'the receiver’s layers.',20)
 d.text(500,450,'Arrows follow one',20);d.text(500,480,'web request.',20)
 d.save(5,'tcp-ip-device-communication','Two devices each show application, transport, internet and link layers. A web request passes down the sender stack, across a network path that may include routers, and up the receiver stack. HTTPS is application, TCP is transport, IP is internet, and NIC/drivers are link.')

if __name__=='__main__':
 import sys
 {1:algorithms,4:systems,5:networks}[int(sys.argv[1])]()
