from science_completion import write
from biology_08_resources import NOTES as GENERIC_NOTES
import re
def generic_section(title):
    match=re.search(r'^## '+re.escape(title)+r'\n.*?(?=^## |\Z)',GENERIC_NOTES,re.M|re.S)
    assert match,title
    return match.group().replace('biological','chemical').replace('Biological','Chemical').replace('warmer conditions increasing enzyme activity up to an optimum','higher concentration increasing successful collision frequency').replace('temperature changes enzyme activity, so keep it constant when investigating pH','temperature changes reaction rate, so keep it constant when investigating concentration').replace('A scientific investigation checks','A scientific investigation checks').replace('a food chain omits many feeding links, and enzyme diagrams omit molecular detail','particle diagrams and reaction profiles omit some molecular detail')
NOTES='\n\n'.join(generic_section(t) for t in ['From question to fair investigation','Measurements, errors and improvements','Evidence, graphs and conclusions'])+r'''
## Preparing a pure dry soluble salt

**Aim:** make a soluble salt from a dilute acid and an **insoluble oxide or carbonate**, such as copper sulfate from copper oxide and sulfuric acid.

1. Warm dilute acid gently. Add insoluble solid in small portions and stir until some remains unreacted, showing the acid has been used.
2. **Filter** to remove excess solid. The **filtrate** contains dissolved salt.
3. Heat gently in a water bath/electric heater to evaporate some water and **concentrate** the solution. Do not heat until all water is gone.
4. Cool so crystals form, then filter/separate them, wash with a small amount of cold distilled water and dry between filter papers or by a suitable gentle method.

**CuO + H₂SO₄ → CuSO₄ + H₂O.** An insoluble carbonate also produces carbon dioxide. Excess insoluble solid is removable by filtration; excess soluble alkali would remain dissolved, needing a different preparation strategy. Use eye protection and careful acid/hot-apparatus handling. Do not assume a blue solution is already a pure dry crystal sample.

## Acid–alkali titration

**Aim:** determine reacting volumes and an unknown strong acid/alkali concentration.

1. Rinse a pipette with the solution it will deliver, and use a **pipette filler** to transfer a known alkali volume into a conical flask.
2. Add a few drops of a suitable endpoint indicator, such as phenolphthalein or methyl orange.
3. Rinse/fill the **burette with acid**, ensure its tip is filled, remove the filling funnel and record the initial reading at the bottom of the meniscus at eye level.
4. Add acid while swirling over a white tile. Near the endpoint add **dropwise** until the first permanent expected colour change.
5. Record the final reading. **Titre = final − initial reading**.
6. Do a rough run, then repeat carefully to obtain **concordant titres**. Average only suitable concordant accurate runs, explaining any rejected result.

![A burette delivers measured acid into a flask containing known alkali volume and indicator.](../Diagrams/titration-apparatus.svg)

Rinse the conical flask with distilled water if needed; extra water there does **not** change the initial moles of alkali, whereas water left in a burette can dilute its acid. A burette scale increases downwards. Never pipette by mouth; use eye protection for acid/alkali.

**Calculation:** 25.0 cm³ NaOH requires 20.0 cm³ of 0.100 mol dm⁻³ HCl. Volume acid = 0.0200 dm³; **moles HCl = 0.100 ×0.0200 = 0.00200 mol**. The equation HCl+NaOH →NaCl+H₂O gives 1:1, so NaOH moles are 0.00200. **NaOH concentration = 0.00200/0.0250 = 0.0800 mol dm⁻³**. With Mr(NaOH)=40, mass concentration = **3.20 g dm⁻³**. Use equation coefficients if the ratio is different.

## Electrolysis of aqueous solutions

**Aim:** predict and identify products from aqueous electrolysis using **inert electrodes**.

1. Put a measured aqueous solution in a suitable vessel and immerse two graphite/inert electrodes separately.
2. Connect to a low-voltage **DC supply**, naming the negative **cathode** and positive **anode**.
3. Predict products using solution ions and the water-derived ions. Use comparable concentration, voltage, electrode immersion and time when comparing solutions.
4. Observe gas/metal formation, collect small gas samples appropriately and identify them with valid tests.

![An aqueous copper sulfate cell deposits copper at the negative cathode and produces oxygen at the positive inert anode.](../Diagrams/aqueous-electrolysis.svg)

- **Cathode:** a metal less reactive than hydrogen is deposited; otherwise hydrogen commonly forms.
- **Anode:** halide solutions can form their halogen; otherwise oxygen commonly forms under GCSE aqueous/inert-electrode conditions. Follow supplied concentration/context where relevant.
- **Copper sulfate:** copper at cathode, oxygen at inert anode.
- Suitable sodium chloride solution: hydrogen at cathode and chlorine at anode under the stated school-test conditions.

Hydrogen: burning splint/pop. Oxygen: glowing splint relights. Chlorine: damp litmus bleached white. Test small quantities with proper ventilation; do not inhale gas. Avoid short circuits and keep electrical connections dry. **Ions move through the liquid; electrons move through external wires**, not through the electrolyte as free electrons.

## Temperature changes in reacting solutions

**Aim:** investigate a variable affecting temperature change in reactions, such as metal displacement, acid/metal, acid/carbonate or neutralisation.

1. Measure solution volumes/concentrations and put them in an **insulated cup** with suitable support and lid.
2. Measure initial temperature. Add a controlled amount of the second reactant, mix consistently and record temperature at fixed intervals until a maximum/minimum is established.
3. Change one chosen variable, keeping other relevant quantities, starting temperature, insulation and apparatus consistent.
4. Repeat and compare **ΔT = final − initial**, not just final temperature.

A positive ΔT normally indicates an **exothermic** reaction transferring energy to surroundings; a negative ΔT indicates **endothermic** uptake. Heat exchange with the room, delayed thermometer response and incomplete reaction affect results. Better insulation and consistent mixing reduce some errors. A temperature–time graph can help estimate the change at mixing by an appropriate extrapolation when the question supplies suitable data.

Do not compare different total liquid masses as if equal ΔT always means equal energy transferred. Where relevant data/formula are supplied, **Q = mcΔT** connects mass, heat capacity and temperature change. Use small safe quantities, eye protection, secure cups and appropriate control of gas-producing reactions; do not tightly seal them.

## Concentration and rate: gas volume

**Aim:** measure concentration’s effect using a gas-producing reaction.

Use equal masses/surface areas of a suitable solid, such as carbonate chips, with a range of known acid concentrations at **fixed total solution volume and temperature**. Mix and promptly seal to a connected gas syringe, then record gas volumes at fixed intervals. Repeat and compare mean curves/initial gradients or a common-interval mean rate.

Higher concentration gives more particles per unit volume, increasing successful collision frequency. **Rate = gas volume/time** for an interval; a **tangent gradient** gives rate at an instant. Final gas amount depends on the limiting reagent and is different from rate.

![A stoppered flask connects to a gas syringe with freely moving plunger.](../Diagrams/gas-volume-apparatus.svg)

Check leaks and start-up delays; they can lose gas and underestimate output. Keep syringe movement free, use suitable dilute acid and eye protection, and never block a gas-producing system.

## Concentration and rate: turbidity or colour

Thiosulfate reacts with dilute acid to form **insoluble sulfur**. Time until cloudiness hides a fixed cross under the same flask.

- Change thiosulfate concentration by dilution, maintaining total solution volume and fixed acid amount.
- Same temperature, flask, cross, viewing conditions, mixing and endpoint rule.
- Repeat and compare **1/time**, a relative rate proxy for a common endpoint.
- A light sensor and fixed threshold can improve subjective judgement.

Keep the solution depth constant: a deeper column can hide the cross with a different amount of sulfur. Sulfur dioxide can be generated, so use suitable ventilation, small quantities, eye protection and the school’s risk assessment. Gas collection and turbidity are **both required approaches**, not interchangeable descriptions of one measurement.

## Paper chromatography

**Aim:** separate and compare coloured substances and calculate Rf.

Draw a **pencil baseline**, apply small dried spots and place the paper in solvent **below the baseline**. Use a covered vessel, let solvent rise, then remove before it reaches the top and immediately mark the solvent front.

**Rf = baseline-to-spot-centre distance/baseline-to-solvent-front distance.** It has no unit. Compare reference samples in the **same solvent/paper/conditions**. Different partition between stationary and mobile phases causes separation.

Large spreading spots, ink baselines, submerged samples and an unmarked front undermine results. One spot may hide overlapping compounds; a different solvent can improve separation. Handle solvents safely, especially flammable ones, with suitable ventilation and no nearby flame.

## Identifying unknown ionic compounds

**Aim:** use chemical tests to identify cations and anions in unknown **single ionic compounds**. Dissolve where appropriate and use **fresh portions for different tests**.

| Test | Method | Main results |
|---|---|---|
| Flame | Clean loop, blue non-luminous flame | Li crimson; Na yellow; K lilac; Ca orange-red; Cu green |
| Hydroxide | Sodium hydroxide dropwise, then excess | Al/Ca/Mg white; only Al dissolves in excess here. Cu blue, Fe²⁺ green, Fe³⁺ brown |
| Carbonate | Dilute acid; test gas | Limewater milky from CO₂ |
| Halides | Nitric acid then silver nitrate | Cl white; Br cream; I yellow |
| Sulfate | Hydrochloric acid then barium chloride | White precipitate |

Record the **observation and inferred ion**. White alone is ambiguous without the reagent and excess test. Do not introduce chloride by using HCl in a halide test, or sulfate by using sulfuric acid before sulfate testing. Use clean reference samples, repeat uncertain observations and apply suitable eye/hot-wire/reagent precautions. Combine ion charges correctly when suggesting a formula.

## Water analysis and purification

**Aim:** compare water sources using **pH, dissolved solids and distillation**.

1. Collect suitable labelled samples and measure pH with indicator or a calibrated probe.
2. Add a known volume to a weighed dry basin, evaporate gently and cool before reweighing. Use repeated heating/cooling to a consistent residue mass.
3. Residue mass is the difference from the empty-basin mass. Compare equal volumes or calculate concentration with correct conversions.
4. Distil another portion: evaporate water and condense the vapour into an **open receiving vessel**, leaving dissolved solids behind.

![Water vapour passes from a heated flask through a separately water-cooled condenser into an open receiver.](../Diagrams/water-distillation.svg)

Cooling water enters the condenser jacket at the lower/appropriate inlet and leaves at the upper outlet, keeping the jacket full. It does not mix with the vapour/distillate. Compare pH/residue before and after, but do not infer drinkability from clarity or pH alone. Keep heating controlled, avoid distilling dry, use eye protection and never taste samples. Small residue masses may be unreliable if close to balance resolution.

## Applying practical skills to new questions

Identify the actual chemical change and choose a measurement that follows it. A method should name variables, apparatus, range, controls, repeats, calculation and hazard-specific precautions.

Connect an improvement to the error it solves: checking leaks limits gas loss; dropwise addition reduces titration overshoot; insulating the cup limits heat exchange. “Be careful” or “repeat it” alone does not explain every limitation. A mean reduces random scatter, while a systematic bias requires correction.

Use labelled tables/graphs, SI units and appropriate precision. Support conclusions with data and uncertainty. Reproducible evidence and peer review strengthen claims, but models and experiments still have limits.

## Sources

- [AQA Chemistry practical assessment](https://www.aqa.org.uk/subjects/chemistry/gcse/chemistry-8462/specification/practical-assessment)
- [AQA Working scientifically](https://www.aqa.org.uk/subjects/chemistry/gcse/chemistry-8462/specification/working-scientifically)
'''
GROUPS=[('investigations','Investigations and evidence','Plan valid comparisons and evaluate measurement quality.','chemistry-atom',['From question to fair investigation','Measurements, errors and improvements','Evidence, graphs and conclusions','Applying practical skills to new questions']),('preparation','Salt preparation and titration','Make crystals and determine reacting quantities accurately.','chemistry-atom',['Preparing a pure dry soluble salt','Acid–alkali titration']),('changes','Electrolysis and temperature changes','Predict products and measure energy-transfer effects.','chemistry-atom',['Electrolysis of aqueous solutions','Temperature changes in reacting solutions']),('rates','Rate investigations','Compare concentration with gas and turbidity methods.','chemistry-atom',['Concentration and rate: gas volume','Concentration and rate: turbidity or colour']),('analysis','Chromatography, ions and water','Separate, identify and purify using valid observations.','chemistry-atom',['Paper chromatography','Identifying unknown ionic compounds','Water analysis and purification'])]
if __name__=='__main__':
    from chemistry_11_practice import QUESTIONS,MAPS
    write('Chemistry - AQA',11,dict(notes=NOTES,groups=GROUPS,questions=QUESTIONS,maps=MAPS,diagrams=[('titration-apparatus','chem-titration',580),('aqueous-electrolysis','remaining-chem-aqueous-cell',650),('gas-volume-apparatus','remaining-chem-gas',650),('water-distillation','remaining-chem-distillation',650)],coverage=['Working scientifically 1–4','Apparatus and techniques AT1–AT8','8.2.1–8.2.8'],practicals=['RPA'+str(i) for i in range(1,9)],checklist={'WS1–4':'Hypotheses/models/evidence/ethics/risk/peer-review,variables/apparatus/sampling/safety/observations/improvements,data/maths/uncertainty/error/conclusions/vocabulary/units','RPA1–RPA4':'Pure dry salt,reacting volumes+HTconcentrations,aqueous inert electrolysis/hypothesis/products,solution temperature-variable investigation','RPA5–RPA8':'Both gas and colour/turbidity concentration methods/hypothesis,chromatography+Rf,all specified unknown ions,water pH/residue/distillation'},evidence='Original questions mapped to current practical and working-scientifically requirements. Reviewed 2023 Paper 2 Higher Q01 for gas-rate technique, Q03.1 for unknown-ion method and Q06 for chromatography; 2022 Q05 supplies water-treatment context. Paper 1 practicals are independently included from the specification. No frequency ranking is claimed.'))
