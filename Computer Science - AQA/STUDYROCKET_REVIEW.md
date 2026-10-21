# Computer Science — Study Rocket coverage review

Reviewed 21 October 2026 against the local AQA 8525 specification for first exams in 2027. This is internal source and coverage tracking, not a student reading page.

All 25 pages linked from [Study Rocket GCSE Computer Science AQA](https://studyrocket.co.uk/revision/gcse-computer-science-aqa) were read. They were used to identify gaps and comparisons. The explanations and practice cards use original wording; the revised AQA specification controls assessable coverage. Full source text is not redistributed.

The index contains no relational databases/SQL page. Topic 07 was independently reviewed against AQA 3.7 and the existing worked database.

| Topic | Cards before | Added | Existing answers refined | Cards now |
|---|---:|---:|---:|---:|
| 01 - Fundamentals of algorithms | 22 | 16 | 1 | 38 |
| 02 - Programming | 26 | 20 | 2 | 46 |
| 03 - Fundamentals of data representation | 22 | 23 | 1 | 45 |
| 04 - Computer systems | 22 | 21 | 2 | 43 |
| 05 - Fundamentals of computer networks | 22 | 21 | 2 | 43 |
| 06 - Cyber security | 28 | 19 | 2 | 47 |
| 07 - Relational databases and SQL | 28 | 17 | 1 | 45 |
| 08 - Ethical legal and environmental impacts | 28 | 20 | 2 | 48 |
| **Total** | **198** | **157** | **13** | **355** |

Each topic keeps its source links, decisions and specification mapping in studyrocket-review.json. Additional cards and answer refinements are stored in revision-flashcards.json so regeneration from Q&A preserves them. Existing Q&A-derived cards remain in the same deck.

## Sources and decisions

### 01 - Fundamentals of algorithms

- [Fundamentals Of Algorithms](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/computational-thinking-and-problem-solving/fundamentals-of-algorithms)
- [Searching Algorithms](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/computational-thinking-and-problem-solving/searching-algorithms)
- [Sorting Algorithms](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/computational-thinking-and-problem-solving/sorting-algorithms)

**Refined note sections:** Inputs, processing, outputs and trace tables, Binary search, Merge sort.

- Existing decomposition, abstraction, inputs/process/output, representations and efficiency were already developed. Added a selective-output trace and the effects of moving initialisation/output.
- Retained correct current binary-search implementation. Added last-candidate and empty-list reasoning. Did not import source bounds that can miss the last item or unsafe REPEAT linear search.
- Existing passes, flags, comparisons and illustrated merges retained. Added an odd-length merge example; equal-sized input is not a requirement.
- Did not import advice to prefer pseudocode regardless of the question. Current AQA explicitly requires the requested response form.

### 02 - Programming

- [Data Structures](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/computational-thinking-and-problem-solving/data-structures)
- [Programming Concepts](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/computational-thinking-and-problem-solving/programming-concepts)
- [Structured Programming](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/computational-thinking-and-problem-solving/structured-programming)

**Refined note sections:** Arrays and records, Subroutines and structured programming.

- Existing types, named values, operator tables, nested control, input and examples retained. Expanded cards on endpoint, branch and post-condition differences.
- Added structure versus persistence and array-of-record reasoning. Did not import claims that records are inherently permanent or every language starts indexing at zero.
- Added a documented interface, parameter-order example, comment quality and shared dependencies. Retained direct use of return values; source claim that returns must be assigned is incorrect. Global-state problems are explained through coupling, not a blanket memory-saving claim.

### 03 - Fundamentals of data representation

- [Binary Arithmetic](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/computational-thinking-and-problem-solving/binary-arithmetic)
- [Number Bases Binary](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/computational-thinking-and-problem-solving/number-bases-binary)
- [Number Bases Hexadecimal](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/computational-thinking-and-problem-solving/number-bases-hexadecimal)
- [Character Encoding](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/written-assessment/character-encoding)
- [Data Compression](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/written-assessment/data-compression)
- [Image Encoding](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/written-assessment/image-encoding)
- [Representing Sound](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/written-assessment/representing-sound)

**Refined note sections:** Binary arithmetic and shifts, Bitmap images, Digital sound, Why compression is used.

- Existing complete conversions and decimal-prefix methods retained; expanded recall on context, units, hex equivalence and the unsigned range.
- Added an original valid three-input addition. Did not copy the inconsistent 106 + 41 worked check or describe discarded right-shift remainders as an underflow error.
- Retained Unicode codes 0–127 and encoding-dependent storage. Did not import the incorrect four-billion-character implication or first-127 wording.
- Added brief metadata context beside the required bitmap formula and supplied missing given values for the existing sound example. Metadata calculation is not represented as an extra requirement; AQA needs pixel count and depth only.
- Preserved detailed RLE/Huffman worked examples, tree and overhead limits. Added an original percentage-saving calculation and focused lossless/lossy retrieval cards.

### 04 - Computer systems

- [Boolean Logic](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/computational-thinking-and-problem-solving/boolean-logic)
- [Programming Languages](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/computational-thinking-and-problem-solving/programming-languages)
- [Memory And Storage](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/written-assessment/memory-and-storage)
- [Software Classification](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/written-assessment/software-classification)
- [System Architecture Cpu](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/written-assessment/system-architecture-cpu)

**Refined note sections:** System and application software, Cache memory.

- Existing full three-input truth table, intermediate columns and gate diagrams retained. Kept XOR, which the source gate overview omits, because it is explicitly required by revised AQA.
- Expanded multitasking versus parallel cores and the purpose/limits of common utilities. Did not import a claim that a core necessarily completes only one instruction per clock.
- Existing FDE, dedicated embedded role and cache explanation retained. Added cache/RAM/saved-file comparison and retrieval cards. Did not import outdated fixed cache sizes, embedded hardware-layout rules or one-cycle-per-instruction equivalence.
- Preserved detailed current HDD/SSD mechanisms and concise tape/USB/card examples. Omitted outdated price/capacity limits and optical storage as mandatory revised content; corrected ROM-only-BIOS and cloud-sync-equals-backup implications.
- Retained revised-AQA interpreter definition and qualified efficiency/portability comparison. No blanket claim that all firmware requires assembly or that compiled programs cannot be reverse-engineered.

### 05 - Fundamentals of computer networks

- [Computer Networks](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/written-assessment/computer-networks)
- [Network Protocols](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/written-assessment/network-protocols)
- [Network Security](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/written-assessment/network-security)
- [Network Topologies](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/written-assessment/network-topologies)

**Refined note sections:** Wired and wireless networks, Protocols.

- Retained PAN/LAN/WAN, media comparison and conditional security. Added bandwidth versus delay and whole-route bottlenecks. Did not import fixed 10 m Bluetooth ranges, AirDrop-as-Bluetooth-only, or speed-of-light as a complete throughput explanation.
- Reviewed bus/star source page; these topologies are not named requirements of revised AQA 3.5. Did not add a compulsory topology section or flashcards.
- Kept the six required protocol names and four layers. Added an original lost/out-of-order data example and routing/reliability/encryption distinction. FTP/UDP and detailed Ethernet/Wi-Fi protocol families were not added as required material.
- Retained accurate MAC spoofing and HTTPS limits. Did not import permanent-unchangeable MAC address or blanket encrypted-messaging guarantees. Added focussed cards on each security control’s distinct job.

### 06 - Cyber security

- [Cyber Security](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/written-assessment/cyber-security)
- [Social Engineering And Malicious Code](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/written-assessment/social-engineering-and-malicious-code)

**Refined note sections:** Pharming and fake destinations, Social engineering, Layered protection and penetration testing.

- Existing required threats and controls retained. Added an original permissions-test lifecycle and focused cards on limits, supported software, reuse, media and recovery. Did not import fixed password-cracking times or the source quiz’s false claim that penetration testing does not find flaws.
- Added targeted-phishing and independent-contact clarification plus HTTPS limits. Did not import a padlock as proof against fraud, a broad-only definition of phishing, or adware as a named revised requirement. Preserved the required virus/trojan/spyware distinction.

### 07 - Relational databases and SQL

No corresponding Study Rocket page; reviewed against AQA 3.7.

**Refined note sections:** Planning and checking a query.

- The supplied Study Rocket index has no relational-database or SQL page. This topic was independently checked against current AQA 3.7 and the existing local notes, rather than claiming Study Rocket coverage.
- Retained all sixteen worked SQL queries, example tables and relationship diagram. Added an integrated query-error comparison and original short cards for keys, filtering, result multiplicity and required data-changing commands. No beyond-spec aggregation or schema commands introduced.

### 08 - Ethical legal and environmental impacts

- [Impact Of Digital Technology](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/written-assessment/impact-of-digital-technology)

**Refined note sections:** Explaining and evaluating an impact, Cloud storage.

- Retained all eight current AQA contexts, including autonomous vehicles absent from the source list. Added cloud-adoption causes and a developed stakeholder example instead of a disconnected list of pros and cons.
- Used the source as a discussion-coverage prompt, not legal guidance. Did not import outdated current-law wording, simplistic hacking/cracking definitions, blanket every-essay-three-perspectives rules or detailed copyright-of-algorithms as a required 2027 context.
- Expanded retrieval on privacy principles, indirect stakeholders, proportionality, employment, implants and lifecycle trade-offs. Existing qualified privacy and data-protection explanations retained.

## Verification

- All 36 direct revision reading groups and all eight expanded decks checked at desktop and two narrow widths. Cards retain focus, keyboard reveal/navigation and access to long answers; print shows all cards without screen height limits.
- Hidden sources, retained images, complete print-all headings and the flat revision menus checked. Existing code-rendering tests and supplement regeneration tests passed.
- Four new SQL card answers executed against fresh copies of the displayed example database, checking retrieval and exact record changes. New trace/calculation examples and final-candidate/empty-list binary searches checked.
