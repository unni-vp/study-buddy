"""Rebuild science mind maps without rewriting notes, Q&A or flash cards."""
from pathlib import Path
import importlib,json,os,re,subprocess,sys
from science_equation_layout import format_markdown

ROOT=Path(__file__).resolve().parents[1]

def build(subject,number):
    folder=next((ROOT/(subject+' - AQA')).glob(f'{number:02d} - *'))
    originals={p.name:p.read_text(encoding='utf-8-sig') for p in (folder/'Mind Maps').glob('*.md')}
    try:
        if subject=='Physics' and number<=5:
            from build_physics_maps import build as render
            render(number)
        elif subject=='Chemistry' and number<=5:
            from build_chemistry_maps import build as render
            render(number)
        elif subject=='Biology' and number==1:
            from cell_biology_mindmaps import build_maps
            build_maps()
        elif subject=='Biology' and number<=4:
            from build_biology_topic_maps import build as render
            render(folder.name)
        else:
            module=importlib.import_module(f'{subject.lower()}_{number:02d}_resources')
            maps=getattr(module,'MAPS',None)
            if maps is None:maps=importlib.import_module(f'{subject.lower()}_{number:02d}_practice').MAPS
            from science_completion import drawing,PURPOSES
            from subject_explanatory_figures import PURPOSES as existing_purposes
            from biology_readable_mindmaps import prepare_panels,build_map
            paths=[];records=[]
            for item in maps:
                panels=prepare_panels(item['panels'])
                for panel,source in zip(panels,item['panels']):
                    panel['text_reserve']=12
                    groups=panel['groups']
                    panel['groups']=[dict(lines=[line for g in groups[i:i+2] for line in g['lines']]) for i in range(0,len(groups),2)]
                    if source.get('visual'):panel['visual']={**source['visual'],'after':source['visual']['after']//2}
                svg,record=build_map(item['title'],item['slug'],panels,columns=item.get('columns'),drawing_provider=drawing,purpose_provider={**existing_purposes,**PURPOSES},apply_biology_visuals=False)
                target=folder/'Mind Maps'/(item['slug']+'.svg');target.write_text(svg,encoding='utf-8');paths.append(str(target))
                text=['# '+item['title']]
                for panel in item['panels']:text.extend(['## '+panel['title'],*panel['lines']])
                target.with_suffix('.md').write_text(format_markdown('\n\n'.join(text)),encoding='utf-8')
                record.update(slug=item['slug'],title=item['title']);records.append(record)
            env=os.environ.copy();env['TEMP']=str(ROOT/'tmp/browser-temp');env['TMP']=env['TEMP']
            node=Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe'
            subprocess.run([str(node),str(ROOT/'scripts/render_mindmap_previews.cjs'),*paths],cwd=ROOT,env=env,check=True)
            review=folder/'mindmap-layout-review.json';data=json.loads(review.read_text(encoding='utf-8-sig'));data['maps']=records
            review.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    except BaseException:
        # A failed layout must not replace the complete written counterparts.
        for name,content in originals.items():
            (folder/'Mind Maps'/name).write_text(content,encoding='utf-8')
        raise
    for path in (folder/'Mind Maps').glob('*.md'):
        old=path.read_text(encoding='utf-8-sig');new=format_markdown(originals.get(path.name,old))
        original=originals.get(path.name,old)
        assert len(re.split(r'\n\s*\n',new.strip()))>=len(re.split(r'\n\s*\n',original.strip())), 'Paragraph breaks lost: '+str(path)
        if new!=old:path.write_text(new,encoding='utf-8')
    review=folder/'mindmap-layout-review.json'
    data=json.loads(review.read_text(encoding='utf-8-sig')) if review.exists() else {}
    data['full_text']='Complete written content, paragraph breaks and lists retained; independent equations and conversions formatted on separate lines.'
    data['equation_layout_review']={'reviewed':'2026-10-19','scope':'Separate independent equations and conversions, retain numerical worked equality chains, keep matching readable text counterparts.','font_policy':'Fixed 11.21 pt body text at 277 mm A4 width; reflow panels rather than shrinking text.','verification':'Rebuild completed; run the SVG and reader/modal A4 checks before publishing.'}
    review.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return folder

if __name__=='__main__':
    build(sys.argv[1],int(sys.argv[2]))
