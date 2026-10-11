from pathlib import Path
import json
root=Path('.')
p=root/'scripts/physics_diagrams.py'
s=p.read_text(encoding='utf-8-sig')
s=s.replace("if __name__=='__main__':\n import sys\n globals()[{'1':'energy'}[sys.argv[1]]]()\n",'')
start=s.index(" b=text(35,40,'Two components, one resultant',26)",s.index('def forces():'))
end=s.index(" b=text(35,35,'Two components, one resultant',26)",start)
s=s[:start]+s[end:]
pos=s.index(" b+=text(300,291,'½ × 4 × 8 = 16 m'")
s=s[:pos]+" save(5,'velocity-time-question','Velocity increases from 0 to 8 m/s in 4 seconds, then remains constant until 7 seconds.',b,h=435)\n"+s[pos:]
s+="\nif __name__=='__main__':\n import sys\n [energy,electricity,particles,atoms,forces][int(sys.argv[1])-1]()\n"
p.write_text(s,encoding='utf-8')
p=root/'scripts/physics_05_qa.py';s=p.read_text(encoding='utf-8-sig').replace('../Diagrams/velocity-time.svg','../Diagrams/velocity-time-question.svg');p.write_text(s,encoding='utf-8')
p=root/'Physics - AQA/00 - Past papers/download-sources.json';d=json.loads(p.read_text(encoding='utf-8-sig'))
for row in d:
 if row[:3]==[2,'23','QP']:row[3]=row[3].replace('.PDF','.pdf')
p.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
