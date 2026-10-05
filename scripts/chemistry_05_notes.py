from chemistry_helpers import notes
notes(5,'Energy changes',r'''
## Exothermic and endothermic reactions

A reaction transfers energy between the reacting chemicals and their **surroundings**. Energy is conserved: it is transferred, not created or destroyed.

Think of the chemicals as an energy account. An exothermic reaction pays energy out to the surroundings; an endothermic reaction takes energy in.

| Reaction | Energy transfer | Surroundings | Examples |
|---|---|---|---|
| **Exothermic** | From reacting chemicals to surroundings | Temperature rises | Combustion, many oxidation reactions, neutralisation |
| **Endothermic** | From surroundings into reacting chemicals | Temperature falls | Thermal decomposition; citric acid reacting with sodium hydrogencarbonate |

- In an exothermic reaction, **products have less energy than reactants**. The difference is transferred out.
- In an endothermic reaction, **products have more energy than reactants**. The extra energy came from the surroundings.
- Temperature is measured in the surrounding solution or apparatus; be clear about **where the energy moves**.

### Applications

Exothermic reactions can warm hands or heat food in a self-heating can. Endothermic changes can cool a sports injury pack. Judge suitability using the **size of temperature change, duration, cost, portability, safety and disposal**. The biggest temperature rise is not necessarily safest for skin.

A reaction can need an initial spark or heating and still be exothermic overall. The initial energy helps it start; the net transfer is a different quantity.

## Reaction profiles and activation energy

A reaction profile plots **energy** vertically against **progress of reaction** horizontally. The horizontal axis is not a time scale.

The **activation energy** is the minimum energy that colliding particles need for a successful reaction. Imagine pushing a ball over a hill: even if the far side is lower, you first need to get over the top.

![Exothermic and endothermic profiles with activation energy measured from the reactants to the peak, and overall change measured between reactants and products.](../Diagrams/reaction-profiles.svg)

- Begin with a flat reactant level and finish with a flat product level.
- Join them with a **curved line rising to a peak**.
- Show activation energy from the **reactant level to the peak**.
- Show overall energy change **between reactant and product levels**.
- Exothermic: products **lower**. Endothermic: products **higher**.

Do not label the full height from the graph baseline as activation energy. Do not confuse the peak with the product energy level.

## Bond energies

**Breaking bonds requires energy. Making bonds releases energy.** Both happen during a reaction; compare their totals to decide the net change.

**Overall energy change = energy to break reactant bonds − energy released forming product bonds.**

| Calculation result | Meaning |
|---|---|
| Negative | More energy released than taken in: **exothermic** |
| Positive | More energy taken in than released: **endothermic** |

### Worked example

**H₂ + Cl₂ → 2HCl**. Supplied bond energies: H–H = 436, Cl–Cl = 243, H–Cl = 431 kJ/mol of bonds.

1. Break **one H–H and one Cl–Cl**: 436 + 243 = **679 kJ** for the molar quantities in the equation.
2. Form **two H–Cl bonds**: 2 × 431 = **862 kJ** released.
3. Overall change = 679 − 862 = **−183 kJ** for the equation as written.
4. It is **exothermic**, because forming product bonds releases 183 kJ more than breaking reactant bonds takes in.

Use the values supplied in the question, even if they differ from another data table. Count every bond and include the equation coefficients. A molecule of methane, CH₄, contains **four C–H bonds**; two water molecules contain **four O–H bonds** altogether.

### Find an unknown bond energy

For the same reaction, suppose overall change is −183 kJ and H–Cl bond energy is x:

**679 − 2x = −183**, so 2x = 862 and **x = 431 kJ/mol**.

The chemical bonds themselves do not release energy when broken. The release happens when the **new bonds form**.

## Required practical: temperature changes

Investigate how **acid concentration affects temperature change** when a fixed amount of alkali is neutralised. Make a prediction, then test it while controlling other variables.

1. Wear goggles. Place a **polystyrene cup in a beaker** for support; use a lid with a thermometer opening to reduce energy transfer to the surroundings.
2. Measure fixed volumes of acid and alkali. Allow them to reach the **same starting temperature**, then record that temperature.
3. Mix in the cup, replace the lid, stir consistently and record temperature at regular intervals. Find the **highest temperature** for an exothermic reaction or the lowest for an endothermic one.
4. Calculate **temperature change = final extreme temperature − initial temperature**. For 20.5 °C rising to 28.0 °C, the change is **+7.5 °C**.
5. Repeat with different acid concentrations, using fresh solutions each time.
6. Keep solution volumes, alkali concentration, starting temperature, apparatus and mixing/measurement method the same. Repeat each condition and calculate means.
7. Plot **acid concentration on the x-axis** and **temperature change on the y-axis**. Examine the trend and possible anomalies.

As acid concentration rises, more acid can react and the temperature rise may increase. Once **alkali is limiting**, extra acid cannot cause proportionally more neutralisation. Do not assume the graph rises forever.

### Improve the measurements

- A lid and insulation reduce **energy transfer to the surroundings**.
- Consistent stirring spreads thermal energy so the thermometer samples the mixture more fairly.
- Record promptly: missing the peak underestimates an exothermic temperature rise.
- Repeats and means reduce the effect of **random error**; they do not remove systematic thermometer error.
- If provided with a temperature–time graph, extend the appropriate trends back to the **mixing time** to estimate the temperature change before energy loss. Use the method shown in the question.

The same principles apply to displacement reactions, acid–metal reactions and acid–carbonate reactions. If gases form, allow them to escape safely; keep flames away from hydrogen. Explain each control in relation to the variable you are investigating.

## Cells and batteries

A chemical cell converts energy from a chemical reaction into **electrical energy**. A simple cell uses **two different metals in contact with an electrolyte**, connected through an external circuit.

- Reactions at the electrodes drive electrons through the wires.
- The electrolyte contains **mobile ions** and completes the internal path for charge.
- Cell voltage depends on the **electrode materials and electrolyte**.
- A **battery** consists of two or more cells in series. Their voltages add when connected in the same direction: three 1.5 V cells give **4.5 V**.

### Comparing cells

Connect a voltmeter to a fixed reference electrode and a test metal in the same electrolyte. Change the test metal while keeping electrolyte type/concentration, temperature and the electrode setup constant.

In a given series of measurements, the polarity and voltage help order metal reactivity. **Use the stated lead convention**: a negative voltage means the polarity is reversed relative to the chosen reference, not that the cell has “negative energy”. Do not assume the highest signed reading is always the most reactive without checking the setup.

| Cell type | Why it stops or how it is renewed |
|---|---|
| **Non-rechargeable**, including ordinary alkaline cells | A reactant is used up, so the reaction stops |
| **Rechargeable** | An external electrical current **reverses the chemical reactions**, restoring reactants |

Compare lifetime cost, capacity, mass, recharge time, replacement frequency and disposal. Do not try to recharge a cell designed for single use.

## Hydrogen fuel cells

A fuel cell produces electricity while **fuel and oxygen are supplied continuously from outside**. In a hydrogen fuel cell, hydrogen is oxidised and the overall product is water:

**2H₂ + O₂ → 2H₂O.**

Think of a fuel cell as a device fed from a tank; a conventional battery contains its reacting chemicals inside. A fuel cell keeps operating while the external supply continues.

![Acidic hydrogen fuel cell showing electron movement through a load, hydrogen ion movement through the electrolyte, and water formed at the oxygen electrode.](../Diagrams/hydrogen-fuel-cell.svg)

### Electrode half-equations

For an **acidic electrolyte**:

- Hydrogen electrode, oxidation: **2H₂ → 4H⁺ + 4e⁻**.
- Oxygen electrode, reduction: **O₂ + 4H⁺ + 4e⁻ → 2H₂O**.

Add them and cancel H⁺ and electrons to recover the overall reaction. Electrons travel through the **external circuit**; ions move through the **electrolyte**.

If the question specifies an **alkaline electrolyte**, use:

- Hydrogen electrode: **2H₂ + 4OH⁻ → 4H₂O + 4e⁻**.
- Oxygen electrode: **O₂ + 2H₂O + 4e⁻ → 4OH⁻**.

These also sum to 2H₂ + O₂ → 2H₂O. Do not mix an acidic half-equation with an alkaline one. Balance both **atoms and charge**.

### Fuel cells compared with rechargeable batteries

| Issue | Hydrogen fuel cell | Rechargeable battery |
|---|---|---|
| Renewing supply | Refuel hydrogen tank; oxygen usually supplied from air | Recharge using electricity |
| During use | Produces water; no direct CO₂ from the hydrogen reaction | No direct exhaust gas from electrical operation |
| Energy source | Hydrogen must be produced; this may use fossil fuels or electricity | Charging electricity may be renewable or fossil-fuel-generated |
| Storage and equipment | Hydrogen storage and transport are difficult; it is flammable; specialised tanks and infrastructure needed | Batteries can be heavy and take time to recharge; performance depends on design |
| Resources and lifetime | Catalysts and equipment have costs and environmental impacts | Manufacture uses materials and energy; finite lifetime and recycling matter |

A hydrogen fuel cell is **not automatically carbon-free overall** just because it makes only water during use. Evaluate hydrogen production, electricity generation, storage, efficiency and lifespan using the data supplied. Both options have advantages in different situations.
''',[
('energy','Energy transfers and practicals','Read profiles, calculate bond energies and investigate temperature.','practical',['Exothermic and endothermic reactions','Reaction profiles and activation energy','Bond energies','Required practical: temperature changes']),
('cells','Cells, batteries and fuel cells','Explain electricity generation and compare energy sources.','transport',['Cells and batteries','Hydrogen fuel cells'])],{'4.5.1.1':'Exothermic and endothermic reactions; Required practical: temperature changes','4.5.1.2':'Reaction profiles and activation energy','4.5.1.3':'Bond energies','4.5.2.1':'Cells and batteries','4.5.2.2':'Hydrogen fuel cells'},['RP4 temperature changes'])
