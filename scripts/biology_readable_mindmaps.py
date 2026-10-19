"""Readable Biology maps: fixed A4 typography, measured content, compact panels.

The complete original Markdown counterparts remain untouched by style updates.
Panel placement adapts to content; no font shrinking or central decorative hub.
"""
from pathlib import Path
from html import escape
import re, json, math
from itertools import product
from functools import lru_cache
from copy import deepcopy
from biology_explanatory_figures import drawing, VISUALS, PURPOSES
from PIL import ImageFont

W, H = 1120, 768
BODY, SUBHEADING, HEADING = 16, 16, 20
LEADING, PAD, GUTTER, MARGIN = 22, 18, 12, 18
INK = '#000000'
COLORS = ['#2366a0', '#b95619', '#468133', '#7651a5', '#167d87', '#b95619']
ROOT = Path(__file__).resolve().parents[1]

@lru_cache(None)
def font(size, bold):
    return ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf' if bold else 'C:/Windows/Fonts/segoeui.ttf', size)

def runs(value):
    assert value.count('**') % 2 == 0, value
    return [(part, i % 2 == 1) for i, part in enumerate(value.split('**')) if part]

def plain(value):
    return value.replace('**', '')

def wrap(value, width, size=BODY, bold=False):
    words=[]
    for part, strong in runs(value):
        for word in part.split():
            if words and re.fullmatch(r'[.,:!?)]', word):
                words[-1]=(words[-1][0]+word,words[-1][1])
            else:
                words.append((word,strong or bold))
    rows=[]; row=[]; used=0
    for word,strong in words:
        word_width=font(size,strong).getlength(word)
        space=font(size,row[-1][1]).getlength(' ') if row else 0
        if row and used+space+word_width>width:
            rows.append(row); row=[]; used=0; space=0
        if word_width>width:
            raise ValueError(f'Unbreakable word: {word}')
        row.append((word,strong)); used+=space+word_width
    if row:rows.append(row)
    return rows

def row_text(row):
    out=[]
    for word,strong in row:
        if out:out.append(' ')
        out.append('**'+word+'**' if strong else word)
    return ''.join(out)

def text(x,y,value,size=BODY,color=INK,bold=False,cls='body-text',anchor='start'):
    content=''.join('<tspan font-weight="700">'+escape(part)+'</tspan>' if strong else escape(part) for part,strong in runs(value))
    weight=700 if bold and '**' not in value else 400
    return f'<text class="{cls}" x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{content}</text>'

def split_facts(value):
    """Keep bold spans balanced when turning compressed clauses into new lines."""
    parts=[]; current=''; strong=False; i=0
    while i<len(value):
        if value[i:i+2]=='**':
            strong=not strong; current+='**'; i+=2; continue
        if value[i]=='.' and value[i+1:i+2]==' ' and re.match(r'(?:\*\*|[A-Z])',value[i+2:]) and not current.endswith(('e.g','i.e','s.f')):
            current+='.'
            parts.append((current+('**' if strong else '')).strip())
            current='**' if strong else ''; i+=1; continue
        if value[i]==';':
            parts.append((current+('**' if strong else '')).strip())
            current='**' if strong else ''; i+=1; continue
        current+=value[i]; i+=1
    if plain(current).strip():parts.append(current.strip())
    return [part for part in parts if plain(part).strip()]

def group(*lines,heading=None):
    return {'heading':heading,'lines':list(lines)}

def panel(title,*groups):
    return {'title':title,'groups':list(groups)}

def prepare_panels(panels):
    return [panel(p['title'],*(group(*split_facts(line)) for line in p['lines'])) for p in panels]

class LayoutPanel:
    def __init__(self,indices,sources,width,title=None,picture=False,drawing_provider=drawing):
        self.indices=list(indices) if isinstance(indices,tuple) else [indices]
        self.width=width
        self.title=title or sources[self.indices[0]]['title']
        self.rows=wrap(self.title,width-72,HEADING,True)
        self.header_h=36+(len(self.rows)-1)*28
        self.body_y=9+self.header_h+30
        self.elements=[]; y=self.body_y
        if picture:
            # Existing mitosis drawing: retain copies, separation and complete sets.
            self.elements.append(('picture',y,None)); y+=131
        for n,index in enumerate(self.indices):
            source=sources[index]
            for j,g in enumerate(source['groups']):
                if self.elements:
                    last=y-LEADING
                    self.elements.append(('divider',last+12,None)); y=last+35
                heading=g.get('heading') or (source['title'] if len(self.indices)>1 and j==0 and (n>0 or not self.title.lower().startswith(source['title'].lower())) else None)
                if heading:
                    for row in wrap(heading,width-PAD*2,SUBHEADING,True):
                        self.elements.append(('subheading',y,row_text(row))); y+=24
                for value in g['lines']:
                    for row in wrap(value,width-PAD*2-source.get('text_reserve',0)):
                        self.elements.append(('text',y,row_text(row))); y+=LEADING
                visual=source.get('visual')
                if visual and visual['after']==j:
                    artwork,height=drawing_provider(visual['kind'],width-PAD*2)
                    top=y-LEADING+18
                    self.elements.append(('diagram',top,artwork)); y=top+height+LEADING
        self.height=y-LEADING+5+PAD

    def svg(self,x,y,color,number):
        out=[f'<g class="map-section" id="section-{number}" data-source-panel="{",".join(map(str,self.indices))}" data-bounds="0,0,{self.width},{self.height}" transform="translate({x} {y})"><rect width="{self.width}" height="{self.height}" rx="16" fill="white" stroke="{color}" stroke-width="1.8"/><g class="section-heading"><rect x="9" y="9" width="{self.width-18}" height="{self.header_h}" rx="11" fill="{color}" opacity=".09"/><circle cx="29" cy="27" r="12" fill="{color}"/>',text(29,32,str(number),16,'white',True,'diagram-label','middle')]
        for i,row in enumerate(self.rows):out.append(text(50,34+i*28,plain(row_text(row)),HEADING,color,True,'panel-title'))
        out.append('</g><g class="section-body">')
        for kind,yy,value in self.elements:
            if kind=='divider':out.append(f'<path class="section-divider" d="M{PAD} {yy}H{self.width-PAD}" stroke="{color}" stroke-opacity=".25" stroke-width="1" fill="none"/>')
            elif kind=='diagram':
                out.append(f'<g transform="translate({PAD} {yy})">'+value+'</g>')
            elif kind=='picture':
                from cell_biology_illustrated_overview import division
                out.append(f'<g class="concept-illustration" transform="translate(0 {yy-73})">'+division()+'</g>')
                out.append(text(PAD,yy,'Two chromosomes shown before copying',cls='diagram-label',bold=True))
            else:out.append(text(PAD,yy,value,SUBHEADING if kind=='subheading' else BODY,color if kind=='subheading' else INK,cls='subsection-title' if kind=='subheading' else 'body-text'))
        out.append('</g></g>')
        return ''.join(out)

def build_map(title,slug,sources,columns=None,merged_titles=None,picture_index=None,*,drawing_provider=drawing,purpose_provider=PURPOSES,apply_biology_visuals=True,_reflow_attempt=False):
    sources=with_visuals(sources,slug) if apply_biology_visuals else deepcopy(sources)
    from science_equation_layout import equation_lines
    for source in sources:
        for content_group in source['groups']:
            content_group['lines']=[part for value in content_group['lines'] for part in equation_lines(value)]
    columns=columns or [[0,1],[2,3],[4,5]]
    merged_titles=merged_titles or {}
    listed=[i for col in columns for item in col for i in (item if isinstance(item,tuple) else [item])]
    assert sorted(listed)==list(range(len(sources))), (slug,listed)
    count=len(columns)
    available=W-2*MARGIN-(count-1)*GUTTER
    cache={}
    def column(k,width):
        key=(k,width)
        if key not in cache:
            try:
                cards=[LayoutPanel(item,sources,width,merged_titles.get(item),picture_index is not None and picture_index in (item if isinstance(item,tuple) else [item]),drawing_provider) for item in columns[k]]
                cache[key]=(cards,sum(c.height for c in cards)+GUTTER*(len(cards)-1))
            except ValueError:
                cache[key]=([],float('inf'))
        return cache[key]
    best=None
    limits={2:(460,616),3:(290,452),4:(210,332)}[count]
    for partial in product(range(*limits,4),repeat=count-1):
        widths=(*partial,available-sum(partial))
        if not limits[0]<=widths[-1]<limits[1]:continue
        heights=[column(k,w)[1] for k,w in enumerate(widths)]
        if picture_index is not None:
            relevant=next(k for k,col in enumerate(columns) if any(picture_index in (item if isinstance(item,tuple) else [item]) for item in col))
            if widths[relevant]<362:continue
        score=(max(heights),sum(abs(w-available/count) for w in widths))
        if best is None or score<best[0]:best=(score,widths,heights)
    if best is None:raise ValueError('No layout')
    _,widths,heights=best
    if max(heights)>H-2*MARGIN:
        # Wider panels can fit separated equation lines without shrinking fonts.
        if not _reflow_attempt and len(sources)==6:
            choices=[[[0,1,2],[3,4,5]],[[0,3],[1,4],[2,5]],[[0,5],[1,3],[2,4]],[[0,4],[1,2],[3,5]]]
            for alternative in choices:
                if alternative==columns:continue
                try:
                    svg,record=build_map(title,slug,sources,alternative,merged_titles,picture_index,drawing_provider=drawing_provider,purpose_provider=purpose_provider,apply_biology_visuals=False,_reflow_attempt=True)
                    record['reflow']='Rebalanced panel columns for separated equation lines; typography unchanged.'
                    return svg,record
                except ValueError:
                    continue
        raise ValueError(f'{slug}: content needs {max(heights)} units; available {H-2*MARGIN}. Reorganise content, not fonts. {widths}, {heights}')
    defs=''.join(f'<marker id="arrow-{c[1:]}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="4" markerHeight="4" orient="auto-start-reverse"><path d="M1 1L9 5L1 9" fill="none" stroke="{c}" stroke-width="2" stroke-linejoin="round"/></marker>' for c in COLORS)
    description=' '.join(s['title']+': '+' '.join(plain(t) for g in s['groups'] for t in g['lines']) for s in sources)
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="2400" height="{2400*H/W}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="map-title map-description" data-print-width-mm="277" font-family="Segoe UI,Arial,sans-serif"><title id="map-title">{escape(title)}</title><desc id="map-description">{escape(description)}</desc><defs>{defs}</defs><rect width="{W}" height="{H}" fill="#fffdf8"/>']
    number=0; x=MARGIN; layout=[]
    # Fill spare vertical space by distributing it between panels, capped at 8 units.
    for k,width in enumerate(widths):
        cards,total=column(k,width)
        spare=min(8*(len(cards)),H-2*MARGIN-total)
        extra=math.floor(spare/len(cards))
        y=MARGIN
        for card in cards:
            card.height+=extra
            number+=1;out.append(card.svg(x,y,COLORS[(number-1)%len(COLORS)],number))
            layout.append({'source_panels':card.indices,'x':x,'y':y,'width':width,'height':card.height})
            y+=card.height+GUTTER
        x+=width+GUTTER
    out.append('</svg>')
    return ''.join(out), {'widths':widths,'column_heights':heights,'panels':layout,'body_pt':round(BODY/W*277/25.4*72,2),'diagrams':[{'source_panel':i,'kind':p['visual']['kind'],'purpose':purpose_provider[p['visual']['kind']]} for i,p in enumerate(sources) if p.get('visual')]}

def with_visuals(sources,slug):
    sources=deepcopy(sources)
    for index,(kind,after) in VISUALS.get(slug,{}).items():
        sources[index]['visual']={'kind':kind,'after':after}
    if slug=='03-transport-processes':
        # Counts, particle legend and arrows now carry these relationships visually.
        sources[2]['groups'][1]['lines']=['**No respiration energy** is needed.']
    if slug=='02-circulation-and-health':
        # Named chambers, vessels and both full flow routes are carried by the diagram.
        # The original complete wording remains in the Markdown/text counterpart.
        sources[0]['groups']=sources[0]['groups'][2:]
    return sources

def build_cell_map(item):
    from biology_readable_cell_content import CONTENT, COLUMNS, MERGED
    return build_map(item['title'],item['slug'],CONTENT[item['slug']],COLUMNS[item['slug']],MERGED.get(item['slug']),2 if item['slug']=='02-cell-processes' else None)[0]

def review(topic,records):
    target=ROOT/'Biology - AQA'/topic/'mindmap-layout-review.json'
    record={'reviewed':'2026-10-13','generator':'scripts/biology_readable_mindmaps.py','style':'Readable panels without a central hub; black explanations, bold colon labels, consistent coloured headings, light inset dividers, compact outer gutters','print':{'width_mm':277,'orientation':'A4 landscape','minimum_body_pt':round(BODY/W*277/25.4*72,2)},'full_text':'Existing full Markdown counterparts retained','maps':records}
    target.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
