from pathlib import Path
p=Path('scripts/check_literature_content.py');s=p.read_text(encoding='utf-8-sig').replace('import fitz','from pypdf import PdfReader').replace('pdf=fitz.open(','pdf=PdfReader(').replace('len(pdf)','len(pdf.pages)').replace('pdf[page-1].get_text()','pdf.pages[page-1].extract_text()');p.write_text(s,encoding='utf-8')
