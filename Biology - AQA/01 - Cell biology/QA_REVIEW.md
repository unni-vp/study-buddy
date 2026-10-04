# Cell biology Q&A review

Reviewed on 4 October 2026. Internal record; excluded from the student resource menu.

## Scope and selection

- 42 original/adapted practice questions in one editable Markdown document. Each answer immediately follows its question.
- Six June Higher Paper 1 series examined: 2018, 2019, 2022, 2023, 2024 and 2025. Question papers and final AQA mark schemes preserved locally in `Biology - AQA/00 - Past papers/Paper 1 Higher`.
- Website directories verified: AQA, Physics & Maths Tutor, Save My Exams and Revision Science. Primary evidence is the AQA papers/mark schemes, including copies hosted by PMT and Revision Science; third-party model answers were not used as marking authority.
- `QA_SOURCE_AUDIT.json` records source URLs, paper/question references, recurrence counts and current specification mapping for every practice item. The download manifest records PDF hashes.
- Recurrence counts describe this six-paper sample, once per type per paper. Broad categories overlap. The resource does not predict the 2027 paper or claim to contain every assessable question.
- Q13, Q20, Q24 and Q29 are additional specification practice. Q28 extends a transferable division-time calculation to specification-required bacterial doubling. Extended stem-cell evaluation and practical methods are assembled practice, with proposed mark allocations.

## Curriculum and marking checks

- Local official PDF Section 4.1 and the current AQA online Cell biology specification checked. Required practicals 1–3 are represented. Mathematical and practical skills remain prominent.
- Used the current maximum incubation temperature of 25°C. Preserved the older downloaded specification unchanged.
- Corrected the internal mapping of 2025 Q07.1/Q07.2 to stem cells, Section 4.1.2.3, despite the printed mark scheme's 4.1.3.2 code.
- Inspected source PDF figures and mark-scheme tables visually, including microscopy images, graphs, inhibition zones, chromosomes and marking columns. The 2022 graph entries explicitly say to mark Q01.7 with Q01.8; extracted text alone can misrepresent this relationship.
- Bold phrases express complete ideas rather than isolated word lists. Suggested points remain distinct from official mark schemes. Six-mark methods/evaluations require sequencing or linked reasons and judgements.

## Scientific and numerical checks

- Osmosis: net water movement from dilute to concentrated solution through a partially permeable membrane; movement continues both ways at zero net change. Equal-sized diagram compartments distinguish water and solute.
- Mitosis: DNA replication before mitosis; joined copies visibly separate; matching complete sets in both daughters; no intact nuclear envelope around separating copies. Simplified diagram tracks two chromosomes and does not halve the daughter chromosome count.
- Stem cells: embryonic and adult sources distinguished; plant meristems treated separately; therapeutic cloning and ethics kept within the stated specification.
- Exchange: features linked to surface area, diffusion distance and maintained gradients. Villi and gills distinguished from alveoli. No detailed counter-current theory required by the practice question.
- All worked calculations independently checked: −12% mass change; ×400 total magnification; ×600 image magnification; 254 mm² circular area to 3 significant figures; 5120 = 5.12 × 10³ bacteria; cube ratios 6:1 and 2:1; 0.30 mol/dm³ zero-change concentration; 90 µm real length; ×12 000 cylinder magnification.
- The original graph's six coordinates match the table and fit a straight line. Diameter/radius, matching length units, signed percentage change and standard form checked.

## Presentation and verification

- One combined Q&A reading page with six mark groups (1–6 marks). Plain numbered prompts; no individual question headings or repeated mark labels. The source directory remains a separate utility page. Existing complete-view bookmarks remain valid. Obsolete thematic HTML pages removed during generation.
- Ascending marks verified across the document and reading page. The 42 question-and-answer bodies and all source content were compared during reformatting and preserved exactly, apart from changing the answer label from a heading to bold text. Source references identify patterns; wording, contexts, data and proposed marks may differ from originals.
- Three original SVG diagrams only; editable source in `scripts/build_cell_biology_qa_support.py`. Full-size and mobile screenshots visually inspected. Desktop Q&A diagrams capped at 640 px to reduce vertical space.
- `scripts/check_project_site.py` checks every generated HTML page and all local links, including the twelve source PDFs.
- `scripts/check_cell_biology_qa_browser.cjs` checks all 42 complete pairs, six same-page mark groups, consecutive question numbers, absence of individual headings/mark labels, print view, images, source links and desktop/mobile overflow.
- `scripts/check_project_site_browser.cjs`: existing notes, diagrams, mind maps and desktop/mobile navigation passed with the new Q&A button enabled.

## Future updates

Edit the combined Markdown source, then regenerate support metadata if headings or questions change and rebuild the website. Recheck recurrence evidence and specification mappings when adding questions. Preserve official PDFs and proposed/official mark distinctions. Continue the selective visual approach and the project's scientific diagram checks.

## Answer formatting update

- All 42 answers now use **Answer:**. Single-point answers appear inline; longer answers retain bullets. One- or two-word answers and short answer fragments use plain text.
- A comparison ignoring emphasis, list markers and label changes confirmed that wording, numerical results, sources and diagram links are preserved.

## Answer disclosures — 4 October 2026

- All 42 HTML answers are collapsed by default, with native keyboard/touch disclosures. The combined Markdown content is unchanged.
- Question diagrams and tables stay visible; the answer graph, explanations and answer-specific hints stay inside the disclosure.
- Printing opens every answer and restores previous choices afterwards. Browser verification checks hidden answers, individual toggling, keyboard access, mobile layout and print restoration.
