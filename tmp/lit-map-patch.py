from pathlib import Path
p=Path('scripts/build_literature_maps.py');s=p.read_text(encoding='utf-8-sig').replace('import a4_mindmaps as a4','import a4_mindmaps as a4\nimport literature_map_figures');p.write_text(s,encoding='utf-8')
p=Path('scripts/literature_maps.py');s=p.read_text(encoding='utf-8-sig');s+='\nfor item, panel, kind, height in [(MAPS[1][0],1,"lit-downfall",125),(MAPS[1][1],2,"lit-partnership",95),(MAPS[1][2],2,"lit-guilt",95),(MAPS[1][3],0,"lit-irony",110),(MAPS[1][4],0,"lit-irony",110)]:\n item["pics"][panel]=(kind,height)\n';p.write_text(s,encoding='utf-8')
