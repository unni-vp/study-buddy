# GCSE resource guidelines

## Purpose

Act as an expert GCSE tutor helping a student aim for **Grade 7 or 8** in the 2027 exams. Simplify complex ideas while keeping the science, mathematics and subject meaning accurate.

## Teaching sequence

1. **Plain English first:** explain the core idea in short, familiar words.
2. **Everyday analogy:** use a vivid example from daily life. Say where the analogy stops working if that matters.
3. **Must-know facts:** prioritise the facts, methods and connections that underpin exam success.
4. **Exam vocabulary:** introduce and **bold** essential terms and precise marking points.
5. **Worked example:** show how to use the idea step by step.
6. **Exam practice:** include retrieval, application and reasoning questions suitable for the topic and tier.
7. **Answers:** explain why the answer works, the marks available and common mistakes.

## Scope and accuracy

- Keep the full official curriculum available locally. Prioritise learning order rather than predicting that an assessable detail cannot appear.
- Avoid unnecessary enrichment, heavy jargon and long lists of low-value details.
- Include Higher-tier content and separate-science-only content where the specification requires it.
- Teach mathematical methods, units, practical reasoning, application and evaluation as well as facts.
- Bold marking points supported by an actual official mark scheme when claiming examiner requirements. Record the paper, question and source. Keep original practice and suggested marking points distinct from official mark schemes in the source page and internal metadata; use only **Answer:** as the label beside each answer.
- A keyword alone does not necessarily earn a mark. Teach the complete relationship, explanation or calculation needed.
- For English, develop supported interpretation, precise evidence, analysis of effects, relevant context and comparison. Avoid implying that naming a technique automatically earns a mark.
- Grade boundaries vary. Do not promise a grade from a fixed percentage or a small set of topics.
- Distinguish official board material from original tutor resources.

## Layout and mind maps

- Use clear headings, bullets, short sentences and small sections.
- Put **must-know facts** near the top. Separate optional extension material.
- Create a mind map when a topic is large or the relationships are hard to follow. Use a central idea, a few meaningful branches, short labels and labelled links.
- Split crowded mind maps into smaller maps. Keep labels readable and pair diagrams with a brief text explanation.
- Present the mind-map selection page as a compact grid of clickable thumbnails showing the actual maps, with clear titles. Open each map on its own page with a link back to the grid. Avoid a long page stacking all full-size maps.
- Keep these thumbnail cards small and responsive: four per row on wide screens, three on medium screens and two on narrow screens. Keep titles readable and use modest preview sizes and padding.

## Standard resource layout

### Website reading layout

- Topic resource buttons must include distinct icons for Revision notes, Mind maps and Questions & answers. Arrange them as three equal-width buttons across the available content area, centring the icon and label inside each. Stack full-width buttons on narrow screens; keep unavailable resources clearly disabled.
- For revision notes across all subjects, use one compact illustrated menu of a few broad groups. Each button opens the full content of that group directly as one page. Do not introduce another menu or subdivide the group into separate subtopic pages. Q&A opens directly as one combined topic page, grouped only by increasing marks, without a thematic split or selection menu.
- Give each revision-notes group page a clear title, Previous/Next links between groups, and a link back to the resource menu. Keep diagrams and explanations together. Avoid chapter-wide progress counters or large lists of everything still to learn.
- The broad-group menu applies only to revision notes. Mind maps have a separate thumbnail menu: each preview opens one mind map on its own page. Do not add grouped sub-menus to mind maps. Q&A uses mark headings on a single combined page.
- Preserve all assessable content. Split presentation rather than silently summarising away definitions, explanations, calculations or practical methods. Keep overview and recall tools available as separate short pages.
- Link to relevant existing mind maps and practical sections. Add Q&A links when the resource exists, without creating empty or misleading links.
- Provide a separate Print all notes view containing the complete notes and sources.
- Maintain one editable Markdown source per resource. For notes, revision-layout.json selects headings into broad groups; scripts/revision_navigation.py validates assignment and builds group pages plus the full print view. For Q&A, use headings such as ## 1 mark and ## 2 marks, plain numbered prompts such as **1.** followed by the actual question, and **Answer:** before the actual answer. Put a single answer on the same line; keep bullets for longer responses. Leave one- or two-word answers in plain text, without bold emphasis. Do not add a separate question title or repeat the marks on each question. scripts/qa_navigation.py validates consecutive numbering, increasing mark groups and paired answers, then builds one topic reading page and an optional source page. qa-layout.json can record mark-group IDs and question IDs for internal tracking; it must not recreate thematic subpages. Fail builds for missing, duplicated or unassigned content.

### Content within a section

- Topic title. Keep qualification code, exam year, tier and specification references in internal metadata, without repeating them in topic notes or diagrams.
- Core idea in plain English.
- Everyday analogy.
- Must-know facts and bold exam terms.
- Worked example or text analysis.
- Common mistakes.
- Mind map where useful.
- Practice questions grouped by marks. Show marks once in each group heading, without a separate title or mark label on individual questions.
- Each question immediately followed by its answer and supported or suggested marking points in the same Q&A document.
- Concise source links where useful; keep verification dates and curriculum tracking in internal metadata.

## Storage

Each subject has `00 - Specification` and numbered main-topic folders. Each topic contains `Revision Notes`, `Mind Maps`, `Questions and Answers`. Use descriptive filenames. Keep official source PDFs intact.

## Combined past-paper Q&A

- Use one combined Q&A document per topic, with each question followed by the answer and marking points. Do not create separate question and answer documents or folders.
- Prioritise recurring question types evidenced across relevant past papers. Do not call questions most common without checking a representative set.
- Record board, qualification, year/series, paper, question number and official source for each past-paper item.
- Distinguish exact official questions from adapted or original questions. Explain recurring patterns without predicting future questions.
- After adding or editing resources, run scripts/build_project_site.py to refresh the HTML library.
- Order the combined Q&A document and its single website reading page by increasing marks. Group under one heading per mark value, with plain numbered questions and no individual question titles or repeated mark labels. Keep answers immediately after their questions, including necessary diagrams and worked calculations. Compact same-page links to mark headings are allowed; do not split questions into thematic pages.
- Collate a concise directory of past-paper websites and retain the examined question papers and mark schemes locally, unchanged. Put sources in an optional page accessible from the combined Q&A reading page; keep curriculum tracking and detailed provenance in internal metadata.
- Define the paper sample before reporting recurrence. Count each question type once per paper and make overlapping categories clear. Verify current specification relevance independently of older mark-scheme content codes; check for incorrect printed codes. Mark additional specification-based practice honestly, without claiming it has recurred in the sample.
- Six-mark methods and evaluations require logical sequencing, linked explanations and, where requested, a reasoned judgement. Do not imply one bullet always equals one mark. Keep proposed allocations distinct from actual official allocations.

- Keep student-facing documents focused on subject content. Do not add grade-target introductions, study-direction preambles, authorship disclaimers, explanations of bold formatting, or statements about marks not being guaranteed. Keep necessary factual distinctions, sources and practical safety instructions concise.

- The student is a visual learner. Organise resources around labelled diagrams, illustrated processes, colour-consistent comparisons and short explanations beside the relevant visual. Mind maps must show meaningful relationships with labelled arrows (structure → function → application), not disconnected lists. Use relevant biological drawings or memorable visual cues, with concise labels. Embed visuals beside the corresponding notes, and use illustrated setups for practicals and worked visual steps for calculations when helpful. Keep text alternatives and readable labels.

- Keep the written revision notes. Add useful labelled diagrams alongside explanations wherever they clarify structures, mechanisms, practical methods or calculations; visuals supplement the notes rather than replacing them.

- Student resources must not show specification references, curriculum tracking, content classification labels (such as separate Biology content), or teaching-process labels such as Plain English first. Keep tracking in resource metadata. Keep clear topic headings and useful required-practical titles.
- Mind maps: group closely related concepts under a clear central theme (for example Cells, Cell processes or Transport processes), with curved colour-coded main branches and concise connected sub-branches. Keep meaningful central illustrations and the established branching layout. Avoid unrelated topics or overcrowding. Do not label comparison tables or flowcharts as mind maps.

- Use diagrams selectively in revision notes: only for a genuinely complex mechanism, structure or relationship that is materially easier to understand visually. Keep straightforward facts and calculations as concise notes or tables. Do not add a diagram to every section or append the whole mind-map gallery to the notes. This selective-use preference overrides earlier wording to include visuals wherever possible. Keep focused mind maps in their separate resource section.

## Scientific diagrams: accuracy and review

These checks apply to future resources and revisions of existing resources.

- Show the mechanism, rather than an unchanged drawing with new labels. A process diagram must make the important physical change visible.
- **Mitosis:** draw each chromosome before copying, two identical joined copies after DNA replication, the copies separating towards opposite ends during mitosis, and one complete matching set in each daughter cell. Use consistent colours and shapes to follow chromosome identity. DNA replication happens before mitosis. DNA amount doubles during replication; a joined pair of sister chromatids is one replicated chromosome. Do not imply that chromosome number doubles during replication or is halved in each daughter cell. Do not draw an intact nuclear envelope around the separating chromosomes. If showing an X-shaped chromosome, each sister chromatid is one side of the X, joined at the centre. Make simplified chromosome counts clear without adding phase-name detail.
- **Differentiation:** distinguish human stem-cell sources from plant meristems. Do not draw an arrow from a human stem cell to a plant cell or imply every stem-cell source can form every cell type.
- **Transport:** identify each particle type with a readable legend. Use equal-sized compartments when particle numbers illustrate concentrations. Osmosis must show water and solute separately, the partially permeable membrane, and net water movement from dilute to concentrated solution. The solute shown as unable to cross must stay on its side. Distinguish net movement from movement in both directions. Active transport must show substances moving against their concentration gradient across a membrane, with energy from respiration. Do not use an unlabelled energy-input arrow that looks like substance movement in the opposite direction.
- **Anatomy:** draw the structure actually named. An alveolus is a small air sac, not a whole lung. Show exchange arrows ending in their true destinations, for example oxygen moving from alveolar air into blood and carbon dioxide moving from blood into air. Organ icons are suitable as mind-map memory cues but cannot substitute for a mechanism or labelled close-up.
- **Scale and maths:** use correct geometry, dimensions, units and numerical relationships. Cubes must be three-dimensional; a 3 cm cube should have three times the drawn side length of a 1 cm cube when drawn to the same scale. Distinguish total surface area from surface area to volume ratio.
- **Biological qualifiers:** do not turn examples into universal claims. Some bacteria have plasmids; photosynthetic plant cells have chloroplasts. Carry these distinctions into mind maps as well as notes.
- **Visual review:** regenerate from the maintained source, inspect every changed diagram and check it against the written explanation and official specification. Inspect the HTML reader at its normal display size and on a narrow screen. Check readable labels, colour consistency, overlapping text, clipping, arrows and loaded images. Keep useful text alternatives. If a label is too small or crowded, simplify the layout before adding more content.
- **Student focus:** retain the selective three-diagram approach for the current Cell biology notes unless a new visual solves a specific learning difficulty. Keep grouped branching mind maps separate. Do not insert authoring explanations, review checklists, qualification/tier/year banners or specification tracking into topic notes.
- **Reproducibility:** update the drawing code or editable diagram source, not just the exported PNG. Remove obsolete generation paths that could recreate an identified mistake. Rebuild the resources and offline site and run the relevant link/browser checks. Record findings and verification dates in internal review metadata.

- Label each Q&A answer **Answer:**, followed by the actual answer. Put single answers on the same line; use bullets where longer responses are easier to follow. Do not use Answer — suggested marking points. One- or two-word answers should be plain text, without bold emphasis. Keep the distinction between practice answers and official mark schemes in sources and internal metadata.

- In HTML Q&A readers, put every answer in its own native details/summary disclosure, closed by default, labelled Answer:. Keep question wording, data and question diagrams visible; hide answer explanations, answer diagrams and answer-specific hints together. Support keyboard and touch use. Printing must reveal all answers and restore the student’s previous open/closed choices afterwards. Keep the editable Markdown as a single combined document with Answer: labels. Apply this to future topics too.

- By default, commit and push changes when the requested work is complete and appropriate checks have passed, unless the user explicitly asks not to commit or push. When work spans multiple topics or sections, complete, verify, commit and push each topic or section separately. This standing user instruction supersedes the earlier local-only rule; do not ask for push permission again unless a new constraint requires it.
- Add a small, relevant visual memory cue beside each main mind-map branch. Match the cue to the concept (for example a water droplet for osmosis, matching daughter cells for mitosis, or folded surfaces for large exchange area). Preserve the branching layout, all labels and readable spacing. Keep biological cues accurate and distinguish an icon from a complete mechanism diagram. Maintain the drawing source and inspect every regenerated map.

- At the top of each HTML Q&A reading page, provide Expand all and Collapse all buttons for all answers on that page. Keep individual disclosures usable, answers collapsed on initial load, and bulk controls hidden in print.

- Mind maps now follow the reference-style visual revision sheet: a central title surrounded by compact bordered panels, concise bullets, highlighted exam keywords and relevant accurate illustrations. Cover all assessable content for the map's named section, including associated practicals and calculations; use an internal coverage checklist. The reference image supplies layout only, never curriculum content. This supersedes the earlier curved-branch requirement.
- Clicking the topic Mind maps button opens a full-screen modal gallery. Clicking an actual map thumbnail opens that map in the same full-screen modal, using all available screen space. Provide fit, zoom, pan/scroll, close/Escape, return-to-gallery and print controls; lock background scrolling and restore focus on close. Retain ordinary page links and a text version as offline/no-JavaScript fallbacks. This supersedes the earlier navigation-only-to-separate-pages preference.

- Use the latest mind-map reference format for both combined overviews and detailed subtopic maps: numbered rounded blue-bordered panels with blue title ribbons, a yellow central theme, curved connecting lines, highlighted key terms and accurate illustrations. Keep one concise combined overview spanning all topic sections alongside the detailed maps. Overview content must use the same core concepts and terms as the notes; it must not introduce additional mandatory terminology. Preserve detailed-map content when changing formatting.

- In reference-format maps, leave a clear gap between the central illustration, title and subtitle. Wrap long central titles rather than extending across the illustration or beyond the circle. Preserve scientific acronym capitalisation, and keep punctuation attached when highlighted terms end a line.

- Approved mind-map style: apply the combined map’s varied section sizes, colour-coded labelled relationships and accurate explanatory drawings to the detailed subtopic maps too. Use landscape layouts for screen viewing, aiming for roughly 16:10 while retaining readable content. Reflow sections rather than stretching a portrait image. Preserve the full source content and text alternatives; avoid forced 3×3 grids and decorative filler icons. Keep chromosome copies/separation, particle legends and measured diagram labels explicit.
- User preference: use Extra High (xhigh) reasoning effort for mind-map generation when the execution interface supports selecting it. A saved preference does not change the current chat setting; never claim the setting was changed without confirmation.

- Allocate mind-map space to content density: use empty corridors to widen crowded sections, and let paragraphs and formula boxes flow from measured text height. Do not position the next paragraph using a fixed y-coordinate when the preceding text can wrap. After combined-map edits, run scripts/check_cell_biology_overview_layout.cjs and inspect the export; check connector labels separately so lines do not cut through words.

- For landscape maps, measure actual browser text using scripts/check_landscape_mindmaps.cjs, including transformed section bounds and canvas clipping. Measure bold headings with the bold font; retain DNA and other scientific acronym capitalisation. Allocate branch widths by content density and inspect the full-screen desktop and narrow-screen viewer.

- Mind-map spacing review must check panel rectangles and central-title padding, not only text collisions. Reserve clear corridors for connectors; no relationship path may pass through a section. Check labels at normal full-screen size. Use spare canvas space for title line spacing and gutters before shrinking text. Wrap long central titles and measure each line with actual browser font metrics.

- Apply internal spacing consistently to every section in every mind map, including combined overviews, detailed maps and future resources. Keep body text, diagrams, tables and formula boxes inset on all sides; leave a distinct gap between the section heading and the first description or diagram, with extra separation around subsection headings. Allocate more panel/canvas space when needed rather than squeezing content against a border or reducing text size. Use physical A4 print measurements, not a fixed SVG coordinate inset, as the spacing standard. Verify body bounds and heading/body clearance in scripts/check_landscape_mindmaps.cjs, alongside section/connector checks.

- A4 mind-map readability: use A4 landscape with 10 mm margins and a fixed 277 mm printed map width. Keep body text at least 11 pt and diagram labels at least 10 pt at that physical size. Do not enlarge the SVG viewBox, reduce font size, or apply a fit-to-page transform to manufacture padding. Adjust section widths, heights, positions and related groups; wrap using measured font widths and leave clear inner padding and heading/body gaps. Use concise wording without dropping assessable concepts. The combined Cell biology overview may use shorter one-page summaries (approved by the user); detailed maps and unchanged full text alternatives preserve the detail. Do not silently split over pages.
- Validate every map using scripts/check_landscape_mindmaps.cjs and inspect its image. Run scripts/check_mindmap_print.cjs then scripts/check_mindmap_print.py to verify both reader and modal produce exactly one A4 landscape page, matching content, minimum physical font sizes, and no clipping. Inspect the rendered A4 proofs. Keep scientific diagram labels readable and explicit when rearranging artwork. Rebuild the HTML site and check desktop/mobile fullscreen navigation before pushing when authorised.


## English Language writing resources

- Teach how to make writing decisions: decode purpose/audience/form, select and develop ideas, give paragraphs distinct jobs, organise the whole piece, maintain register and edit for meaning and accuracy.
- Put particular emphasis on article writing through complete original examples, paragraph-level commentary and weak-to-improved examples. Include other task forms without turning the notes into a rhetorical-device checklist.
- Match Eduqas Component 2 Section B: two compulsory 20-mark tasks, each split 12 for communication/organisation and 8 for vocabulary/sentences/spelling/punctuation. Check current paper instructions before giving word-count or timing advice.
- Present paragraph routes as flexible teaching tools, not compulsory examiner formulas. Do not claim every technique or bullet earns a mark. Keep short skill-practice mark allocations distinct from the actual exam format in sources and metadata.
- Use credible examples and clearly framed hypothetical situations. Do not teach students to fabricate survey results or expert quotations as established facts.
- Keep full writing models within the intended task length and explain why their content, organisation, tone and sentence choices work. Preserve natural paragraphs within expandable answers.

- For graphical overview revisions, use compact informative illustrations and give most space to readable explanations. The illustrated Cell biology alternative omits the central heading panel to reclaim space. Put separate facts and calculations on separate lines or bullets, rather than packing them together with semicolons. Reflow panel widths and heights while preserving the physical print font size.

- In graphical mind maps, use bold keywords with colons for labels, functions and associations; bold the colon with its keyword so it stays visible. Keep longer explanations on separate lines. Reserve arrows for actual movement or process sequences. This supersedes the earlier separator preferences for arrows and em dashes.

- For the Cell biology overview, retain only the existing mitosis diagram. Use the removed illustration space for clear content subsections, fuller explanations, practical methods and calculations. The approved illustrated artwork is now the main 00-cell-biology-overview and replaces the older overview. Keep one overview entry, followed by the detailed maps; do not recreate the removed 07 alternative. In future maps, prioritise useful explanations and add a diagram only when it provides clear learning value.

- Keep mind-map section and subsection headings coloured, and use black for the content beneath them, including bold keywords, explanations, diagram captions and calculations.

- Use a consistent font size and bold weight for all subsection headings within each mind map. In the new Cell biology overview, match Compare discs (16 SVG units, about 11.2 pt on A4). Keep explanatory phrases in the black body text rather than mixing them into a coloured heading.

- Main mind-map panel gutters may be reduced to reclaim useful content space, while preserving clear separation, internal padding and readable text sizes. Reorganise or enlarge panels before reducing body fonts.

- Use light, inset divider lines between natural content groups within mind-map panels, matching the panel colour. Keep clear space above and below each line; do not separate every fact or let a line touch text or diagrams.

- Biology mind maps now use the readable panel style from the approved Cell biology overview: no central hub, measured widths/heights, black body text with bold colon labels, consistent coloured headings, light inset dividers and compact outer gutters. Apply it to existing Biology maps while preserving their complete text counterparts. Use scripts/biology_readable_mindmaps.py through the maintained subject generators. Keep Previous and Next controls inside every mind-map viewer, with a position count and disabled controls at the ends.

- Use diagrams selectively in every Biology mind map: retain or restore a labelled structure, changing mechanism, comparison graph or practical setup when it explains something more clearly than the text alone. The previous instruction to retain only mitosis applied to the combined Cell Biology overview; it does not mean removing useful diagrams from every detailed map. Avoid filler icons and decorative pictures. Preserve readable A4 text, clear labels and written explanations; allocate diagram space by rearranging panels. Record each diagram's learning purpose in internal review metadata.

- Apply the approved readable Biology panel style to Chemistry, English Literature and Physics mind maps too. Use scripts/readable_subject_mindmaps.py through each maintained subject generator. Preserve complete text counterparts and all named content groups; keep body text and diagram labels at least 11 pt on A4 landscape, with no central decorative hub or font shrinking. Reflow panel widths/heights, use black explanations, consistent coloured headings, bold colon labels and light inset dividers. Select explanatory structures, processes, graphs, practical apparatus and meaningful literary relationships rather than filler icons; record their learning purpose. Review every export and A4 proof and retain fullscreen Previous/Next navigation.

## Literature quotation analysis

- In Macbeth Act and Theme notes and poetry notes, link each quotation to a specific language, imagery, form or structure choice, followed by its meaning and effect. Use only categories supported by the particular words or their placement; do not force all four onto every quotation. Keep this relationship clear in model answers too.
- Poetry notes follow six sections: relevant poet context; Poem context — form and structure; Content and deeper meaning (including relevant setting); 5–6 key quotations with methods and effects; Language and imagery; Example quotation analysis. Preserve useful comparisons and major theme tags.
- Include biographical facts only when they help explain a particular poem. Distinguish poet from constructed speaker and supported context from speculative intention. Explain form and structural development against the official poem, rather than adding a disconnected list of terms.
- Check verse lines, stanza divisions and turns in the official anthology page layout. A printed page break or wrapped line does not establish a stanza break or an extra verse line. In Decomposition, analyse reflective free verse and the shift to self-criticism; do not rely on the inherited five-quatrain claim.

## Macbeth connected revision

- Treat VAGGAS as a flexible six-theme memory aid with distinct Guilt and Gender entries; keep Kingship as a separate theme. Choose links that answer the question, without prescribing a fixed number of themes or paragraphs.
- For Eduqas Macbeth, distinguish the 15-mark printed-extract analysis from the 25-mark whole-play essay. Do not import advice that sends an extract answer away from its printed passage.
- Distinguish regicide from usurpation, and divine-right belief from a proven divine appointment. Ground succession in Duncan naming Malcolm; do not impose a universal primogeniture rule on the play's Scotland. The dagger precedes Duncan's death.
- Keep character interpretations qualified: Banquo is tempted; Lady Macbeth's influence changes; Macduff joins grief with public duty; Malcolm promises restoration but his reign is not shown. Use terms such as hubris, hamartia and catalyst only alongside plain meanings and specific evidence.
- Synchronise edited Literature mind-map Markdown with the same maintained definitions used for artwork, through scripts/build_literature_maps.py. Preserve readable A4 fonts, selected explanatory diagrams and viewer navigation.

- Where a reading Q&A bank shares a passage, store the passage in the topic's qa-stimulus.md. Render it visibly before the mark groups, outside answer disclosures; retain paragraph labels and a single combined Q&A reader. Keep original practice texts clearly distinguished from official extracts in the source page and metadata.

- Readability and language quality must be preserved when making resources concise. Use short, complete sentences and manageable paragraphs, explain causal links and define unfamiliar vocabulary in context. Retain important facts, named evidence, qualifications and explanations. Remove repetition or reorganise material before cutting the words needed to understand it. Do not turn revision notes into compressed fragments, unexplained lists, slash-heavy shorthand or crowded single-line summaries. This applies to every subject and future resource.

- When extending revision notes, integrate related detail into the existing logical sections. For case studies, group material under place/context, causes or processes, effects, management and evaluation as appropriate. Do not append a parallel heading for another explanation of the same point. Keep paragraph breaks, useful bold lead-ins, comparison tables and important evidence; remove repetition without compressing the language. This organisation standard applies across all subjects.

- Do not show resource-availability badges (such as Resources available or Not yet prepared) on subject topic cards. Keep the topic number, assessment-paper label, title and Revised checkbox.

- Within a case-study explanation, keep a consistent level of development. Integrate brief facts into short paragraphs with bold lead-ins rather than placing an expanded explanation after a duplicate terse bullet list. Retain useful comparison tables, genuine process or method steps, named evidence and qualifications. Keep related material under its existing logical heading.

- When using a supplied revision booklet, audit every named case study for useful omitted numerical evidence, dates, locations and named strategies. Keep an internal claim-by-claim decision record. Preserve accurate historical figures with their date, scope and units; distinguish forecasts from outcomes and national figures from local ones. Correct conflicting claims with sources rather than silently dropping the evidence or importing it uncritically.

- Landscape case studies must explain geomorphic processes at named places: identify the process, explain how it works, link it to the landform, and show how geology, climate and human management affect it. Verify sediment directions and local connections; do not assume every coastline belongs to one continuous transport route or every gorge formed by waterfall retreat.

- Keep reference/source sections in editable documents and embedded HTML, but hide them entirely in normal reading and print. Do not show a source heading, disclosure, toggle or source-directory link in the reading flow. Hide bibliography sections only; retain teaching content such as grid references, sources and bias, energy resources and historical-source analysis.

- Do not display High-yield checklist sections in student reading pages or print views. Keep any retained checklist content hidden for internal tracking, without a visible heading or reveal control. Preserve the actual teaching explanations and important facts in the notes.

- Hide Exam pointer sections, including named case-study exam pointers, in reading and print views. Do not leave a visible heading or reveal control. Keep substantive process explanations, case evidence and model answers visible.

- Do not display the generic Evaluating a strategy section in student reading or print views. Keep specific case-study evaluations and supported judgements visible.

- Equation layout: put each main equation on its own line or in a clear table row. Define one symbol and its unit per bullet or table row. Separate given values, unit conversions, substitution and the final answer into readable worked steps. Keep different examples apart. A source-code line break inside a Markdown paragraph does not create a visible break: check the rendered desktop and mobile pages.

- Mind-map equations follow the same readability standard as notes: put independent relationships and conversions on separate lines, distinguish work done W from the watt unit, and keep complete text counterparts consistent. Preserve genuine numerical equality chains. Rebalance panel widths, heights and column groups before considering any content change; never reduce the established A4 font sizes to make separated lines fit. Use scripts/rebuild_science_mindmaps.py for map-only rebuilds so notes, Q&A and flash cards are preserved.

- Practical diagrams must appear beside the method on its own revision group page; a diagram in another group does not cover that practical. Audit the full required-practical list across all three sciences, reuse useful existing artwork in the practical-skills chapters, and show apparatus connections, measurement positions and controls accurately. Regenerate and reinsert these shared diagrams with scripts/science_practical_diagrams.py SUBJECT TOPIC after regenerating notes; review the SVG labels and the affected desktop/mobile readers. Keep tables for observations and retain the full written methods.
