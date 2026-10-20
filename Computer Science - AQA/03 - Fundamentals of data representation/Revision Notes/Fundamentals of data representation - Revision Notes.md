# Fundamentals of data representation

## Binary, decimal and hexadecimal

Computers store every instruction and piece of data as **bit patterns**. The same pattern could represent a number, character, pixel or sound sample; its meaning depends on how software interprets it.

| Base | Digits | Place values |
|---|---|---|
| Decimal, base 10 | 0–9 | powers of 10 |
| Binary, base 2 | 0 and 1 | powers of 2 |
| Hexadecimal, base 16 | 0–9 and A–F | powers of 16 |

Hexadecimal is a compact, readable way to write binary: **one hexadecimal digit represents four bits**. It is used for values such as colour codes and memory addresses.

## Converting number bases

For an 8-bit binary number, use place values:

| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|---:|---:|---:|---:|---:|---:|---:|---:|

`10110110` = 128 + 32 + 16 + 4 + 2 = **182**.

To convert decimal to binary, select place values that add to the number. For 45: 32 + 8 + 4 + 1, so **00101101**.

For binary ↔ hexadecimal, split binary into groups of four from the right:

`1101 0110` → D and 6 → **D6**.

Hexadecimal `7B` = (7 × 16) + 11 = **123**. Values in this course range from 0 to 255, equal to `00000000`–`11111111` or `00`–`FF`.

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

## Character encoding

A **character set** is the collection of characters that can be represented. A character encoding assigns each character a numeric code.

| Feature | 7-bit ASCII | Unicode |
|---|---|---|
| Range | 128 possible codes. | Far more alphabets, symbols and emoji. |
| Characters supported | A limited set, suitable for basic English text and control characters. | Characters used across many languages. |
| Relationship | Codes 0–127 form the ASCII set. | Uses the same character codes as ASCII for 0–127. |


Codes are grouped in sequences: if `A` is 65, then `B` is 66.

Unicode is needed because ASCII cannot represent the wide range of characters used worldwide. You do not need details of UTF-8 or UTF-16.

## Bitmap images

A **pixel** is one picture element. A bitmap stores a grid of pixels and a code for each pixel's colour.

| Setting | What it measures | Effect of increasing it |
|---|---|---|
| **Image dimensions** | Width × height, in pixels. | More pixels can record more detail, but increase uncompressed file size at fixed colour depth. |
| **Colour depth** | Bits used for each pixel. | More possible colours, but a larger uncompressed file at fixed dimensions. |


Number of possible colours = **2^colour depth**.

**Image size in bits = width × height × colour depth**

For 800 × 600 pixels at 24 bits per pixel:

800 × 600 × 24 = 11,520,000 bits = **1,440,000 bytes**.

Simple black-and-white bitmap questions may ask you to convert each 0 or 1 into a pixel, row by row.

## Digital sound

Sound waves are analogue. To store sound digitally, an analogue-to-digital converter measures the wave's amplitude at regular times.

| Setting | What it measures | Effect of increasing it |
|---|---|---|
| **Sampling rate** | Samples per second, measured in hertz (Hz). | Records changes more frequently. At fixed resolution and duration, the uncompressed file grows. |
| **Sample resolution** | Bits used for each sample. | Records amplitude more precisely. At fixed rate and duration, the uncompressed file grows. |


Both can improve how accurately the digital recording represents the original sound.

**Sound size in bits = sampling rate × sample resolution × duration in seconds**

44,000 Hz × 16 bits × 10 s = 7,040,000 bits = **880,000 bytes**.

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

## Run-length encoding

**Run-length encoding (RLE)** is a **lossless** method. It stores each run as a frequency/data pair, so the original sequence can be reconstructed exactly. It works well when data contains long repeated sequences.

`0000011100000011` becomes:

`5 0, 3 1, 6 0, 2 1`

RLE can make varied data larger because short runs need their own frequency values. Treat each bitmap row separately when the question tells you to encode rows.

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


## Calculation checklist

- Write the formula before substituting values.
- Keep bits and bytes distinct; divide bits by 8 to get bytes.
- Use decimal prefixes of 1,000 for this course.
- Show place values or four-bit groups in base conversions.
- Include units and do not round unless instructed.

## Sources

- AQA GCSE Computer Science 8525 specification, section 3.3.
