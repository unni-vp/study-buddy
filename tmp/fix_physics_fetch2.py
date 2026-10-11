from pathlib import Path
p=Path('tmp/fetch_physics_archive.py');s=p.read_text(encoding='utf-8');a=s.index('for paper in [1,2]:');b=s.index('def fetch(item):')
s=s[:a]+"for paper in [1,2]:\n for year in ['22','23']:\n  for kind in ['QP','MS']:\n   jobs.append((paper,year,kind,f'https://pmt.physicsandmathstutor.com/download/Physics/GCSE/Past-Papers/AQA/Paper-{paper}H/{kind}/June%2020{year}%20{kind}.PDF'))\n"+s[b:];p.write_text(s,encoding='utf-8')
