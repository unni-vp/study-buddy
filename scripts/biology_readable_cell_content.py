"""Cell Biology wording and semantic panel groups for the readable map style."""
from biology_readable_mindmaps import panel as p, group as g

CONTENT={
'01-cells':[
p('Animal cells',g('**Eukaryotic:** DNA is enclosed in a nucleus.'),g(
'**Nucleus:** stores genetic material and controls cell activities.',
'**Cytoplasm:** enzyme-controlled chemical reactions.',
'**Membrane:** controls entry and exit.',
'**Mitochondria:** aerobic respiration transfers energy.',
'**Ribosomes:** make proteins.')),
p('Plant cells',g('Also have the structures found in animal cells.'),g(
'**Cellulose wall:** strength and support. Algae also have cellulose walls.',
'**Permanent vacuole:** cell sap. Water helps keep the cell firm.'),g(
'**Chloroplasts:** chlorophyll absorbs light for photosynthesis.',
'Only photosynthetic cells have them. Root hairs normally do not.')),
p('Bacterial cells',g('**Prokaryotic:** smaller than animal or plant cells.',
'**No nucleus:** main DNA is a circular loop in the cytoplasm.',
'Some have **plasmids:** small DNA rings with extra genes.'),g(
'Have membrane, cytoplasm, ribosomes and a **non-cellulose wall**.',
'No mitochondria or chloroplasts.')),
p('Sperm cells',g('**Tail:** helps the cell swim.',
'**Mitochondria:** respiration supplies energy for movement.',
'**Acrosome enzymes:** help penetrate the egg’s outer layers.')),
p('Nerve & muscle cells',g('**Nerve:** a long fibre carries electrical impulses.',
'Branched ends connect to other cells.'),g('**Muscle:** contractile proteins shorten the cell.',
'Mitochondria provide energy for contraction.')),
p('Root hair cells',g('**Long extension:** large absorption area.',
'Water enters by **osmosis**.',
'Minerals enter by **active transport** when less concentrated in soil.'),g(
'Mitochondria supply respiration energy. Normally no chloroplasts underground.')),
p('Xylem & phloem',g('**Xylem:** dead, hollow tubes carry water and minerals.',
'**Lignin:** strengthens walls against collapse.'),g('**Phloem:** sieve tubes transport dissolved sugars.',
'Companion cells supply energy for loading.'),g('Link a cell’s **structure** to its effect and function.')),
p('Differentiation',g('Cells develop specialised structures for a particular function.',
'Most animal cells differentiate **early in development**.',
'Many plant cells can do so **throughout life**.'),g(
'In mature animals, division mainly repairs or replaces cells.',
'Differentiation is the process. Specialisation is the result.'))],
'02-cell-processes':[
p('Chromosomes & genes',g('The nucleus contains **chromosomes made of DNA**.',
'Each carries many genes. Body-cell chromosomes normally occur in pairs.'),g(
'A copied X is **one chromosome** with two joined identical copies.')),
p('Grow & copy DNA',g('Before mitosis, the cell grows and makes more ribosomes and mitochondria.'),g(
'DNA replicates. **DNA amount doubles**.',
'**Chromosome number stays the same** until the copies separate.')),
p('Mitosis',g('The joined copies **separate**. A complete set moves to each end and the nucleus divides.'),g(
'DNA copying happens **before mitosis**.',
'Daughter cells keep the parent’s chromosome number.')),
p('Divide the cell',g('Cytoplasm and membrane divide into **two genetically identical daughter cells**.'),g(
'Needed for growth, development, repair and replacement, such as healing skin.',
'Bacteria divide by **binary fission**, not mitosis.')),
p('Human stem cells',g('**Undifferentiated cells:** divide and produce cells that can become specialised.'),g(
'**Embryonic:** most human cell types.',
'**Bone marrow:** a limited range, including blood cells.',
'The source determines which cells can form.')),
p('Medical uses',g('Potentially replace insulin-producing cells in **diabetes**, or nerve cells in **paralysis**.'),g(
'**Therapeutic cloning:** an embryo has the patient’s genes.',
'Its stem cells are not rejected by the patient’s immune system.',
'These are potential treatments, not guaranteed cures.')),
p('Benefits, risks & ethics',g('**Benefit:** replace damaged tissue.',
'**Risks:** viral infection and uncontrolled division.'),g(
'Destroying embryos raises ethical or religious objections.',
'Others prioritise treatment benefits. Give a reasoned judgement based on the source, benefits and risks.')),
p('Plant meristems',g('Can form **any plant cell type throughout life**.'),g(
'Produce clones quickly and economically.',
'Protect rare plants from extinction.',
'Clone useful crops, such as disease-resistant varieties.',
'Plant cells come from plant meristems, not human stem cells.'))],
'03-transport-processes':[
p('Diffusion',g('**Net movement:** gas or dissolved particles move from high to low concentration.'),g(
'Particles move randomly. **No respiration energy** is needed.',
'Examples: oxygen, carbon dioxide and urea entering blood plasma.'),g(
'At equilibrium, particles still move but there is **no net movement**.')),
p('Faster diffusion',g('**Steeper gradient:** greater net movement per second.',
'**Higher temperature:** more kinetic energy.'),g('**Larger area:** more particles cross at once.',
'**Thinner barrier:** shorter diffusion path.')),
p('Osmosis',g('**Water** moves from a dilute to a concentrated solution through a **partially permeable membrane**.'),g(
'The dilute side has more water relative to solute.',
'Water crosses. Some solutes cannot.',
'Movement is both ways, with a net direction. No respiration energy is needed.')),
p('Water gain & loss',g('**Dilute outside:** water enters.',
'Plant cell becomes **turgid**. Its wall prevents bursting.',
'Animal cell may swell or burst.'),g('**Concentrated outside:** water leaves.',
'Plant cell becomes **flaccid**. Severe loss pulls the membrane from the wall: **plasmolysis**.',
'Animal cell shrinks.')),
p('Active transport',g('Particles move **low to high concentration**, against the gradient, through membrane proteins.'),g(
'Requires **energy from respiration**, like moving uphill.',
'Diffusion and osmosis move down gradients. Osmosis is water-only.')),
p('Where it helps',g('**Roots:** take up mineral ions even when soil concentration is lower.'),g(
'**Gut:** absorbs sugars into blood even when blood concentration is higher.',
'Sugars fuel respiration. Many mitochondria support high energy demand.')),
p('Osmosis practical',g('Change salt or sugar concentration.',
'Use equal-size potato cylinders. Record initial mass.'),g(
'Control tissue source, size, solution volume, time and temperature.',
'Include distilled water. Blot consistently, reweigh and repeat.',
'Blotting removes surface liquid. Cut safely.')),
p('Calculate & interpret',g('**% change = (final − initial) ÷ initial × 100**',
'2.50 g to 2.20 g: −0.30 ÷ 2.50 × 100 = **−12%**.'),g(
'Plot concentration on x and mean percentage change on y.',
'The 0% crossing means **no net water movement**.',
'Positive: gain. Negative: loss.'),g('**Rate = change ÷ time**',
'0.12 g ÷ 30 min = **0.004 g/min**.',
'Investigate anomalies. Repeat near the 0% crossing.'))],
'04-exchange-surfaces':[
p('Why exchange systems?',g('Single cells have a **large surface area to volume ratio**.',
'Their outer surface can meet exchange needs.'),g(
'Large multicellular organisms have a **lower ratio** and longer diffusion distances.',
'They need specialised exchange surfaces and transport systems.')),
p('Surface area : volume',g('Cube side a:', '**Surface area = 6a²**', '**Volume = a³**'),g(
'1 cm cube: 6 ÷ 1 = **6:1**.',
'3 cm cube: 54 ÷ 27 = **2:1**.'),g(
'A larger cube has more total area, but less area per unit volume.',
'Cutting it into pieces exposes more area without changing total volume.')),
p('Lung alveoli',g('Many tiny air sacs give a **large surface area**.',
'Thin alveolar and capillary walls give a **short diffusion path**.'),g(
'Blood supply and ventilation maintain steep gradients.',
'**Oxygen:** air to blood.', '**Carbon dioxide:** blood to air.',
'An alveolus is one air sac.')),
p('Small intestine',g('**Villi and microvilli:** large surface area.',
'**Thin lining:** short diffusion distance.'),g(
'Blood removes absorbed substances, maintaining gradients.',
'Sugars can enter blood by **active transport**, against a gradient.')),
p('Fish gills',g('Many **filaments and lamellae:** large surface area.',
'**Thin surfaces:** short diffusion distance.'),g(
'Blood and flowing water maintain gradients.',
'Oxygen moves from water to blood. Carbon dioxide moves out.')),
p('Plant roots',g('**Root hairs:** large contact area with soil.',
'Water enters by **osmosis** through a partially permeable membrane.'),g(
'Minerals enter against a gradient by **active transport**, using respiration energy.')),
p('Plant leaves',g('**Broad:** large surface area.', '**Thin:** short diffusion distance.'),g(
'**Stomata:** let gases in and out.',
'Internal **air spaces** shorten diffusion paths.',
'For photosynthesis, carbon dioxide enters and oxygen can diffuse out.')),
p('Explain an adaptation',g('**Large area:** more particles cross at once.',
'**Thin barrier:** shorter diffusion path.'),g(
'**Blood supply:** brings or removes substances to maintain gradients.',
'**Ventilation:** refreshes air or water.'),g(
'Name the substance and direction. Explain how the feature makes exchange faster.'))],
'05-microscopy':[
p('Magnification & resolution',g('**Magnification:** image enlargement.',
'**Resolution:** distinguish two close points as separate.'),g(
'Enlarging a blurred photograph adds no detail. Bigger does not mean clearer.')),
p('Light & electron',g('**Light microscopes:** show cells and visible structures.'),g(
'**Electron microscopes:** much greater magnification and resolving power.',
'They reveal finer sub-cellular detail.')),
p('Size formulae',g('**Magnification = image ÷ actual**',
'**Actual size = image ÷ magnification**',
'**Image size = actual × magnification**'),g(
'Convert to the **same units** first.',
'Magnification has no unit. Image and actual sizes do.')),
p('Worked magnification',g('Image: 30 mm. Actual cell: 60 µm.',
'30 × 1,000 = **30,000 µm**.',
'30,000 ÷ 60 = **×500**.'),g(
'Microscope total = eyepiece × objective.',
'×10 × ×40 = **×400**.',
'Drawing magnification depends on drawing size, not automatically the microscope setting.')),
p('Units & standard form',g('**1 cm = 10 mm**', '**1 mm = 1,000 µm**', '**1 µm = 1,000 nm**'),g(
'1 µm = 10⁻⁶ m. 1 nm = 10⁻⁹ m.',
'Larger to smaller units: multiply. Reverse: divide.'),g(
'Standard form: **a × 10ⁿ**, with **1 ≤ a < 10**.',
'0.000060 m = **6.0 × 10⁻⁵ m**.')),
p('Scale & area',g('20 µm ÷ 2 µm = 10: **one order of magnitude**.',
'Convert units before comparing.'),g(
'A scale bar shows actual distance. Compare image length with the bar.',
'Estimate sizes or areas when boundaries are unclear.'),g(
'For similar shapes, doubling length makes **area four times larger**. State the assumption.')),
p('Prepare the slide',g('Observe **plant and animal cells**.',
'Thin onion epidermis, water and a suitable stain such as iodine.'),g(
'Lower the coverslip **at an angle** to reduce air bubbles.',
'Thin tissue lets light through and avoids overlap.'),g(
'Use teacher-approved animal samples. Handle glass, stains and samples safely.')),
p('Focus & draw',g('Start with the lowest-power objective.',
'**Coarse then fine focus**. Centre cells, increase magnification and use fine focus.'),g(
'Clear pencil outlines. No shading.',
'Label visible structures. Add a **magnification scale or scale bar**.',
'Draw what you observe, not just what you remember.'))],
'06-culturing-microorganisms':[
p('Binary fission',g('One bacterium divides into two.',
'Division may take **20 minutes** with enough nutrients and suitable temperature. Use the given time.'),g(
'**1 → 2 → 4 → 8:** repeated doubling, not addition.',
'Bacteria have no nucleus and do not use mitosis.')),
p('Growing a culture',g('**Nutrient broth:** nutrients for growth.',
'**Agar:** a surface for colonies, visible groups from an initial cell or group.'),g(
'Uncontaminated cultures allow fair comparisons.',
'**Aseptic technique:** keeps unwanted microbes out.')),
p('Sterile equipment',g('Sterilise dishes and growth medium to remove unwanted microbes.'),g(
'**Flame the loop**, then let it **cool** so it does not kill the culture.',
'Open the lid briefly to limit airborne contamination.',
'Follow school handling and disposal procedures.')),
p('Safe incubation',g('**Tape the edges:** stops accidental opening.',
'Do not seal completely. Allow gas exchange.'),g(
'**Store upside down:** stops condensation dripping onto the culture.',
'**Maximum 25°C in school:** limits harmful human pathogens.',
'Do not open incubated plates.')),
p('Antimicrobial discs',g('Use aseptic technique to prepare a bacterial lawn on sterile agar.',
'Add antibiotic or antiseptic discs and a **solvent-only control**.'),g(
'Incubate safely. Measure inhibition zones.',
'Repeat and calculate a mean for each treatment.')),
p('Variables & conclusions',g('**Change:** substance or concentration.',
'**Measure:** clear-zone diameter or area.'),g(
'Keep bacterial strain, agar, disc size, substance volume, time and temperature equal.'),g(
'A larger zone shows greater inhibition **under these conditions**.',
'Different diffusion rates mean this does not prove effectiveness in a patient.')),
p('Zone area',g('**Radius = diameter ÷ 2**', '**Area = πr²**'),g(
'Diameter 12 mm: radius 6 mm.',
'π × 6² = **113 mm²** (3 significant figures).'),g(
'Use squared units. Subtract disc area only if asked.',
'A clear zone means **growth was inhibited**.')),
p('Repeated doubling',g('**n = total time ÷ division time**',
'**Final population = start × 2ⁿ**'),g(
'50 bacteria, 20-minute divisions, 2 hours:',
'120 ÷ 20 = **6 doublings**.',
'50 × 2⁶ = **3,200 = 3.2 × 10³**.'),g(
'Keep time units consistent. Apply the stated growth conditions.'))],
}

# Retain the original overview's scope, but use prose labels for associations.
from a4_mindmap_content import COMPACT
from biology_readable_mindmaps import prepare_panels
CONTENT['00-cell-biology-overview']=[
p('Cell structures',g(
'**Nucleus:** DNA and cell control.', '**Cytoplasm:** chemical reactions.',
'**Membrane:** controls entry and exit.', '**Mitochondria:** aerobic respiration.',
'**Ribosomes:** protein synthesis.'),g(
'**Plants and algae:** cellulose wall and permanent vacuole.',
'Photosynthetic cells have chloroplasts.',
'**Bacteria:** smaller, no nucleus, DNA loop. Some have plasmids.')),
p('Specialised cells',g(
'**Sperm:** tail, mitochondria, acrosome enzymes.',
'**Nerve:** long fibre and branches.', '**Muscle:** contractile proteins and mitochondria.',
'**Root hair:** large absorption area.', '**Xylem:** hollow, lignified water tubes.',
'**Phloem:** sugar transport and companion cells.')),
p('Differentiation & stem cells',g(
'**Differentiation:** becoming specialised.',
'Animals mainly early in life. Many plant cells can do this throughout life.',
'**Embryonic:** most human cell types.', '**Bone marrow:** limited types.',
'**Meristems:** any plant cell type.'),g(
'Uses: tissue repair and plant clones.',
'Balance benefits, infection risk and ethics.')),
p('Microscopy',g(
'**Resolution:** distinguish nearby points.',
'Electron microscopes give greater magnification and finer detail.'),g(
'**Magnification = image ÷ actual**', 'Use the same units. 1 mm = 1,000 µm.'),g(
'**Slide:** thin sample, stain, angled coverslip.',
'Low power, focus, draw, label and a scale.')),
p('Culturing microorganisms',g(
'**Binary fission:** repeated doubling.', '**Population = start × 2ⁿ**',
'**n = time ÷ division time**'),g(
'**Asepsis:** sterilise equipment and cool the loop.',
'Tape edges, invert plate, incubate at **≤25°C** in school.'),g(
'Compare antimicrobial discs. Use a solvent control and repeats.',
'**Zone area = πr²**. Radius = diameter ÷ 2.')),
p('Cell cycle',g(
'**Grow → copy DNA → mitosis → divide**',
'Copies separate into two complete sets.',
'Nuclei divide, then cytoplasm and membrane divide.',
'**Two identical cells:** same chromosome number.',
'For growth, development, repair and replacement.')),
p('Diffusion & exchange',g(
'**Diffusion:** net movement from high to low concentration. No respiration energy.',
'Faster with a steeper gradient, higher temperature or larger area.'),g(
'Large organisms have **lower SA:V**.', 'Need exchange and transport systems.',
'Cube: **SA = 6a²**, **volume = a³**.'),g(
'Alveoli, villi and gills: large area, thin barrier and blood supply.',
'Ventilation maintains gas gradients.')),
p('Osmosis & transport',g(
'**Osmosis:** water moves from dilute to concentrated solution through a **partially permeable membrane**.',
'Gain: plant turgid, animal swells. Loss: plant flaccid, animal shrinks.'),g(
'**Practical:** equal plant samples, weigh, soak, blot and reweigh.',
'**% change = (final − initial) ÷ initial × 100**'),g(
'**Active transport:** low to high concentration, using respiration energy.',
'Examples: root mineral uptake and gut sugar absorption.'))]


# The full overview uses larger semantic groups, with dividers at their boundaries.
CONTENT['00-cell-biology-overview']=[p(s['title'],g(*(t for block in s['groups'] for t in block['lines']))) for s in CONTENT['00-cell-biology-overview']]

COLUMNS={
'00-cell-biology-overview': [[(0,1),3],[(5,2),4],[6,7]],
'01-cells': [[0,1],[2,3,4],[5,6,7]],
'02-cell-processes': [[0,1,5],[2,3],[4,6,7]],
'03-transport-processes': [[0,1,2],[(4,5),3],[6,7]],
'04-exchange-surfaces': [[0,1],[2,3,4],[5,6,7]],
'05-microscopy': [[0,1,5],[2,3,4],[6,7]],
'06-culturing-microorganisms': [[0,7],[(1,2),3],[(4,5),6]],
}
MERGED={
'00-cell-biology-overview': {(0,1):'Cells & specialisation',(5,2):'Division & stem cells'},
'03-transport-processes': {(4,5):'Active transport & uses'},
'06-culturing-microorganisms': {(1,2):'Uncontaminated cultures',(4,5):'Compare antimicrobial discs'},
}
