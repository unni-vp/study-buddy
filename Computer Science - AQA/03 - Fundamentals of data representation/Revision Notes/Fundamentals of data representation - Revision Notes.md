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

A **logical left shift** moves bits left and fills empty positions with zero. Each place left multiplies an unsigned whole number by 2 if no important bit is lost.

A **logical right shift** moves bits right and fills with zero. Each place right performs integer division by 2; bits shifted out are lost.

Example: `00010110` (22) shifted left once becomes `00101100` (44).

## Character encoding

A **character set** is the collection of characters that can be represented. A character encoding assigns each character a numeric code.

- **7-bit ASCII** has 128 possible codes.
- **Unicode** represents far more alphabets, symbols and emoji.
- Unicode uses the same codes as ASCII from 0 to 127.
- Codes are grouped in sequences: if `A` is 65, then `B` is 66.

Unicode is needed because ASCII cannot represent the wide range of characters used worldwide. You do not need details of UTF-8 or UTF-16.

## Bitmap images

A **pixel** is one picture element. A bitmap stores a grid of pixels and a code for each pixel's colour.

- **Image dimensions** are width × height in pixels.
- **Colour depth** is the number of bits used for each pixel.
- More pixels can improve detail but increase file size.
- Greater colour depth allows more colours but increases file size.
- Number of possible colours = **2^colour depth**.

**Image size in bits = width × height × colour depth**

For 800 × 600 pixels at 24 bits per pixel:

800 × 600 × 24 = 11,520,000 bits = **1,440,000 bytes**.

Simple black-and-white bitmap questions may ask you to convert each 0 or 1 into a pixel, row by row.

## Digital sound

Sound waves are analogue. To store sound digitally, an analogue-to-digital converter measures the wave's amplitude at regular times.

- **Sampling rate:** samples taken each second, measured in hertz.
- **Sample resolution:** bits used for each sample.
- A higher sampling rate records changes more frequently.
- A higher resolution records amplitude more precisely.
- Both can improve accuracy but increase file size.

**Sound size in bits = sampling rate × sample resolution × duration in seconds**

44,000 Hz × 16 bits × 10 s = 7,040,000 bits = **880,000 bytes**.

## Why compression is used

**Compression** reduces the number of bits required to store or transmit data.

Benefits include less storage, faster transfer and lower bandwidth use. Compression and decompression require processing, and some methods may lose information.

## Run-length encoding

**Run-length encoding (RLE)** stores each run as a frequency/data pair. It works well when data contains long repeated sequences.

`0000011100000011` becomes:

`5 0, 3 1, 6 0, 2 1`

RLE can make varied data larger because short runs need their own frequency values. Treat each bitmap row separately when the question tells you to encode rows.

## Huffman coding

**Huffman coding** gives shorter codes to more frequent symbols and longer codes to less frequent symbols.

1. Count each symbol's frequency.
2. Repeatedly combine the two lowest-frequency nodes.
3. Label branches 0 and 1.
4. Read each symbol's code from root to leaf.

No code is the prefix of another, so the encoded stream can be decoded unambiguously.

To calculate compressed size, multiply each symbol's frequency by its code length and add the results. Compare with uncompressed ASCII at **7 bits per character** when instructed.

## Calculation checklist

- Write the formula before substituting values.
- Keep bits and bytes distinct; divide bits by 8 to get bytes.
- Use decimal prefixes of 1,000 for this course.
- Show place values or four-bit groups in base conversions.
- Include units and do not round unless instructed.

## Sources

- AQA GCSE Computer Science 8525 specification, section 3.3.
