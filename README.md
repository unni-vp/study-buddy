# Shreya's Study Buddy

This project holds the official curriculum sources and topic folders for creating clear, focused revision resources aimed at **Grades 7-8**.

## Confirmed courses

| Subject | Board | Code | Tier / choices |
| --- | --- | --- | --- |
| Computer Science | AQA | 8525 | Python and pseudocode; revised course for first exams in 2027; untiered |
| English Language | Eduqas | C700QS | Untiered |
| English Literature | Eduqas | C720QS | Macbeth; A Christmas Carol; An Inspector Calls; 2027 poetry anthology; untiered |
| Maths | Pearson Edexcel | 1MA1 | Higher |
| Geography | OCR A | J383 | Geographical Themes; untiered |
| French | AQA | 8652 | Higher |
| Biology | AQA | 8461 | Separate science; Higher |
| Chemistry | AQA | 8462 | Separate science; Higher |
| Physics | AQA | 8463 | Separate science; Higher |

## Open the HTML study library

Open [index.html](index.html) in a browser. It works locally without an internet connection or a server. Navigate Subjects → subject contents → topic → revision notes, mind maps or Questions & answers. Resource readers include links back to the topic and a Print button.

Topics without resources are marked Not yet prepared. Cell biology has 42 practice questions with answers together on one page, grouped by marks. Select Answer to reveal each answer when you are ready to check it. All answers are included when printing. Future topics follow the same combined Q&A layout.

## How to use the library

- Open the relevant subject folder and its README.md for topic navigation and official source links.
- `00 - Specification` contains the complete official PDF and a searchable .txt extraction.
- Numbered main-topic folders contain places for notes, mind maps and combined questions with answers.
- The PDF is authoritative: text extraction can lose tables, superscripts and symbols.
- Biology 4.1 Cell biology now has revision notes, four visual mind maps and combined questions with answers. Other topic folders are ready for resource creation.

## Project instructions

Your teaching preferences are saved in [RESOURCE_GUIDELINES.md](RESOURCE_GUIDELINES.md) and [AGENTS.md](AGENTS.md) for future work. Confirmed course details are in [project-config.json](project-config.json).

## Download verification

Downloaded from official exam-board sources on **4 October 2026**. [specification-manifest.json](specification-manifest.json) records source URLs, page counts, file sizes and SHA-256 hashes for nine full specifications plus the 2027 Literature poetry anthology. AQA's CDN links were obtained from its official qualification pages.

Use the revised 2027 Computer Science course and the new Eduqas poetry anthology, rather than older resources. French uses 8652; the three sciences use the separate-science specifications supplied by the user. Check official updates again before producing resources that depend on exam arrangements or before the exams.

## Details still to confirm

- Liverpool numerical fieldwork data, site details and evaluation (enquiry and qualitative findings confirmed).
- River Alyn numerical data, site spacing, exact velocity method and evaluation (enquiry and qualitative findings confirmed).

The confirmed Geography case studies, energy examples and fieldwork locations are listed in [Geography case studies](Geography%20-%20OCR%20A/CASE_STUDIES.md).

## Reusable scripts

`scripts/download_specifications.py` downloads missing PDFs, verifies they can be read and creates searchable copies plus the manifest. `scripts/setup_topics.py` creates the topic structure and course configuration. The scripts require Python with pypdf; existing PDFs are preserved. Do not rerun setup after personalising course choices without updating the script first.

## Refresh the HTML library

Run `scripts/build_project_site.py` after adding resources. It rebuilds subject contents, topic pages and HTML readers from the current topic folders. `scripts/check_project_site.py` checks local links and the combined folder structure. The original revision notes, images and official PDFs remain available in their subject folders.
