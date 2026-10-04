"""Combined map: varied visual explanations connected by labelled relationships.
Its approved panel artwork is reflowed by landscape_mindmaps for screen viewing.
"""
from html import escape
from mindmap_figures import figure

INK='#173452';BLUE='#1e67bc';ORANGE='#dc701b';GREEN='#418643'
PURPLE='#8258b8';TEAL='#168c98';RED='#bb5447';GOLD='#af8019'
W,H=2400,3120

def visual_overview(m,wrap):
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title description"><title id="title">Cell biology overview</title><desc id="description">'+escape(' '.join(p['title']+': '+' '.join(p['lines']).replace('**','') for p in m['panels']))+'</desc><defs><radialGradient id="animalFill"><stop stop-color="#fff5de"/><stop offset="1" stop-color="#dceafd"/></radialGradient><radialGradient id="nucleusFill"><stop stop-color="#ddc7f4"/><stop offset="1" stop-color="#9b79c2"/></radialGradient><linearGradient id="leafFill" x2="0" y2="1"><stop stop-color="#edf7b8"/><stop offset="1" stop-color="#bfd882"/></linearGradient></defs><rect width="2400" height="3120" fill="#fffefa"/><g font-family="Segoe UI, Arial, sans-serif" fill="#173452">']
    def raw(s):svg.append(s)
    def t(x,y,s,size=28,colour=INK,bold=False,anchor='start'):
        raw(f'<text x="{x}" y="{y}" font-size="{size}" fill="{colour}" font-weight="{700 if bold else 400}" text-anchor="{anchor}">{escape(s)}</text>')
    def para(x,y,s,width,size=28,colour=INK):
        raw('<g class="map-paragraph">')
        for row in wrap(s,width,size):
            xx=x
            for word,bold,w in row:
                if bold:raw(f'<rect x="{xx-2:.1f}" y="{y-size+5}" width="{w:.1f}" height="{size+5}" rx="5" fill="{colour}" opacity=".10"/>')
                t(f'{xx:.1f}',y,word,size,colour,bold);xx+=w
            y+=size+9
        raw('</g>')
        return y
    active_section=False
    def box(x,y,w,h,c,title,n):
        nonlocal active_section
        if active_section:raw('</g>')
        raw(f'<g class="map-section" id="section-{n}" data-bounds="{x},{y},{w},{h}">')
        active_section=True
        raw(f'<rect x="{x+5}" y="{y+7}" width="{w}" height="{h}" rx="30" fill="{c}" opacity=".09"/><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="30" fill="white" stroke="{c}" stroke-width="5"/><path d="M{x+28} {y+80}H{x+w-28}" stroke="{c}" stroke-width="2" opacity=".20"/>')
        raw(f'<circle cx="{x+46}" cy="{y+43}" r="27" fill="{c}"/>');t(x+46,y+53,str(n),31,'white',True,'middle');t(x+91,y+56,title,40,c,True)
    def pill(x,y,w,h,c,lines,size=26):
        line_count=sum(len(wrap(line,w-36,size)) for line in lines)
        h=max(h,line_count*(size+9)+18)
        raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="17" fill="{c}" fill-opacity=".08" stroke="{c}" stroke-opacity=".4" stroke-width="2"/>')
        yy=y+size+12
        for line in lines:yy=para(x+18,yy,line,w-36,size,c)
        return y+h
    def arr(x1,y1,x2,y2,c=INK):
        from mindmap_figures import arrow
        raw(arrow(x1,y1,x2,y2,c))
    def badge(x,y,n,c=BLUE):
        raw(f'<circle cx="{x}" cy="{y}" r="16" fill="white" stroke="{c}" stroke-width="2.5"/>');t(x,y+7,str(n),20,c,True,'middle')
    def mito(x,y):
        raw(f'<ellipse cx="{x}" cy="{y}" rx="23" ry="12" transform="rotate(-20 {x} {y})" fill="#eebf7c" stroke="#ad6024" stroke-width="3"/><path d="M{x-15} {y}l7-6 7 11 7-10 8 3" fill="none" stroke="#ad6024" stroke-width="2.5"/>')
    def cell(x,y,kind,scale=1,numbered=False):
        raw(f'<g transform="translate({x} {y}) scale({scale})">')
        if kind=='animal':
            raw('<path d="M30 92C14 34 55 8 116 13C170-3 231 25 232 81C256 139 214 187 144 187C73 207 9 155 30 92Z" fill="url(#animalFill)" stroke="#3374b5" stroke-width="5"/>')
            raw('<ellipse cx="107" cy="83" rx="44" ry="37" fill="url(#nucleusFill)" stroke="#644a99" stroke-width="4"/><path d="M83 84q15-26 30 0t20-1" fill="none" stroke="#7358a0" stroke-width="3"/>')
            mito(183,122);mito(74,154)
            for xx,yy in [(171,49),(187,64),(48,72),(67,113),(148,152),(186,164),(60,51),(161,100)]:raw(f'<circle cx="{xx}" cy="{yy}" r="4" fill="#b95864"/>')
            if numbered:
                for xx,yy,n in [(106,83,1),(51,132,2),(223,85,3),(190,121,4),(166,45,5)]:badge(xx,yy,n)
        elif kind=='plant':
            raw('<path d="M27 12H215Q233 12 232 35V172Q230 188 212 185H27Q11 185 13 167V33Q10 13 27 12Z" fill="url(#leafFill)" stroke="#468440" stroke-width="8"/><rect x="24" y="24" width="197" height="150" rx="12" fill="none" stroke="#398bae" stroke-width="3"/><path d="M94 48Q176 20 194 73L190 135Q144 175 92 132Q70 83 94 48Z" fill="#c4e5ed" stroke="#4e9dab" stroke-width="3"/><ellipse cx="60" cy="93" rx="24" ry="29" fill="url(#nucleusFill)" stroke="#644a99" stroke-width="3"/>')
            for xx,yy in [(61,39),(197,46),(204,152),(66,158)]:
                raw(f'<ellipse cx="{xx}" cy="{yy}" rx="20" ry="10" fill="#78a851" stroke="#467934" stroke-width="2"/>')
                for dx in [-8,0,8]:raw(f'<path d="M{xx+dx} {yy-6}v12" stroke="#375f2c" stroke-width="2"/>')
            mito(45,130)
            if numbered:
                for xx,yy,n in [(15,71,6),(145,91,7),(201,151,8)]:badge(xx,yy,n,GREEN)
        else:
            raw('<path d="M63 38Q7 47 18 103Q33 160 89 151L190 128Q245 116 223 60Q207 24 167 28Z" fill="#eadcf1" stroke="#795795" stroke-width="6"/><path d="M64 49Q18 58 29 101Q41 144 88 140L187 118Q230 107 213 64Q199 35 165 39Z" fill="none" stroke="#9371ad" stroke-width="3"/><path d="M70 84C73 47 115 58 115 84S154 126 166 86S118 37 101 81S53 117 70 84Z" fill="none" stroke="#6d4d96" stroke-width="5"/><circle cx="178" cy="78" r="15" fill="none" stroke="#6d4d96" stroke-width="4"/>')
            for xx,yy in [(55,110),(63,56),(141,118),(188,104),(147,48)]:raw(f'<circle cx="{xx}" cy="{yy}" r="4" fill="#7b5a93"/>')
        raw('</g>')
    # Relationships use dedicated gutters; labels sit on clear backgrounds.
    def relationship_label(x,y,lines,c):
        longest=max(sum(v[2] for v in row) for line in lines for row in wrap(line,1000,25))
        width=longest+26;height=len(lines)*32+12
        raw(f'<rect x="{x-width/2:.1f}" y="{y-28}" width="{width:.1f}" height="{height}" rx="9" fill="#fffefa"/>')
        for line in lines:t(x,y,line,25,c,True,'middle');y+=32
    for path,c in [
        ('M1200 1050C1190 994 1125 984 1100 941',BLUE),
        ('M1320 1045C1350 878 1330 806 1370 680',ORANGE),
        ('M1465 1170C1520 1170 1510 1115 1560 1115',GREEN),
        ('M1140 1270C1110 1330 1130 1400 1070 1440',PURPLE),
        ('M1320 1310C1370 1370 1380 1405 1430 1470',TEAL),
        ('M1270 1325C1190 1350 1120 1380 1120 1540V2260Q1120 2330 1175 2410',RED),
        ('M850 2220C850 2265 775 2265 775 2315',GOLD)]:
        raw(f'<path class="relationship-path" d="{path}" stroke="{c}" stroke-width="7" stroke-linecap="round" fill="none"/>')
    relationship_label(1050,994,['compare structures'],BLUE)
    relationship_label(1305,858,['adapted','to a job'],ORANGE)
    relationship_label(1470,1030,['observe'],GREEN)
    # Short vertical labels stay inside the narrow lower gutters.
    raw(f'<rect x="1105" y="1378" width="30" height="181" rx="8" fill="#fffefa"/><text x="1128" y="1545" transform="rotate(-90 1128 1545)" font-size="23" fill="{PURPLE}" font-weight="700">make new cells</text>')
    relationship_label(1440,1423,['move substances'],TEAL)
    raw(f'<rect x="1106" y="1830" width="30" height="388" rx="8" fill="#fffefa"/><text x="1129" y="2205" transform="rotate(-90 1129 2205)" font-size="23" fill="{RED}" font-weight="700">investigate bacterial growth</text>')
    relationship_label(786,2273,['measure changes'],GOLD)
    # Compact centre frees width for the cell-division and transport sections.
    raw('<g transform="translate(323 230) scale(.84)"><path d="M1024 1000Q1028 937 1085 958Q1130 919 1170 957Q1240 925 1265 982Q1340 970 1353 1036Q1420 1087 1376 1145Q1409 1214 1340 1235Q1311 1315 1247 1285Q1176 1335 1120 1287Q1046 1316 1022 1252Q947 1250 966 1176Q916 1114 968 1068Q945 1005 1024 1000Z" fill="#f3f8ff" stroke="#173452" stroke-width="8"/>')
    t(1167,1094,'Cell',86,INK,True,'middle');t(1167,1218,'Biology',86,INK,True,'middle');raw('</g>')
    # 1: the wider upper panel uses the former empty space between sections.
    box(25,25,1150,940,BLUE,'Cell structure',1)
    t(65,154,'Animal cell',34,BLUE,True);cell(51,189,'animal',1.10,True)
    yy=182
    for n,line in enumerate(['**Nucleus:** DNA; controls activities.','**Cytoplasm:** chemical reactions.','**Membrane:** controls entry/exit.','**Mitochondria:** aerobic respiration.','**Ribosomes:** protein synthesis.'],1):
        badge(365,yy-9,n);yy=para(395,yy,line,740,29)+12
    raw(f'<path d="M55 429H1145" stroke="{BLUE}" stroke-opacity=".2" stroke-width="2"/>')
    t(65,479,'Plant cell',34,GREEN,True);cell(51,506,'plant',1.10,True)
    yy=502
    for n,line in [(6,'**Cellulose wall:** support in plants and algae.'),(7,'**Permanent vacuole:** cell sap.'),(8,'**Chloroplasts:** photosynthesis in photosynthetic cells.')]:
        badge(365,yy-9,n,GREEN);yy=para(395,yy,line,740,29,GREEN)+12
    para(395,yy+3,'Also has the animal-cell structures.',740,27)
    raw(f'<path d="M55 738H1145" stroke="{BLUE}" stroke-opacity=".2" stroke-width="2"/>')
    t(65,785,'Bacterial cell',34,PURPLE,True);cell(68,802,'bacteria',.87)
    para(365,801,'**Prokaryotic:** much smaller; **no nucleus**. One main DNA loop; some have **plasmids**. Cytoplasm, membrane and a cell wall.',770,29)
    # 2: each picture exposes the adaptation explained beside it.
    box(1225,25,1150,680,ORANGE,'Specialised cells',2)
    rows=[('Sperm','Tail → swimming; mitochondria → energy; acrosome enzymes → penetrate egg.', 'sperm'),('Nerve','Long fibre → carries impulses; branches → connects to other cells.','nerve'),('Muscle','Contractile proteins → shortening; many mitochondria → energy.','muscle'),('Root hair','Long extension → large area for water and mineral uptake; normally no chloroplasts.','root'),('Xylem / phloem','Hollow, lignified xylem → water transport and support. Phloem → sugar transport.','pipes')]
    for i,(name,line,kind) in enumerate(rows):
        y=122+i*107
        if i:raw(f'<path d="M1255 {y-19}H2340" stroke="{ORANGE}" stroke-opacity=".22" stroke-width="2"/>')
        raw(f'<g transform="translate(1260 {y-7})">')
        if kind=='sperm':
            raw('<ellipse cx="37" cy="31" rx="29" ry="18" fill="#bbd0ec" stroke="#375b86" stroke-width="3"/><path d="M10 23q20-22 29-10" fill="none" stroke="#84689e" stroke-width="7"/><path d="M64 31h31Q112 58 144 31T220 31" fill="none" stroke="#375b86" stroke-width="5"/>')
            for x in [68,78,88]:raw(f'<ellipse cx="{x}" cy="30" rx="4" ry="8" fill="#d08c41"/>')
        elif kind=='nerve':
            raw('<path d="M42 33L22 10M42 33L6 31M42 33L18 57M42 33L42 72M42 33L68 4M42 33L67 57M58 33H169L191 14M169 33L210 34M169 33L192 62" fill="none" stroke="#7e589f" stroke-width="5"/><circle cx="44" cy="33" r="18" fill="#c1a0df" stroke="#7e589f" stroke-width="3"/>')
        elif kind=='muscle':
            raw('<path d="M6 45Q94-5 216 35Q132 86 6 45Z" fill="#e9a99a" stroke="#b25644" stroke-width="4"/>')
            for dy in [0,9,18]:raw(f'<path d="M30 {36+dy}Q108 {8+dy} 190 {31+dy}" fill="none" stroke="#b25644" stroke-width="3"/>')
        elif kind=='root':
            raw('<path d="M12 8h80v21h119v18H92v25H12Z" fill="#ebf3c9" stroke="#568647" stroke-width="4"/><circle cx="32" cy="39" r="12" fill="#c7a6e2"/><ellipse cx="68" cy="39" rx="17" ry="25" fill="#c2e1ec"/>')
        else:
            raw('<rect x="20" y="0" width="48" height="78" rx="9" fill="#f2dfb6" stroke="#98683c" stroke-width="6"/><path d="M26 19h8M54 19h8M26 39h8M54 39h8M26 59h8M54 59h8" stroke="#98683c" stroke-width="5"/><rect x="103" y="0" width="42" height="78" rx="6" fill="#e5efc2" stroke="#668549" stroke-width="4"/><path d="M106 25h37M106 51h37" stroke="#668549" stroke-width="3"/><rect x="152" y="0" width="22" height="78" rx="4" fill="#cde1ad" stroke="#668549" stroke-width="3"/><circle cx="162" cy="42" r="6" fill="#916aa9"/>')
        raw('</g>')
        if name=='Xylem / phloem':
            t(1510,y+14,'Xylem /',28,ORANGE,True);t(1510,y+55,'phloem',28,ORANGE,True)
        else:t(1510,y+17,name,29,ORANGE,True)
        para(1725,y+13,line,610,28)
    # 3: measured text flow leaves space below the resolution comparison.
    box(1540,750,835,650,GREEN,'Microscopy & magnification',3)
    t(1575,875,'Light: observe cells',27,GREEN,True);t(1970,875,'Electron: finer detail',27,GREEN,True)
    for x in [1730,2140]:raw(f'<circle cx="{x}" cy="953" r="58" fill="#eef7e7" stroke="{GREEN}" stroke-width="3"/>')
    raw('<ellipse cx="1730" cy="952" rx="39" ry="22" fill="#97b8cd"/><circle cx="2115" cy="952" r="18" fill="#3774a3"/><circle cx="2165" cy="952" r="18" fill="#3774a3"/>')
    t(1730,1045,'Merged points',25,GREEN,False,'middle');t(2140,1045,'Separate points',25,GREEN,False,'middle')
    yy=para(1575,1100,'**Resolution:** distinguish nearby points as separate. Electron microscopes have greater resolution **and** magnification.',755,28)
    pill(1575,yy+20,755,96,GREEN,['**Magnification = image size ÷ actual size**','Same units first; rearrange for image or actual size.'],25)
    # 4: wider and taller, with paragraphs positioned from measured line counts.
    box(25,1010,1070,1230,PURPLE,'Cell division & stem cells',4)
    yy=para(65,1130,'**Chromosomes:** DNA carrying many genes; normally paired in body cells. DNA copying happens **before mitosis**.',990,29)
    raw(f'<svg class="cell-cycle-figure" x="65" y="{yy+12}" width="990" height="300" viewBox="0 0 600 205">'+figure('cell-cycle')+'</svg>')
    yy=pill(65,yy+337,990,90,PURPLE,['**Grow / copy DNA → mitosis → divide**','Identical daughter cells; same chromosome number.'],28)+56
    for line in [
        '**Grow first:** more ribosomes and mitochondria. Copies separate; nucleus, then cytoplasm and membrane divide. For growth, development and repair.',
        '**Differentiation** = becoming specialised. Most animal cells do this early; many plant cells can throughout life.',
        '**Stem cells:** undifferentiated; divide and differentiate. Embryo → most human types; bone marrow → blood cells; meristems → any plant cell.',
        'Potential diabetes/paralysis treatment. **Therapeutic cloning:** matching patient genes avoids rejection. Weigh benefits against **viral infection** and ethical/religious objections. Plant clones conserve rare species and disease-resistant crops.'
    ]:
        yy=para(65,yy,line,990,28)+24
    if yy>2215:raise ValueError(f'Cell division needs more space: {yy}')
    # 5: diagrams are beside definitions, direction and examples.
    box(1150,1465,1225,830,TEAL,'Transport & exchange',5)
    xs=[1180,1370,1640,2070]
    for x,s in zip(xs,['Process','Particle model','Direction / membrane','Energy & examples']):t(x,1595,s,24,TEAL,True)
    for i,(name,kind,definition,key) in enumerate([
        ('Diffusion','diffusion','**Particles:** net movement from **high → low** concentration. Gases or dissolved substances.','**No respiration energy.** Oxygen, carbon dioxide, urea.'),
        ('Osmosis','osmosis','**Water only:** dilute → concentrated solution through a **partially permeable membrane**.','**No respiration energy.** Plant water uptake.'),
        ('Active transport','active','**Substances:** low → high, **against the concentration gradient**, across a membrane.','**Energy from respiration.** Root minerals; gut sugars.')]):
        y=1625+i*150
        raw(f'<rect x="1174" y="{y}" width="1177" height="145" rx="10" fill="{TEAL}" opacity="{.04 if i%2==0 else .08}"/>')
        para(xs[0],y+39,'**'+name+'**',175,26,TEAL)
        # Compact, explicitly keyed particle models with equal compartments.
        raw(f'<g transform="translate(1380 {y+22})">')
        if kind=='diffusion':
            raw('<rect x="0" y="0" width="245" height="77" rx="8" fill="#edf7fc" stroke="#bddce4" stroke-width="2"/>')
            for xx,yy in [(20,17),(43,17),(66,17),(20,39),(43,39),(66,39),(20,61),(43,61),(66,61),(193,18),(222,55)]:raw(f'<circle cx="{xx}" cy="{yy}" r="6" fill="{BLUE}"/>')
            arr(94,40,163,40,TEAL);t(123,107,'● = particles; net movement',18,TEAL,False,'middle')
        else:
            raw('<rect x="0" y="0" width="245" height="77" rx="8" fill="#edf7fc" stroke="#bddce4" stroke-width="2"/>')
            raw(f'<path d="M122 0V77" stroke="{GREEN}" stroke-width="3" stroke-dasharray="5 4"/>')
            if kind=='osmosis':
                for xx,yy in [(17,15),(42,15),(68,15),(92,22),(20,40),(46,60),(82,54),(184,20),(209,59)]:raw(f'<circle cx="{xx}" cy="{yy}" r="5" fill="{BLUE}"/>')
                for xx,yy in [(66,39),(161,14),(203,23),(175,48),(222,49)]:raw(f'<rect x="{xx}" y="{yy}" width="10" height="10" fill="{ORANGE}"/>')
                arr(99,40,146,40,TEAL);t(123,107,'● water   ■ solute',19,TEAL,False,'middle')
            else:
                for xx,yy in [(29,21),(67,57),(159,16),(188,22),(213,17),(167,45),(216,50),(184,66)]:raw(f'<circle cx="{xx}" cy="{yy}" r="6" fill="{BLUE}"/>')
                raw('<rect x="114" y="29" width="16" height="26" rx="5" fill="#bb9dcf" stroke="#775699" stroke-width="2"/>');arr(88,42,156,42,TEAL);t(123,107,'● = transported substance',18,TEAL,False,'middle')
        raw('</g>');para(xs[2],y+31,definition,408,25);para(xs[3],y+31,key,263,24)
    t(1380,2103,'Dashed line = membrane; arrows show net movement',21,TEAL)
    yy=para(1180,2154,'**Faster diffusion:** steeper gradient, higher temperature, larger area. Large organisms have **lower SA:V** → need exchange surfaces and transport systems.',1150,25)
    para(1180,yy+18,'**Alveoli, villi, gills:** large area, thin barrier, good blood supply; gas exchange also needs ventilation. **Roots:** root hairs; **leaves:** thin with air spaces.',1150,25)
    # 6: keep the zone measurement and both formulae on one uncluttered panel.
    box(1150,2345,1225,765,RED,'Culturing microorganisms',6)
    raw('<circle cx="1304" cy="2570" r="102" fill="#eaf3d5" stroke="#5c8760" stroke-width="4"/><circle cx="1304" cy="2570" r="58" fill="white" stroke="#bc7e60" stroke-width="3"/><circle cx="1304" cy="2570" r="15" fill="#c5d4e8" stroke="#4e75a1" stroke-width="3"/>')
    for xx,yy in [(1242,2503),(1360,2500),(1224,2585),(1373,2605),(1275,2654),(1335,2657)]:raw(f'<circle cx="{xx}" cy="{yy}" r="5" fill="#638d65"/>')
    raw('<path d="M1246 2570H1362" stroke="#bb5447" stroke-width="3"/>');t(1304,2717,'Clear-zone diameter',23,RED,True,'middle')
    yy=2475
    for line in ['**Binary fission:** bacteria double with nutrients and suitable temperature. Nutrient broth or colonies on agar.',
                 '**Aseptic technique:** sterilise dishes, medium and loop; cool loop. Tape at edges; invert; **maximum 25°C** in school.',
                 '**Compare antibiotic / antiseptic discs:** solvent control; same conditions; repeat. Larger zone → more growth inhibition under these conditions.']:
        yy=para(1465,yy,line,870,26)+14
    yy=pill(1185,max(yy+3,2760),1149,88,RED,['**Zone area = πr²; radius = diameter ÷ 2** (use squared units).','Population = start × 2ⁿ; n = time ÷ division time; use standard form.'],25)+40
    yy=para(1185,yy,'**Why these precautions?** Sterilising prevents contamination; cooling protects the culture. Tape prevents accidental opening; inversion stops condensation drips. **25°C** reduces growth of harmful human pathogens.',1149,25)+8
    bottom=pill(1185,yy,1149,80,RED,['**Worked doubling:** 50 bacteria, 20-minute divisions, 2 hours.', 'n = 120 ÷ 20 = 6; population = 50 × 2⁶ = **3,200 = 3.2 × 10³**.'],25)
    if bottom>3090:raise ValueError(f'Culturing needs more space: {bottom}')
    # 7: every block follows the previous block's actual height.
    box(25,2290,1070,820,GOLD,'Practicals & key calculations',7)
    yy=2408
    for line in ['**Microscopy:** thin stained sample; angled coverslip. Low power → fine focus. Draw and label plant and animal cells; include a scale.',
                 '**Osmosis:** equal-size plant samples in salt/sugar solutions. Initial mass → equal time → blot → final mass.',
                 'Keep tissue source, dimensions, volume, time and temperature constant. **Repeat and calculate means.**']:
        yy=para(65,yy,line,990,28)+21
    yy=pill(65,yy+1,990,125,GOLD,['**% mass change = (final − initial) ÷ initial × 100**','Graph concentration against % change: **0% → no net water movement**. Rate = mass change ÷ time.'],27)+51
    yy=para(65,yy,'Dilute surroundings → water enters: plant **turgid**; animals may swell. Concentrated → water leaves: plant **flaccid**; animals shrink.',990,27)+24
    yy=para(65,yy,'**1 cm = 10 mm; 1 mm = 1,000 µm; 1 µm = 1,000 nm.** Cube: **SA = 6a²; V = a³**. Tenfold difference = one order of magnitude.',990,27)
    if yy>3090:raise ValueError(f'Practicals need more space: {yy}')
    raw('</g></g></svg>')
    return ''.join(svg)
