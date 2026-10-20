"""Generate the editable Huffman tree and verify the BANANA example."""
from collections import Counter
from pathlib import Path
from html import escape

ROOT=Path(__file__).resolve().parents[1] if Path(__file__).parent.name=='scripts' else Path('D:/Shreya/study-buddy')
WORD='BANANA'
FREQUENCIES=Counter(WORD)
TREE=('A',('B','N'))  # The two frequency-3 nodes may be placed either way.

def codes(node,prefix=''):
 if isinstance(node,str):return {node:prefix}
 return {**codes(node[0],prefix+'0'),**codes(node[1],prefix+'1')}

def example():
 mapping=codes(TREE);encoded=''.join(mapping[c] for c in WORD)
 assert all(not b.startswith(a) for x,a in mapping.items() for y,b in mapping.items() if x!=y)
 node=TREE;decoded=''
 for bit in encoded:
  node=node[int(bit)]
  if isinstance(node,str):decoded+=node;node=TREE
 assert decoded==WORD and node==TREE
 assert len(encoded)==sum(FREQUENCIES[c]*len(mapping[c]) for c in FREQUENCIES)==9
 return dict(word=WORD,frequencies=dict(FREQUENCIES),codes=mapping,encoded=encoded,message_bits=len(encoded),ascii_bits=len(WORD)*7,saved_bits=len(WORD)*7-len(encoded))

def draw():
 data=example();parts=[]
 def text(x,y,value,size=24,bold=False):
  parts.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" font-weight="{700 if bold else 400}">{escape(str(value))}</text>')
 def branch(x1,y1,x2,y2,bit):
  parts.append(f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="#243b64" stroke-width="3"/>')
  mx=(x1+x2)/2;my=(y1+y2)/2
  parts.append(f'<circle cx="{mx}" cy="{my}" r="18" fill="#fffefa"/>');text(mx,my+8,bit,bold=True)
 text(400,38,'Huffman tree for BANANA',28,True)
 branch(400,103,185,207,'0');branch(400,103,570,210,'1')
 branch(570,238,455,338,'0');branch(570,238,690,338,'1')
 for x,y,weight in [(400,90,6),(570,224,3)]:
  parts.append(f'<circle cx="{x}" cy="{y}" r="28" fill="#e4ebf4" stroke="#243b64" stroke-width="2"/>');text(x,y+8,weight,25,True)
 for x,y,symbol in [(185,249,'A'),(455,380,'B'),(690,380,'N')]:
  parts.append(f'<rect x="{x-65}" y="{y-42}" width="130" height="92" rx="10" fill="#e4f0e8" stroke="#477557" stroke-width="2"/>')
  text(x,y-4,f'{symbol}: {FREQUENCIES[symbol]}',24,True);text(x,y+32,'code '+data['codes'][symbol],22)
 text(155,365,'0 = left branch',22);text(155,400,'1 = right branch',22)
 description='Root frequency 6. Left branch 0 reaches A, frequency 3. Right branch 1 reaches the combined B and N node, frequency 3. Its left branch 0 reaches B, frequency 1; its right branch 1 reaches N, frequency 2. Codes: A 0, B 10, N 11.'
 out=ROOT/'Computer Science - AQA/03 - Fundamentals of data representation/Diagrams/huffman-banana.svg';out.parent.mkdir(exist_ok=True)
 out.write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" role="img" aria-labelledby="title desc"><title id="title">Huffman coding worked example: BANANA</title><desc id="desc">'+escape(description)+'</desc><rect width="800" height="450" fill="#fffefa"/><g font-family="Segoe UI, Arial, sans-serif" fill="#182c3b">'+''.join(parts)+'</g></svg>',encoding='utf-8')
 return data

if __name__=='__main__':
 import json
 print(json.dumps(draw(),ensure_ascii=False))
