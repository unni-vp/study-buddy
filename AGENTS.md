# GCSE preparation project

Read RESOURCE_GUIDELINES.md, project-config.json, the relevant subject README.md and the official local specification before authoring resources.

- Prepare students for summer 2027, targeting Grades 7-8.
- Follow the confirmed boards, qualification codes, tiers and Literature text choices in project-config.json.
- Start with simple plain English, then use an everyday analogy, then introduce precise exam vocabulary.
- Highlight must-know facts and bold key terms and supported marking points.
- Prioritise useful exam content without silently removing assessable curriculum content.
- Use short sentences, clear headings, bullets and manageable chunks. Use mind maps for large or complex topics.
- Preserve official downloaded documents. Use the PDF as the source of truth; extracted text may lose table structure and symbols.
- Put each resource in the matching subject/topic/type folder. Record specification sections in internal metadata; keep any student-facing source links concise.
- Clearly distinguish original practice questions and suggested marking points from official questions and mark schemes. Never invent examiner requirements.
- Use Python and pseudocode for Computer Science.
- Use the confirmed Geography case studies in project-config.json and Geography - OCR A/CASE_STUDIES.md. Verify school-specific facts and topic mappings before authoring. Do not assume unconfirmed fieldwork investigations.

This file applies to all future work in this project.

- Use the site_title from project-config.json (Shreya's Study Buddy) in the site header and browser titles. Keep the home page free of the Subjects breadcrumb, YOUR REVISION STARTS HERE preamble and Choose a subject heading. Omit the Subjects breadcrumb and topic/resource availability counts on subject landing pages too; retain useful breadcrumbs on topic and resource pages.
- Keep Computer Science language choices and specification-version details in the project configuration rather than displaying a Python & pseudocode / revised 2027 specification line on its subject landing page.
- Keep the Shreya's Study Buddy header smaller on inner pages, with a smaller wordmark and logo and reduced header height/padding. Preserve the larger home-page branding and keep the name linked to the home page.

- Store one combined Q&A document per topic in Questions and Answers; place each answer directly after its question. Prioritise recurring past-paper question types with verifiable sources.
- Present each topic’s Q&A as one combined reading page, grouped only by increasing marks (1 mark, 2 marks and so on). Do not divide it into thematic menus or separate pages. Use plain numbered prompts, without individual question titles or repeated mark labels. Keep each answer immediately after its question. Link to a separate source directory from the Q&A page; keep specification mapping and review notes outside student resource folders.
- Check past-paper content against the current specification independently of the content codes printed in older mark schemes. For frequency claims, define the sample and count a question type only once per paper; distinguish specification-based additional practice from recurring types. Extended methods and evaluations need linked explanations and judgements, rather than a claim that every bullet automatically earns one mark.
- Maintain the offline HTML library. Run scripts/build_project_site.py after resource changes so navigation stays current.

- Keep student-facing documents focused on subject content. Do not add grade-target introductions, study-direction preambles, authorship disclaimers, explanations of bold formatting, or statements about marks not being guaranteed. Keep necessary factual distinctions, sources and practical safety instructions concise.

- The student is a visual learner. Organise resources around labelled diagrams, illustrated processes, colour-consistent comparisons and short explanations beside the relevant visual. Mind maps must show meaningful relationships with labelled arrows (structure → function → application), not disconnected lists. Use relevant biological drawings or memorable visual cues, with concise labels. Embed visuals beside the corresponding notes, and use illustrated setups for practicals and worked visual steps for calculations when helpful. Keep text alternatives and readable labels.

- Keep the written revision notes. Add useful labelled diagrams alongside explanations wherever they clarify structures, mechanisms, practical methods or calculations; visuals supplement the notes rather than replacing them.

- Student resources must not show specification references, curriculum tracking, content classification labels (such as separate Biology content), or teaching-process labels such as Plain English first. Keep tracking in resource metadata. Keep clear topic headings and useful required-practical titles.
- Mind maps: group closely related concepts under a clear central theme (for example Cells, Cell processes or Transport processes), with curved colour-coded main branches and concise connected sub-branches. Keep meaningful central illustrations and the established branching layout. Avoid unrelated topics or overcrowding. Do not label comparison tables or flowcharts as mind maps.

- Use diagrams selectively in revision notes: only for a genuinely complex mechanism, structure or relationship that is materially easier to understand visually. Keep straightforward facts and calculations as concise notes or tables. Do not add a diagram to every section or append the whole mind-map gallery to the notes. This selective-use preference overrides earlier wording to include visuals wherever possible. Keep focused mind maps in their separate resource section.

- Do not repeat board, qualification code, tier or exam-year banners in topic notes or diagrams. Keep these details in project configuration and subject navigation.
- Before publishing any scientific diagram, follow the accuracy and visual review checks in RESOURCE_GUIDELINES.md. Show the actual mechanism changing between stages; do not reuse an unchanged icon with different labels. For mitosis, visibly draw the joined chromosome copies, their separation and a complete set in each daughter cell. Preserve chromosome identity and number consistently.
- Regenerate diagrams from their editable source and inspect the resulting images and HTML reader. Correct misleading symbols, arrows, scaling, anatomical labels and text overlap before marking a resource ready. Keep review records and specification tracking outside student-facing resource folders.
- Mind-map navigation must use a compact grid of clickable thumbnails of the actual maps, with clear titles. Each opens one mind map on a separate page with a back link. Do not stack every full mind map on the selection page. Keep the illustrated broad-group buttons for revision notes only; Q&A uses one page grouped by marks.
- Keep mind-map thumbnail cards small: four across on wide screens, three on medium screens and two on narrow screens. Reduce card padding and preview size rather than displaying oversized buttons.
- On topic pages, give Revision notes, Mind maps and Questions & answers buttons distinct icons. Use three equally sized buttons filling the content width, with each icon and label centred. Stack them at full width on narrow screens. Keep disabled resource buttons visually clear and accessible names unchanged.
- For future revision notes in every subject, use one compact illustrated menu of a few broad groups. Each group opens its content directly as a single page; do not add another menu or separate pages for individual subtopics. Previous/Next links move between broad groups. Keep full content and a complete print view. Use revision-layout.json as described in RESOURCE_GUIDELINES.md. Q&A has one editable document and one combined reading page per topic, grouped only by marks, with no question titles or individual mark labels. Mind maps use clickable thumbnails, with one map per page and no additional grouping layer.

- Label each Q&A answer **Answer:**, followed by the actual answer. Put single answers on the same line; use bullets where longer responses are easier to follow. Do not use Answer — suggested marking points. One- or two-word answers should be plain text, without bold emphasis. Keep the distinction between practice answers and official mark schemes in sources and internal metadata.

- In HTML Q&A readers, put every answer in its own native details/summary disclosure, closed by default, labelled Answer:. Keep question wording, data and question diagrams visible; hide answer explanations, answer diagrams and answer-specific hints together. Support keyboard and touch use. Printing must reveal all answers and restore the student’s previous open/closed choices afterwards. Keep the editable Markdown as a single combined document with Answer: labels. Apply this to future topics too.
