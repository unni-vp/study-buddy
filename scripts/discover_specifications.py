import urllib.request, re, concurrent.futures
pages = {
 'Biology':'https://www.aqa.org.uk/subjects/biology/gcse/biology-8461/specification',
 'Chemistry':'https://www.aqa.org.uk/subjects/chemistry/gcse/chemistry-8462/specification',
 'Physics':'https://www.aqa.org.uk/subjects/physics/gcse/physics-8463/specification',
 'French':'https://www.aqa.org.uk/subjects/french/gcse/french-8652/specification',
 'Geography':'https://www.ocr.org.uk/qualifications/gcse/geography-a-geographical-themes-j383-from-2016/',
 'English Language':'https://www.eduqas.co.uk/qualifications/english-language-gcse/',
 'English Literature':'https://www.eduqas.co.uk/qualifications/english-literature-gcse/'}
def run(item):
 name,url=item
 try:
  html=urllib.request.urlopen(url,timeout=45).read().decode()
  links=list(dict.fromkeys(re.findall(r'(?:https://[^\s\"<>]+|/media/[^\s\"<>]+|/Images/[^\s\"<>]+)\.pdf',html,re.I)))
  return name,[x for x in links if 'spec' in x.lower() or 'cdn.sanity' in x.lower()]
 except Exception as e:return name,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:
 for row in ex.map(run,pages.items()):print(row)
