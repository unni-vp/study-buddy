"""Find question/mark-scheme pairs; extracted text is a reading aid, not the figures."""
from pathlib import Path
import re
import sys

D = Path(__file__).resolve().parents[1] / 'Biology - AQA' / '00 - Past papers' / 'Paper 1 Higher'
for year in sys.argv[1:]:
    raw=(D/f'AQA-84611H-MS-JUN{year}.txt').read_text(encoding='utf-8')
    parts=re.split(r'(?m)^\s*(0\d\.\d+)\s*\n',raw)
    print('\nYEAR',year)
    for i in range(1,len(parts),2):
        body=parts[i+1]
        if '4.1.' in body:
            print('\nQUESTION',parts[i],re.sub(r'\n\s*\n','\n',body).strip())
