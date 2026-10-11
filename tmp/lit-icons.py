from pathlib import Path
p=Path('scripts/mindmap_navigation.py');s=p.read_text();s=s.replace("    if 'cell-process' in slug:",'''    if 'literature-book' in slug:
        body='<path d="M90 30C65 15 35 15 15 25v92c25-8 50-5 75 10 25-15 50-18 75-10V25c-20-10-50-10-75 5Z" fill="#e7f0fb" stroke="#276cad" stroke-width="4"/><path d="M90 30v97M30 45h40M30 65h40m40-20h40m-40 20h40" stroke="#276cad" stroke-width="3"/>'
    elif 'literature-drama' in slug:
        body='<path d="M22 20h75v65c-15 37-60 37-75 0Z" fill="#e7f0fb" stroke="#276cad" stroke-width="4"/><path d="M85 35h75v60c-15 35-60 35-75 0Z" fill="#f8e0c3" stroke="#bf7030" stroke-width="4"/><path d="M38 45h12m19 0h12M36 80q24 30 47 0M100 61h12m17 0h12M99 108q22-27 47 0" stroke="#425968" stroke-width="4"/>'
    elif 'literature-pen' in slug:
        body='<rect x="28" y="14" width="104" height="115" rx="9" fill="#e7f0fb" stroke="#276cad" stroke-width="4"/><path d="M45 42h55M45 65h55M45 88h30m12 12 52-66 18 14-52 66-25 7Z" fill="#f8e0c3" stroke="#bf7030" stroke-width="4"/>'
    elif 'cell-process' in slug:''');p.write_text(s,encoding='utf-8')
