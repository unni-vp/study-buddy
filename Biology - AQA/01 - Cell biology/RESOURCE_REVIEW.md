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

## Branch memory cues — 4 October 2026

- Added one relevant icon above each of the four main branches on all four maps. Labels, connections, dimensions and central illustrations are unchanged.
- DNA copying shows a single chromosome becoming joined identical copies; daughter-cell icons show matching complete sets. Human differentiation is separate from the plant-meristem cue.
- Water droplets, high-to-low particles, energy/uphill arrows, folds, thin barriers and blood-refresh cues relate directly to the corresponding branch. Cube icons are three-dimensional and use a 1:3 side-length ratio.
- Changes remain local. Do not commit, push or deploy without a new explicit user request.

- Inspected all four regenerated maps and the desktop/mobile HTML readers. Branch icons and labels have clear spacing; the site still loads one map per page. Local validation passed across 103 HTML pages and the existing desktop/mobile navigation checks.

## Bulk answer controls — 4 October 2026

- Added Expand all and Collapse all above the mark-group links on both combined Q&A reader URLs. The shared renderer includes these controls for future topics.
- All 42 answers start collapsed. Bulk controls affect answer explanations and answer diagrams, while question wording and diagrams remain visible. Individual disclosures remain usable after either bulk action.
- Browser checks passed on desktop and mobile, including repeated clicks, keyboard activation, all 42 answers, answer diagrams, print expansion and restoration of previous choices. Bulk controls are hidden in print.
- Inspected both Q&A reader screenshots. Changes remain local and uncommitted.

## Reference-style revision maps and full-screen viewer — 4 October 2026

- Replaced the brief branch summaries with six complete visual revision sheets: Cells, Cell processes, Transport processes, Exchange surfaces, Microscopy and Culturing microorganisms. Each has a central title, eight compact bordered panels, highlighted keywords and concept-specific drawings. The attached image supplied layout only; none of its subject content was imported.
- Reviewed AQA 8461 section 4.1 against the official local PDF (PDF pages 15–22) and the current AQA Cell biology webpage. map-coverage.json maps all twelve specification subsections, required practicals 1–3, practical evaluation and relevant maths to the sheets. No phase-name detail or unrelated organelles were imported from the reference.
- Scientific review: DNA copying visibly creates joined copies before mitosis; separation has no intact nuclear envelope; each daughter cell has a matching complete set. Captions identify the simplified two-chromosome example. Root hair drawings have an extension and no chloroplasts; the meristem cue shows a growing tip. Transport drawings distinguish water and solute, net movement and respiration energy. SA:V cubes have a 1:3 side ratio; gas arrows end in alveolar air and blood respectively. Binary fission, colonies, taped plates and inhibition zones have separate illustrations.
- SVG originals preserve sharp text and diagrams during zoom; PNG exports supply actual-map thumbnails. Editable panel content and accessible Markdown text versions are maintained alongside the drawing source. The broader resource builder now delegates standalone-map pages to the shared viewer builder.
- Topic Mind maps opens a full-screen modal gallery. Thumbnails open one map in that modal. Fit, zoom in/out, actual size, mouse drag, touch/scroll panning, back-to-gallery, close/Escape, text version and printing are available. Background scrolling is locked; forward/reverse Tab wraps within the modal and closing restores the trigger's focus. Normal links and standalone pages remain usable without JavaScript.
- Inspected all six map exports and the desktop/mobile modal screenshots. Local link verification passed across 112 HTML pages, including standalone map readers. Existing notes/navigation and 42-answer Q&A browser checks passed. The dedicated viewer check passed for all six maps, full viewport dimensions, fit/zoom/pan, focus and Escape, print isolation, mobile scrolling, no-script text fallback and locally hosted /study-buddy/ asset paths.
- These changes remain local, uncommitted and unpublished. The new layout and viewer preferences are recorded in AGENTS.md and RESOURCE_GUIDELINES.md for future resources.

## Combined overview and consistent reference format — 4 October 2026

- Added Cell biology overview as the first thumbnail, preserving all six detailed maps. The overview connects eight sections to a yellow central theme: Cell structure, Specialised cells, Differentiation & stem cells, Microscopy, Culturing microorganisms, Chromosomes & mitosis, Diffusion & exchange, and Osmosis & active transport.
- Applied the same numbered blue-bordered panels, blue heading ribbons, curved connections, yellow centre, highlighted key terms and biological illustrations to all seven maps. Detailed maps use a shorter canvas to avoid unnecessary empty space; their text is preserved.
- Checked the overview against the official local specification, PDF pages 15–22. It includes the three practicals, magnification and unit conversions, bacterial population doubling, inhibition-zone area, SA:V and percentage mass change. The six detailed maps retain fuller methods and worked examples. Added overview coverage to map-coverage.json.
- The reference supplies format only. No arbitrary light-microscope magnification ceiling, unnecessary mitosis phase names or new mandatory terminology were imported. Qualifiers such as some bacteria having plasmids and photosynthetic cells having chloroplasts are retained.
- The overview cell-cycle drawing shows two chromosomes before copying, joined copies, matching sets separating without a nuclear envelope, and two matching daughter cells. Colours preserve chromosome identity. Its caption explicitly identifies the simplified example. Water/solute and diffusion/active-transport directions are unchanged.
- Inspected all seven exports. Corrected central illustration/title overlap, wrapped long central titles and preserved DNA capitalisation. Fixed punctuation wrapping so a full stop cannot become a separate line after a highlighted term.
- All 114 local HTML pages passed link checks. Website navigation and desktop/mobile layouts passed. The final dedicated viewer check passed all seven SVGs, full-screen dimensions, fitting, zoom/pan, focus/Escape, scroll locking, printing, mobile scrolling, no-JavaScript text fallbacks and /study-buddy/ hosted asset paths.
- Preferences recorded in AGENTS.md and RESOURCE_GUIDELINES.md. All work remains local, uncommitted and unpublished.

## Combined visual-relationship map — 4 October 2026

- Redesigned only 00-cell-biology-overview following the latest reference: asymmetric section sizes, a central cloud title and coloured labelled links. Detailed maps remain on their existing renderer pending explicit user approval.
- Added function-keyed organelle markers on animal/plant cells, a bacterial DNA-loop/plasmid drawing, adaptation illustrations alongside specialised-cell explanations, a resolution comparison, a clearly visible chromosome-copy/separation/daughter-cell sequence, particle models beside transport definitions, and an inhibition-zone diameter drawing with the area formula. Illustrations explain the adjacent content rather than filling reserved icon slots.
- Retained all topic sections, all three practicals, maths, stem-cell sources/applications/risks, exchange adaptations and relevant qualifiers. Checked the official local PDF; layout reference does not override the specification. Source text remains available in the reader.
- Reviewed complete export, chromosome close-up and browser viewer. Corrected overlapping row labels, branch-label clipping, bottom calculation clipping and empty space. Kept xylem lumen visually open, chromosome identity consistent, no nucleus around separating copies, membrane and particle legends explicit, and water movement dilute to concentrated.
- Passed 114-page local link check and the full desktop/mobile viewer check, including fitting, zoom/pan, focus/Escape, print and no-JavaScript fallbacks. SHA-256 comparison confirms all 24 subtopic SVG, PNG, Markdown and standalone HTML files are byte-for-byte unchanged.
- Saved requested Extra High reasoning preference in authoring instructions; this did not change the active turn's model setting. Changes remain local, uncommitted and unpublished.

## Combined-map spacing correction — 4 October 2026

- Reclaimed the large empty upper corridor: Cell structure is now wider and shallower, and Specialised cells sits alongside it with a 50 px gutter. Cell division starts higher and has a 1070 × 1230 px panel, compared with 860 × 1020 px previously. Its diagram and body text are larger, with clear paragraph gaps.
- Paragraphs now flow from measured wrapped line counts; formula boxes grow to fit their text. Repositioned connector labels onto clear backgrounds in reserved gutters. Split labels and the two-line central title have sufficient line spacing.
- Added a browser geometry check for actual rendered text, including nested SVG transforms. It caught and resolved two further bounding-box collisions (the central title and Xylem/phloem label). Final result: 672 text elements, no overlapping text and none outside its section border. Inspected the full export and desktop full-screen viewer.
- Full-screen desktop/mobile, fit/zoom/pan, keyboard, print and offline/hosted-path browser checks passed; all 114 local HTML pages passed link verification. SHA-256 comparison confirms all 30 subtopic source/image/HTML map files and readers are unchanged from the start of this correction.
- Only the combined map was changed. No commit, push or deployment was made.

## Landscape mind maps — 4 October 2026

- Applied the user-approved visual style to all six detailed maps and reflowed the combined overview into landscape for the full-screen website viewer. Retained the approved overview's section artwork, with changed positions and relationship routes.
- Detailed maps use measured text, varied branch widths, highlighted terms and labelled concept illustrations. Kept all eight source panels per detailed map assigned exactly once. All seven editable Markdown text alternatives are byte-for-byte unchanged.
- Preserved joined chromosome copies, separation into matching sets, water/solute legends, net-movement direction, size geometry and the diameter-to-radius calculation. Added a labelled slide preparation diagram and an illustrative osmosis graph.
- Reviewed all seven exported images. Browser measurements pass for 3,165 rendered text elements: no text collisions, section overflow or canvas clipping. Bold subheadings use bold font metrics; scientific DNA capitalisation is retained.
- Verification passed: scripts/check_landscape_mindmaps.cjs; scripts/check_mindmap_modal_browser.cjs (desktop/mobile, seven SVG maps, fit/zoom/pan, focus/Escape, print isolation, offline fallbacks and hosted asset paths); scripts/check_project_site.py (114 pages, local links and 73 topic folders).
- Rebuilt standalone readers and the offline website. Saved the landscape preference in AGENTS.md and RESOURCE_GUIDELINES.md. No commit, push or deployment performed.

## Spacing correction — 4 October 2026

The earlier text-only layout check missed intersecting panel rectangles and cramped relationship corridors in the landscape overview. Repositioned the seven overview sections with wider gutters and independent connector routes. Expanded the Culturing microorganisms centre to two well-spaced lines with measured padding; moved the lower branches into spare canvas space. Content and diagrams are unchanged. The layout check now also verifies section/heading separation, central-title padding and sampled connector paths against panel interiors. All seven maps pass these checks. Changes remain local.

## Consistent internal section padding — 4 October 2026

Applied to all seven mind maps: larger side/bottom insets, clear heading-to-body separation, more subsection spacing, and wider section/central-title spacing across all detailed maps. Overview panels now contain independent heading and body groups with padded placement; biological artwork retains its proportions. Connector routes use clear corridors above/below the section rows. Browser checks now require at least 16 px body inset and 18 px heading/body separation at the native 2400 px export, and fail when either metadata group is missing. All seven pass. Full source content and editable text alternatives retained; no commit or push.
