from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
maps=list(Path('Physics - AQA').glob('*/Mind Maps/*.png'))
for i in range(0,len(maps),4):
 batch=maps[i:i+4];sheet=Image.new('RGB',(1600,1140),'white');d=ImageDraw.Draw(sheet)
 for j,p in enumerate(batch):
  im=Image.open(p).convert('RGB');im.thumbnail((795,530));x=(j%2)*800;y=(j//2)*570
  sheet.paste(im,(x,y+25));d.text((x+5,y+5),p.stem,fill='black')
 sheet.save(f'tmp/physics-contact-{i//4}.png')
