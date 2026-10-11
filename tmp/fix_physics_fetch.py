from pathlib import Path
p=Path('tmp/fetch_physics_archive.py');s=p.read_text(encoding='utf-8-sig').replace('from bs4 import BeautifulSoup','import re,html')
s=s.replace("soup=BeautifulSoup(urllib.request.urlopen(url).read(),'html.parser')\n for a in soup.find_all('a',href=True):\n  href=a['href'];label=a.get_text(' ',strip=True)","page=urllib.request.urlopen(url).read().decode()\n for raw in re.findall(r'href=[\"\\\']([^\"\\\']+)',page):\n  href=html.unescape(raw)")
p.write_text(s,encoding='utf-8')
