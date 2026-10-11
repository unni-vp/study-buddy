from biology_course_maps import p,m
MAPS={1:[
m('00-energy-overview','Energy overview',['Track changes','Measure transfers','Choose resources'],[
p('Stores → transfers','**Energy is conserved.** Stores include kinetic, gravitational, elastic, thermal, chemical and nuclear.','Transfers: mechanically, electrically, by heating or radiation. Light and sound are not stores.'),
p('Calculate store changes','**Eₖ = ½mv²; Eₚ = mgΔh; Eₑ = ½ke².** Use kg, m, m/s and N/m.','Spring: extension, not total length; stay within proportional limit. Doubling v or e quadruples energy.'),
p('Power & efficiency','**P = E/t = W/t.** Watts = joules per second. Same work in less time → greater power.','Efficiency = useful output / total input; ×100 for %. Dissipated energy is less useful, not destroyed.'),
p('Heating & insulation','**ΔE = mcΔθ.** Temperature change, not final temperature. Measure mass, energy and temperature rise.','Insulation: low conductivity and greater thickness reduce transfer. Compare cooling with controls.'),
p('Resources & reliability','Non-renewable: coal, oil, gas, nuclear. Renewable: biofuel, wind, Sun, tides, waves, hydro, geothermal.','Uses: heating, transport, electricity. Wind/Sun vary; tides are predictable but not continuous.'),
p('Evaluate a choice','Compare emissions, waste, habitat effects, cost, reliability and suitable sites.','A resource mix helps match demand. Science informs decisions; economic and social choices matter.')],{2:('energy-share',80)}),
m('01-energy-stores-and-calculations','Stores & calculations',['Follow the energy','Use equations','Reduce waste'],[
p('Describe a change','Thrown ball: kinetic → gravitational; air resistance also warms surroundings.','Brakes: kinetic → thermal. Kettle: electrical transfer → water’s thermal store.','In collisions, kinetic energy may decrease while total energy is conserved.'),
p('Conservation','Closed system: no net change in total energy. Include surroundings receiving transfers.','Dissipation spreads energy into less useful stores. “Wasted” does not mean destroyed.'),
p('Motion & height','**Eₖ = ½mv²; Eₚ = mgΔh.** Use given g. A 2 kg object at 3 m/s has 9 J.','Rearrange: **v = √(2Eₖ/m)**. Double speed → four times kinetic energy.'),
p('Springs','**Eₑ = ½ke²** within proportional limit. e = stretched length − original length, in metres.','k = 200 N/m, e = 0.050 m → Eₑ = 0.25 J. Square the converted extension.'),
p('Power is a rate','**P = E/t = W/t; E = Pt.** 1,800 J in 30 s → 60 W.','1 kW = 1,000 W; 1 kJ = 1,000 J. Powerful does not automatically mean efficient.'),
p('Efficiency','Useful output / total input, for energy or power. No unit; at most 1 or 100%.','350 J useful from 500 J → 70%; 150 J dissipated. Lubrication reduces friction and unwanted heating.')]),
m('02-heating-and-practicals','Heating & practicals',['Link energy & temperature','Measure fairly','Limit cooling'],[
p('Specific heat capacity','Energy to warm **1 kg by 1°C** without a state change. Units: J/kg°C.','**ΔE = mcΔθ.** Higher c → less warming for the same mass and input.'),
p('Worked example','0.50 kg water, c = 4,200 J/kg°C, warmed 20 → 40°C.','Δθ = 20°C; ΔE = 0.50 × 4,200 × 20 = **42,000 J**. Convert grams to kg first.'),
p('Measure c','Balance → mass; thermometer → rise; joulemeter or Pt → energy.','Insulate a block; improve heater/probe contact. Record initial temperature, heat, record rise.','**c = E/(mΔθ)**. Repeat; keep electrical parts dry; avoid hot surfaces.'),
p('Explain error','Energy also heats equipment and surroundings. Using all input for the sample makes c too high.','Insulation reduces losses. Good thermal contact reduces lag. Energy vs temperature-rise gradient = mc ideally.'),
p('Insulators','Thicker material or lower conductivity → slower conduction under matching conditions.','Trapped air reduces transfer; draught-proofing limits escaping warm air.','Payback time = cost / yearly saving, assuming constant savings.'),
p('Cooling investigation','Compare equal thicknesses; same containers, lids, water mass, starting temperature and room.','Measure temperature at equal intervals; repeat and average. Smaller drop in same time → better insulation.','For thickness: keep material fixed. Handle hot water safely.')]),
m('03-energy-resources','Energy resources',['Finite fuels','Renewable supply','Make a judgement'],[
p('Fossil & nuclear fuels','Coal, oil, gas and nuclear fuels are finite. Fossil fuels support heating, electricity and transport.','Burning fossil fuels releases CO₂ and pollutants. Nuclear: reliable electricity, low operational CO₂, radioactive waste.'),
p('Costs beyond fuel','Extraction damages habitats. Nuclear plants need expensive construction/decommissioning.','Biofuel can regrow, but uses land and releases CO₂ when burned. Carbon balance depends on regrowth and production.'),
p('Wind, Sun & waves','No fuel combustion during operation, but output varies with weather. Solar also varies with daylight.','Wind: visual/noise/wildlife concerns. Waves: harsh conditions and maintenance. Solar: area and siting matter.'),
p('Water & Earth','Hydro reservoirs can supply on demand but flood land; drought reduces supply.','Tides are predictable, not continuous; estuary impacts. Geothermal is steady at suitable sites, with drilling costs.'),
p('Match supply to use','Heating, transport and electricity have different needs. Use a mix, storage and flexible backup.','Renewable means replenished as used; it does not mean always available or impact-free.'),
p('Use evidence','Compare power, reliability, cost, emissions, waste and habitats. Justify which matters most.','Read totals and percentage shares carefully. Scientific evidence cannot alone settle political or economic choices.')])
]}
MAPS[2]=[
m('00-electricity-overview','Electricity overview',['Charge & circuits','Measure behaviour','Transfer & protect'],[
p('Current, pd & resistance','**Q = It; V = IR.** Current = charge per second. Pd = energy per coulomb.','A complete circuit needs a source of pd. Charge is not used up. Ammeter in series; voltmeter in parallel.'),
p('Series vs parallel','Series: same I, shared V, **Rtotal = R₁ + R₂**.','Parallel: same V, branch currents add. More paths reduce total resistance below the smallest branch R.'),
p('Components','Ohmic: constant-temperature straight I–V line. Lamp heats → R rises. Diode conducts one way.','Thermistor R falls when hotter. LDR R falls when brighter; both can be sensors.'),
p('Circuit practicals','Wire: vary length, measure V/I; fix material, thickness and temperature. Switch off between readings.','I–V: vary supply, record paired values, reverse polarity; use protective resistor with diode.'),
p('Power, mains & Grid','**P = VI = I²R; E = Pt = QV.** UK mains: 230 V, 50 Hz ac.','Live brown; neutral blue; earth green/yellow. Grid: higher V → lower I at same power → less I²R heating.'),
p('Static & fields','Rubbing transfers electrons: gain → negative; loss → positive. Like repel; unlike attract.','Field acts on charges without contact. Strong fields can ionise air → spark.')],{5:('field-positive',85)}),
m('01-circuits-and-components','Circuits & components',['Use measurements','Compare connections','Interpret graphs'],[
p('Charge carries energy','**Q = It; E = QV.** C = A × s; V = J/C. Conventional current: + to − outside supply.','Metal electrons move oppositely. A cell provides pd; it does not create charge.'),
p('Resistance','**R = V/I** in Ω. At fixed V, greater R gives smaller I.','Ammeter in series, voltmeter across component. Use standard symbols; a dot marks a junction.'),
p('One loop: series','Same current throughout. Supply pd = sum of component pds.','4 Ω + 8 Ω across 12 V → 12 Ω total, 1 A; voltage drops 4 V and 8 V.'),
p('Branches: parallel','Same pd across supply-connected branches; total I = sum of branch currents.','Extra paths reduce total R. One broken branch need not stop others. Appliances can switch independently.'),
p('Resistor & lamp','I vertical, V horizontal: ohmic line through origin at constant temperature; slope = 1/R.','Lamp heats as current rises → ions vibrate more → R increases; curve flattens. Use V/I at a point.'),
p('Diode & sensors','Diode: high reverse R; conducts forward with sufficient pd. LED emits light.','Thermistor R decreases with temperature; thermostat. LDR R decreases with light; dark-triggered lamp controls.')]),
m('02-circuit-investigations','Circuit investigations',['Construct safely','Compare resistance','Plot & explain'],[
p('Measurement circuit','Low-voltage supply, switch, ammeter and test component in series. Voltmeter across test component.','Variable resistor controls current. Never put an ammeter directly across a supply.'),
p('Quality & safety','Record matched V and I; calculate R = V/I. Secure connections; check meter ranges and zero.','Repeat; avoid hot wire; switch off between readings. A repeated zero error is not removed by averaging.'),
p('Length of wire','Change measured wire length using movable contact and ruler.','Keep material, cross-sectional area and temperature fixed. Low current limits heating.','R vs length should be proportional for uniform wire at constant temperature.'),
p('Combinations','Measure each resistor, then the same pair in series and parallel.','Series total = sum. Parallel total is less than either. Extra parallel path increases total current at fixed V.'),
p('I–V method','Vary pd, record paired I/V readings across a useful range. Reverse supply for negative values.','Repeat for resistor, lamp and diode; protective series resistor for diode. Stay within ratings.'),
p('Graph conclusions','Ohmic: straight through origin if temperature constant. Lamp: flatter at larger |V| as it heats.','Diode: forward conduction, tiny reverse current. Draw smooth best-fit curves; do not connect noisy points mechanically.')]),
m('03-power-mains-and-fields','Power, mains & fields',['Use energy equations','Transmit safely','Explain static'],[
p('Energy & power','**P = VI; P = I²R; E = Pt; E = QV.** Use W, V, A, Ω, J, s, C.','12 V × 2 A = 24 W; for 30 s → 720 J. Double I at fixed R → four times heating power.'),
p('Mains & protection','UK: **230 V, 50 Hz ac**; polarity reverses. Cell: dc.','Live brown; neutral blue near 0 V; earth green/yellow, 0 V. Earth normally has no current.','Live-to-case fault → earth current → fuse/breaker disconnects. Live can remain dangerous with switch open.'),
p('National Grid','Step up V for transmission; for same P = VI, current falls.','Cable heating **I²R** falls. Step down V for consumers. High voltage does not lower cable resistance.'),
p('Charging by friction','Electrons transfer between insulators; protons remain in nuclei. Equal opposite charges result.','Gain electrons → negative. Lose electrons → positive. Like charges repel, unlike attract.'),
p('Electric field','Force on a positive test charge defines direction. Isolated + sphere: outwards; − sphere: inwards.','Closer to sphere → stronger field. Lines never cross.'),
p('Sparks','Large charge imbalance can give a strong field. Air ionises and becomes conducting.','Charge flows suddenly through the air, reducing the imbalance. Force can act before contact.')],{4:('field-positive',85)})]
MAPS[3]=[
m('00-particle-model-overview','Particle model overview',['Describe matter','Track internal energy','Explain pressure'],[
p('States & density','Solid: vibrate in fixed positions. Liquid: close, move past. Gas: far apart, random movement.','**ρ = m/V.** Gas has low density from large spacing. Ice is less dense than liquid water.'),
p('Density practical','Balance → mass. Regular solid: dimensions → volume. Irregular solid: displaced water → volume.','Liquid: subtract empty-container mass. Read meniscus at eye level; avoid trapped bubbles.'),
p('Temperature changes','Internal energy = total particle kinetic + potential energy. Temperature links to average kinetic energy.','**ΔE = mcΔθ.** c: energy to warm 1 kg by 1°C, J/kg°C.'),
p('State changes','Physical and reversible; mass conserved in a closed sample.','**E = mL.** During melting/boiling, potential energy rises, temperature stays constant. Fusion: solid/liquid; vaporisation: liquid/gas.'),
p('Pressure from collisions','Gas particles hit walls → force per area. Force is perpendicular to wall.','At fixed volume and mass, warming → faster particles, more frequent/harder collisions → higher pressure.'),
p('Compress a gas','Fixed mass, constant temperature: **p₁V₁ = p₂V₂**. Smaller volume → more wall collisions → greater p.','Rapid compression does work on gas → internal energy and temperature can increase.')]),
m('01-states-and-density','States & density',['Model particles','Measure volume','Calculate & evaluate'],[
p('Three states','Solid: close, fixed arrangement; vibration. Liquid: close, irregular, able to flow.','Gas: widely spaced, random motion; easily compressed. Individual particles do not expand when heated.'),
p('Physical changes','Melting/freezing; boiling or evaporation/condensation; sublimation solid → gas.','No new substance; reversing restores properties. Open-container mass loss may be escaping vapour.'),
p('Regular & irregular solids','Weigh solid. Cuboid volume = lwh; cylinder = πr²h. Use ruler, callipers or micrometer.','Irregular: fully submerge; final water volume − initial = solid volume. Displacement can is an alternative.'),
p('Liquids & good readings','Weigh empty dry cylinder, then cylinder + liquid. Subtract to find liquid mass.','Read meniscus at eye level. Avoid bubbles/splashes; unsuitable for solids that dissolve or absorb water.'),
p('Density equation','**ρ = m/V; m = ρV; V = m/ρ.**','240 g / 80 cm³ = 3.0 g/cm³ = **3,000 kg/m³**.','1 cm³ = 10⁻⁶ m³. Keep units consistent.'),
p('Explain changes','Fixed mass spreads over larger volume → lower density. Gas spacing explains low density.','Do not claim every solid is denser than its liquid: ice is an exception. Repeats assess random variation; check zero errors.')]),
m('02-heating-and-gas-pressure','Heating & gas pressure',['Warm or change state','Read energy changes','Use collision models'],[
p('Internal energy','Total kinetic + potential energy of all particles. Temperature is related to average kinetic energy.','**ΔE = mcΔθ** when temperature changes; use kg, J/kg°C and a temperature difference.'),
p('Latent heat','**E = mL**, L in J/kg. Change state without changing temperature.','Melting/boiling: potential energy rises. Freezing/condensing releases energy. c and L describe different changes.'),
p('Heating graphs','Slopes: temperature rises. Plateaus: state changes while energy still enters.','Constant-power heating: longer time means more input energy. Cooling gives the reverse changes.'),
p('Combine stages','0.10 kg ice at 0°C → water at 20°C: mL + mcΔθ.','With L = 334,000 and c = 4,200, total = **41,800 J**. At 100 W, ideal time = 418 s; losses add time.'),
p('Fixed-volume heating','Fixed mass: hotter → higher average kinetic energy → faster particles.','More frequent wall collisions and larger momentum changes → greater force per area → greater pressure.'),
p('Volume & compression','Fixed mass, constant T: **pV constant**. 100 kPa × 60 cm³ = 150 kPa × 40 cm³.','Rapid compression does work and may heat gas, so constant-T rule may not apply.')])]
MAPS[4]=[
m('00-atomic-structure-overview','Atomic structure overview',['Model the atom','Track nuclear changes','Use radiation wisely'],[
p('Particles & isotopes','Tiny positive nucleus: protons + neutrons; negative electrons in energy levels.','**Z = protons; A = protons + neutrons.** Isotopes differ in neutrons. Losing electrons forms positive ions.'),
p('Evidence changes models','Electron → plum pudding. Alpha scattering → tiny dense nucleus, mostly empty space.','Bohr: specific levels; Chadwick: neutrons. Absorb radiation → electron rises; emit → falls.'),
p('Decay & equations','Random nuclear decay. Activity in **Bq = decays/s**; detector count rate may be lower.','Alpha: A−4, Z−2. Beta-minus: A unchanged, Z+1. Gamma: A and Z unchanged.'),
p('Half-life','Time for activity/undecayed nuclei to halve. After n half-lives, **(½)ⁿ remains**.','Subtract background first. After 3 half-lives, 1/8 remains and 7/8 has decayed.'),
p('Hazards & uses','Contamination = radioactive material present; irradiation = exposure. Alpha especially harmful inside.','Gamma tracers; targeted treatment. Match half-life and penetration to use; balance benefit and dose.'),
p('Fission & fusion','Fission: large nucleus absorbs neutron → splits, releasing energy, neutrons and gamma.','Neutrons can cause a chain reaction. Fusion: light nuclei join; some mass becomes radiation energy.')]),
m('01-atoms-and-nuclear-equations','Atoms & nuclear equations',['Count & explain','Follow evidence','Balance decays'],[
p('Count particles','Proton +1, neutron 0, electron −1. Neutral: protons = electrons.','Carbon-14: 6p, 8n, 6e. Isotopes share proton number; ions differ in electron count.'),
p('Size & levels','Atom radius ≈ 10⁻¹⁰ m; nucleus less than 1/10,000 of that, holding almost all mass.','Absorb radiation → higher electron level. Emit → lower. Removing an electron ionises the atom.'),
p('Alpha scattering','Most pass straight → mostly empty space. Some deflect → positive repulsion.','Very few return → mass and charge concentrated in tiny nucleus; plum pudding fails.'),
p('Models develop','Indivisible sphere → electron discovery → plum pudding → nuclear atom.','Bohr adds specific electron levels; later proton identification; Chadwick gives neutron evidence.'),
p('Alpha & beta-minus','Alpha is ⁴₂He: daughter **A−4, Z−2**.','Beta-minus: neutron → proton + emitted electron; daughter **A unchanged, Z+1**. Electron is from nucleus, not shell.'),
p('Balance both numbers','²³⁸₉₂U → ²³⁴₉₀Th + ⁴₂He.','¹⁴₆C → ¹⁴₇N + ⁰₋₁e. Totals of A and Z match on both sides.','Gamma loses energy with no change in A or Z.')]),
m('02-radiation-and-half-life','Radiation & half-life',['Compare emissions','Use decay maths','Measure carefully'],[
p('Alpha, beta, gamma','Alpha: helium nucleus, highly ionising, stopped by paper/skin; cm in air.','Beta: fast nuclear electron; medium ionisation, stopped by mm of aluminium; metres in air.','Gamma: EM radiation; less ionising, very penetrating; thick lead/concrete reduces intensity.'),
p('Random decay','Cannot predict when one nucleus will decay. A large sample follows a predictable pattern.','Activity = decays/s (Bq). Count rate is detector events per unit time; not all emissions are detected.'),
p('Half-life','Same time interval halves the remaining undecayed nuclei or activity.','640 → 320 → 160 → 80 Bq: three half-lives. With 2 h half-life, elapsed time = **6 h**.'),
p('Remaining vs decayed','After n half-lives, remaining fraction = **(½)ⁿ**.','Three half-lives: remaining 1/8, decline 7/8. Remaining : initial = 1:8; decline : initial = 7:8.'),
p('Background correction','Measure background without source; subtract from total using matching time units.','84 total − 4 background = 80 counts/s source. One half-life later: 40 + 4 = **44 total**.'),
p('Graph & measurement','Read time between a source count and half that count; check other starting values.','Keep geometry/shielding fixed. Longer counting and repeats reduce random fluctuations; they do not control decay.')]),
m('03-radiation-uses-and-nuclear-energy','Radiation uses & nuclear energy',['Compare exposure','Choose a source','Release nuclear energy'],[
p('Exposure routes','Irradiation: source exposes object; remove/shield source → exposure ends.','Contamination: unwanted radioactive material remains and decays. Alpha is especially harmful internally; gamma can irradiate from outside.'),
p('Dose & precautions','Reduce time, increase distance, use suitable shielding and prevent inhaling/swallowing material.','Background: rocks/radon, cosmic rays, living things; fallout adds human-made sources. Location/work affect dose. **1 Sv = 1,000 mSv**.'),
p('Useful emissions','Gamma tracer escapes body; choose half-life long enough to measure, short enough to limit dose.','Target radiation to destroy unwanted tissue while limiting healthy-tissue damage. Beta can monitor thin-sheet thickness; gamma sterilises equipment.'),
p('Judge risks','Same nuclei count: shorter half-life → greater initial activity, faster decline. Long-lived contamination persists.','Consider type, dose, position and time with benefit and alternatives. Peer review checks research claims.'),
p('Fission','Large unstable nucleus usually absorbs a neutron and splits into two smaller nuclei.','Releases 2–3 neutrons, gamma and energy; products have kinetic energy. Neutrons can trigger more fissions; reactor controls the chain.'),
p('Fusion','Two light nuclei join into a heavier nucleus; some mass becomes radiation energy.','High temperatures help overcome repulsion; powers stars. Not the same as melting. Both fission and fusion change nuclei.')])]
MAPS[5]=[
m('00-forces-overview','Forces overview',['Interact & deform','Turn & move','Stop & conserve'],[
p('Vectors & resultants','Vectors have magnitude + direction; scalars have magnitude only. Force in N; weight **W = mg**.','Resultant combines forces. Zero resultant → constant velocity, possibly zero. Resolve perpendicular components with scale drawings.'),
p('Work & springs','**W = Fs; F = ke; Eₑ = ½ke².** Use extension in m. Spring equations within proportional limit.','Elastic returns to original shape; inelastic leaves deformation. Measure force/extension with ruler and known loads.'),
p('Moments & pressure','**M = Fd**, perpendicular d. Balance clockwise/anticlockwise moments. Levers/gears transmit turning.','**p = F/A; p = hρg**. Greater depth → greater p; pressure difference gives upthrust.'),
p('Motion & laws','**v = s/t; a = Δv/t; v²−u² = 2as** for constant acceleration.','Distance–time slope = speed; velocity–time slope = a, area = displacement. **F = ma**; third-law forces act on different objects.'),
p('Stopping & falling','Stopping = thinking + braking. Thinking = vt; braking transfers kinetic energy to thermal stores.','Weight > drag → accelerates. Drag grows with speed until forces balance at terminal velocity.'),
p('Momentum','**p = mv; F = Δp/Δt.** Closed system: total momentum conserved. Use signed velocities.','Airbags/mats increase stopping time, reducing average force for the same momentum change.')]),
m('01-interactions-work-and-springs','Interactions, work & springs',['Represent forces','Transfer energy','Investigate elasticity'],[
p('Contact or non-contact','Contact: friction, drag, tension, normal force. Non-contact: gravity, electrostatic, magnetic.','Scalar: speed, mass, energy. Vector: force, velocity, momentum. Arrow length and direction represent a vector.'),
p('Weight & components','**W = mg**, N = kg × N/kg; weight acts at centre of mass. Mass stays the same if g changes.','For angled forces, draw tip-to-tail at a stated scale. Diagonal = resultant; perpendicular components have the same combined effect.'),
p('Work done','**W = Fs**, distance along force. 40 N × 3 m = 120 J. Work against friction warms surfaces.','A stationary object needs more than one force to change shape: pulls at opposite ends, for example.'),
p('Hooke’s law','**F = ke** up to proportional limit. 6 N / 0.030 m = 200 N/m.','Elastic = recovers shape; inelastic = permanent. Losing proportionality need not immediately mean permanent deformation.'),
p('Spring practical','Record unloaded length; add known loads; let settle; read length at eye level.','Extension = loaded − original. F = mg includes hanger. Repeat; secure stand, avoid overload and falling masses.'),
p('Graph & stored energy','F vertical vs e horizontal: straight-line gradient = k. Unload to test elastic recovery.','**Eₑ = ½ke²**, triangular area under proportional F–e graph. Do not use final force × extension.')]),
m('02-moments-and-fluid-pressure','Moments & fluid pressure',['Turn about pivots','Apply pressure','Explain floating'],[
p('Moment','**M = Fd**, in Nm; d is perpendicular pivot-to-force-line distance.','20 N × 0.30 m = 6 Nm. Longer lever → less force for the same turning effect.'),
p('Balance, levers & gears','Clockwise moments = anticlockwise moments. 30 N at 0.20 m balances 15 N at 0.40 m.','Adjacent gears rotate oppositely. Larger driven gear turns more slowly with greater turning effect in an ideal system.'),
p('Pressure on an area','Fluid = liquid or gas. Forces are normal to surfaces. **p = F/A**, Pa = N/m².','Smaller area → greater p for same F. **1 cm² = 10⁻⁴ m²**.'),
p('Pressure with depth','**p = hρg** for a liquid column; increases with depth and density.','2 m water at g = 9.8 → 19,600 Pa above surface pressure. Δp = Δhρg; add atmospheric p if total requested.'),
p('Upthrust','Greater pressure on bottom than top gives upward resultant.','Floating at rest: **upthrust = weight**. Compare average density including air spaces; hollow steel ships can float.'),
p('Atmosphere','Air molecules collide with surfaces. Higher altitude has less air above, lower density and lower pressure.','For submerged objects, compare weight/upthrust and include other forces if present; sinking does not mean zero upthrust.')]),
m('03-motion-and-graphs','Motion & graphs',['Describe journeys','Calculate changes','Read slopes & areas'],[
p('Distance vs displacement','Distance: total path, scalar. Displacement: straight start-to-finish change with direction, vector.','Round trip → zero displacement, nonzero distance. Average speed = total distance / total time.'),
p('Useful estimates','Walking ≈ 1.5 m/s; running 3; cycling 6; sound in air 330. Conditions change values.','**s = vt** at constant speed. Convert minutes to seconds and km to m before calculating.'),
p('Velocity & acceleration','Velocity = speed with direction. Circle: constant speed can still mean changing velocity.','**a = (v−u)/t**, m/s². 5 → 17 m/s in 4 s gives 3 m/s².'),
p('Uniform acceleration','**v²−u² = 2as** only for constant a. From rest, a=2 over 25 m gives v=10 m/s.','Free fall near Earth ≈ 9.8 m/s² when air resistance is negligible.'),
p('Distance–time','Gradient = speed. Flat = rest; straight slope = constant speed.','Curved graph: draw tangent at required time; gradient estimates instantaneous speed. Use a large gradient triangle.'),
p('Velocity–time','Gradient = acceleration. Flat = constant velocity. Signed area = displacement; sum absolute areas for distance.','Triangle + rectangle areas give movement. Count squares for a curved section if needed.')]),
m('04-newtons-laws-and-practical','Newton’s laws & practical',['Explain motion','Follow falling forces','Measure acceleration'],[
p('First law & inertia','Zero resultant → rest or constant velocity. Inertia is the tendency to retain that motion.','Balanced forces do not mean no forces. A steady car has driving force = resistance.'),
p('Second & third laws','**F = ma**, using resultant F. Inertial mass = F/a. More mass → less a for same F.','Third law: equal opposite forces of same type on different objects. Weight and normal force on one book are not a pair.'),
p('Terminal velocity','Initially weight > drag → downward acceleration. Speed rises → drag rises → resultant and a fall.','Drag = weight → constant terminal velocity. Opening parachute increases drag, slowing fall to a lower terminal speed.'),
p('Measure acceleration','Low-friction trolley, string, pulley, hanging mass. Light gates or motion sensor measure velocity changes.','Calculate a = Δv/Δt before hanger hits floor. Secure pulley; stop trolley safely; control friction.'),
p('Vary force','Transfer masses from trolley to hanger: total moving mass constant, driving weight increases.','For whole system, driving force ≈ hanger weight if friction negligible. Trolley tension alone is not hanger weight while accelerating.'),
p('Vary mass','Keep hanging mass fixed; add mass to trolley. Force approximately constant, total mass increases.','Repeat; a vs F should be proportional at fixed mass. a vs 1/m should be proportional at fixed force.')]),
m('05-stopping-and-momentum','Stopping & momentum',['Stop safely','Conserve momentum','Reduce impact forces'],[
p('Thinking & braking','Stopping distance = thinking + braking. Thinking = speed × reaction time. Typical reaction time 0.2–0.9 s.','Tiredness, drugs/alcohol and distractions can delay reaction. Ruler-drop tests: repeat, control setup, consider anticipation.'),
p('Braking factors','Wet/icy roads, worn tyres/brakes reduce effective braking. Friction transfers kinetic energy to thermal stores.','Same mass/force: double speed → four times braking distance. Thinking only doubles at fixed reaction time. Large deceleration risks overheating/loss of control.'),
p('Momentum is a vector','**p = mv**, kg m/s. Choose a positive direction and use signed velocities.','Closed system with zero resultant external force: total momentum before = after.'),
p('Collisions & recoil','2 kg at 3 m/s joins stationary 1 kg: 6 kg m/s / 3 kg = **2 m/s**.','Recoil from rest: equal opposite momenta, lighter mass moves faster. Kinetic energy need not be conserved.'),
p('Force changes momentum','**F = Δp/Δt = m(v−u)/Δt**. Gives average force for the interval.','60 kg at 10 m/s → rest: |Δp|=600 kg m/s. Over 0.20 s → 3,000 N; over 0.50 s → 1,200 N.'),
p('Safety features','Airbags, belts, helmets, mats and soft surfaces increase stopping time for the same momentum change.','Average force is lower. They do not stop momentum changing or destroy energy.')])]

# Explanatory drawings occupy reserved panel space; typography stays fixed.
FIGURES={
 1:{1:(3,'ph-spring',120),2:(0,'ph-specific',120)},
 2:{1:(3,'ph-circuit',140),2:(3,'ph-circuit',140)},
 3:{0:(0,'ph-particles',95),1:(0,'ph-particles',95),2:(2,'ph-heat',120)},
 4:{0:(3,'ph-half-life',125),1:(2,'ph-scatter',115),2:(2,'ph-half-life',125)},
 5:{0:(3,'ph-motion',120),1:(5,'ph-spring',120),2:(0,'ph-lever',100),3:(5,'ph-motion',120),4:(2,'ph-terminal',125)}
}
for n,entries in FIGURES.items():
 for index,(panel,kind,height) in entries.items():MAPS[n][index]['pics'][panel]=(kind,height)
