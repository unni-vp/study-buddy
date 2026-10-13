"""Clearer poster wording; original full course-map sources remain available."""
from copy import deepcopy
from biology_course_maps import MAPS
from biology_readable_mindmaps import prepare_panels

OVERRIDES={
('02 - Organisation','00-organisation-overview'):[
['Cells form tissues. Tissues form organs. Organs work together in organ systems.',
'**Tissue:** similar cells with a shared function. An organism contains cooperating systems.',
'**Digestion:** large insoluble molecules become small soluble molecules for absorption into blood.'],
['**Amylase:** starch to sugars. **Protease:** proteins to amino acids. **Lipase:** lipids to glycerol and fatty acids.',
'**Enzymes:** protein catalysts with specific active sites. Bile neutralises acid and emulsifies fat.',
'Food tests identify nutrients. The amylase pH investigation uses iodine. **Relative rate = 1/time.**'],
['**Right ventricle:** pumps blood to lungs. **Left ventricle:** pumps blood to the body. Valves prevent backflow.',
'**Arteries:** away from heart. **Veins:** towards heart. **Capillaries:** exchange with tissues.',
'**Red cells:** carry oxygen. **White cells:** defend. **Platelets:** clot. **Plasma:** carries dissolved substances.',
'Alveoli have large area and thin walls. Blood flow and ventilation maintain gradients.'],
['Fatty deposits narrow coronary arteries, reducing oxygen supply. **Stents** keep them open. **Statins** lower cholesterol.',
'Risk factors raise disease probability. Diet, smoking and exercise affect cardiovascular risk. Correlation alone is not causation.',
'**Benign tumours:** stay local. **Malignant tumours:** invade and spread.'],
['**Palisade cells:** chloroplasts absorb light. **Spongy mesophyll:** air spaces allow gas diffusion.',
'**Epidermis and cuticle:** protect and limit water loss. **Guard cells:** control stomata.',
'**Meristems:** dividing cells at root and shoot tips.'],
['**Root hairs:** water by osmosis, mineral ions by active transport.',
'**Xylem:** water and minerals. **Phloem:** dissolved sugars by translocation.',
'Transpiration is water loss through leaves. Heat, wind and usually light increase it. High humidity lowers it.',
'A **potometer** measures water uptake, which estimates water loss.']],
('02 - Organisation','01-digestion-and-enzymes'):[
['**Mouth:** chewing and amylase. **Oesophagus:** moves food to the stomach.',
'**Stomach:** acid, protease and mixing. **Pancreas:** supplies digestive enzymes.',
'**Small intestine:** digestion and absorption. **Large intestine:** absorbs water.',
'**Egestion:** undigested food leaves. **Excretion:** metabolic waste leaves.'],
['**Amylase:** starch → sugars. Made in salivary glands, pancreas and small intestine.',
'**Protease:** protein → amino acids. Made in stomach, pancreas and small intestine.',
'**Lipase:** lipid → glycerol + fatty acids. Made in pancreas and small intestine.'],
['Enzymes are reusable **protein catalysts**. Substrate fits a **complementary active site**, like a lock and key.',
'Warming increases collisions up to an optimum. Cold slows the reaction.',
'Excess heat or extreme pH can **denature** the enzyme: the active site changes shape, so substrate cannot fit.'],
['**Liver:** makes bile. **Gall bladder:** stores it. Alkaline bile neutralises stomach acid.',
'**Emulsification:** smaller fat droplets give more surface area for lipase. Bile is not an enzyme.',
'Absorbed products build new molecules. Glucose can be used in respiration.'],
['**Benedict’s:** reducing sugar gives a coloured precipitate after heating in a water bath.',
'**Iodine:** starch turns blue-black. **Biuret:** protein turns purple. **Sudan III:** lipid forms a red oil layer.',
'Use separate samples and positive/negative controls. Wear goggles and heat safely.'],
['Vary buffer pH. Control temperature, enzyme/starch concentrations and volumes.',
'Test samples on fresh iodine every **30 seconds**. When starch is digested, iodine stays **orange-brown**.',
'Repeat. For the same starch quantity, **relative rate = 1/time**. Shorter sampling intervals improve endpoint resolution.']],
('02 - Organisation','02-circulation-and-health'):[
['**Body → vena cava → right atrium → right ventricle → pulmonary artery → lungs**',
'**Lungs → pulmonary vein → left atrium → left ventricle → aorta → body**',
'The left ventricle has a thicker muscular wall for higher pressure. Valves stop backflow. Coronary arteries supply heart muscle.'],
['Pacemaker cells in the **right atrium** set the rhythm. Artificial pacemakers correct irregularities.',
'**Cardiac output = heart rate × stroke volume**',
'70 beats/min × 75 cm³/beat = **5,250 cm³/min = 5.25 dm³/min**.'],
['**Arteries:** thick muscle and elastic walls withstand high pressure. **Veins:** wide lumen and valves help return blood.',
'**Capillaries:** one-cell-thick walls give a short exchange path.',
'**Alveoli:** large area, thin walls, blood flow and ventilation. Oxygen moves to blood. Carbon dioxide moves to air.'],
['**Red cells:** haemoglobin binds oxygen. Biconcave shape gives a large area. No nucleus leaves space for haemoglobin.',
'**White cells:** phagocytosis, antibodies and antitoxins. **Platelets:** clotting.',
'**Plasma:** transports cells, nutrients, hormones, carbon dioxide and urea. Distributes heat.'],
['Fatty deposits narrow coronary arteries, reducing oxygen for heart-muscle respiration. **Stents:** keep arteries open. **Statins:** lower cholesterol.',
'Faulty valves leak or restrict flow. Biological or mechanical replacements restore flow.',
'Compare donor or artificial hearts: benefit, surgery, blood-clot risk and possible rejection of donor tissue.'],
['**Health:** physical and mental well-being. Diseases can interact. Lifestyle, environment and genes affect risk.',
'Smoking damages lungs and raises cancer risk. Obesity raises Type 2 diabetes risk. Alcohol can damage the liver and brain.',
'**Cancer:** uncontrolled division. **Benign:** local. **Malignant:** invades and forms secondary tumours.',
'Correlation alone is not causation. Compare representative rates and social/financial costs.']],
('02 - Organisation','03-plant-tissues-and-transport'):[
['**Epidermis and waxy cuticle:** protect and limit evaporation. **Palisade cells:** chloroplasts absorb light.',
'**Spongy mesophyll:** air spaces shorten gas diffusion paths. **Guard cells:** open or close stomata.'],
['**Root hairs:** large area for absorption. Water enters by **osmosis**, mineral ions by **active transport**.',
'**Meristems:** dividing cells at root and shoot tips. Cells differentiate to form specialised tissues.'],
['**Xylem:** dead hollow tubes. Lignin strengthens the walls. Water and minerals move from roots to leaves.',
'**Phloem:** living elongated cells with pores in end walls. Dissolved sugars move by **translocation** to growing or storage tissues.'],
['Water **evaporates** from mesophyll cells. Water vapour **diffuses** out through stomata.',
'Water loss pulls a continuous stream up xylem. Guard cells balance gas exchange against water loss.'],
['**Heat:** faster evaporation and diffusion. **Wind:** removes humid air, maintaining a steep gradient.',
'**High humidity:** smaller gradient and slower loss. **Light:** usually opens stomata, increasing loss when water is available.'],
['Cut the shoot under water. Seal an airtight setup. Dry leaves, allow acclimatisation, vary one factor and repeat.',
'A potometer measures **water uptake**, not exact water loss. **Rate = distance/time. Volume = πr² × distance.**',
'Sample stomata in several random measured areas. Calculate the mean number per unit area.']],
}

def course_panels(topic,item):
    data=deepcopy(item['panels'])
    key=(topic,item['slug'])
    if key in OVERRIDES:
        assert len(data)==len(OVERRIDES[key])
        for p,lines in zip(data,OVERRIDES[key]):p['lines']=lines
    return prepare_panels(data)
