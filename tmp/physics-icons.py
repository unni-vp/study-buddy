from pathlib import Path
p=Path('scripts/physics_map_figures.py');s=p.read_text(encoding='utf-8');a=s.index(" if kind=='ph-circuit':");b=s.index("  b=line(f'M20 34V12H65",a);s=s[:a]+" if kind=='ph-circuit':\n"+s[b:];p.write_text(s,encoding='utf-8')
p=Path('scripts/physics_maps.py');s=p.read_text(encoding='utf-8').replace(",3:(0,'ph-scatter',115)",'').replace("# Scattering illustrates the atom-model map only, not exposure routes.\nFIGURES[4].pop(3)\n",'');p.write_text(s,encoding='utf-8')
p=Path('scripts/mindmap_navigation.py');s=p.read_text(encoding='utf-8');s=s.replace("    if 'literature-book' in slug:",'''    if slug.startswith('physics-'):
        if 'heat' in slug:
            body='<path d="M75 85V25a15 15 0 0 1 30 0v60a28 28 0 1 1-30 0Z" fill="#fbe6d3" stroke="#bf7030" stroke-width="4"/><path d="M90 35v70" stroke="#bf7030" stroke-width="9"/><path d="M116 40h18m-18 20h12" stroke="#bf7030" stroke-width="3"/>'
        elif 'circuit' in slug:
            body='<path d="M25 55V25h130v90H25V75M10 55h30M17 75h16" stroke="#276cad" stroke-width="4"/><rect x="67" y="15" width="47" height="20" fill="#e7f0fb" stroke="#276cad" stroke-width="4"/><circle cx="90" cy="115" r="19" fill="#fff" stroke="#276cad" stroke-width="4"/><path d="m78 103 24 24m-24 0 24-24" stroke="#bf7030" stroke-width="3"/>'
        elif 'atom' in slug:
            body='<ellipse cx="90" cy="70" rx="70" ry="35" stroke="#276cad" stroke-width="3"/><ellipse cx="90" cy="70" rx="35" ry="60" stroke="#276cad" stroke-width="3"/><circle cx="90" cy="70" r="17" fill="#f8e0c3" stroke="#bf7030" stroke-width="3"/><circle cx="160" cy="70" r="7" fill="#276cad"/><circle cx="90" cy="10" r="7" fill="#276cad"/>'
        elif 'particles' in slug:
            body='<rect x="15" y="15" width="150" height="110" rx="8" fill="#e7f0fb" stroke="#276cad" stroke-width="3"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="9" fill="#276cad"/>' for x,y in [(35,35),(83,29),(140,42),(55,76),(123,88),(40,107)])
        elif 'motion' in slug:
            body='<path d="M25 20v100h135" stroke="#425968" stroke-width="4"/><path d="M27 117 90 45h60" stroke="#276cad" stroke-width="7"/>'
        elif 'forces' in slug:
            body='<rect x="60" y="40" width="60" height="60" rx="8" fill="#e7f0fb" stroke="#276cad" stroke-width="3"/><path d="M65 70H10m15-12L10 70l15 12m90-12h55m-15-12 15 12-15 12" stroke="#25826c" stroke-width="5"/>'
        else:
            body='<path d="M95 10 40 80h43l-5 50 63-77H98Z" fill="#f4d471" stroke="#bf7030" stroke-width="4"/>'
    elif 'literature-book' in slug:''');p.write_text(s,encoding='utf-8')
