"""Use the approved readable Biology panel layout for other subjects."""
from pathlib import Path
from datetime import date
import json,re,subprocess
from copy import deepcopy
from biology_readable_mindmaps import build_map,prepare_panels,plain,group
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
 ('English Literature - Eduqas',1,'00-macbeth-overview'):{1:('lit-downfall',2)},
 ('English Literature - Eduqas',1,'01-characters-and-relationships'):{2:('lit-partnership',2)},
 ('English Literature - Eduqas',1,'02-power-and-guilt'):{3:('lit-guilt',2)},
 ('English Literature - Eduqas',1,'03-deception-and-gender'):{0:('lit-irony',1)},
 ('English Literature - Eduqas',1,'04-drama-and-exam-writing'):{0:('lit-irony',1)},
 ('English Literature - Eduqas',2,'00-anthology-overview'):{5:('lit-camera',1)},
 ('English Literature - Eduqas',2,'01-nature-and-childhood'):{5:('lit-nature',1)},
 ('English Literature - Eduqas',2,'02-love-and-absence'):{5:('lit-absence',1)},
 ('English Literature - Eduqas',2,'03-family-and-identity'):{2:('lit-bond',1)},
 ('English Literature - Eduqas',2,'04-war-and-exclusion'):{4:('lit-return',1)},
 ('English Literature - Eduqas',2,'05-witnessing-and-trauma'):{2:('lit-camera',1)},
 ('English Literature - Eduqas',2,'06-home-and-belonging'):{0:('lit-home',1)},
 ('Physics - AQA',1,'00-energy-overview'):{2:('ph-energy',1)},
 ('Physics - AQA',1,'01-energy-stores-and-calculations'):{3:('ph-spring',1)},
 ('Physics - AQA',1,'02-heating-and-practicals'):{0:('ph-specific',1)},
 ('Physics - AQA',2,'00-electricity-overview'):{5:('ph-field',1)},
 ('Physics - AQA',2,'01-circuits-and-components'):{3:('ph-circuit',1)},
 ('Physics - AQA',2,'02-circuit-investigations'):{3:('ph-circuit',1)},
 ('Physics - AQA',2,'03-power-mains-and-fields'):{4:('ph-field',1)},
 ('Physics - AQA',3,'00-particle-model-overview'):{0:('ph-particles',1)},
 ('Physics - AQA',3,'01-states-and-density'):{0:('ph-particles',1)},
 ('Physics - AQA',3,'02-heating-and-gas-pressure'):{2:('ph-heat',1)},
 ('Physics - AQA',4,'00-atomic-structure-overview'):{3:('ph-half-life',1)},
 ('Physics - AQA',4,'01-atoms-and-nuclear-equations'):{2:('ph-scatter',1)},
 ('Physics - AQA',4,'02-radiation-and-half-life'):{2:('ph-half-life',1)},
 ('Physics - AQA',5,'00-forces-overview'):{3:('ph-motion',1)},
 ('Physics - AQA',5,'01-interactions-work-and-springs'):{5:('ph-spring',1)},
 ('Physics - AQA',5,'02-moments-and-fluid-pressure'):{0:('ph-lever',1)},
 ('Physics - AQA',5,'03-motion-and-graphs'):{5:('ph-motion',1)},
 ('Physics - AQA',5,'04-newtons-laws-and-practical'):{2:('ph-terminal',1)},
}
COLUMNS={
 ('Chemistry - AQA',4,'03-titration'):[[0,3],[1,4],[2,5]],
}

def colon_labels(value):
    # Bold a short leading label together with its colon. Leave full sentences alone.
    match=re.match(r'^([^:*]{1,42}):\s+(.*)$',value)
    if match and '. ' not in match[1] and len(match[1].split())<=6:return '**'+match[1]+':** '+match[2]
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
            if subject!='Chemistry - AQA':panel['text_reserve']=12
            if panel['title'] in ('Evidence → decision','Charge → formula'):
                panel['title']=panel['title'].replace(' → ',' & ')
            for g in panel['groups']:g['lines']=[colon_labels(clarify_associations(t)) for t in g['lines']]
        key=(subject,n,item['slug'])
        if key==('English Literature - Eduqas',1,'00-macbeth-overview'):
            source[0]['groups']=[group(
                '**Act 1:** prophecy and choice.',
                '**Act 2:** Duncan murdered. Macbeth crowned.',
                '**Act 3:** Banquo killed. Fleance escapes. Ghost at banquet.',
                '**Act 4:** misleading assurances. Macduff’s family killed.',
                '**Act 5:** Lady Macbeth dies. Resistance defeats Macbeth. Malcolm restores rule.')]
        if key==('Physics - AQA',5,'03-motion-and-graphs'):
            source[1]['groups'][0]['lines']=[
                '**Walking:** about 1.5 m/s.', '**Running:** about 3 m/s.',
                '**Cycling:** about 6 m/s.', '**Sound in air:** about 330 m/s.',
                'Conditions change these estimates.']
            source[3]['groups'][0]['lines']=[
                '**v²−u² = 2as** only for constant acceleration.',
                'From rest, a = 2 m/s² over 25 m gives v = 10 m/s.']
        if key==('Chemistry - AQA',4,'03-titration'):
            source[1]['groups'][2]['lines']=['Water left in the burette dilutes the acid.','This changes its concentration.']
        for index,(kind,after) in VISUALS.get(key,{}).items():
            source[index]['visual']={'kind':kind,'after':after}
        svg,record=build_map(item['title'],item['slug'],source,columns=COLUMNS.get(key),drawing_provider=drawing,purpose_provider=PURPOSES,apply_biology_visuals=False)
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
