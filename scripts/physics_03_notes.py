from physics_helpers import notes
notes(3,r'''
## Particles, states and density

A material's particles stay the same when it changes state; their **arrangement and movement** change. Imagine the same people in fixed theatre seats, moving around a crowded room, then spread across a field. The people do not become larger or vanish.

| State | Arrangement | Movement | Shape and volume |
|---|---|---|---|
| Solid | Close together, usually ordered | Vibrate about fixed positions | Fixed shape and volume |
| Liquid | Close together, irregular | Move past one another | Fixed volume; takes container's shape |
| Gas | Far apart | Rapid, random motion | Fills container; easily compressed |

**Density is mass per unit volume: ρ = m/V.** Use kg and m³ for kg/m³, or g and cm³ for g/cm³.

Gases usually have much lower density because particles are much farther apart. Many solids are denser than their liquids, but **ice is less dense than liquid water**. Particle arrangement, not a change in individual particle mass, explains this.

- **1 cm³ = 1 × 10⁻⁶ m³**; **1 g/cm³ = 1,000 kg/m³**.
- A block of mass 240 g and volume 80 cm³ has density **3.0 g/cm³ = 3,000 kg/m³**.
- For a fixed mass, expanding the volume **reduces density**. A 2.0 kg sample occupying 0.0010 m³ has density **2,000 kg/m³**.

## Practical: measure density

**Regular solid**

1. Measure mass using a zeroed balance.
2. Measure dimensions with a ruler, callipers or micrometer suitable for the object's size. Check zero and read carefully.
3. Calculate volume: for a cuboid **V = length × width × height**; for a cylinder **V = πr²h**.
4. Calculate **ρ = m/V**. Repeat dimensions at different positions if appropriate and use a representative mean.

**Irregular solid**

- Measure mass. Record water volume in a measuring cylinder, then fully submerge the object: **object volume = final − initial water volume**.
- Alternatively, fill a displacement can to the spout, let excess water finish draining, submerge the object and collect the displaced water in a measuring cylinder.
- Remove trapped air bubbles, avoid splashes and read the meniscus at eye level. Use a thin thread if needed. The method assumes the solid does not dissolve, absorb significant water or react with it.

**Liquid**

- Measure the mass of an empty, dry measuring cylinder, then the cylinder plus liquid.
- Subtract to get **liquid mass**. Read its volume at eye level, then use ρ = m/V.
- Repeats help assess random variation. A more suitable small-volume cylinder improves resolution; repeating a zero error does not remove it.

If a cylinder's mass rises from 45 g to 85 g when 50 cm³ of liquid is added, liquid density = (85 − 45)/50 = **0.80 g/cm³**. Do not include the container's mass.

## Changes of state conserve mass

- **Melting:** solid → liquid; **freezing:** liquid → solid.
- **Boiling or evaporation:** liquid → gas; **condensation:** gas → liquid.
- **Sublimation:** solid → gas without becoming liquid first.

These are **physical changes**: reversing them restores the material's original properties. No new substance is made. **Mass is conserved** when no material enters or leaves. An open beaker may lose mass because vapour escapes, not because particles are destroyed.

Evaporation occurs at a liquid's surface below its boiling point. Boiling occurs throughout the liquid at its boiling temperature for the prevailing pressure.

## Internal energy and temperature

**Internal energy is the total kinetic and potential energy of all the particles in a system.** Kinetic energy relates to their movement; potential energy relates to their arrangement and interactions.

Temperature relates to **average particle kinetic energy**, not the total energy of the sample. A large warm bath can have more internal energy than a tiny hotter cup. Heating can increase temperature or change state.

For a temperature rise without a state change, use **ΔE = mcΔθ**:

- ΔE in J, m in kg, c in J/kg°C, temperature change Δθ in °C.
- c is energy needed to warm **1 kg by 1°C**.
- 0.20 kg of water warming by 15°C, with c = 4,200 J/kg°C, gains **12,600 J**.
- At equal energy input, a larger mass or greater c gives a smaller temperature rise.

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

- **Sloping sections:** temperature and average kinetic energy rise; use **mcΔθ**.
- **Flat sections:** both states coexist, temperature stays constant, but internal energy rises as potential energy increases; use **mL**.
- Cooling reverses the changes: energy leaves the material.
- On a constant-power heating graph, a longer plateau means more energy transferred during that phase change for that sample.

**Two-stage example:** melt 0.10 kg of ice at 0°C and warm the water to 20°C. Use L = 334,000 J/kg and c = 4,200 J/kg°C.

E = mL + mcΔθ = 33,400 + 8,400 = **41,800 J**. A 100 W heater would take at least E/P = **418 s**; heat loss increases the real time.

To investigate latent heat of fusion, compare meltwater collected in a fixed time from ice at 0°C with and without an electrical heater. Subtract the unheated melting due to the room, measure input energy and use **L = E/extra mass melted**. Keep conditions alike and electrical connections clear of water.

## Gas pressure and temperature

Gas particles move randomly and collide with container walls. The collisions exert a force; **pressure is force per unit area**. The force on a wall is perpendicular to it.

At **constant volume and fixed gas mass**, heating makes average particle kinetic energy increase:

1. Particles move faster.
2. They collide with walls more often and change momentum more strongly in each collision.
3. The total force on a given area increases, so **pressure rises**.

A sealed, rigid tyre can therefore have higher pressure after warming. It is the **particles' motion**, not the individual particles becoming larger, that explains the change.

## Compressing and expanding gases

For a **fixed mass of gas at constant temperature**, **pV = constant**, so **p₁V₁ = p₂V₂**.

- Halving volume doubles pressure. Particles have the same average speed but collide with the walls more frequently per unit area.
- Increasing volume reduces pressure because wall collisions are less frequent per unit area.
- Use Pa and m³, or the same consistent pressure and volume units on both sides of a ratio calculation.

A gas at 100 kPa occupies 60 cm³. Slowly compressing it to 40 cm³ at constant temperature gives p₂ = 100 × 60/40 = **150 kPa**.

**Rapid compression is different:** pushing a bicycle pump does **work on the gas**, increasing its internal energy and temperature when there is little time for energy to escape. Pressure can then rise for two reasons: smaller volume and higher temperature. Do not use the constant-temperature pV rule if the question says temperature changes.
''',[
('matter','States and density','Explain particle arrangements and measure mass per volume.','physics-particles',['Particles, states and density','Practical: measure density','Changes of state conserve mass']),
('heating','Heating and changes of state','Read heating curves and choose the right energy equation.','physics-heat',['Internal energy and temperature','Latent heat and heating curves']),
('gas','Gas pressure','Connect particle collisions, temperature and volume.','physics-particles',['Gas pressure and temperature','Compressing and expanding gases'])],['4.3.1.1–4.3.1.2','4.3.2.1–4.3.2.3','4.3.3.1–4.3.3.3'],[5])
