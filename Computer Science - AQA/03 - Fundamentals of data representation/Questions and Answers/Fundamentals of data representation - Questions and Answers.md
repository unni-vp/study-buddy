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
