from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json

ROOT=Path(__file__).resolve().parents[1]
failures=[]
class Links(HTMLParser):
 def __init__(self,page):super().__init__();self.page=page
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  for key in ['href','src']:
   if key not in d:continue
   url=d[key];parts=urlsplit(url)
   if parts.scheme or not parts.path:continue
   target=(self.page.parent/unquote(parts.path)).resolve()
   if not target.exists():failures.append((str(self.page.relative_to(ROOT)),url))
pages=[ROOT/'index.html']+list(ROOT.glob('* - */index.html'))+list(ROOT.glob('* - */[0-9][0-9] - */index.html'))+list((ROOT/'library'/'resources').glob('*.html'))
for page in pages:Links(page).feed(page.read_text(encoding='utf-8'))
config=json.loads((ROOT/'project-config.json').read_text())
for name,subject in config['subjects'].items():
 for i,t in enumerate(subject['topics'],1):
  folder=ROOT/name/f'{i:02d} - {t["title"]}'
  assert (folder/'Questions and Answers').is_dir()
  assert not (folder/'Exam Questions').exists()
  assert not (folder/'Answers and Marking Points').exists()
assert not failures,failures
print(f'PASS: {len(pages)} HTML pages checked; all local links resolve; all 73 topics use combined Q&A folders.')
