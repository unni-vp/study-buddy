import html, re

def inline(s):
 s=html.escape(s)
 s=re.sub(r'!\[([^\]]*)\]\(([^)]+)\)',r'<img src="\2" alt="\1">',s)
 s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
 s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
 s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
 return s

def render_md(text):
 out=[]; lines=text.splitlines(); i=0
 while i<len(lines):
  line=lines[i]
  if not line.strip():i+=1;continue
  if line.startswith('#'):
   n=len(line)-len(line.lstrip('#')); out.append(f'<h{n}>{inline(line[n:].strip())}</h{n}>');i+=1
  elif line.startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].startswith('|'):
    cells=[s.strip() for s in lines[i].strip('|').split('|')]
    if not all(re.fullmatch(r'[- :]+',s) for s in cells): rows.append(cells)
    i+=1
   out.append('<table>')
   for j,row in enumerate(rows):
    tag='th' if j==0 else 'td';out.append('<tr>'+''.join(f'<{tag}>{inline(s)}</{tag}>' for s in row)+'</tr>')
   out.append('</table>')
  elif line.startswith('- ') or re.match(r'^\d+\. ',line):
   numbered=bool(re.match(r'^\d+\. ',line)); tag='ol' if numbered else 'ul';out.append('<'+tag+'>')
   while i<len(lines) and (bool(re.match(r'^\d+\. ',lines[i])) if numbered else lines[i].startswith('- ')):
    content=re.sub(r'^\d+\. ','',lines[i]) if numbered else lines[i][2:]
    out.append('<li>'+inline(content)+'</li>');i+=1
   out.append('</'+tag+'>')
  else:
   para=[line];i+=1
   while i<len(lines) and lines[i].strip() and not re.match(r'^(#|\||- |\d+\. )',lines[i]):para.append(lines[i]);i+=1
   out.append('<p>'+inline(' '.join(para))+'</p>')
 return '\n'.join(out)

