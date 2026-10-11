from physics_helpers import notes
notes(1,r'''
## Stores and transfers

Energy is a way of keeping track of changes. Imagine money moving between accounts: the amount in each account changes, but moving it does not create extra money.

A **system** is the object or group of objects you are considering. Describe **which store decreases, how energy transfers, and which store increases**.

| Store | Example |
|---|---|
| Kinetic | A moving cyclist |
| Gravitational potential | A book raised above the floor |
| Elastic potential | A stretched spring |
| Thermal / internal | Hot water |
| Chemical | Food, fuel or a battery |
| Nuclear | An atomic nucleus |
| Magnetic | Repelling magnets held close together |
| Electrostatic | Repelling charges pushed closer together |

Energy transfers **mechanically** when forces do work, **electrically** when charge flows, **by heating**, or **by radiation** such as light. Light and sound transfer energy; do not describe them as stores.

- A ball thrown upwards: **kinetic → gravitational potential**. Air resistance also increases the thermal stores of the ball and surroundings.
- A moving car brakes: its **kinetic store decreases**; brakes, tyres and surroundings warm through mechanical work against friction.
- A collision: kinetic energy may become elastic energy during deformation, then thermal energy and sound. Total energy is conserved even when kinetic energy is not.
- A motor accelerates a trolley: energy transfers electrically from the supply, then mechanically to increase the trolley's kinetic store.
- A kettle: electrical work increases the water's thermal store, with some energy transferred to the kettle and surroundings. Once boiling, continued heating can change state without raising temperature.

## Calculating changes in stores

| Equation | Quantities and units |
|---|---|
| **Eₖ = ½mv²** | Kinetic energy Eₖ in J; mass m in kg; speed v in m/s |
| **Eₚ = mgΔh** | Gravitational energy change Eₚ in J; g in N/kg; vertical height change Δh in m |
| **Eₑ = ½ke²** | Elastic energy Eₑ in J; spring constant k in N/m; extension e in m |

The spring equation applies **within the limit of proportionality**. Extension is the change in length, not the whole spring length. Use the value of g supplied in the question.

**Worked examples**

- A 2.0 kg object at 3.0 m/s: Eₖ = ½ × 2.0 × 3.0² = **9.0 J**.
- Lift a 4.0 kg bag by 1.5 m, with g = 9.8 N/kg: Eₚ = 4.0 × 9.8 × 1.5 = **58.8 J**.
- Stretch a 200 N/m spring by 5.0 cm. Convert first: e = 0.050 m. Eₑ = ½ × 200 × 0.050² = **0.25 J**.

**Doubling speed quadruples kinetic energy.** Doubling extension quadruples elastic energy while the spring remains proportional. Doubling mass doubles kinetic energy at the same speed.

To find speed from energy, rearrange first: **v = √(2Eₖ/m)**. If 36 J becomes the kinetic energy of a 2.0 kg object, v = √(72/2) = **6.0 m/s**.

## Conservation, dissipation and efficiency

**Energy cannot be created or destroyed.** In a closed system, total energy stays constant. Choose a boundary that includes the surroundings receiving the transferred energy.

**Dissipation** means energy spreads into the surroundings, usually into thermal stores. It becomes less useful because it is harder to use for the intended purpose. “Wasted” does not mean destroyed.

![An energy budget: 100 J supplied becomes 60 J useful lifting energy and 40 J transferred to thermal stores.](../Diagrams/energy-budget.svg)

- **Efficiency = useful energy output ÷ total energy input.**
- Alternatively, **efficiency = useful power output ÷ total power input**.
- Multiply a decimal efficiency by 100 for a percentage. Efficiency has **no unit** and cannot exceed 1 or 100%.
- A motor transfers 500 J and raises a load by 350 J: efficiency = 350/500 = **0.70 = 70%**. The remaining **150 J** is transferred in unwanted ways.
- If efficiency is 0.80 and useful output is 240 J, input = 240/0.80 = **300 J**.

**Lubrication reduces friction**, so less energy is transferred to unwanted thermal stores. Insulation reduces unwanted heating of surroundings. A more efficient device needs less input for the **same useful output**.

## Power and work

**Power is the rate of energy transfer**, or the rate of doing work. A joule measures an amount of energy; a watt measures how quickly it transfers.

**P = E/t = W/t**. P is power in W, E or work done W is in J, and t is in s. **1 W = 1 J/s**. Here W can mean the symbol for work or the unit watt; read its position carefully.

A motor transfers 1,800 J in 30 s: P = 1,800/30 = **60 W**. A 120 W motor could transfer the same energy in **15 s**.

Two identical motors may lift the same load through the same height. They do the same useful work. The one doing it in less time has greater useful power; greater power alone does not prove greater efficiency.

**1 kJ = 1,000 J; 1 kW = 1,000 W; 1 minute = 60 s.** Keep energy and power separate when interpreting graphs or comparing appliances.

## Heating and specific heat capacity

**Specific heat capacity** is the energy needed to raise the temperature of **1 kg** of a substance by **1°C**, without changing state. Think of a larger c as a bigger energy cost for each degree of warming.

**ΔE = mcΔθ**

- ΔE: change in thermal energy, J.
- m: mass, kg; c: specific heat capacity, J/kg°C.
- Δθ: **final temperature − initial temperature**, °C. It is not the final temperature alone.

For 0.50 kg of water warmed from 20°C to 40°C, c = 4,200 J/kg°C:

ΔE = 0.50 × 4,200 × (40 − 20) = **42,000 J**.

At the same mass and energy input, a material with **larger c has a smaller temperature rise**. During melting or boiling, use latent heat instead; temperature need not rise.

## Practical: measure specific heat capacity

1. Measure the mass of a metal block using a balance. Fit an electrical heater and thermometer into its holes. A little suitable oil improves thermal contact.
2. Wrap the block in insulation. Record its initial temperature.
3. Use a low-voltage supply. Measure energy input with a joulemeter, or record power and heating time using **E = Pt**. If needed, measure V and I and use E = VIt.
4. Record temperature at regular time intervals while heating. Switch off before the block becomes dangerously hot.
5. Find Δθ, then calculate **c = E/(mΔθ)**. Repeat and compare results.

If 12,000 J heats a 1.0 kg block by 30°C, c = 12,000/(1.0 × 30) = **400 J/kg°C**.

**Improve the method:** good insulation and contact reduce heat loss and temperature lag. A lid can help for a liquid; stir the liquid gently for an even temperature. Keep electrical parts dry.

Not all electrical energy heats the sample. Some heats the heater and surroundings. Treating all input as the sample's energy usually makes the calculated c **too high**. On a graph of energy supplied against temperature rise, the ideal gradient is **mc**; divide by mass to find c.

## Insulation and cooling

Energy transfers from hotter to cooler surroundings. **Higher thermal conductivity means faster conduction**, for the same dimensions and temperature difference. A thicker wall or lower-conductivity material reduces this transfer.

- Loft insulation and cavity-wall insulation trap air, reducing conduction and air circulation.
- Double glazing traps a layer of gas between panes; draught-proofing reduces warm air escaping.
- Thicker insulation usually slows cooling, but each extra layer may give a smaller extra benefit.
- Compare cost with savings and practicality. Simple **payback time = installation cost ÷ annual saving** when annual savings are assumed constant.

## Practical: compare thermal insulators

1. Wrap identical containers in equal thicknesses of different materials. Include an uninsulated control.
2. Add the same mass of hot water at the same starting temperature. Use matching lids and thermometers.
3. Measure temperature at equal time intervals for the same total time. Keep room conditions, exposed area and container size constant.
4. Repeat each material and calculate mean temperature drops. **Smaller drop in the same time means better insulation** under these conditions.
5. Plot temperature against time. A less steep cooling curve shows a lower rate of energy loss for matching conditions.

Use hot water carefully on a stable surface; handle containers with suitable protection. To investigate **thickness**, keep the material fixed and change only thickness. Do not change both at once. Repeats reduce the effect of random variation; they do not remove a thermometer's zero error.

## Energy resources and decisions

A **renewable resource is replenished as it is used**. Fossil fuels and nuclear fuels are non-renewable: their usable supplies are finite.

| Resource | Uses and strengths | Limitations and impacts |
|---|---|---|
| Coal, oil and gas | Controllable heating and electricity; oil fuels transport | CO₂ contributes to climate change; pollution; extraction damage; finite fuels |
| Nuclear fuel | Reliable large-scale electricity, low operational CO₂ | Radioactive waste, high building/decommissioning costs; finite fuel |
| Biofuel | Heating, electricity or transport; can be regrown | Land competes with food/habitats; burning produces CO₂; carbon balance depends on regrowth and processing |
| Wind | Renewable electricity without burning fuel | Variable wind; visual/noise impacts; wildlife and site constraints |
| Sun | Solar electricity and water heating | Daylight/weather vary; large area may be needed |
| Hydroelectric | Electricity; stored water can respond quickly to demand | Reservoirs flood habitats/settlements; drought can reduce supply |
| Tides | Predictable timing for electricity | Output is not continuous; high cost and estuary/ecosystem changes |
| Waves | Renewable electricity | Variable sea conditions; difficult maintenance; coastal impacts |
| Geothermal | Heating and electricity; steady at suitable sites | Suitable sites limited; drilling costs |

**Reliable does not always mean renewable**, and renewable does not mean impact-free. A mix of resources, storage and flexible generation can help match variable supply to demand.

When evaluating a choice, use the given data: output, reliability, cost, land use and emissions. State which factor matters most for the situation, then give a justified conclusion. Scientists can measure emissions and risks; policy also depends on **economic, social, ethical and political decisions**.

For trends, distinguish an increase in total energy from an increase in percentage share. New technology, cost, fuel availability and environmental policy can change the mix. Avoid inventing current percentages when the question supplies a graph.
''',[
('stores','Stores and calculations','Track transfers and calculate energy, power and efficiency.','physics-energy',['Stores and transfers','Calculating changes in stores','Conservation, dissipation and efficiency','Power and work']),
('heat','Heating and practicals','Explain warming, insulation and reliable measurements.','physics-heat',['Heating and specific heat capacity','Practical: measure specific heat capacity','Insulation and cooling','Practical: compare thermal insulators']),
('resources','Energy resources','Compare supply, reliability and environmental impacts.','physics-energy',['Energy resources and decisions'])],['4.1.1.1–4.1.1.4','4.1.2.1–4.1.2.2','4.1.3'],[1,2])
