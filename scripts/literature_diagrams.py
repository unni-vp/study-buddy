from literature_helpers import ROOT,SUBJECT,TOPICS
from biology_topic_diagrams import text,arrow,save

def macbeth():
 f=ROOT/SUBJECT/TOPICS[0]/'Diagrams';s=text(500,35,'Power grows; the partnership breaks',27,'middle')
 rows=[(100,'Macbeth','#e7f0fb',[('Act 1','Hesitates; knows','murder is wrong'),('Act 2','Kills Duncan;','fears discovery'),('Act 3','Plans more murder;','keeps his wife out'),('Acts 4–5','Acts as a tyrant;','ends isolated')]),(290,'Lady Macbeth','#f5e7ee',[('Act 1','Directs the plot;','challenges Macbeth'),('Act 2','Returns daggers;','dismisses guilt'),('Act 3','Excluded from plans;','manages the banquet'),('Act 5','Sleepwalks; cannot','escape imagined blood')])]
 for y,label,fill,boxes in rows:
  s+=text(20,y-20,label,24)
  for i,(act,a,b) in enumerate(boxes):
   x=10+i*250;s+=f'<rect x="{x}" y="{y}" width="230" height="115" rx="12" fill="{fill}" stroke="#587285"/>'+text(x+115,y+29,act,22,'middle')+text(x+115,y+66,a,18,'middle')+text(x+115,y+93,b,18,'middle')
   if i<3:s+=arrow(f'M{x+235} {y+57}H{x+246}')
 s+=text(500,453,'Shared ambition → hidden plans → isolation',23,'middle')
 save(f,'changing-partnership','Parallel changes in Macbeth and Lady Macbeth across the play',s,h=480)
if __name__=='__main__':macbeth()
