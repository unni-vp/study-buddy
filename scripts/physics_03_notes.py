from physics_helpers import notes
notes(3,r'''
## Particles, states and density

A material's particles stay the same when it changes state; their **arrangement and movement** change. Imagine the same people in fixed theatre seats, moving around a crowded room, then spread across a field. The people do not become larger or vanish.

| State | Arrangement | Movement | Shape and volume |
|---|---|---|---|
| Solid | Close together, usually ordered | Vibrate about fixed positions | Fixed shape and volume |
| Liquid | Close together, irregular | Move past one another | Fixed volume; takes container's shape |
| Gas | Far apart | Rapid, random motion | Fills container; easily compressed |

**Density is mass per unit volume.**

**ρ = m/V**

- **ρ:** density, in kg/m³.
- **m:** mass, in kg.
- **V:** volume, in m³.

Alternatively, use mass in g and volume in cm³ to obtain density in g/cm³.

Gases usually have much lower density because particles are much farther apart. Many solids are denser than their liquids, but **ice is less dense than liquid water**. Particle arrangement, not a change in individual particle mass, explains this.

**Useful conversions**

- **1 cm³ = 1 × 10⁻⁶ m³**
- **1 g/cm³ = 1,000 kg/m³**

**Example: a solid block**

Mass = 240 g. Volume = 80 cm³.

Density = 240 ÷ 80 = **3.0 g/cm³ = 3,000 kg/m³**.

**Example: a larger sample**

Mass = 2.0 kg. Volume = 0.0010 m³.

Density = 2.0 ÷ 0.0010 = **2,000 kg/m³**.

For a fixed mass, expanding the volume **reduces density**.

## Practical: measure density

**Regular solid**

1. Measure mass using a zeroed balance.
2. Measure dimensions with a ruler, callipers or micrometer suitable for the object's size. Check zero and read carefully.
3. For a cuboid, calculate **V = length × width × height**.
4. For a cylinder, calculate **V = πr²h** instead.
5. Calculate **ρ = m/V**. Repeat dimensions at different positions if appropriate and use a representative mean.

**Irregular solid**

- Measure mass. Record water volume in a measuring cylinder, then fully submerge the object: **object volume = final − initial water volume**.
- Alternatively, fill a displacement can to the spout, let excess water finish draining, submerge the object and collect the displaced water in a measuring cylinder.
- Remove trapped air bubbles, avoid splashes and read the meniscus at eye level. Use a thin thread if needed. The method assumes the solid does not dissolve, absorb significant water or react with it.

**Liquid**

- Measure the mass of an empty, dry measuring cylinder, then the cylinder plus liquid.
- Subtract to get **liquid mass**. Read its volume at eye level, then use ρ = m/V.
- Repeats help assess random variation. A more suitable small-volume cylinder improves resolution; repeating a zero error does not remove it.

**Example: liquid density**

A cylinder's mass rises from 45 g to 85 g when 50 cm³ of liquid is added.

1. Subtract the container's mass: liquid mass = 85 − 45 = **40 g**.
2. Calculate density: ρ = 40 ÷ 50 = **0.80 g/cm³**.

Do not include the container's mass.

## Changes of state conserve mass

- **Melting:** solid → liquid.
- **Freezing:** liquid → solid.
- **Boiling or evaporation:** liquid → gas.
- **Condensation:** gas → liquid.
- **Sublimation:** solid → gas without becoming liquid first.

These are **physical changes**: reversing them restores the material's original properties. No new substance is made. **Mass is conserved** when no material enters or leaves. An open beaker may lose mass because vapour escapes, not because particles are destroyed.

Evaporation occurs at a liquid's surface below its boiling point. Boiling occurs throughout the liquid at its boiling temperature for the prevailing pressure.

## Internal energy and temperature

**Internal energy** is the total kinetic and potential energy of all the particles in a system. The kinetic part comes from their movement. The potential part depends on their arrangement and interactions.

**Temperature** tells you about average particle kinetic energy. It does not tell you the total energy of the whole sample. A warm bath contains far more water than a tiny hotter cup, so the bath can have more internal energy even though its temperature is lower.

Heating transfers energy into the material. This can make the particles move faster and raise the temperature. Alternatively, it can change their arrangement during a **change of state**.

For a temperature rise without a change of state, use **ΔE = mcΔθ**.

| Quantity | Meaning and unit |
|---|---|
| ΔE | Energy transferred, in J |
| m | Mass, in kg |
| c | Specific heat capacity, in J/kg°C |
| Δθ | Final temperature minus initial temperature, in °C |

**Specific heat capacity** is the energy needed to warm **1 kg by 1°C**.

For example, 0.20 kg of water warming by 15°C gains 0.20 × 4200 × 15 = **12 600 J**.

If the same energy is supplied to a greater mass, the temperature rise is smaller. A material with a larger specific heat capacity also warms less for the same mass and energy input.

## Latent heat and heating curves

At a state change, energy can increase **particle potential energy** without increasing average kinetic energy. Imagine paying to rearrange a room rather than paying people to move faster.

**Specific latent heat** is energy needed to change the state of **1 kg without changing its temperature**. Its unit is **J/kg**, unlike specific heat capacity.

**E = mL**

- **Fusion:** melting or freezing.
- **Vaporisation:** boiling or condensation.
- Melting and boiling absorb energy; freezing and condensation release energy.
- Melting 0.10 kg of ice already at its melting point, with L = 334,000 J/kg, needs **33,400 J**.

![A heating curve with rising temperature between state changes and flat sections during melting and boiling.](../Diagrams/heating-curve.svg)

For a pure substance at constant pressure:

**Sloping sections:** the temperature rises, so the particles' average kinetic energy increases. Use **E = mcΔθ** to calculate the energy for this temperature change.

**Flat sections:** two states coexist while the material melts or boils. Its temperature stays constant. Energy increases the particles' potential energy as their arrangement changes, so internal energy still rises. Use **E = mL** for this stage.

Cooling reverses these changes as energy leaves the material. On a constant-power heating graph, a longer flat section means more energy is transferred during that phase change for that sample.

**Two-stage example:** melt 0.10 kg of ice at 0°C and warm the water to 20°C. Use L = 334,000 J/kg and c = 4,200 J/kg°C.

1. Melt the ice: E = mL = 0.10 × 334 000 = **33 400 J**.
2. Warm the water: E = mcΔθ = 0.10 × 4200 × 20 = **8400 J**.
3. Add the two amounts: total energy = 33 400 + 8400 = **41 800 J**.
4. With a 100 W heater, the minimum time is E/P = 41 800 ÷ 100 = **418 s**. Heat loss makes the actual time longer.

To investigate latent heat of fusion, compare meltwater collected in a fixed time from ice at 0°C with and without an electrical heater. Subtract the unheated melting due to the room, measure input energy and use **L = E/extra mass melted**. Keep conditions alike and electrical connections clear of water.

## Gas pressure and temperature

Gas particles move randomly and collide with container walls. The collisions exert a force; **pressure is force per unit area**. The force on a wall is perpendicular to it.

At **constant volume and fixed gas mass**, heating makes average particle kinetic energy increase:

1. Particles move faster.
2. They collide with walls more often and change momentum more strongly in each collision.
3. The total force on a given area increases, so **pressure rises**.

A sealed, rigid tyre can therefore have higher pressure after warming. It is the **particles' motion**, not the individual particles becoming larger, that explains the change.

## Compressing and expanding gases

For a **fixed mass of gas at constant temperature**:

**pV = constant**

For two states of the same gas:

**p₁V₁ = p₂V₂**

**When volume decreases:** the particles have less space to move in. At constant temperature their average speed stays the same, but collisions with the walls become more frequent per unit area. Pressure rises. Halving the volume doubles the pressure.

**When volume increases:** wall collisions become less frequent per unit area, so pressure falls.

Use Pa and m³, or keep the pressure and volume units consistent on both sides of a ratio calculation.

**Example: compressing a gas**

A gas at 100 kPa occupies 60 cm³. It is slowly compressed to 40 cm³ at constant temperature.

1. Rearrange: p₂ = p₁V₁/V₂.
2. Substitute: p₂ = 100 × 60 ÷ 40.
3. The new pressure is **150 kPa**.

**Rapid compression is different:** pushing a bicycle pump does **work on the gas**, increasing its internal energy and temperature when there is little time for energy to escape. Pressure can then rise for two reasons: smaller volume and higher temperature. Do not use the constant-temperature pV rule if the question says temperature changes.
''',[
('matter','States and density','Explain particle arrangements and measure mass per volume.','physics-particles',['Particles, states and density','Practical: measure density','Changes of state conserve mass']),
('heating','Heating and changes of state','Read heating curves and choose the right energy equation.','physics-heat',['Internal energy and temperature','Latent heat and heating curves']),
('gas','Gas pressure','Connect particle collisions, temperature and volume.','physics-particles',['Gas pressure and temperature','Compressing and expanding gases'])],['4.3.1.1–4.3.1.2','4.3.2.1–4.3.2.3','4.3.3.1–4.3.3.3'],[5])
