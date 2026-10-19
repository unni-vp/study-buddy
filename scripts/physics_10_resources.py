from science_completion import write,q,p,m
NOTES=r'''
## Choose a relationship before calculating

A calculation is a short explanation written with numbers. Think of an equation sheet as a toolbox: knowing where the tools are helps, but you still need to choose the right tool and use it correctly.

1. Identify what is asked for and its unit.
2. Write the quantities you know, with units.
3. Choose a relationship containing the unknown and useful known values.
4. Check the conditions, such as constant acceleration or an ideal transformer.
5. Convert units, rearrange if needed, substitute and calculate.
6. State the answer with a unit and sensible precision. Check that its size is plausible.

The **full equation sheet is supplied in the exams**. Use the [official equation sheet](../../00 - Specification/AQA-8463-equations-JUN27.pdf) when practising. Understanding symbols, units and conditions is still essential.

The same symbol may mean different quantities:

- **W:** work done or weight.
- **p:** pressure or momentum.
- **V:** volume or potential difference.

Decide from the context and units.

## Units and conversions

| Prefix | Multiplier | Example |
|---|---|---|
| tera, T | 10¹² | 1 TJ = 10¹² J |
| giga, G | 10⁹ | 1 GHz = 10⁹ Hz |
| mega, M | 10⁶ | 1 MJ = 10⁶ J |
| kilo, k | 10³ | 1 kW = 1,000 W |
| centi, c | 10⁻² | 1 cm = 0.01 m |
| milli, m | 10⁻³ | 1 mA = 0.001 A |
| micro, μ | 10⁻⁶ | 1 μC = 10⁻⁶ C |
| nano, n | 10⁻⁹ | 1 nm = 10⁻⁹ m |

- **Mass:** 1 kg = 1,000 g.
- **Mass:** 1 g = 1,000 mg.
- **Time:** 1 minute = 60 s.
- **Time:** 1 hour = 3,600 s.
- **Area:** 1 cm² = **10⁻⁴ m²**, because both dimensions are converted.
- **Volume:** 1 cm³ = **10⁻⁶ m³**, because all three dimensions are converted.
- **Density:** 1 g/cm³ = **1,000 kg/m³**.
- **Speed:** divide km/h by **3.6** to get m/s.
- **Speed:** multiply m/s by **3.6** to get km/h.

**Example: area and pressure**

A force of 600 N acts on a contact area of 20 cm².

1. Convert area: 20 × 10⁻⁴ = **0.0020 m²**, not 0.20 m².
2. Calculate pressure: p = F/A = 600 ÷ 0.0020 = **300,000 Pa**.

Units also describe relationships:

- **1 W = 1 J/s**
- **1 Pa = 1 N/m²**
- **1 V = 1 J/C**

A result for power should not end in joules alone.

## Standard form, estimates and significant figures

**Standard form: a × 10ⁿ**

The number a must satisfy **1 ≤ a < 10**.

- 48,000 = **4.8 × 10⁴**.
- 0.00032 = **3.2 × 10⁻⁴**.

- Multiplying powers: 10³ × 10⁵ = 10⁸.
- Dividing powers: 10⁸/10² = 10⁶.
- For addition, express quantities using compatible powers before combining. Use the calculator's exponent key carefully.
- An **order-of-magnitude estimate** compares powers of ten. Check whether an answer should be tens, thousands or millions before accepting it.

**Mathematical symbols**

| Symbol | Meaning |
|---|---|
| ≈ | Approximately equal |
| ∝ | Proportional to |
| < | Less than |
| > | Greater than |
| ≪ | Much less than |
| ≫ | Much greater than |

**Significant figures** communicate numerical precision. Leading zeros do not count: 0.00450 has **three significant figures**. 3.746 rounds to **3.7** at two significant figures and **3.75** at three. Keep extra calculator digits during intermediate steps and round the final answer appropriately. Do not round every step or claim precision unsupported by the data.

## Rearrange and recognise proportionality

Keep both sides of an equation balanced, like a balance scale. Perform the same operation on both sides.

**Finding resistance**

1. Start with V = IR.
2. Divide both sides by I: **R = V/I**.

To find current instead, divide V by R: **I = V/R**.

**Finding speed from kinetic energy**

1. Start with Eₖ = ½mv².
2. Multiply by 2 and divide by m: v² = 2Eₖ/m.
3. Take the square root: **v = √(2Eₖ/m)**.

For a 2.0 kg object with 25 J of kinetic energy:

v = √(2 × 25 ÷ 2.0) = **5.0 m/s**

**Finding a changed gas pressure:** for a fixed mass at constant temperature, pV is constant.

Write **p₁V₁ = p₂V₂**,

then divide by V₂ to obtain p₂ = p₁V₁/V₂.

**Finding acceleration:** for constant acceleration, start with v² − u² = 2as.

Divide by 2s to obtain **a = (v² − u²)/(2s)**.

| Relationship | What happens when x doubles? | Graph |
|---|---|---|
| **Direct proportion: y = kx** | y doubles, with other factors fixed. | Straight line through the origin. |
| **Inverse proportion: y = k/x** | y halves. At fixed force, doubling mass halves acceleration. | A decreasing curve; plotting y against 1/x gives a straight line through the origin. |
| **Squared relationship: y = kx²** | y becomes four times as large. At fixed mass, doubling speed quadruples kinetic energy. | Plotting y against x² gives a straight line through the origin. |

Elastic energy also follows a squared relationship with extension when spring constant is fixed and the spring remains within its proportional region.

## Equations: energy and heating

| Relationship | Use or condition |
|---|---|
| **Eₖ = ½mv²** | Kinetic energy. Square the speed. |
| **Eₚ = mgh** | Gravitational potential energy change. Use the change in height. |
| **Eₑ = ½ke²** | Elastic energy. Use extension within proportional spring behaviour. |
| **ΔE = mcΔθ** | Heating. Use temperature change, not final temperature. |
| **E = mL** | Energy for a change of state. |
| **P = E/t** | Power is the rate of energy transfer. |
| **P = W/t** | Power is also the rate of doing work. |
| **Efficiency = useful output/total input** | Use both energies or both powers. Multiply by 100 for %. |

**Symbols and units**

| Symbol | Quantity | Unit |
|---|---|---|
| E, Eₖ, Eₚ, Eₑ, ΔE | Energy or energy change | J |
| m | Mass | kg |
| v | Speed | m/s |
| g | Gravitational field strength | N/kg |
| h | Height change | m |
| k | Spring constant | N/m |
| e | Extension | m |
| c | Specific heat capacity | J/kg°C |
| Δθ | Temperature change | °C |
| L | Specific latent heat | J/kg |
| P | Power | W |
| W | Work done | J |
| t | Time | s |
| Efficiency | Fraction of useful output | No unit |

In **W/t**, W means work done. After a power value, W is the unit watt.

**Choose c or L:** warming without a state change uses **mcΔθ**. Melting or boiling at constant temperature uses **mL**. If both occur, calculate separate stages and add the energies.

**Example: heating and efficiency**

A 0.20 kg sample warms from 20°C to 40°C. Its specific heat capacity is 900 J/kg°C. The total energy input is 4,500 J.

1. Temperature rise = 40 − 20 = **20°C**.
2. Useful energy = 0.20 × 900 × 20 = **3,600 J**.
3. Efficiency = 3,600 ÷ 4,500 = **0.80**.
4. Percentage efficiency = 0.80 × 100 = **80%**.

## Equations: electricity and matter

| Relationship | Use or condition |
|---|---|
| **Q = It** | Charge transferred. Current is constant over the stated interval. |
| **V = IR** | Use resistance at the relevant operating conditions. |
| **P = VI** | Electrical power. |
| **P = I²R** | Heating power. |
| **E = Pt** | Energy transferred in a time interval. |
| **E = QV** | Energy transferred by a quantity of charge. |
| **ρ = m/V** | Density. Use matching mass and volume units. |
| **pV = constant** | Fixed mass of gas at **constant temperature**. Use matching pressure and volume units. |

**Symbols and units**

| Symbol | Quantity | Unit |
|---|---|---|
| Q | Charge | C |
| I | Current | A |
| t | Time | s |
| V in electrical equations | Potential difference | V |
| R | Resistance | Ω |
| P | Power | W |
| E | Energy transferred | J |
| ρ | Density | kg/m³ |
| m | Mass | kg |
| V in density or gas equations | Volume | m³ |
| p | Pressure | Pa |

An alternative matching density unit is **g/cm³**, using mass in g and volume in cm³.

**Example: charge and energy**

A current of 0.50 A flows for 3 minutes at 12 V.

1. Convert time: 3 × 60 = **180 s**.
2. Find charge: Q = 0.50 × 180 = **90 C**.
3. Find energy: E = QV = 90 × 12 = **1,080 J**.

For gas changes, do not use inverse pressure–volume reasoning if temperature or the amount of gas also changes. Calculate **p₂ = p₁V₁/V₂** when the conditions apply.

## Equations: forces and motion

| Relationship | Use or condition |
|---|---|
| **Weight W = mg** | Mass is not weight. |
| **Work W = Fs** | Displacement along the force's line of action. |
| **F = ke** | Extension within the proportional region. |
| **Moment M = Fd** | d is perpendicular distance to the force's line of action. |
| **p = F/A** | Force normal to the surface. |
| **p = hρg** | Pressure due to a liquid column. |
| **s = vt** | Constant speed, or an appropriate average speed. |
| **a = (v − u)/t** | Average acceleration over the interval. |
| **v² − u² = 2as** | Constant acceleration. Convert before squaring. |
| **F = ma** | F is the **resultant force**. |
| **Momentum p = mv** | Include direction. |
| **F = Δp/Δt** | Average force over the interval. |
| **F = m(v − u)/Δt** | Average force for constant mass. |

**Symbols and units**

| Symbol | Quantity | Unit |
|---|---|---|
| W in W = mg | Weight | N |
| W in W = Fs | Work done | J |
| m | Mass | kg |
| g | Gravitational field strength | N/kg |
| F | Force | N |
| s | Distance or displacement, as required | m |
| k | Spring constant | N/m |
| e | Extension | m |
| M | Moment | Nm |
| d | Perpendicular distance | m |
| p in pressure equations | Pressure | Pa |
| A | Area | m² |
| h | Liquid depth | m |
| ρ | Density | kg/m³ |
| v | Final velocity, or speed in s = vt | m/s |
| u | Initial velocity | m/s |
| a | Acceleration | m/s² |
| t, Δt | Time interval | s |
| p, Δp in momentum equations | Momentum or momentum change | kg m/s |

Use a consistent positive direction in momentum questions. For a closed system with zero resultant external force, **total momentum before = total momentum after**. This does not imply that kinetic energy is also conserved.

**Example: a collision**

A 2 kg trolley moving at +3 m/s sticks to a stationary 1 kg trolley.

1. Initial momentum = 2 × 3 = **6 kg m/s**.
2. Combined mass = 2 + 1 = **3 kg**.
3. Final velocity = 6 ÷ 3 = **+2 m/s**.

## Equations: waves and electromagnetism

| Relationship | Use or condition |
|---|---|
| **T = 1/f** | T is period. |
| **v = fλ** | Frequency stays unchanged at a medium boundary. |
| **Magnification = image height/object height** | Use matching height units. Magnification has no unit. |
| **F = BIl** | Conductor perpendicular to the field. Use length **inside the field**. |
| **Vₚ/Vₛ = nₚ/nₛ** | Keep matching subscripts together. |
| **VₚIₚ = VₛIₛ** | Equal input and output power for an **ideal transformer**. |

**Symbols and units**

| Symbol | Quantity | Unit |
|---|---|---|
| T | Period | s |
| f | Frequency | Hz |
| v | Wave speed | m/s |
| λ | Wavelength | m |
| F | Force | N |
| B | Magnetic flux density | tesla (T) |
| I, Iₚ, Iₛ | Current | A |
| l | Wire length inside the field | m |
| Vₚ, Vₛ | Primary and secondary potential difference | V |
| nₚ, nₛ | Primary and secondary coil turns | Count of turns |

For an echo, use the wave relationship plus the journey: **one-way distance = vt/2**. The time includes the return trip.

For a real transformer with given efficiency, use **input power = output power/efficiency** before finding current.

## Linked calculations

Some questions need two or more relationships. Plan the route before entering numbers.

**A motor lifts a load:** mass and height → useful gravitational energy → useful power → input power using efficiency.

**Example:** lift 10 kg by 2.0 m in 4.0 s, with g = 10 N/kg and efficiency 0.50.

1. Useful energy = mgh = 10 × 10 × 2.0 = **200 J**.
2. Useful power = 200/4.0 = **50 W**.
3. Input power = 50/0.50 = **100 W**.

**Heat and melt:** calculate energy for the temperature rise, then latent energy for the state change. Do not use a temperature-rise equation for the constant-temperature stage.

**Uncertainty check:** if a measured length is 0.050 ± 0.001 m, percentage uncertainty is 0.001/0.050 × 100 = **2%**.

Whether an improvement matters depends on the biggest sources of uncertainty, not just adding more decimal places.

## Read linear graphs and their units

**y = mx + c**

- **m:** gradient.
- **c:** y-intercept.

A straight line through the origin has c = 0.

A non-zero intercept can reveal an offset or a physical starting value. It is not always an error.

- **Gradient = Δy/Δx**, using two widely separated points on the best-fit line.
- Gradient units are **y-axis unit / x-axis unit**.
- F against extension: gradient = **k**, N/m.
- I against V: gradient = **1/R**, A/V.
- V against I: gradient = **R**, V/A.
- Distance against time: gradient = speed, m/s.
- Velocity against time: gradient = acceleration, m/s².

**Example: a force–extension gradient**

The best-fit line passes through **(0.010 m, 2 N)** and **(0.040 m, 8 N)**.

1. Change in force = 8 − 2 = **6 N**.
2. Change in extension = 0.040 − 0.010 = **0.030 m**.
3. Gradient = 6 ÷ 0.030 = **200 N/m**.

Read values from the fitted line, not a tiny triangle between noisy neighbouring measurements.

## Tangents and area under a graph

On a curved distance–time graph, draw a **tangent at the required time**. Use a large triangle along that straight tangent to calculate **instantaneous speed**. A chord joining two points on the curve gives an average rate over that interval, not necessarily the rate at the chosen point.

![A tangent touches the curved distance–time graph at the chosen point. A large triangle gives its gradient and therefore the speed at that instant.](../Diagrams/tangent-speed.svg)

The meaning of **area** depends on the axes.

- **Velocity–time:** signed area gives **displacement**. Add magnitudes above and below zero for total distance.
- **Force–extension:** area gives work transferred to the spring, **½ke²** within proportional behaviour.
- Count squares for an irregular area, multiplying by the physical quantity represented by one square.
- Rectangle area = base × height. Triangle area = **½ × base × height**.

![The area of a velocity–time graph represents displacement.](../Diagrams/velocity-area.svg)

**Example: area under a velocity–time graph**

Velocity rises from 0 to 8 m/s over 4 s, then remains at 8 m/s for 3 s.

1. Triangular area = ½ × 4 × 8 = **16 m**.
2. Rectangular area = 3 × 8 = **24 m**.
3. Displacement = 16 + 24 = **40 m**.

The area under a distance–time graph is not a distance.

## Statistics, charts and correlations

- **Mean:** sum divided by number. With a frequency table, use **Σ(value × frequency)/Σfrequency**.
- **Median:** middle value after sorting. For an even number, average the middle two.
- **Mode:** most frequent value; a set may have more than one mode or none.
- **Range:** maximum − minimum. It describes spread, not the typical value.
- **Percentage change:** (new − original)/original × 100. Use the original quantity as the denominator.

For the values **20, 21, 21, 22 and 26**:

- Mean = **22**.
- Median = **21**.
- Mode = **21**.
- Range = **6**.

The high value affects the mean more than the median.

Use a bar chart for categories and a scatter graph for paired numerical data. **Positive correlation** rises overall; **negative correlation** falls. Neither establishes cause by itself.

In a histogram, adjacent numerical intervals have adjoining bars. With unequal interval widths, **frequency is represented by area**, so **frequency density = frequency/interval width**. A taller bar does not automatically contain more observations if widths differ.

## Angles, areas and three-dimensional shapes

- Draw a normal **90° to a surface**. Reflection angles are measured from it; i = r.
- A force's moment uses the **perpendicular distance** from the pivot to its line of action.
- Use a scale drawing to combine angled forces, keeping arrow directions. Do not add their magnitudes as though they act along one line.
- Rectangle area = length × width.
- Triangle area = ½ × base × perpendicular height.
- Cuboid volume = length × width × height.
- Cube volume = side³.
- Cube total surface area = **6 × side²**.
- Use 2D views to understand a 3D object. A thin wire's diameter must be measured with suitable precision; tiny dimension errors can strongly affect calculated area or volume.

**Example: a cube of side 2.0 cm**

| Quantity | In centimetre units | In SI units |
|---|---|---|
| Side | 2.0 cm | 0.020 m |
| Volume | 8.0 cm³ | 8.0 × 10⁻⁶ m³ |
| Surface area | 24 cm² | 2.4 × 10⁻³ m² |

## Check your result

- Is the **unit** correct and consistent with the equation?
- Did you square converted values and take any required square root?
- Did you use a temperature change, extension, perpendicular distance or one-way echo distance correctly?
- Is efficiency at most 1 or 100%? Does input exceed useful output when losses are present?
- Does a greater mass at fixed force give smaller acceleration, as expected?
- Have you retained direction where velocity, force or momentum is a vector?
- Is the answer's order of magnitude plausible? A car speed of 10,000 m/s should trigger a check.
- Does the result depend on a condition, such as constant temperature, constant acceleration or an ideal transformer, that the question actually supplies?

## Sources

- [AQA Maths requirements](https://www.aqa.org.uk/subjects/physics/gcse/physics-8463/specification/mathematical-requirements)
- [AQA equation-sheet arrangements](https://www.aqa.org.uk/news/gcse-maths-sciences-formulae-equation-sheets-2027-28)
- [Official equation sheet](../../00 - Specification/AQA-8463-equations-JUN27.pdf)
'''
GROUPS=[
 ('numbers','Numbers and units','Select relationships, convert units and rearrange carefully.','physics-equations',['Choose a relationship before calculating','Units and conversions','Standard form, estimates and significant figures','Rearrange and recognise proportionality']),
 ('equations','Equation toolkit','Use the equation families and their physical conditions.','physics-equations',['Equations: energy and heating','Equations: electricity and matter','Equations: forces and motion','Equations: waves and electromagnetism','Linked calculations']),
 ('graphs','Graphs and data','Use gradients, tangents, areas and statistical summaries.','physics-motion',['Read linear graphs and their units','Tangents and area under a graph','Statistics, charts and correlations']),
 ('geometry','Geometry and checking','Use dimensions and directions, then check the result.','physics-forces',['Angles, areas and three-dimensional shapes','Check your result'])]
if __name__=='__main__':
    from physics_10_practice import QUESTIONS,MAPS
    write('Physics - AQA',10,dict(notes=NOTES,groups=GROUPS,questions=QUESTIONS,maps=MAPS,coverage=['7:MS1a–1d,MS2a–2c,MS2f–2h,MS3a–3d,MS4a–4f,MS5a–5c','Appendix A: all 35 equation entries, including alternative power and efficiency forms','2027 full Physics equation sheet'],diagrams=[('tangent-speed','remaining-tangent',580),('velocity-area','ph-motion',580)],evidence='June 2022 and 2023 Paper 2 Higher were reviewed. Equation selection, substitutions and conversions are represented by 2022 Q07.2,Q07.5 and 2023 Q05.3,Q06.2,Q08.2. Current mathematical requirements and all 35 entries in the official 2027 equation sheet were checked independently. Questions here are original skill practice, not copied past-paper wording or a ranked frequency prediction.',checklist={'MS1':'Units/conversions, standard form, ratio/percent, estimates','MS2':'Significant figures, mean/median/mode/range, frequency tables, charts/histograms, correlation/order of magnitude','MS3':'Symbols, rearrangement, substitutions and linked equations','MS4':'Linear graphs, slope/intercept, tangents, signed areas/counting squares','MS5':'Angles, 2D/3D interpretation, rectangle/triangle areas and cube/cuboid dimensions','Equations':'All families in toolkit, conditions and units; full official2027sheet linked locally'}))
