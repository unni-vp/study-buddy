from literature_helpers import ROOT,SUBJECT,TOPICS
from biology_topic_diagrams import text,arrow,save
f=ROOT/SUBJECT/TOPICS[1]/'Diagrams'
s=text(500,34,'One shared question; two different responses',26,'middle')
s+='<rect x="325" y="65" width="350" height="62" rx="12" fill="#fff1bb" stroke="#a38a38"/>'+text(500,104,'How does memory affect people?',21,'middle')
for x,title,a,b,col in [(25,'Wordsworth','Pleasure returns','Memory brings relief','#2166ad'),(555,'Remains','Violence returns','Memory brings distress','#7750a1')]:
 s+=f'<rect x="{x}" y="185" width="420" height="120" rx="12" fill="#f5f8fc" stroke="{col}"/>'+text(x+210,215,title,23,'middle')+text(x+210,254,a,21,'middle')+text(x+210,285,b,21,'middle')
 s+=arrow(f'M500 132L{x+210} 178')
s+=text(500,353,'Similar process: a past event enters the present',22,'middle')+text(500,395,'Different effect: restoration versus renewed suffering',22,'middle')
s+=text(500,444,'Compare the language and the ending to explain the difference.',20,'middle')
save(f,'comparison-argument','A comparison links Wordsworth and Remains through the different effects of returning memories',s,h=480)
