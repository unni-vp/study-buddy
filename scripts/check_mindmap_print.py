"""Check actual browser print output after check_mindmap_print.cjs."""
from pathlib import Path
from collections import Counter
from pypdf import PdfReader, PdfWriter
import pdfplumber
import pypdfium2 as pdfium

folder = Path('tmp/pdfs')
writer = PdfWriter()
readers = sorted(folder.glob('*-reader.pdf'))
assert len(readers) == 7, 'Expected one reader proof for each map'
for reader in readers:
    texts=[]
    for source in (reader, reader.with_name(reader.name.replace('-reader','-modal'))):
        pdf=PdfReader(source)
        assert len(pdf.pages)==1, f'{source}: must be one page'
        page=pdf.pages[0]
        assert abs(float(page.mediabox.width)*25.4/72-297)<0.5
        assert abs(float(page.mediabox.height)*25.4/72-210)<0.5
        with pdfplumber.open(source) as doc:
            p=doc.pages[0]
            sizes=Counter(round(c['size'],2) for c in p.chars)
            assert sizes and min(sizes)>=10, (source,sizes)
            assert sizes.most_common(1)[0][0]>=11, (source,'body text smaller than 11 pt')
            assert all(27<=c['x0']<=c['x1']<=p.width-27 and 27<=c['top']<=c['bottom']<=p.height-27 for c in p.chars), f'{source}: text outside print margins'
            texts.append(p.extract_text())
        rendered=pdfium.PdfDocument(source)
        rendered[0].render(scale=1.5).to_pil().save(source.with_suffix('.png'))
        rendered.close()
    assert texts[0]==texts[1], f'{reader}: modal content differs or duplicates underlying page'
    writer.add_page(page)
    print(f'PASS {reader.stem}: reader/modal match; one A4 landscape page; body {sizes.most_common(1)[0][0]} pt, smallest label {min(sizes)} pt')
writer.write(folder/'a4-print-proof.pdf')
