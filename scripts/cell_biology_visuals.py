from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math
BASE=Path(__file__).resolve().parents[1]/'Biology - AQA'/'01 - Cell biology'
INK='#17354b'; BLUE='#276cad'; GREEN='#25826c'; ORANGE='#bf7030'; PURPLE='#8253ac'
def f(n,b=False):return ImageFont.truetype('C:/Windows/Fonts/'+('segoeuib.ttf' if b else 'segoeui.ttf'),n)
def label(d,xy,text,n=25,c=INK,b=False):
 for i,s in enumerate(text.split('\n')):d.text((xy[0],xy[1]+i*(n+9)),s,font=f(n,b),fill=c,anchor='mm')
def arrow(d,a,b,c=BLUE,width=5):
 d.line([a,b],fill=c,width=width);ang=math.atan2(b[1]-a[1],b[0]-a[0]);d.polygon([b,(b[0]-20*math.cos(ang-.45),b[1]-20*math.sin(ang-.45)),(b[0]-20*math.cos(ang+.45),b[1]-20*math.sin(ang+.45))],fill=c)
def cell(d,x,y,kind='animal',s=1):
 w=int(110*s);h=int(65*s)
 if kind=='plant':d.rounded_rectangle((x-w-8,y-h-8,x+w+8,y+h+8),radius=15,outline=GREEN,width=7)
 d.ellipse((x-w,y-h,x+w,y+h),fill='#e7f0fb' if kind!='plant' else '#edf6df',outline=BLUE if kind!='plant' else GREEN,width=4)
 if kind=='bacteria':
  d.line([(x-40,y),(x-20,y-20),(x+10,y+20),(x+40,y),(x-40,y)],fill=PURPLE,width=4);d.ellipse((x+50,y+20,x+70,y+40),outline=PURPLE,width=3)
 else:
  d.ellipse((x-55,y-28,x-5,y+22),fill='#d4bde8',outline=PURPLE,width=3)
  if kind=='plant':
   d.ellipse((x+5,y-30,x+60,y+30),fill='#c6e6ee',outline=BLUE,width=2)
   for a,b in [(x-70,y+35),(x+65,y-35)]:d.ellipse((a-15,b-8,a+15,b+8),fill=GREEN)
  else:mito(d,x+40,y+20,.6)
def mito(d,x,y,s=1):
 d.ellipse((x-65*s,y-28*s,x+65*s,y+28*s),fill='#f8e0c3',outline=ORANGE,width=4)
 d.line([(x-45*s,y),(x-25*s,y-15*s),(x-5*s,y+15*s),(x+15*s,y-15*s),(x+35*s,y+15*s)],fill=ORANGE,width=3)
def icon(d,x,y,kind):
 if kind=='muscle':
  d.rounded_rectangle((x-95,y-35,x+95,y+35),radius=30,fill='#f2d3d8',outline='#a94e69',width=4)
  for xx in range(x-65,x+80,25):d.line((xx,y-25,xx,y+25),fill='#a94e69',width=3)
 elif kind=='sperm':
  d.ellipse((x-70,y-25,x-20,y+25),fill='#d5e2fa',outline=BLUE,width=4);d.line([(x-20,y),(x+20,y+20),(x+55,y-15),(x+100,y)],fill=BLUE,width=5)
 elif kind=='leaf':
  d.ellipse((x-75,y-35,x+75,y+35),fill='#d7ecd3',outline=GREEN,width=4);d.line((x-85,y,x+70,y),fill=GREEN,width=4)
  for xx in range(x-40,x+50,25):d.line((xx,y,xx+20,y-22),fill=GREEN,width=2)
 elif kind=='root':
  d.rounded_rectangle((x-60,y-30,x+45,y+30),radius=12,fill='#e4efcf',outline=GREEN,width=4);d.rectangle((x+43,y-10,x+125,y+10),fill='#e4efcf');d.line([(x+45,y-10),(x+125,y-10),(x+125,y+10),(x+45,y+10)],fill=GREEN,width=3)
 elif kind=='nerve':
  d.ellipse((x-85,y-25,x-35,y+25),fill='#e4d8f3',outline=PURPLE,width=3);d.line((x-35,y,x+90,y),fill=PURPLE,width=5)
  for dy in [-40,0,40]:d.line((x-60,y,x-110,y+dy),fill=PURPLE,width=3);d.line((x+90,y,x+120,y+dy),fill=PURPLE,width=3)
 elif kind=='lung':
  d.line((x,y-70,x,y),fill=BLUE,width=6)
  for dx in [-60,60]:d.ellipse((x+dx-45,y-20,x+dx+45,y+60),fill='#e1effb',outline=BLUE,width=4);d.line((x,y,x+dx,y),fill=BLUE,width=5)
 elif kind=='gill':
  d.line((x-60,y-65,x-60,y+65),fill=ORANGE,width=5)
  for dy in range(-50,60,20):d.line((x-60,y+dy,x+75,y+dy),fill=ORANGE,width=6)
