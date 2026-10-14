# Fundamentals of data representation questions & answers

## 1 mark

**1.** How many bits are in one byte?

**Answer:** 8.

**2.** What decimal value is represented by hexadecimal A?

**Answer:** 10.

**3.** What does pixel stand for?

**Answer:** Picture element.

**4.** State the unit normally used for sampling rate.

**Answer:** Hertz (Hz).

**5.** Name the compression method that stores frequency/data pairs.

**Answer:** Run-length encoding.

**6.** How many different values can four bits represent?

**Answer:** 16.

## 2 marks

**7.** Give two reasons hexadecimal is used in computer science.

**Answer:**

- It represents long binary patterns more compactly.
- It is easier for people to read and copy while converting directly to four-bit groups.

**8.** Convert binary `10110110` to decimal.

**Answer:** 128 + 32 + 16 + 4 + 2 = **182**.

**9.** Convert hexadecimal `7B` to decimal.

**Answer:** (7 × 16) + 11 = **123**.

**10.** Explain the difference between sampling rate and sample resolution.

**Answer:**

- Sampling rate is the number of amplitude measurements taken per second.
- Sample resolution is the number of bits used to store each measurement.

**11.** Give two advantages of Unicode over 7-bit ASCII.

**Answer:**

- Unicode can represent far more characters, alphabets and symbols.
- It keeps the same codes as ASCII for values 0–127, supporting compatibility.

**12.** Explain how a one-place logical left shift affects an unsigned whole number.

**Answer:** The bits move left and a zero enters on the right, multiplying the value by 2 if no significant bit is lost.

## 3 marks

**13.** Convert decimal 45 into 8-bit binary.

**Answer:**

- 45 = 32 + 8 + 4 + 1.
- Set those place values to 1.
- The result is **00101101**.

**14.** Convert binary `11010110` into hexadecimal.

**Answer:**

- Split into `1101` and `0110`.
- `1101` is D and `0110` is 6.
- The answer is **D6**.

**15.** Add binary `00110101` and `00011110`.

**Answer:**

```text
  00110101
+ 00011110
= 01010011
```

The result is **01010011**.

**16.** Calculate the uncompressed size in bits of a 320 × 200 bitmap with a colour depth of 8 bits.

**Answer:**

- Size = width × height × colour depth.
- 320 × 200 × 8.
- **512,000 bits**.

**17.** Calculate the size in bytes of 5 seconds of sound sampled at 8,000 Hz with 16-bit resolution.

**Answer:**

- Bits = 8,000 × 16 × 5 = 640,000 bits.
- Bytes = 640,000 ÷ 8.
- **80,000 bytes**.

**18.** Encode `0000011100000011` using RLE frequency/data pairs.

**Answer:** **5 0, 3 1, 6 0, 2 1**.

## 4 marks

**19.** Explain how increasing bitmap dimensions and colour depth affects the image and file size.

**Answer:**

- More pixels can show finer spatial detail.
- More pixels increase width × height, so more pixel codes are stored.
- Greater colour depth allows more possible colours for each pixel.
- Both changes increase the number of bits and therefore the file size.

**20.** Explain how an analogue sound wave is represented digitally.

**Answer:**

- The wave's amplitude is measured at regular time intervals.
- Each measurement is a sample.
- The sample is rounded to one of the available levels.
- Each level is stored as a binary value using the chosen sample resolution.

**21.** Explain how Huffman coding compresses data.

**Answer:**

- Count how frequently each symbol occurs.
- Build a tree by repeatedly combining the two least frequent nodes.
- Assign 0 and 1 to branches and read each root-to-leaf path as a code.
- Frequent symbols receive shorter codes, reducing the total number of bits.

**22.** A text contains 40 characters. Calculate its uncompressed 7-bit ASCII size and explain how to find the number of bits saved by a 190-bit Huffman encoding.

**Answer:**

- ASCII size = 40 × 7 = **280 bits**.
- Huffman size is 190 bits.
- Bits saved = 280 − 190.
- The encoding saves **90 bits**.

## 6 marks

**23.** Compare RLE and Huffman coding for compressing a simple image with large areas of one colour.

**Answer:**

- RLE replaces repeated runs with frequency/data pairs.
- Large same-colour areas create long runs, so RLE may be very effective.
- Short or frequently changing runs may add overhead and make RLE ineffective.
- Huffman coding assigns short codes to frequent colour values and longer codes to rare values.
- Huffman can still save space when repeated colours are not next to one another.
- The better method depends on both run lengths and colour frequencies; sample calculations should compare their encoded sizes.

**24.** A student wants better-quality digital audio but a small file. Explain the trade-offs involved.

**Answer:**

- Increasing sampling rate measures the wave more often and can reproduce changes more accurately.
- Increasing sample resolution records amplitude more precisely and reduces quantisation error.
- Both increase file size because more samples or more bits per sample are stored.
- Compression can reduce storage and transmission time.
- Lossless compression retains all represented data but may save less space.
- The student must balance required quality, duration, storage and transfer limits.

**25.** Convert binary `11001010` to decimal and hexadecimal. Add binary `00010101` to it, showing the binary result. Then apply a logical right shift of two places to the sum. State the shifted result in binary and decimal, and explain any lost information.

**Answer:**

- Decimal: **128 + 64 + 8 + 2 = 202**.
- Hexadecimal: `1100 1010` gives **CA**.

```text
  11001010
+ 00010101
= 11011111
```

The sum is **223**. Shifting right twice gives **00110111**, which is **55** in decimal. Zeros enter on the left; the two rightmost bits, **11**, are discarded. This is the integer quotient of 223 ÷ 4, so the remainder is lost rather than retained as a fractional value.

**26.** A bitmap is 320 pixels wide and 200 pixels high, with an 8-bit colour depth. Calculate its size in bits and bytes. The designer keeps the same dimensions but changes to 16 bits per pixel. Calculate the new byte size and explain the effect on the image. Which version meets a limit of 100,000 bytes? Ignore headers and metadata.

**Answer:**

- Original size: **320 × 200 × 8 = 512,000 bits**.
- In bytes: **512,000 ÷ 8 = 64,000 bytes**.
- New size: **320 × 200 × 16 ÷ 8 = 128,000 bytes**.
- Doubling the colour depth **doubles the pixel-data size**.
- More bits per pixel permit **more colour values**. The pixel dimensions are unchanged, so the image does not gain more spatial detail.
- Only the **8-bit version** meets the 100,000-byte limit.

**27.** A ten-second mono recording uses a sampling rate of 12,000 Hz and 12 bits per sample. Calculate its uncompressed size in bits and kilobytes, using 1 kB = 1,000 bytes. Compare changing only the rate to 24,000 Hz with changing only the resolution to 24 bits. Explain why the two changes improve different aspects of the representation. Ignore headers and compression.

**Answer:**

- Original size: **12,000 × 12 × 10 = 1,440,000 bits**.
- Bytes: **1,440,000 ÷ 8 = 180,000 bytes = 180 kB**.
- Doubling just the rate gives **360 kB**; doubling just the resolution also gives **360 kB**.
- A higher **sampling rate** takes measurements more frequently, representing changes over time more closely.
- A higher **sample resolution** provides more possible amplitude levels, reducing rounding of each measurement.
- Equal file sizes do **not** mean identical sound representation: one option increases the number of samples; the other increases the precision of each sample.

## 7 marks

**28.** A Huffman code uses `A = 0`, `B = 10`, `C = 110`, `D = 111`. Encode `AAAABBCD`. Calculate the encoded size, its size using 7-bit ASCII and the number of bits saved. Decode `010110111`. Explain why the variable-length codes can be decoded unambiguously. Ignore the storage needed for the code table.

**Answer:**

- Encoding: `0 0 0 0 10 10 110 111`, or **00001010110111**.
- Encoded size: **4 × 1 + 2 × 2 + 1 × 3 + 1 × 3 = 14 bits**.
- ASCII size: **8 × 7 = 56 bits**.
- Saving: **56 − 14 = 42 bits**.
- Decoding `0 10 110 111` gives **ABCD**.
- The code is **prefix-free**: no complete character code is the beginning of another character code, so each character boundary can be recognised.
- The frequent A has the shortest code. In an actual file, the **code table or tree also needs storage**, so its overhead must be considered when comparing complete files.

**29.** A monochrome image row is `0000000011110000`. Encode it as RLE frequency/value pairs. Each frequency is stored in 4 bits and each value in 1 bit. Calculate the encoded size and the saving compared with the raw row. Then calculate the encoded size of the alternating row `0101010101010101`. Explain why RLE helps one row more than the other and whether decoding loses pixel data. Ignore other overheads.

**Answer:**

- The first row gives **(8, 0), (4, 1), (4, 0)**.
- Each pair needs **4 + 1 = 5 bits**; three pairs need **15 bits**.
- Raw data needs **16 bits**, so the saving is **1 bit**.
- The alternating row contains **16 runs of length 1**, requiring **16 × 5 = 80 bits**.
- Its encoded form is therefore **64 bits larger** than its 16-bit raw form.
- RLE replaces each run with a pair, so **long runs reduce repetition** while short runs add too much counting overhead.
- It is **lossless**: the original row is recovered exactly by repeating each value the stated number of times.

## Past-paper sources

Original practice questions and tutor answers. Longer questions use tutor practice mark allocations, with independent checks against the current specification. They are not official marked questions or a prediction of future paper structure.

- [Current specification](../../00%20-%20Specification/AQA-8525-specification-2027.pdf)
- [AQA assessment resources](https://www.aqa.org.uk/subjects/computer-science/gcse/computer-science-8525/assessment-resources)
- [June 2022 Paper 2](../../00%20-%20Past%20papers/Paper%202/AQA-85252-QP-JUN22.PDF) and [mark scheme](../../00%20-%20Past%20papers/Paper%202/AQA-85252-MS-JUN22.PDF)
- [June 2023 Paper 2](../../00%20-%20Past%20papers/Paper%202/AQA-85252-QP-JUN23.PDF) and [mark scheme](../../00%20-%20Past%20papers/Paper%202/AQA-85252-MS-JUN23.PDF)

The added 6–7 mark tasks are original consolidation and application practice. Mark values are tutor allocations rather than evidence that every topic has that exact mark value in official papers. Extended explanations need connected reasoning and, where requested, a justified judgement; a list of isolated words is insufficient.
