from pathlib import Path
from PIL import Image,ImageDraw
files=[Path('tmp')/f for f in ['01-energy-budget.svg.png','02-iv-graphs.svg.png','03-heating-curve.svg.png','04-half-life.svg.png','04-fission-fusion.svg.png','05-force-components.svg.png','05-velocity-time.svg.png']]
for i in range(0,len(files),4):
 sheet=Image.new('RGB',(1500,1150),'white');d=ImageDraw.Draw(sheet)
 for j,p in enumerate(files[i:i+4]):
  im=Image.open(p).convert('RGB');im.thumbnail((740,530));x=(j%2)*750;y=(j//2)*575;sheet.paste(im,(x,y+25));d.text((x+5,y+5),p.stem,fill='black')
 sheet.save(f'tmp/physics-diagrams-{i//4}.png')
files=list(Path('tmp/pdfs').glob('*-reader.png'))
names={p.stem for p in Path('Physics - AQA').glob('*/Mind Maps/*.svg')}
files=[p for p in files if p.stem.removesuffix('-reader') in names]
for i in range(0,len(files),4):
 sheet=Image.new('RGB',(1600,1140),'white')
 for j,p in enumerate(files[i:i+4]):
  im=Image.open(p).convert('RGB');im.thumbnail((800,570));sheet.paste(im,((j%2)*800,(j//2)*570))
 sheet.save(f'tmp/physics-print-{i//4}.png')
