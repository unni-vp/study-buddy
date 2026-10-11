from pathlib import Path
p=Path('scripts/html_utils.py');s=p.read_text();needle="  elif line.startswith('|'):";new="""  elif line.startswith('>'):
   quote=[]
   while i<len(lines) and lines[i].startswith('>'):
    quote.append(inline(lines[i][1:].lstrip().rstrip()));i+=1
   out.append('<blockquote class="verse-extract">'+'<br>'.join(quote)+'</blockquote>')
""";s=s.replace(needle,new+needle).replace("r'^(#|\\||- |\\d+\\. )'","r'^(#|>|\\||- |\\d+\\. )'");p.write_text(s)
p=Path('scripts/literature_qa_writer.py');s=p.read_text(encoding='utf-8-sig').replace('gcse-english-literature/wjec-eduqas/','gcse-english-literature/');p.write_text(s,encoding='utf-8')
p=Path('AGENTS.md');s=p.read_text(encoding='utf-8');s+='\n- Literature extracts must preserve verse line breaks and speaker labels in HTML as well as Markdown. Check displayed passages visually; never flatten verse into a paragraph. Use the current Eduqas anthology for 2027 (15 poems), not the previous anthology. Shakespeare and poetry assessment objectives differ: verify against the specification, and keep source/evidence notes separate from student answers.\n';p.write_text(s,encoding='utf-8')
