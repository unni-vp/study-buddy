# Fundamentals of data representation

## Binary, decimal and hexadecimal

Computers store every instruction and piece of data as **bit patterns**. The same pattern could represent a number, character, pixel or sound sample; its meaning depends on how software interprets it.

| Base | Digits | Place values |
|---|---|---|
| Decimal, base 10 | 0–9 | powers of 10 |
| Binary, base 2 | 0 and 1 | powers of 2 |
| Hexadecimal, base 16 | 0–9 and A–F | powers of 16 |

Hexadecimal is a compact, readable way to write binary: **one hexadecimal digit represents four bits**. It is used for values such as colour codes and memory addresses.

### Place value and meaning

In a base, each place is worth the base times the place to its right. In decimal, 342 means 3 hundreds, 4 tens and 2 units. In binary, the places are 1, 2, 4, 8 and so on, read from right to left.

Electronic circuits can distinguish two states, represented as **0 and 1**. Software uses patterns of those bits to encode many types of information. A bit pattern has no single meaning without its context: `01000001` could mean the integer 65 or the character `A` in ASCII.

Hexadecimal does not make a computer's stored data smaller by itself. It gives people a shorter way to write the **same bit pattern**, reducing the number of digits they need to read or copy.

## Converting number bases

For an 8-bit binary number, use place values:

| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|---:|---:|---:|---:|---:|---:|---:|---:|

`10110110` = 128 + 32 + 16 + 4 + 2 = **182**.

To convert decimal to binary, select place values that add to the number. For 45: 32 + 8 + 4 + 1, so **00101101**.

For binary ↔ hexadecimal, split binary into groups of four from the right:

`1101 0110` → D and 6 → **D6**.

Hexadecimal `7B` = (7 × 16) + 11 = **123**. Values in this course range from 0 to 255, equal to `00000000`–`11111111` or `00`–`FF`.

### Decimal to binary, step by step

Convert **73** to an 8-bit binary value. Work from the largest place to the smallest, subtracting only when that place is used.

| Place value | Remaining amount before the decision | Bit and decision |
|---|---|---|
| 128 | 73 | Write 0 because 128 is too large. |
| 64 | 73 | Write 1 and subtract 64, leaving 9. |
| 32 | 9 | Write 0 because 32 is too large. |
| 16 | 9 | Write 0 because 16 is too large. |
| 8 | 9 | Write 1 and subtract 8, leaving 1. |
| 4 | 1 | Write 0. |
| 2 | 1 | Write 0. |
| 1 | 1 | Write 1, leaving 0. |

The answer is **`01001001`**. Check it by adding 64 + 8 + 1 = 73. Leading zeroes preserve a requested width without changing the number's value.

### Converting hexadecimal in either direction

The letters **A, B, C, D, E and F** represent decimal 10, 11, 12, 13, 14 and 15.

To convert `9C` to binary, convert each digit separately: 9 becomes `1001`, and C becomes `1100`. Joining them gives **`10011100`**. Keep four bits for each hexadecimal digit, including leading zeroes within a group.

To convert decimal 156 directly to hexadecimal:

1. Divide 156 by 16. The quotient is **9** and the remainder is **12**.
2. Write the quotient as the first digit, 9.
3. Convert remainder 12 to C. The answer is **`9C`**.

To reverse it, calculate **(9 × 16) + 12 = 156**. This is the same value represented in a different base, not a new quantity.

## Bits, bytes and prefixes

- A **bit** is one binary digit, 0 or 1.
- A **byte** is 8 bits.
- Lower-case **b** means bit; upper-case **B** means byte.

Use decimal prefixes:

- 1 kB = 1,000 bytes
- 1 MB = 1,000 kB
- 1 GB = 1,000 MB
- 1 TB = 1,000 GB

To move to a larger unit, divide by 1,000. To move to a smaller unit, multiply by 1,000.

### Comparing sizes without mixing units

A file of **2.4 MB** contains 2,400,000 bytes. Multiplying by 8 gives **19,200,000 bits**. Converting MB to bits therefore requires both the decimal prefix and the bits-per-byte conversion.

To compare 900 kB with 1.2 MB, convert 1.2 MB to **1,200 kB**. The second file is larger by **300 kB**. Comparing the numbers 900 and 1.2 without their units would give the wrong result.

## Binary arithmetic and shifts

Binary addition follows these facts:

- 0 + 0 = 0
- 0 + 1 = 1
- 1 + 1 = 10, so write 0 and carry 1
- 1 + 1 + 1 = 11, so write 1 and carry 1

| Feature | Logical left shift | Logical right shift |
|---|---|---|
| Bit movement | Moves bits left; fills empty positions with zero. | Moves bits right; fills empty positions with zero. |
| One-place effect | Multiplies an unsigned whole number by 2 **if no significant bit is lost**. | Performs integer division by 2 on an unsigned whole number. |
| What can be lost? | Bits shifted beyond the left edge are discarded. | Bits shifted beyond the right edge are discarded, so an odd value loses its remainder. |


Example: `00010110` (22) shifted left once becomes `00101100` (44).

### A complete addition

Add `00001101` (13) and `00000111` (7). Start at the rightmost column and include any carry from the previous column.

```text
  00001101
+ 00000111
----------
  00010100
```

| Column, starting at the right | Values added | Bit written | Carry to the next column |
|---|---|---|---|
| 1 | 1 + 1 | 0 | 1 |
| 2 | 0 + 1 + carry 1 | 0 | 1 |
| 4 | 1 + 1 + carry 1 | 1 | 1 |
| 8 | 1 + 0 + carry 1 | 0 | 1 |
| 16 | 0 + 0 + carry 1 | 1 | 0 |

The remaining leading columns are zero. Check: **13 + 7 = 20**, and `00010100` is 16 + 4 = 20.

A column containing three 1s has a total of binary `11`: write 1 and carry 1. The same rule applies when adding three binary numbers.

### Shifts and discarded bits

A two-place left shift multiplies by **4**, provided no significant bit is lost. For example, `00000111` (7) becomes `00011100` (28).

A logical right shift fills the left positions with zeroes. Shifting `00000111` right once gives `00000011` (3): the final 1 is discarded, so the result is whole-number division, not 3.5.

With a fixed 8-bit width, shifting `10000001` left once gives `00000010`. The leading 1 falls outside the available width, so the stored result is not twice the original value. Always show the specified number of positions.

### Adding three numbers

The same column rules work for three inputs. Add 21, 10 and 4 using eight bits:

```text
  00010101
  00001010
+ 00000100
----------
  00100011
```

Work from right to left, carrying into the next column when needed. The 4s column contains two 1s, so write 0 and carry 1 into the 8s column. That carry combines with the existing 1 in the 8s column, producing another carry. The final result is **35**, which checks against 21 + 10 + 4.

A logical right shift discards low-order bits and keeps the whole-number result. Shifting 13 right twice gives 3 because **13 DIV 4 = 3**. The discarded remainder is not a fractional value retained elsewhere in the bit pattern.

## Character encoding

A **character set** is the collection of characters that can be represented. A character encoding assigns each character a numeric code.

| Feature | 7-bit ASCII | Unicode |
|---|---|---|
| Range | 128 possible codes. | Far more alphabets, symbols and emoji. |
| Characters supported | A limited set, suitable for basic English text and control characters. | Characters used across many languages. |
| Relationship | Codes 0–127 form the ASCII set. | Uses the same character codes as ASCII for 0–127. |


Codes are grouped in sequences: if `A` is 65, then `B` is 66.

Unicode is needed because ASCII cannot represent the wide range of characters used worldwide. You do not need details of UTF-8 or UTF-16.

### Using a code table

A shared encoding lets a sender and receiver agree on which character a number represents. Without that agreement, the same stored value could be displayed incorrectly.

If uppercase `A` is 65, uppercase `D` is **68**, because it is three positions later in that sequence. If lowercase `a` is 97, lowercase `d` is **100**. Do not assume the uppercase and lowercase groups are adjacent.

The character `"4"` is a symbol in text. Its ASCII code is 52; the integer 4 has a different purpose. Spaces and control characters also occupy codes and must be counted when calculating encoded text size.

For 20 characters stored in 7-bit ASCII, the character data needs **20 × 7 = 140 bits**. Use the encoding width stated in the question. Unicode supports far more characters, but its storage per character depends on the encoding; it is not always one fixed number of bits.

## Bitmap images

A **pixel** is one picture element. A bitmap stores a grid of pixels and a code for each pixel's colour.

| Setting | What it measures | Effect of increasing it |
|---|---|---|
| **Image dimensions** | Width × height, in pixels. | More pixels can record more detail, but increase uncompressed file size at fixed colour depth. |
| **Colour depth** | Bits used for each pixel. | More possible colours, but a larger uncompressed file at fixed dimensions. |


Number of possible colours = **2^colour depth**.

**Image size in bits = width × height × colour depth**

For 800 × 600 pixels at 24 bits per pixel:

1. The image has 800 × 600 = **480,000 pixels**.
2. Each pixel uses 24 bits, so the data needs 480,000 × 24 = **11,520,000 bits**.
3. Divide by 8 to get **1,440,000 bytes**, or **1.44 MB**.

This calculation covers uncompressed pixel data. Include extra storage only if the question supplies it.

Simple black-and-white bitmap questions may ask you to convert each 0 or 1 into a pixel, row by row.

### Turning bits into pixels

Use this key: **0 is white, and 1 is black**. Read each row from left to right, then move down to the next row.

| Row | Stored bits | Pixel row |
|---|---|---|
| 1 | `010` | White, black, white. |
| 2 | `111` | Black, black, black. |
| 3 | `010` | White, black, white. |

These rows form a small cross. To encode a drawing, reverse the process and write the code for every pixel, including white background pixels. The image needs **3 × 3 × 1 = 9 bits** of pixel data.

At colour depth 2, the four codes `00`, `01`, `10` and `11` can represent four colours. At depth 8, **2⁸ = 256 colours** are possible. The image need not actually use every available colour.

At fixed depth, doubling the width doubles the pixel data. Doubling both width and height makes **four times** as many pixels. At fixed dimensions, changing depth from 8 to 24 bits makes the pixel data **three times** as large. More pixels or colours allow more detail to be represented, but do not guarantee that a poor original image becomes detailed.

### Pixel data and metadata

**Metadata** describes other data. For a bitmap, the dimensions and colour depth tell software how to interpret its stored pixel bits. The same 24 bits could describe a 4 × 6 image at 1 bit per pixel or a 2 × 6 image at 2 bits per pixel.

The calculation `width × height × colour depth` gives the **pixel data**, not necessarily the size of a complete saved file. Headers or other metadata can need additional storage, while compression can reduce the pixel representation. Use the values supplied by the question; do not invent an extra allowance.

## Digital sound

Sound waves are analogue. To store sound digitally, an analogue-to-digital converter measures the wave's amplitude at regular times.

| Setting | What it measures | Effect of increasing it |
|---|---|---|
| **Sampling rate** | Samples per second, measured in hertz (Hz). | Records changes more frequently. At fixed resolution and duration, the uncompressed file grows. |
| **Sample resolution** | Bits used for each sample. | Records amplitude more precisely. At fixed rate and duration, the uncompressed file grows. |


Both can improve how accurately the digital recording represents the original sound.

**Sound size in bits = sampling rate × sample resolution × duration in seconds**

For a single-channel recording lasting **10 seconds**, sampled at **44,000 Hz** with **16 bits per sample**:

1. There are 44,000 × 10 = **440,000 samples**.
2. At 16 bits per sample, the data needs 440,000 × 16 = **7,040,000 bits**.
3. Divide by 8 to obtain **880,000 bytes**, or **880 kB**.

### What a sample records

An analogue wave varies continuously. Sampling measures its **amplitude at separate, regularly spaced times**, then represents those measurements using binary values. Imagine noting the height of a moving wave at regular moments: more observations follow its changing shape more closely.

Sampling rate controls **how often** measurements are made. Sample resolution controls **how precisely each amplitude** can be represented. Increasing one does not automatically increase the other.

A resolution of 8 bits allows **256 different amplitude values**. A resolution of 16 bits allows **65,536 values**, so rounding each measurement to an available value can be more precise.

At fixed duration and resolution, doubling sampling rate doubles the uncompressed data. At fixed rate and duration, doubling bits per sample also doubles it. Convert minutes to seconds before using the formula: 2 minutes is **120 seconds**.

## Why compression is used

**Compression** reduces the number of bits required to store or transmit data.

Benefits include less storage, faster transfer and lower bandwidth use. Compression and decompression require processing, and some methods may lose information.

### Lossy and lossless compression

**Lossless compression** reduces the amount of data without discarding information. Decompression restores the **original data exactly**.

**Lossy compression** permanently discards some information, often detail that people are less likely to notice. Decompression **cannot restore all the original data**.

Think of lossless compression as packing the same clothes more efficiently. Lossy compression is like leaving some clothes behind: there is less to carry, but unpacking cannot bring back what was left out.

| Feature | Lossless compression | Lossy compression |
|---|---|---|
| **Information** | No information is discarded. | Some information is permanently discarded. |
| **Recovering the original** | The original data can be recovered **exactly**. | The original data cannot be recovered exactly from the compressed version alone. |
| **Quality** | Decompressed data matches the original. | Images or sound may lose noticeable quality, especially with stronger compression. |
| **Suitable use** | Programs, text and records where every detail must remain correct. Also useful for images that need exact preservation. | Photos, music and video when some loss of detail is acceptable. |
| **Examples** | RLE, Huffman coding, ZIP archives and PNG images. | Typical JPEG photographs and MP3 audio. |
| **File-size trade-off** | The saving depends on the data and method; some data may not become smaller. | Can often make larger reductions by accepting a loss of detail. |

**Choose lossless for program code:** losing even one character could change how the program behaves. A smaller music file may justify some loss of sound detail, but that depends on the required quality.

### Comparing a saving

Suppose a file is reduced from **800 kB to 600 kB**:

1. Subtract the compressed size from the original: 800 − 600 = **200 kB saved**.
2. Compare the saving with the original: 200 ÷ 800 = **0.25**.
3. Multiply by 100 to obtain a **25% reduction**.

The compressed file retains **75% of the original size**. This is not the same statement as saying 75% was saved. A size reduction alone does not tell you whether a method is lossy or lossless; that depends on whether the original data can be recovered exactly.

## Run-length encoding

**Run-length encoding (RLE)** is a **lossless** method. It stores each run as a frequency/data pair, so the original sequence can be reconstructed exactly. It works well when data contains long repeated sequences.

`0000011100000011` becomes:

`5 0, 3 1, 6 0, 2 1`

RLE can make varied data larger because short runs need their own frequency values. Treat each bitmap row separately when the question tells you to encode rows.

### Decoding and checking storage

For frequency/data pairs `4 1, 2 0, 3 1`, write four 1s, two 0s and three 1s. The original sequence is **`111100111`**. The frequencies add to 9, which checks the number of reconstructed pixels.

The written digits alone do not tell you the compressed size. If a question allocates 4 bits to each frequency and 1 bit to each pixel value, three pairs use **3 × (4 + 1) = 15 bits**. This is larger than the original nine 1-bit pixels.

Long uniform areas often compress well with RLE. Alternating black and white pixels produce short runs, so storing a count for each run may add more data than it saves.

## Huffman coding

**Huffman coding** represents symbols using codes of different lengths. Frequently used symbols generally receive shorter codes. Some symbols still share the same code length.

Huffman coding is **lossless**: the correct tree or code table lets the receiver recover every original symbol.

1. Count each symbol's frequency.
2. Repeatedly combine the two lowest-frequency nodes.
3. Label branches 0 and 1.
4. Read each symbol's code from root to leaf.

The codes are **prefix-free**: no complete code is the start of another code. This lets the receiver decode the message without needing spaces between codes.

To calculate compressed size, multiply each symbol's frequency by its code length and add the results. Compare with uncompressed ASCII at **7 bits per character** when instructed.

### Worked example: BANANA

#### 1. Count the characters

The message **BANANA** has six characters:

- **A:** 3 occurrences.
- **N:** 2 occurrences.
- **B:** 1 occurrence.

#### 2. Build the tree

Always combine the **two lowest frequencies still available**:

1. Combine **B (1)** and **N (2)** to make a node with frequency **3**.
2. Combine that node **(3)** with **A (3)** to make the root, frequency **6**.

In this tree, a **left branch is 0** and a **right branch is 1**.

![Huffman tree for BANANA. The root has frequency 6. Its left branch, 0, leads to A with frequency 3. Its right branch, 1, leads to a node of frequency 3. That node's left branch, 0, leads to B with frequency 1; its right branch, 1, leads to N with frequency 2.](../Diagrams/huffman-banana.svg)

#### 3. Read the codes and encode the message

Read each path **from the root to the character**:

| Character | Frequency | Code |
|---|---|---|
| A | 3 | `0` |
| N | 2 | `11` |
| B | 1 | `10` |

Match each character to its code:

```text
B  A  N  A  N  A
10 0  11 0  11 0
```

Joining the codes gives **`100110110`**. The spaces above only make the groups easier to see.

**To decode**, follow the bits from the root until reaching a character. Write that character, then restart at the root. For example, `10` gives B, then `0` gives A.

#### 4. Calculate the compressed message size

Multiply each character's frequency by its code length:

- **A:** 3 × 1 = **3 bits**.
- **N:** 2 × 2 = **4 bits**.
- **B:** 1 × 2 = **2 bits**.

Total = 3 + 4 + 2 = **9 bits**.

#### 5. Compare with 7-bit ASCII

For the **message data alone**:

- **ASCII:** 6 characters × 7 bits = **42 bits**.
- **Huffman:** **9 bits**.
- **Saving:** 42 − 9 = **33 bits**.

If a question supplies storage for the code table or tree, include it in the compressed total.

When frequencies tie, more than one valid tree may be possible. The codes can differ, so follow the tree and branch labels given in the question.

### RLE and Huffman coding

| Feature | Run-length encoding | Huffman coding |
|---|---|---|
| Main idea | Replaces consecutive repeated values with frequency/data pairs. | Gives shorter codes to more frequent symbols. |
| What matters | The lengths of consecutive runs. | How often each symbol appears. |
| Example | Five consecutive zeroes become `5 0`. | A common character gets a shorter code than a rare character. |
| Checking the saving | Include the space needed to store each pair; short runs can make data larger. | Multiply each symbol’s frequency by its code length, then add the results. |
| Original data | Can be recovered exactly when decoded. | Can be recovered exactly using the correct code tree. |

### Checking a supplied tree

Read the branch labels actually shown; a tree may use a different left/right convention. Continue until a **leaf**, not merely an internal node. After decoding one symbol, return to the root before reading the next bits.

When building a tree, put each combined frequency back among the remaining frequencies before choosing the next two smallest. Keep that whole subtree together when combining it again. Equal frequencies may allow different valid trees, but decoding always depends on the chosen tree.

The compressed message size is the sum of **frequency × code length for every symbol**, including spaces if present. A short message may save few or no bits once the tree or code table also has to be stored. Distinguish a calculation for message bits alone from a calculation that includes this extra information.

## Calculation checklist

- Write the formula before substituting values.
- Keep bits and bytes distinct; divide bits by 8 to get bytes.
- Use decimal prefixes of 1,000 for this course.
- Show place values or four-bit groups in base conversions.
- Include units and do not round unless instructed.

## Sources

- AQA GCSE Computer Science 8525 specification, section 3.3.

- [PMT Education: original Summary Notes](../Reference Materials/PMT - Summary Notes.pdf). Unmodified source retained with its printed attribution and licence.
- [AQA specification for first exams in 2027](../../00 - Specification/AQA-8525-specification-2027.pdf).
- [Study Rocket: Binary Arithmetic](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/computational-thinking-and-problem-solving/binary-arithmetic). Coverage reference; checked against the current AQA specification.
- [Study Rocket: Number Bases Binary](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/computational-thinking-and-problem-solving/number-bases-binary). Coverage reference; checked against the current AQA specification.
- [Study Rocket: Number Bases Hexadecimal](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/computational-thinking-and-problem-solving/number-bases-hexadecimal). Coverage reference; checked against the current AQA specification.
- [Study Rocket: Character Encoding](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/written-assessment/character-encoding). Coverage reference; checked against the current AQA specification.
- [Study Rocket: Data Compression](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/written-assessment/data-compression). Coverage reference; checked against the current AQA specification.
- [Study Rocket: Image Encoding](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/written-assessment/image-encoding). Coverage reference; checked against the current AQA specification.
- [Study Rocket: Representing Sound](https://studyrocket.co.uk/revision/gcse-computer-science-aqa/written-assessment/representing-sound). Coverage reference; checked against the current AQA specification.
