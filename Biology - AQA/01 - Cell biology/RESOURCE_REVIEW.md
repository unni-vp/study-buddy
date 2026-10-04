# Internal resource review — Cell biology

Reviewed 4 October 2026 against the local AQA 8461 specification and the current official Cell biology page:
https://www.aqa.org.uk/subjects/biology/gcse/biology-8461/specification/subject-content/cell-biology

Coverage: 4.1.1.1–4.1.3.3, required practicals 1–3. The current web specification gives a maximum school culture incubation temperature of 25°C; the notes use that wording.

## Findings and corrections

- Mitosis previously reused generic cell drawings with DNA labels. Replaced with actual single chromosomes, joined copies, separating copies, and identical complete sets in two daughter cells. The enlarged chromosome shows each sister chromatid as one side of the X. Clarified DNA amount versus chromosome count in the notes.
- The former combined division/stem-cell image could imply a human stem cell differentiates into a plant cell. Removed that unrelated differentiation branch from the mitosis diagram. Human and plant sources remain correctly distinguished in the written table.
- Osmosis previously had water dots without solute particles, making dilute/concentrated solutions unclear. Added separate particle symbols, equal compartments, a membrane, and net versus reverse movement. Active transport now crosses a membrane protein; its energy requirement is labelled without a competing backwards arrow.
- The exchange image previously drew squares as cubes, with inconsistent size ratios, and labelled a lung icon as alveoli. Replaced with cubes in a 1:3 linear size ratio and an alveolar sac close-up with air, surrounding blood, and correctly directed gas arrows.
- The Cells mind map implied all bacteria had plasmids and all plant cells had chloroplasts. Added the appropriate qualifiers.
- Removed remaining specification tracking, scope commentary and the repeated qualification/tier/year banner from the student notes. Sources remain a concise official link.
- Reviewed the cell-structure functions, differentiation, microscopy, culture methods, stem cells, transport, exchange and osmosis practical. Checked worked calculations: ×500 magnification; 3,200 bacteria; 113 mm² circular area; −12% mass change; 0.004 g/min; cube SA:V 6:1 and 2:1.

## Maintained sources

- Revision Notes/Cell Biology - Revision Notes.md
- scripts/reviewed_cell_diagrams.py: three selected revision-note diagrams
- scripts/cell_biology_mindmaps.py: four grouped branching maps
- scripts/build_cell_biology_resources.py and scripts/build_project_site.py: generated HTML

Project-wide prevention checks are recorded in AGENTS.md and RESOURCE_GUIDELINES.md. This review file sits outside the student-facing resource folders.

## Verification

- Regenerated the three selected diagrams, four mind maps, standalone resources and offline HTML library from their maintained sources.
- Visually inspected all changed diagrams and mind maps, the mitosis diagram rendered inside the reader, and the large-icon mind-map grid on desktop and mobile.
- The mind-map grid opens four individual pages, each with one image and a back link. No full-map gallery remains on the selection page.
- Local-link check passed across 93 library pages. Browser check passed for home → subject → topic → notes, loaded diagrams, absence of the repeated notes banner, all four map links and back links, and mobile layouts without horizontal overflow.

## Grouped reading layout — 4 October 2026

- The default revision reader is now a compact illustrated menu of four groups: Cells, Cell processes, Transport and Practical investigations.
- Each group opens its notes directly as one document. No further menus or subtopic pages remain. Previous/Next links move between the four group pages.
- The source Markdown is unchanged. revision-layout.json maps all original content blocks exactly once, with overview/recall tools separate and sources retained in the complete print view. The build fails on missing or duplicated content.
- All three scientific diagrams remain next to their corresponding explanations. Relevant mind-map and practical links connect the groups.
- Mind-map navigation remains unchanged: large illustrated buttons open individual maps. Grouped reading is limited to revision notes and future Q&A, with the supported qa-layout.json workflow keeping question/answer pairs together.
- Removed the superseded generated subtopic pages from this edit. Local-link validation passed for the resulting 100 pages. Browser validation passed for all four direct reading pages, Previous/Next, back links, complete printing, existing mind maps and mobile widths. Desktop revision selection fits within the tested 1440 × 1000 viewport; inspected the 390 px mobile layout visually.
- Updated AGENTS.md and RESOURCE_GUIDELINES.md to preserve this preference across future subjects and topics.
