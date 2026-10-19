from physics_helpers import notes
notes(2,r'''
## Charge, current and potential difference

A circuit needs a **complete conducting loop** and a source of **potential difference**. Think of a closed delivery route: charges circulate, carrying energy from the supply to components. The charges are not used up; energy is transferred.

**Current** measures how much charge passes a point each second.

**I = Q/t**

Rearranged to find charge:

**Q = It**

- **Q:** charge, in coulombs (C).
- **I:** current, in amperes (A).
- **t:** time, in seconds (s).

**Potential difference** tells you how much energy is transferred for each coulomb passing through a component.

Use **V = E/Q**.

One volt means one joule per coulomb.

**Resistance** describes how strongly a component opposes current.

Use **V = IR**, with resistance R in ohms (Ω).

At the same potential difference, a greater resistance produces a smaller current.

In metal wires, electrons are the moving charges. **Conventional current** goes from positive to negative outside the supply. Electrons move in the opposite direction.

**Example: charge transferred**

A current of 0.40 A flows for 50 s.

Q = It = 0.40 × 50 = **20 C**

**Example: resistance**

A component has 6.0 V across it and carries 0.20 A.

R = V/I = 6.0 ÷ 0.20 = **30 Ω**

## Circuit symbols and measuring resistance

![Standard circuit symbols: cell, battery, switch, resistor, variable resistor, lamp, ammeter, voltmeter, diode, LED, thermistor and LDR.](../Diagrams/circuit-symbols.svg)

Draw wires as straight lines and use **standard symbols**, not pictures of equipment. A dot marks a connected junction; crossing wires without a dot need not be connected.

![A low-voltage circuit with an ammeter in series and a voltmeter in parallel across the test resistor.](../Diagrams/resistance-circuit.svg)

- **Ammeter in series**: it measures charge flow through the component.
- **Voltmeter in parallel**: it compares potential at the component's two ends.
- Include a variable resistor to adjust current. Calculate **R = V/I** from a matched pair of readings.
- Do not connect an ammeter directly across the supply: its low resistance would allow a dangerously large current.

## Series and parallel circuits

| Feature | Series: one loop | Parallel: separate branches |
|---|---|---|
| Current | Same through every component | Total current = sum of branch currents |
| Potential difference | Shared; component values add to supply pd | Same across each branch connected to the supply |
| Resistance | **Rtotal = R₁ + R₂ + …** | Total is smaller than the smallest branch resistance |
| Adding a resistor | More opposition in the route; current falls for fixed supply pd | Extra route for charge; total current rises for fixed supply pd |
| Broken component | Breaks the whole loop | Other complete branches can still work |

**Series example**

Two resistors, 4 Ω and 8 Ω, are connected in series across 12 V.

1. Add the resistances: R = 4 + 8 = **12 Ω**.
2. Find the current: I = V/R = 12 ÷ 12 = **1 A**.
3. The potential differences are **4 V and 8 V**, adding to the 12 V supply.

**Parallel example:** two branches across 6 V have currents 0.30 A and 0.20 A.

Total current is **0.50 A**.

Both branches have **6 V** across them.

Charge is conserved at a junction; it does not collect there.

A household circuit uses parallel branches so appliances receive the same supply voltage and can be switched independently. You do not need a reciprocal-resistance formula to explain why adding a parallel path reduces the total resistance.

## Components and I–V graphs

On an **I–V graph**, current is usually vertical and potential difference horizontal. Check the axes: reversing them changes the meaning of the gradient.

![Current–voltage graphs for a constant-temperature resistor, filament lamp and diode.](../Diagrams/iv-graphs.svg)

**Ohmic conductor:** at constant temperature, **current is directly proportional to potential difference**. Its I–V graph is a straight line through the origin because resistance stays constant. On these axes, the gradient is **1/R**.

**Filament lamp:** increasing current heats the filament. The metal ions vibrate more and interfere more with electron flow. **Resistance increases**, so the I–V curve becomes less steep as the size of the potential difference increases. Calculate resistance using **V/I at a particular point**. The gradient of a tangent does not generally give 1/R for this changing resistance.

**Diode:** current flows readily in the forward direction once the forward potential difference is large enough. In reverse, resistance is very high. Its graph is therefore not symmetric. An **LED** is a light-emitting diode.

**Thermistor:** the type studied has a **lower resistance at a higher temperature**. This makes it useful as a temperature sensor, for example in a thermostat.

**LDR:** its **resistance decreases as light intensity increases**. With a suitable control circuit, it can help switch a light on when it gets dark.

For sensors, connect the change to current or pd in the actual circuit given. Do not assume every thermistor circuit switches on when hot: that depends on how the control circuit is arranged.

## Practical: resistance of a wire and resistor combinations

1. Fix a uniform resistance wire alongside a ruler. Connect a low-voltage supply, switch and ammeter in series; put a voltmeter across the measured wire length.
2. Use a movable contact to choose the length. Record V and I, then calculate **R = V/I**.
3. Repeat for several lengths, keeping **material, cross-sectional area and temperature** constant. Use a low current and switch off between readings to limit heating.
4. Repeat measurements, calculate means and plot **resistance against length**. For a uniform wire at constant temperature, the graph is approximately a straight line through the origin.
5. Longer wire gives electrons more opportunities to interact with the lattice, increasing resistance. A hot wire would also change resistance and spoil the comparison.

For combinations, measure each resistor, then measure the pair in series and parallel. The series total should match the sum; the parallel total should be smaller than either resistor. Measure at a suitable low voltage so heating is small. Secure connections and avoid touching hot wire.

## Practical: investigate I–V characteristics

- Set up the ammeter/voltmeter circuit above. Use a variable resistor or adjustable supply to vary pd.
- Record matched **V and I** readings across a useful range, keeping within component ratings.
- Reverse the supply to obtain negative readings; plot them with the correct signs.
- Repeat for a resistor, filament lamp and diode. Use a protective series resistor with the diode.
- For the ohmic resistor, limit heating so temperature stays approximately constant. For the lamp, the changing filament temperature is part of its behaviour.
- Repeat doubtful measurements. Draw suitable best-fit lines or smooth curves and explain them using resistance, temperature and direction of conduction.

## Electrical energy and power

| Equation | Use |
|---|---|
| **P = VI** | Electrical power from pd and current |
| **P = I²R** | Heating power from current and resistance |
| **E = Pt** | Energy from power and time |
| **E = QV** | Energy transferred by a quantity of charge |

**Symbols and units**

| Symbol | Quantity | Unit |
|---|---|---|
| P | Power | watts (W) |
| V | Potential difference | volts (V) |
| I | Current | amperes (A) |
| R | Resistance | ohms (Ω) |
| E | Energy transferred | joules (J) |
| t | Time | seconds (s) |
| Q | Charge | coulombs (C) |

**Example: energy supplied to a motor**

A 12 V motor carries 2.0 A for 30 s.

1. Calculate power: P = VI = 12 × 2.0 = **24 W**.
2. Calculate energy: E = Pt = 24 × 30 = **720 J**.

Not all of this energy becomes useful movement.

A 10 Ω resistor carrying 0.50 A transfers P = 0.50² × 10 = **2.5 W**.

Doubling current at fixed R gives **four times the heating power**.

An electric heater increases thermal stores; a motor transfers energy into movement as well as unwanted heating. For equal running time, greater power means more energy transferred. A high power rating does not alone tell you efficiency.

## Mains electricity and safety

**Direct potential difference** has one polarity, such as a cell. **Alternating potential difference** repeatedly reverses polarity, making current reverse direction. UK mains is about **230 V at 50 Hz**.

| Wire | Colour | Role |
|---|---|---|
| Live | **Brown** | Carries alternating pd; about 230 V relative to earth |
| Neutral | **Blue** | Completes the normal circuit; close to 0 V |
| Earth | **Green and yellow** | Safety connection; normally carries no current; 0 V |

If live touches an earthed metal case, a large fault current flows through the earth path. A correctly fitted fuse melts or circuit breaker opens, disconnecting the supply. A fuse belongs in the **live wire**. Double-insulated appliances use insulating barriers and do not need a metal-case earth connection.

A connection from live to earth through a person can give a dangerous shock. A live wire can still be dangerous when an appliance switch is open, because the supply side remains connected to live. School circuit experiments use **low-voltage supplies**, not mains wiring.

## The National Grid

The **National Grid** is a system of cables and transformers that links power stations to consumers.

**Generator → step-up transformer → transmission cables → step-down transformer → consumers.**

1. The **step-up transformer increases the potential difference** before transmission.
2. For the **same transferred power**, a higher potential difference means a lower current because **P = VI**.
3. The cables heat up as current flows. Their heating power is **P = I²R**, so reducing current greatly reduces energy loss.
4. **Step-down transformers reduce the potential difference** for the supplies needed by homes and other consumers.

For example, halving the current makes the heating power **one quarter** as large if the cable resistance stays the same. High-voltage transmission reduces the current needed; it does **not** reduce the cable's resistance.

## Static charge and electric fields

Rubbing two suitable insulators transfers **electrons**, not protons. The one gaining electrons becomes negative; the other loses the same number and becomes equally positive. Charge is transferred, not created.

- **Like charges repel; unlike charges attract**. The force acts without contact.
- An **electric field** is a region where a charge experiences a force. Field direction is the force direction on a **positive test charge**.
- Around an isolated positive sphere, lines point **radially outwards**; around a negative sphere, **inwards**. Field lines never cross.
- The field is stronger close to the object; lines are closer together there. Charges farther away experience a weaker force.
- A sufficiently strong electric field can **ionise air**, making it conducting. Charge suddenly flows through the air as a **spark**, reducing the charge imbalance.

The tiny moving electron and the much larger charged object are different scales. An insulating rod does not become charged because whole atoms travel from one end to the other.
''',[
('circuits','Circuits and components','Connect charge flow, resistance and circuit behaviour.','physics-circuit',['Charge, current and potential difference','Circuit symbols and measuring resistance','Series and parallel circuits','Components and I–V graphs']),
('practicals','Circuit practicals','Measure resistance and investigate component graphs.','physics-circuit',['Practical: resistance of a wire and resistor combinations','Practical: investigate I–V characteristics']),
('power','Power, mains and static','Explain energy transfer, safety, the Grid and electric fields.','physics-energy',['Electrical energy and power','Mains electricity and safety','The National Grid','Static charge and electric fields'])],['4.2.1.1–4.2.1.4','4.2.2','4.2.3.1–4.2.3.2','4.2.4.1–4.2.4.3','4.2.5.1–4.2.5.2'],[3,4])
