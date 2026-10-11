from pathlib import Path
p=Path('scripts/qa_navigation.py');s=p.read_text();s=s.replace('from urllib.parse import unquote','from urllib.parse import unquote, urlsplit, urlunsplit')
s=s.replace("            return match[1]+'=\"'+link(page, (source.parent/unquote(url)).resolve())+'\"'","            parts = urlsplit(url)\n            relocated = link(page, (source.parent/unquote(parts.path)).resolve())\n            return match[1]+'=\"'+urlunsplit(('', '', relocated, parts.query, parts.fragment))+'\"'")
p.write_text(s)
