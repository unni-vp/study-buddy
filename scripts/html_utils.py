import html, re

FENCE_RE = re.compile(r'^ {0,3}(`{3,}|~{3,})([^\r\n]*)$')


def fence_start(line):
 match=FENCE_RE.match(line)
 if match and not (match[1][0]=='`' and '`' in match[2]):return match
 return None


def fence_end(line, fence):
 return bool(re.fullmatch(r' {0,3}'+re.escape(fence[0])+'{'+str(len(fence))+r',}[ \t]*',line))


def _inline_text(s):
 s=html.escape(s)
 s=re.sub(r'!\[([^\]]*)\]\(([^)]+)\)',r'<img src="\2" alt="\1">',s)
 s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
 s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
 return s


def inline(s):
 # Keep Markdown-like operators, links and emphasis inside code literal.
 out=[];end=0
 for match in re.finditer(r'(?<!`)(`+)(?!`)(.+?)(?<!`)\1(?!`)',s):
  out.append(_inline_text(s[end:match.start()]))
  out.append('<code>'+html.escape(match[2])+'</code>')
  end=match.end()
 out.append(_inline_text(s[end:]))
 return ''.join(out)


def is_reference_heading(title):
 # Match bibliography labels only, never teaching headings such as Sources and bias.
 return bool(re.fullmatch(r'(?:sources(?: for .+)?|case-study sources|reference sources|references|past-paper sources|further reading)', title.strip(), re.I))


def is_revision_checklist_heading(title):
 return bool(re.fullmatch(r'(?:High[-– ]yield checklist|(?:.+ )?Exam pointers?)', title.strip(), re.I))


def render_md(text, *, hide_reference_sections=True):
 out=[]; lines=text.splitlines(); i=0
 while i<len(lines):
  line=lines[i]
  if not line.strip():i+=1;continue
  fence=fence_start(line)
  if fence:
   marker=fence[1];info=fence[2].strip();indent=len(line)-len(line.lstrip(' '));code=[];i+=1
   while i<len(lines) and not fence_end(lines[i],marker):
    value=lines[i]
    # Only the fence's own indentation is removed; Python indentation remains.
    removed=min(indent,len(value)-len(value.lstrip(' ')))
    code.append(value[removed:]);i+=1
   if i<len(lines):i+=1
   language=info.split()[0] if info else ''
   attr=' class="language-'+html.escape(language,quote=True)+'"' if re.fullmatch(r'[A-Za-z0-9_+-]+',language) else ''
   body='\n'.join(code)+('\n' if code else '')
   out.append('<pre class="code-block"><code'+attr+'>'+html.escape(body)+'</code></pre>')
  elif line.strip()=='---':
   out.append('<hr>');i+=1
  elif line.startswith('**Themes:** '):
   tags=[tag.strip() for tag in line[len('**Themes:** '):].split(' · ') if tag.strip()]
   out.append('<div class="poem-theme-tags" role="group" aria-label="Poem themes"><span class="poem-theme-label">Themes:</span>'+''.join('<span class="poem-theme-tag">'+html.escape(tag)+'</span>' for tag in tags)+'</div>');i+=1
  elif line.startswith('#'):
   n=len(line)-len(line.lstrip('#')); title=line[n:].strip()
   if hide_reference_sections and n >= 2 and (is_reference_heading(title) or is_revision_checklist_heading(title)):
    # Keep tracking sections in HTML without a visible heading or toggle.
    end=i+1;active_fence=None
    while end<len(lines):
     value=lines[end]
     if active_fence:
      if fence_end(value,active_fence):active_fence=None
     else:
      opening=fence_start(value)
      if opening:active_fence=opening[1]
      else:
       heading=re.match(r'^(#{1,6}) ',value)
       if heading and len(heading[1])<=n:break
     end+=1
    body=render_md('\n'.join(lines[i:end]),hide_reference_sections=False)
    kind="reference-sources" if is_reference_heading(title) else "revision-checklist"
    out.append('<section class="'+kind+'" hidden>'+body+'</section>');i=end
   else:
    out.append(f'<h{n}>{inline(title)}</h{n}>');i+=1
  elif line.startswith('>'):
   quote=[]
   while i<len(lines) and lines[i].startswith('>'):
    quote.append(inline(lines[i][1:].lstrip().rstrip()));i+=1
   out.append('<blockquote class="verse-extract">'+'<br>'.join(quote)+'</blockquote>')
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
   while i<len(lines) and lines[i].strip() and not fence_start(lines[i]) and not re.match(r'^(#|>|\||- |\d+\. )',lines[i]):para.append(lines[i]);i+=1
   out.append('<p>'+inline(' '.join(para))+'</p>')
 return '\n'.join(out)
