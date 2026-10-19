from science_completion import write,q,p,m
NOTES=r'''
## Units, prefixes and standard form

A biological calculation is like comparing prices: both values must be expressed on the same basis. A millimetre and a micrometre are both lengths, but they are not the same-sized unit.

| Unit/prefix | Relationship |
|---|---|
| kilo, k | ×10³ |
| centi, c | ×10⁻² |
| milli, m | ×10⁻³ |
| micro, µ | ×10⁻⁶ |
| nano, n | ×10⁻⁹ |
| mega, M | ×10⁶ |
| giga, G | ×10⁹ |
| tera, T | ×10¹² |

**Length conversions**

- **1 m = 100 cm**.
- **1 m = 1000 mm**.
- **1 mm = 1000 µm**.
- **1 µm = 1000 nm**.

Multiply when converting into a smaller unit. Divide when converting into a larger one.

**Example**

1. 0.045 mm × 1000 = **45 µm**.
2. 45 µm × 1000 = **45 000 nm**.

For area and volume, square or cube the conversion factor:

- **1 cm² = 100 mm²**.
- **1 cm³ = 1000 mm³**.
- **1 cm³ = 1 mL**.
- **1000 cm³ = 1 dm³**.

Do not multiply an area by only 10 when converting cm² to mm².

**Standard form** is **a ×10ⁿ**, with **1 ≤ a <10** and integer n.

Example: 0.0000062 m = **6.2 ×10⁻⁶ m**.

Negative powers represent small fractions, not negative lengths.

For multiplication, multiply coefficients and add powers.

For division, divide coefficients and subtract powers.

## Estimates, scale and significant figures

Estimate first to spot impossible calculator outputs. Approximate 49.6/0.21 as 50/0.2 = **250**; an exact answer near 236 is plausible, whereas 2.36 is not.

**Order of magnitude** describes scale using powers of ten. A 10 µm cell is about **ten times** a 1 µm bacterium, one order larger. Compare lengths before comparing surface areas or volumes: doubling every length gives four times area and eight times volume.

Significant figures start at the first non-zero digit. **0.00450 has three significant figures**; the final zero records precision. Round only at the end: 0.02746 to two significant figures is **0.027**. Follow any requested precision and avoid claiming more precision than the measurements justify. Decimal places and significant figures are different.

## Ratios, fractions and percentages

**Fractions and percentages**

- **Fraction = part/whole**.
- **Percentage = part/whole × 100**.

For 18 of 60 successful treatments:

Success = 18 ÷ 60 × 100 = **30%**.

**Percentage change**

**Percentage change = (new − original)/original × 100**

From 40 to 50, the increase is **25%**, not 20%. The starting value is the denominator.

**Ratios**

- Compare quantities in matching units: 12:18 simplifies to **2:3**.
- A ratio of 1:3 affected:unaffected gives affected fraction **1/(1+3) = 1/4**, not 1/3.

**Percentage points**

These are the direct difference between percentages. From 20% to 30% is **10 percentage points**, but a **50% relative increase**.

**Example: a decrease in tissue mass**

The mass falls from 2.5 g to 2.0 g. Keep the negative sign.

1. Mass change = 2.0 − 2.5 = **−0.5 g**.
2. Percentage change = −0.5 ÷ 2.5 × 100 = **−20%**.

This is a **20% decrease**.

## Magnification and scale bars

**Magnification = image size/actual size.** Rearrange:

- **Actual size = image size/magnification.**
- **Image size = actual size × magnification.**

**Example: actual size from magnification**

An image is 36 mm long at ×600 magnification.

1. Actual size = 36 ÷ 600 = **0.060 mm**.
2. Convert to micrometres: 0.060 × 1000 = **60 µm**.

Convert units first if image size and actual size are supplied in different units.

Magnification has **no unit**, because length divided by length cancels.

**A scale bar resizes with the image**, so it remains useful when both are enlarged or reduced together.

For a scale bar representing **5 µm**, its printed length is 10 mm. A cell on the same image measures 36 mm.

1. Compare image lengths: 36 ÷ 10 = **3.6 scale-bar lengths**.
2. Multiply by the real bar length: 3.6 × 5 = **18 µm**.
3. This is the cell's actual length. The printed bar length is not its actual biological size.

**Microscope magnification** is eyepiece magnification × objective magnification. A photograph or drawing resized afterwards needs its own image magnification.

## Rates, efficiency and inverse relationships

**Rate = change/time**

**Example:** 12 cm³ of oxygen is produced in 4 minutes.

- In cm³ min⁻¹: rate = 12 ÷ 4 = **3 cm³ min⁻¹**.
- In cm³ s⁻¹: rate = 12 ÷ 240 = **0.05 cm³ s⁻¹**.

Make the time unit match the requested answer.

For a common enzyme endpoint, **relative rate = 1/time**.

A time of 25 s gives **0.040 s⁻¹**.

Halving the endpoint time doubles the rate proxy. This only compares the same amount of change under comparable starting conditions.

**Biomass transfer efficiency = next-level biomass/previous-level biomass ×100.**

Transfer of 40 kg from 500 kg gives **8%**.

Use the same mass basis; a pyramid bar width represents mass, not simply number of organisms.

For a suitable point-source model:

**Light intensity ∝ 1/distance²**

**Example: tripling the distance**

New intensity = original intensity ÷ 3².

The new intensity is **1/9** of its previous value.

**Example: doubling the distance**

The intensity is 200 units at 10 cm.

1. At 20 cm, distance has doubled.
2. New intensity = 200 ÷ 2² = **50 units**.

This does not guarantee that photosynthesis rate quarters. Other limiting factors can affect rate.

## Probability in inheritance

Probability ranges from **0 to 1**.

For a simple **Aa × Aa** cross, the four equally likely combinations are **AA, Aa, Aa and aa**.

- Probability of aa = **1/4 = 0.25 = 25%**.
- Probability of a carrier = **2/4 = 50%**.

**Expected number = probability × number of trials.**

With an affected probability of 1/4 across 80 births, the expected affected count is 80 × 1/4 = **20**.

This is an average expectation, not a guaranteed result.

**Each pregnancy is a new event.** For independent events, multiply probabilities. The probability that both children in a specified pair of births are affected is **1/4 × 1/4 = 1/16**.

Distinguish “both”, “at least one” and “exactly one” when interpreting a prompt. Do not turn a ratio of affected to unaffected into a probability without including both groups in the total.

## Averages, spread and frequency tables

- **Mean:** total/number of values.
- **Median:** middle of an ordered list; for an even count, average the two middle values.
- **Mode:** most frequent value; a dataset can have multiple modes or none.
- **Range:** maximum − minimum.

For the values **2, 3, 3 and 8**:

- Mean = **4**.
- Median = **3**.
- Mode = **3**.
- Range = **6**.

Mean is influenced strongly by an extreme value. Investigate unusual measurements before removing them.

For a frequency table of exact values:

**Mean = sum(value × frequency) ÷ sum(frequency)**

**Example**

| Count | Frequency | Count × frequency |
|---|---|---|
| 0 | 2 | 0 |
| 1 | 3 | 3 |
| 2 | 5 | 10 |

Mean = (0 + 3 + 10) ÷ 10 = **1.3**.

Do not average only the three displayed counts.

For grouped continuous data, class midpoints give an **estimated mean**. Retain that it is an estimate.

## Sampling and population estimates

Random sampling limits selection bias, but enough representative samples are still needed. A transect with regular quadrats tests change across a gradient; it is systematic.

**Population estimate = mean per quadrat × total habitat area ÷ quadrat area.**

For a mean of six plants per 0.5 m² quadrat in a 200 m² habitat:

1. The habitat contains 200 ÷ 0.5 = **400 quadrat-sized areas**.
2. Estimated population = 6 × 400 = **2400 plants**.

Convert area units before scaling. Confidence depends on representative sampling. Patchy distribution, mistaken species identification and a small sample can all affect the estimate.

## Choosing and reading graphs

| Graph | Use | Main check |
|---|---|---|
| Bar chart | Categories, such as treatment types | Separate bars and labelled categories |
| Histogram | Numerical class intervals | Touching bars; with unequal widths, area represents frequency |
| Scatter diagram | Relationship between two numerical variables | Plot paired values and assess correlation |
| Line/curve | Ordered numerical variables, such as time/concentration | Appropriate best fit rather than invented point-to-point detail |

Use clearly labelled axes with units and even, sensible scales. Usually put independent variable on x and dependent on y. Describe **positive, negative or no correlation** and use values. Correlation alone is not proof of a causal mechanism.

Interpolate within the measured range more cautiously than reading a precise data point. **Extrapolation** extends beyond the observations and is less secure because the relationship may change. A graph need not start at zero unless it helps or the question requires it; inspect scales before comparing slopes or differences.

## Straight lines, gradients and curved rates

**y = mx + c** describes a straight line:

- **m = gradient = change in y/change in x**.
- **c = y-intercept**, where x = 0.
- A directly proportional relationship is a straight line through the origin, **y ∝ x**.

Choose a **large triangle on the best-fit line**. Use two points far apart, not two noisy raw observations.

**Example:** the line passes through (2, 5) and (8, 17).

1. Change in y = 17 − 5 = **12**.
2. Change in x = 8 − 2 = **6**.
3. Gradient = 12 ÷ 6 = **2**.
4. The y-intercept is **1**.

For a curve, draw a **tangent at the specified point** and calculate its gradient using a large triangle. This gives the instantaneous rate there. A chord across an interval gives an **average rate**, not the rate at one instant. For a decreasing pH curve the slope is negative; a stated magnitude of pH decline is positive. pH is unitless, so express the time basis clearly.

When given a rate–time graph, its area represents total change:

- Rectangle area = **rate × time**.
- Triangle area = **½ × base × height**.

Confirm the axis quantities before assigning meaning to an area.

## Algebra and mathematical symbols

| Symbol | Meaning |
|---|---|
| = | Equal |
| < | Less than |
| > | Greater than |
| ≪ | Much less than |
| ≫ | Much greater than |
| ∝ | Proportional to |
| ~ | Approximately equal or similar in an indicated context |

Rearrange using the same operation on both sides.

**Example: M = I/A**

1. Multiply both sides by A: **MA = I**.
2. Divide both sides by M: **A = I/M**.

Substitute only after identifying what each symbol represents. A familiar formula with mismatched units still gives a wrong answer.

## Areas, volumes and exchange surfaces

- Rectangle area = **length × width**.
- Triangle area = **½ base × perpendicular height**.
- Cube surface area = **6 × side²**.
- Cube volume = **side³**.
- **Surface area to volume ratio = total surface area/volume**.
- Circular inhibition-zone area = **πr²**, where radius = diameter/2.

![Cubes drawn to the same scale show how surface area to volume ratio decreases as size increases.](../Diagrams/cube-comparison.svg)

**Comparing cubes**

| Side length | Surface area | Volume | SA:V |
|---|---|---|---|
| 1 cm | 6 cm² | 1 cm³ | 6:1 |
| 3 cm | 54 cm² | 27 cm³ | 2:1 |

The larger cube has more total surface, but **less surface per unit volume**. This makes it harder for diffusion to meet all internal needs. Do not say its total surface is smaller.

**Example: a circular zone with diameter 10 mm**

1. Radius = 10 ÷ 2 = **5 mm**.
2. Area = π × 5² = **25π ≈ 78.5 mm²**.

If asked to exclude the disc, subtract the disc area. Keep the requested definition and unit clear.

## Calculation checks

1. Identify the quantity and choose the appropriate relationship.
2. Convert units and write substitution clearly.
3. Calculate while retaining extra figures.
4. Add the correct unit and requested precision.
5. Compare with an estimate and explain the result in its biological context.

## Sources

- [AQA Biology mathematical requirements](https://www.aqa.org.uk/subjects/biology/gcse/biology-8461/specification/mathematical-requirements)
'''
QUESTIONS=[
q(1,'Convert 2 mm to micrometres.','2000 µm.','MS1a;WS4.5'),q(1,'Write 0.000004 m in standard form.','4 ×10⁻⁶ m.','MS1b'),q(1,'How many significant figures are in 0.00620?','Three.','MS2a'),q(1,'What is the range of 5, 6, 8 and 12?','7.','MS2f'),q(1,'What is the probability of an impossible event?','Zero.','MS2e'),q(1,'What does ∝ mean?','Proportional to.','MS3a'),q(1,'Which graph shows paired numerical measurements to identify a correlation?','Scatter diagram.','MS2g'),q(1,'Does magnification have a unit?','No.','4.1.1.5'),
q(2,'Convert 0.035 mm to µm and then nm.','- 0.035 ×1000 = **35 µm**.\n- 35 ×1000 = **35 000 nm**.','WS4.5'),
q(2,'Convert 3.2 cm² to mm², explaining the factor.','- Each linear dimension is multiplied by 10, so area is multiplied by **100**.\n- 3.2 ×100 = **320 mm²**.','MS5c'),
q(2,'Calculate (6 ×10⁵)/(2 ×10²).','- Divide coefficients: 6/2 = 3. Subtract powers: 5−2 = 3.\n- Answer = **3 ×10³**.','MS1b'),
q(2,'Round 0.03476 to two significant figures and explain where counting starts.','- Count from the first non-zero digit, 3.\n- Rounded result = **0.035**.','MS2a'),
q(2,'Simplify 15:25 and express the first group as a fraction of the total.','- Ratio = **3:5**.\n- Fraction = 3/(3+5) = **3/8**.','MS1c'),
q(2,'Calculate the percentage represented by 27 successful outcomes out of 90.','- Percentage = 27/90 ×100.\n- Result = **30%**.','MS1c'),
q(2,'A microscope has ×10 eyepiece and ×40 objective. Determine its total power.','- Multiply eyepiece by objective: 10 ×40.\n- Total = **×400**.','RPA1'),
q(2,'An image is 30 mm long at ×500 magnification. Calculate actual size in µm.','- Actual = 30/500 = **0.060 mm**.\n- Convert: 0.060 ×1000 = **60 µm**.','4.1.1.5','2022 1H Q03.3: adapted numerical context'),
q(2,'A pondweed produces 18 cm³ oxygen in 6 minutes. Calculate rate per minute.','- Rate = volume/time = 18/6.\n- Rate = **3 cm³ min⁻¹**.','MS1c'),
q(2,'A reaction reaches a fixed endpoint in 40 s. Calculate reciprocal-time rate.','- Rate proxy = 1/40.\n- **0.025 s⁻¹**, for a comparable endpoint.','RPA5;RPA10'),
q(2,'A distance doubles in an inverse-square light model. What happens to intensity?','- Intensity ∝ 1/d².\n- New intensity = **1/4** of the original.','4.4.1.2'),
q(2,'Explain why a positive correlation does not prove causation.','- Values tend to rise together in the data.\n- Another variable may affect both, so a controlled comparison is needed to isolate a cause.','MS2g;WS3.6'),
q(2,'Distinguish interpolation from extrapolation.','- Interpolation estimates **within** the measured range.\n- Extrapolation extends **outside** it, where the relationship may change.','MS4a'),
q(2,'A bacterium is 2 µm long and a cell is 20 µm long. Compare their linear scale.','- 20/2 = **10 times**.\n- The cell is about **one order of magnitude** larger in length.','MS2h'),
q(3,'Calculate percentage mass change from 2.50 g to 2.10 g.','- Change = 2.10−2.50 = **−0.40 g**.\n- Percentage = −0.40/2.50 ×100.\n- **−16%**, a 16% decrease.','MS1c;RPA3'),
q(3,'A success rate rises from 20% to 30%. Calculate percentage-point change and relative percentage increase.','- Difference = **10 percentage points**.\n- Relative increase = (30−20)/20 ×100.\n- Relative increase = **50%**.','MS1c'),
q(3,'A 4 µm scale bar measures 8 mm on an image. A cell measures 30 mm. Calculate cell size.','- Cell/bar image-length ratio = 30/8 = 3.75.\n- Actual cell size = 3.75 ×4.\n- **15 µm**.','4.1.1.5'),
q(3,'Calculate biomass-transfer efficiency if 45 kg is gained from 600 kg available.','- Efficiency = next/previous ×100.\n- 45/600 ×100.\n- **7.5%**, using matching mass units/basis.','4.7.4.3'),
q(3,'For counts 1, 2, 2, 7, calculate mean, median and mode.','- Mean = 12/4 = **3**.\n- Median = (2+2)/2 = **2**.\n- Mode = **2**.','MS2b;MS2f'),
q(3,'Counts 0, 1 and 2 occur with frequencies 3, 4 and 3. Calculate the mean.','- Total count = 0×3 +1×4 +2×3 = **10**.\n- Total frequency = 3+4+3 = **10**.\n- Mean = 10/10 = **1**.','MS2c'),
q(3,'A carrier cross predicts a 1/4 affected probability. Calculate expected affected count in 120 births and explain its limitation.','- Expected count = 120 ×1/4.\n- **30** affected births expected.\n- Random variation means an actual sample need not have exactly 30.','MS2e'),
q(3,'A line passes through (2, 6) and (8, 18). Find gradient and intercept.','- Gradient = (18−6)/(8−2) = **2**.\n- Use y = 2x+c: 6 = 4+c, so **c = 2**.\n- Equation: **y = 2x+2**.','MS4b;MS4d'),
q(3,'A tangent to a pH-time curve passes through (1 day, pH 7) and (5 days, pH 5). Calculate slope and describe the change.','- Slope = (5−7)/(5−1).\n- **−0.5 per day**.\n- At the tangent point, pH decreases at magnitude **0.5 per day**.','MS4d;WS3.3','2023 2H Q04.4: adapted tangent calculation'),
q(3,'A 12 mm circular inhibition zone includes its disc. Calculate area to three significant figures.','- Radius = **6 mm**.\n- Area = π ×6² = 113.097…\n- **113 mm²**.','MS5c;RPA2'),
q(4,'A 2 cm cube exchanges substances through its surface. Calculate surface area, volume and SA:V ratio.','- Surface area = 6 ×2² = **24 cm²**.\n- Volume = 2³ = **8 cm³**.\n- SA:V = 24:8 = **3:1**.\n- It has less surface per unit volume than a 1 cm cube, making diffusion less effective for meeting internal demand.','MS5c;4.1.3.1'),
q(4,'Ten 0.25 m² quadrats contain a total of 30 plants. Estimate population in a 150 m² habitat and state a limitation.','- Mean = 30/10 = **3 per quadrat**.\n- Density = 3/0.25 = **12 plants m⁻²**.\n- Estimated population = 12 ×150 = **1800**.\n- Patchy distribution or biased/limited sampling may make the estimate unrepresentative.','MS2d;RPA9'),
q(4,'Explain how to calculate the rate at one instant on a curved biological graph.','- Draw a **tangent at the specified point**.\n- Use two well-separated points on that tangent to form a large triangle.\n- Calculate change in y divided by change in x using actual axis scales.\n- State units/sign meaning; a chord across the curve gives an average rather than instantaneous rate.','MS4d;WS3.3'),
q(4,'A 10 mm inhibition zone contains a 4 mm disc. Calculate clear-agar area excluding the disc.','- Zone radius = 5 mm; total area = **25π mm²**.\n- Disc radius = 2 mm; disc area = **4π mm²**.\n- Clear area = (25−4)π = **21π mm²**.\n- ≈ **66.0 mm²**, to three significant figures.','MS5c;RPA2'),
q(4,'Two independent births each have affected probability 1/4. Find probabilities of both affected and exactly one affected.','- Both affected = 1/4 ×1/4 = **1/16**.\n- First affected, second unaffected = 1/4 ×3/4 = **3/16**.\n- First unaffected, second affected also **3/16**.\n- Exactly one = 3/16+3/16 = **6/16 = 3/8**.','MS2e'),
q(4,'A rate rises linearly from 0 to 6 cm³ min⁻¹ over 4 minutes. Calculate total gas produced from the rate-time graph.','- Total change is the **area under the rate–time graph**.\n- Region is a triangle: ½ ×base ×height.\n- ½ ×4 ×6 = **12**.\n- Units min ×cm³ min⁻¹ give **12 cm³**.','WS3.3;MS5c')]
MAPS=[
m('00-biology-maths-overview','Biology maths',p('Units and size','Convert before substituting.','mm, µm and nm differ by factors of 1000.','Square/cube conversion factors for area/volume.','Standard form: 1 ≤ coefficient <10.'),p('Fractions and changes','Part/whole ×100 gives percentage.','(New − original)/original ×100 gives change.','Ratios need both groups in the total.','Check percentage points versus relative change.'),p('Magnification and rates','Magnification = image/actual size.','Rate = change/time. Same-endpoint proxy = 1/time.','Efficiency = next/previous biomass ×100.','Light intensity ∝ 1/distance² in suitable model.'),p('Probability and data','Expected count = probability × trials.','Mean, median, mode and range describe data.','Random representative samples reduce bias.','Correlation alone does not prove causation.'),p('Graphs and algebra','y = mx+c: gradient and intercept.','Large triangle on best-fit line/tangent.','Rearrange with matching operations.','Use units and sensible significant figures.'),p('Geometry','Rectangle: length ×width. Triangle: ½bh.','Cube: surface 6a², volume a³.','SA:V falls as size rises.','Circle area πr², using half-diameter.')),
m('01-units-and-proportions','Units, standard form and proportions',p('Unit ladder','1 m = 100 cm = 1000 mm.','1 mm = 1000 µm. 1 µm = 1000 nm.','Smaller unit: larger numerical value.','kg, g, mg follow ×1000 steps.'),p('Area and volume','1 cm² = 100 mm².','1 cm³ = 1000 mm³.','1000 cm³ = 1 dm³.','Convert powers, not just one length.'),p('Standard form','a ×10ⁿ with 1 ≤a <10.','0.0000062 = 6.2 ×10⁻⁶.','Multiply: add powers. Divide: subtract powers.','Negative exponent is a fraction, not negative length.'),p('Rounding and estimates','0.00450 has three significant figures.','Round final result, not intermediate steps.','Estimate expected scale to catch errors.','Tenfold difference: one order of magnitude.'),p('Fractions and ratios','Part/whole ×100 = percentage.','1:3 gives first fraction 1/4.','Match units before simplifying ratios.','Probability lies between 0 and 1.'),p('Percentage change','(New − original)/original ×100.','Keep negative sign for a decrease.','20% to 30%: +10 percentage points.','Relative increase: 50%.')),
m('02-calculations-and-inheritance','Magnification, rates and inheritance',p('Image sizes','M = image/actual. Actual = image/M.','Use same unit for both sizes.','36 mm at ×600: 60 µm actual.','Magnification has no unit.'),p('Scale bars','Cell/bar image ratio ×bar actual length.','36 mm cell, 10 mm bar labelled 5 µm.','Actual cell = 18 µm.','Resizing preserves ratios when bar resizes too.'),p('Rate calculations','Change/time; state time basis.','12 cm³ in 4 min: 3 cm³ min⁻¹.','Same-endpoint rate proxy: 1/time.','25 s gives 0.040 s⁻¹.'),p('Transfer and light','Efficiency = next/previous biomass ×100.','40/500 ×100 = 8%.','Intensity ∝ 1/d². Triple distance: 1/9 intensity.','Photosynthesis can have other limiting factors.'),p('Inheritance probabilities','Aa ×Aa: AA, Aa, Aa, aa.','aa: 1/4 affected. Aa: 1/2 carrier.','Expected number = probability ×trials.','Actual counts vary randomly.'),p('Independent events','Multiply independent probabilities.','Both affected: 1/4 ×1/4 = 1/16.','Exactly one: add both possible orders.','Each pregnancy is a new event.')),
m('03-data-graphs-and-algebra','Data, graphs and algebra',p('Averages and spread','Mean: total/count. Median: ordered middle.','Mode: most frequent. Range: max−min.','Frequency mean: Σ(value ×frequency)/Σfrequency.','Investigate anomalies before exclusion.'),p('Sampling estimate','Mean per quadrat ×habitat/quadrat area.','Mean 6 in 0.5 m², habitat 200 m²: 2400.','Representative random samples for overall abundance.','Transects for distribution gradients.'),p('Choose a graph','Bars: categories. Histogram: numerical intervals.','Scatter: paired numerical variables.','Line/curve: suitable ordered relationship.','Label quantity, unit and sensible scale.'),p('Interpret relationships','Positive, negative or no correlation.','Use data values and consider other influences.','Interpolate within measured range.','Extrapolation beyond range is less secure.'),p('Gradient and intercept','y = mx+c. m = Δy/Δx, c at x=0.','Large triangle on best-fit line.','Tangent at specified point gives instantaneous rate.','A chord gives an interval average.'),p('Algebra and units','Rearrange using same operation on both sides.','M = I/A gives A = I/M.','Rate–time area gives total change where appropriate.','Check units, sign and final precision.')),
m('04-geometry-and-exchange','Geometry and exchange surfaces',p('Area formulas','Rectangle: length ×width.','Triangle: ½base ×perpendicular height.','Areas use squared units.','Use consistent lengths.'),p('Cube formulas','Surface area = 6a².','Volume = a³.','SA:V = surface/volume.','Double side: fourfold surface, eightfold volume.'),p('Same-scale comparison','Larger total surface, smaller surface per volume.',visual={'kind':'cubes','after':0}),p('Diffusion consequence','Lower SA:V gives less exchange surface per internal volume.','Longer distances also slow diffusion.','Large organisms need specialised exchange/transport.','Total surface area is not the ratio.'),p('Circles and zones','Radius = diameter/2. Area = πr².','12 mm diameter: about 113 mm².','Subtract disc area only if requested.','Use squared length units.'),p('Calculation routine','Choose relation and convert units.','Show substitution and working.','Round only final result.','Estimate and explain biological meaning.'))]
GROUPS=[('numbers','Units and numerical skills','Convert, estimate, round and compare proportions.','biology-cells',['Units, prefixes and standard form','Estimates, scale and significant figures','Ratios, fractions and percentages']),('calculations','Biological calculations','Work with images, rates, efficiencies and inheritance.','biology-cells',['Magnification and scale bars','Rates, efficiency and inverse relationships','Probability in inheritance']),('data','Data, graphs and algebra','Interpret samples, distributions and relationships.','biology-leaf',['Averages, spread and frequency tables','Sampling and population estimates','Choosing and reading graphs','Straight lines, gradients and curved rates','Algebra and mathematical symbols']),('geometry','Geometry and exchange','Calculate area, volume and ratios with correct units.','biology-cells',['Areas, volumes and exchange surfaces','Calculation checks'])]
if __name__=='__main__':
    write('Biology - AQA',9,dict(notes=NOTES,groups=GROUPS,questions=QUESTIONS,maps=MAPS,diagrams=[('cube-comparison','cubes',580)],coverage=['Mathematical requirements 1a–1d,2a–2h,3a/3d,4a–4d,5c','WS3.3;WS4.3–4.6','Topic-specific magnification,probability,rate/efficiency,sampling,inverse-square and inhibition-area calculations'],checklist={'Arithmetic':'Decimals,standard form,ratios/fractions/percentages,estimates','Data':'Significant figures,means,frequency distributions/bars/histograms,sampling,probability,median/mode,scatter correlation,orders of magnitude','Algebra/graphs':'All stated symbols,solve/rearrange,numerical/graph translation,y=mx+c,plotting,slope/intercept and applied tangents','Geometry':'Triangles/rectangles,cube surface/volume and applied circular areas'},evidence='All questions use original values. June 2022 Paper 1 Higher Q03.3 verifies magnification/rearrangement/unit conversion as an assessed type; June 2023 Paper 2 Higher Q04.4 verifies tangent rate comparison. Other practice follows the current mathematical requirements and topic calculations. These examples do not support a frequency ranking.'))
