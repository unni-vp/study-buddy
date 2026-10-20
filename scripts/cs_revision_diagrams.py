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

if __name__=='__main__':
 import sys
 {1:algorithms}[int(sys.argv[1])]()
