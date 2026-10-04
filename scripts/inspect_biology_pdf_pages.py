"""Print selected page text, or render selected source pages for visual inspection."""
from pathlib import Path
import sys
import pypdfium2 as pdfium
from PIL import Image, ImageDraw
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
folder=ROOT/'Biology - AQA'/'00 - Past papers'/'Paper 1 Higher'
year,kind=sys.argv[1:3]
pages=[int(p) for p in sys.argv[3].split(',')]
source=folder/f'AQA-84611H-{kind}-JUN{year}.pdf'
if '--render' not in sys.argv:
    reader=PdfReader(source)
    for n in pages: print(f'\nPAGE {n}\n'+reader.pages[n-1].extract_text())
else:
    dest=ROOT/'tmp'/'biology-paper-review'
    dest.mkdir(parents=True,exist_ok=True)
    pdf=pdfium.PdfDocument(source)
    thumbs=[]
    for n in pages:
        picture=pdf[n-1].render(scale=1.6).to_pil().convert('RGB')
        picture.save(dest/f'{year}-{kind}-{n}.png')
        picture.thumbnail((570,820))
        thumb=Image.new('RGB',(590,860),'#edf2f8')
        ImageDraw.Draw(thumb).text((12,10),f'June 20{year} {kind} - PDF page {n}',fill='#12223c')
        thumb.paste(picture,(10,35))
        thumbs.append(thumb)
    for start in range(0,len(thumbs),4):
        batch=thumbs[start:start+4]
        sheet=Image.new('RGB',(1180,860*((len(batch)+1)//2)),'white')
        for i,t in enumerate(batch):sheet.paste(t,((i%2)*590,(i//2)*860))
        target=dest/f'{year}-{kind}-sheet-{start//4+1}.png'
        sheet.save(target)
        print(target)
