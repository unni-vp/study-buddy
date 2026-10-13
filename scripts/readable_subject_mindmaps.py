"""Use the approved readable Biology panel layout for other subjects."""
from pathlib import Path
from datetime import date
import json,re,subprocess
from copy import deepcopy
from biology_readable_mindmaps import build_map,prepare_panels,plain
from subject_explanatory_figures import drawing,PURPOSES

ROOT=Path(__file__).resolve().parents[1]

# Diagrams are selected for an explicit explanatory purpose, not one per panel.
VISUALS={
 ('Chemistry - AQA',1,'01-atoms-isotopes-and-models'):{3:('chem-ion',1)},
 ('Chemistry - AQA',2,'00-bonding-overview'):{0:('chem-pairs',1)},
 ('Chemistry - AQA',2,'01-ionic-and-covalent-bonds'):{2:('chem-lattice',1)},
 ('Chemistry - AQA',2,'02-structures-and-states'):{3:('chem-alloy',1)},
 ('Chemistry - AQA',2,'03-carbon-and-nanoparticles'):{1:('chem-graphite',2)},
 ('Chemistry - AQA',3,'01-moles-and-reacting-masses'):{4:('chem-limiting',2)},
 ('Chemistry - AQA',4,'00-chemical-changes-overview'):{4:('chem-electrodes',2)},
 ('Chemistry - AQA',4,'03-titration'):{1:('chem-titration',2)},
 ('Chemistry - AQA',4,'04-electrolysis'):{0:('chem-electrodes',1)},
 ('Chemistry - AQA',5,'00-energy-changes-overview'):{1:('chem-profile',1)},
 ('Chemistry - AQA',5,'01-profiles-and-bond-energies'):{3:('chem-profiles',2)},
}

def colon_labels(value):
    # Bold a short leading label together with its colon. Leave full sentences alone.
    match=re.match(r'^([^:*]{1,42}):\s+(.*)$',value)
    if match and len(match[1].split())<=6:return '**'+match[1]+':** '+match[2]
    return value

def clarify_associations(value):
    for old,new in {
        'Insoluble solid → filtration':'Insoluble solid: filtration',
        'Dissolved solid → crystallisation':'Dissolved solid: crystallisation',
        'Solvent → simple distillation':'Solvent: simple distillation',
        'Miscible liquids → fractional distillation':'Miscible liquids: fractional distillation',
        'Dyes → chromatography':'Dyes: chromatography',
        'Same main group → same outer electrons':'Same main group: same outer electrons',
        'period → occupied shells':'period: occupied shells',
        'Scattering evidence → tiny positive nucleus':'Scattering evidence: tiny positive nucleus',
        'HCl → chlorides':'HCl: chlorides','H₂SO₄ → sulfates':'H₂SO₄: sulfates','HNO₃ → nitrates':'HNO₃: nitrates',
    }.items():value=value.replace(old,new)
    return value

def build(subject,topics,maps,n):
    topic=ROOT/subject/topics[n-1];folder=topic/'Mind Maps';paths=[];records=[]
    for item in maps[n]:
        source=prepare_panels(item['panels'])
        for panel in source:
            if panel['title'] in ('Evidence → decision','Charge → formula'):
                panel['title']=panel['title'].replace(' → ',' & ')
            for g in panel['groups']:g['lines']=[colon_labels(clarify_associations(t)) for t in g['lines']]
        key=(subject,n,item['slug'])
        for index,(kind,after) in VISUALS.get(key,{}).items():
            source[index]['visual']={'kind':kind,'after':after}
        svg,record=build_map(item['title'],item['slug'],source,drawing_provider=drawing,purpose_provider=PURPOSES,apply_biology_visuals=False)
        target=folder/(item['slug']+'.svg');target.write_text(svg,encoding='utf-8');paths.append(str(target))
        record['slug']=item['slug'];record['title']=item['title'];record['source_panels_preserved']=len(source);records.append(record)
    node=Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe'
    subprocess.run([str(node),str(ROOT/'scripts/render_mindmap_previews.cjs'),*paths],cwd=ROOT,check=True)
    (topic/'mindmap-layout-review.json').write_text(json.dumps({
        'reviewed':date.today().isoformat(),'generator':'scripts/readable_subject_mindmaps.py',
        'style':'Content-sized panels; no central hub; black body text; bold colon labels; consistent coloured headings; light inset dividers; compact gutters',
        'print':{'orientation':'A4 landscape','width_mm':277,'body_pt':11.21,'minimum_diagram_label_pt':11.21},
        'full_text':'Existing complete Markdown counterparts retained unchanged',
        'maps':records},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Built',subject,topics[n-1],len(records),'readable maps')
