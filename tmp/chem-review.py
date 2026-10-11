from PIL import Image,ImageOps,ImageDraw
from pathlib import Path
files=sorted(Path('Chemistry - AQA/02 - Bonding structure and properties of matter/Mind Maps').glob('*.png'))
out=Image.new('RGB',(2240,1600),'#ddd')
for i,f in enumerate(files):
 im=Image.open(f).convert('RGB');im.thumbnail((1120,768));out.paste(im,((i%2)*1120,(i//2)*800))
out.save('tmp/chem-bonding-review.png')
