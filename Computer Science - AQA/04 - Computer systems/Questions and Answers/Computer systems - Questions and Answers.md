# Computer systems questions & answers

## 1 mark

**1.** Define hardware.

**Answer:** The physical components of a computer system.

**2.** Which logic gate outputs 1 only when its two inputs are different?

**Answer:** XOR.

**3.** Which CPU component performs calculations and logical comparisons?

**Answer:** Arithmetic logic unit (ALU).

**4.** Which translator converts assembly language into machine code?

**Answer:** Assembler.

**5.** Name the volatile main memory used for active programs and data.

**Answer:** RAM.

**6.** What is an embedded system?

**Answer:** A computer built into a larger device to perform a dedicated or limited function.

## 2 marks

**7.** Explain the relationship between hardware and software.

**Answer:**

- Software supplies instructions and data that control operations.
- Hardware provides the physical components that execute those instructions.

**8.** Explain the difference between system software and application software.

**Answer:**

- System software manages computer resources and provides a platform.
- Application software performs tasks for the end user.

**9.** Give two functions of an operating system.

**Answer:** Any two of processor scheduling, memory management, device/I/O management, application management, file management or security.

**10.** Explain the difference between machine code and assembly language.

**Answer:**

- Machine code is binary executed directly by a particular processor.
- Assembly uses mnemonic instructions with a one-to-one correspondence to machine-code instructions.

**11.** Explain the difference between volatile and non-volatile memory.

**Answer:**

- Volatile memory loses its contents when power is removed.
- Non-volatile memory retains its contents without power.

**12.** Give one advantage and one disadvantage of cloud storage compared with local storage.

**Answer:**

- It can be accessed from different locations and can provide off-site backup.
- It depends on connectivity/provider availability or may create privacy and ongoing-cost concerns.

## 3 marks

**13.** Give the outputs of AND, OR and XOR when A = 1 and B = 1.

**Answer:**

- AND = 1.
- OR = 1.
- XOR = 0.

**14.** Describe the fetch-decode-execute cycle.

**Answer:**

- Fetch the next instruction from main memory into the CPU.
- Decode it to determine the required operation.
- Execute the instruction, including any required read or write.

**15.** Explain how cache size can affect CPU performance.

**Answer:**

- Cache stores frequently used instructions and data close to the CPU.
- A larger cache can hold more of this data.
- This can reduce slower accesses to main memory and improve performance.

**16.** Compare RAM and ROM.

**Answer:**

- RAM is volatile and stores programs/data currently in use.
- ROM is non-volatile and stores instructions or data that must persist.
- Both provide electronic storage used by the computer system.

**17.** Give three advantages of high-level languages over low-level languages.

**Answer:**

- They are easier for people to read and write.
- Programs are faster to develop, test and maintain.
- The source can usually be translated for different processor types.

**18.** Explain why an SSD is suitable for a laptop.

**Answer:**

- It has no moving parts, so it is resistant to physical shock.
- It provides fast access to programs and data.
- It is quiet and generally uses less power than magnetic storage.

## 4 marks

**19.** Compare a compiler and an interpreter.

**Answer:**

- A compiler translates the whole high-level program and produces machine/object code.
- The translated program can run later without translating every statement again.
- An interpreter processes statements while the program runs and does not directly create a machine-code program.
- Interpretation supports quick testing but requires the interpreter and may be slower during repeated execution.

**20.** Explain the roles of the ALU, control unit, clock and registers.

**Answer:**

- The ALU performs arithmetic and logical operations.
- The control unit coordinates instruction processing and sends control signals.
- The clock supplies timing signals that synchronise operations.
- Registers hold immediate instructions, data or intermediate results inside the CPU.

**21.** Compare magnetic and solid-state secondary storage.

**Answer:**

- Magnetic storage magnetises a surface and often contains moving parts.
- It normally gives high capacity at a lower cost per gigabyte.
- Solid-state storage uses electronic circuits with no moving parts, so it is faster and more resistant to shock.
- Solid state often costs more per gigabyte and has limited write endurance.

**22.** Explain how clock speed, cores and cache can affect CPU performance.

**Answer:**

- Higher clock speed allows more cycles each second.
- Multiple cores can process more tasks simultaneously when software supports parallel work.
- Larger cache reduces time spent waiting for main memory.
- Overall improvement depends on the workload, software and other system bottlenecks.

## 6 marks

**23.** A school is choosing between local and cloud storage for student work. Evaluate the options.

**Answer:**

- Local storage can work without internet access and gives the school direct control.
- It requires the school to buy, maintain and back up its own hardware.
- Cloud storage supports access from home and school, sharing and scalable capacity.
- Remote copies can protect against damage at the school site.
- Cloud access depends on reliable internet and provider availability.
- Security, privacy, subscription cost and recovery arrangements should be compared; a combined local and cloud backup strategy may reduce risk.

**24.** Explain why a washing-machine controller is an embedded system and how its hardware may differ from a laptop.

**Answer:**

- It is built into a larger product and performs a specific control task.
- It reads sensors and controls components such as valves, heater and motor.
- Its software is designed for a limited, predictable set of operations.
- It may use a low-power processor with limited RAM and storage.
- A laptop is general purpose and runs many user-selected applications.
- The embedded design can be smaller, cheaper and more reliable for its dedicated job.

**25.** A CPU executes an instruction that adds two values stored in main memory and stores the result back there. Explain the fetch–decode–execute cycle for this task, linking the control unit, ALU, registers, buses and clock to their roles. You do not need to name individual registers.

**Answer:**

- During **fetch**, the next instruction is read from main memory into the CPU. **Buses carry the addresses, data and control signals** needed for this transfer.
- A **register** holds the instruction or other immediate data while it is being processed, rather than requiring every intermediate value to remain in main memory.
- During **decode**, the **control unit interprets the instruction** and coordinates the operations it requires.
- During **execute**, the required data values are obtained and the **ALU performs the addition**.
- The result is held temporarily and **written back to main memory** as required by the instruction.
- The **clock supplies timing signals** that synchronise these operations; the CPU then continues with the next instruction.

The ALU carries out the arithmetic; it is not the component responsible for interpreting the instruction.

**26.** A laptop runs a video call, a browser and a word processor at the same time. Explain how its operating system supports these applications through processor management, memory management, input/output, application management and security. Explain why it is system software.

**Answer:**

The operating system **allocates processor time** so the applications can make progress rather than one application taking control indefinitely. It **allocates and tracks memory**, keeping each application's working data available and preventing one from simply overwriting another's memory.

It manages access to **devices through drivers**, coordinating resources such as the microphone, camera and printer. It also **loads, runs and closes applications**, providing the services they use to interact with the machine.

**Accounts and permissions** restrict access to files and resources. These functions make it **system software**: it manages the computer's resources and provides the platform on which the user applications run. The word processor itself is application software because it performs an end-user task.

**27.** Explain the appropriate translator for each situation: a developer translating assembly instructions for a particular CPU; a company distributing an executable application; and a learner repeatedly running and correcting a high-level program during development. Include how each translator works and one relevant advantage or limitation.

**Answer:**

- An **assembler** translates assembly language into machine code. Assembly instructions correspond closely to the processor's instructions, so the source is hardware-specific and must target the appropriate CPU instruction set.
- A **compiler** translates the high-level program and produces machine/object code. Once the required executable has been produced, it can run without translating the source on every run. A different target platform may need another build; finding no syntax errors does not prove the program is logically correct.
- An **interpreter** carries out high-level statements as the program runs, using routines in its own implementation. This supports rapid testing and correction without a separate full compile–run step each time, but execution needs the interpreter and may involve repeated processing overhead.

These are suitable choices for the stated situations, rather than a claim that compiled programs cannot be tested or that every language has only one possible implementation.

## 7 marks

**28.** A model cooling fan switches on when the temperature is high (`A = 1`) **or** a manual request is active (`B = 1`), but only when maintenance mode is off (`C = 0`). Write its Boolean expression using AND, OR and NOT, then using AQA's dot, plus and overbar symbols. Complete the full three-input truth table, including useful intermediate columns, and explain the effect of maintenance mode.

**Answer:**

**F = (A OR B) AND NOT C**

Using Boolean symbols: **F = (A + B) . C̅**.

| A | B | C | A OR B | NOT C | F |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 0 |
| 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 | 1 |
| 0 | 1 | 1 | 1 | 0 | 0 |
| 1 | 0 | 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 1 | 0 | 0 |
| 1 | 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 | 0 |

When **C is 1**, NOT C is 0, forcing the final AND output to 0 regardless of A and B. When C is 0, either request can switch the fan on. The parentheses ensure that the maintenance condition applies to **both** ways of requesting the fan.

## Past-paper sources

Original practice questions and tutor answers. Longer questions use tutor practice mark allocations, with independent checks against the current specification. They are not official marked questions or a prediction of future paper structure.

- [Current specification](../../00%20-%20Specification/AQA-8525-specification-2027.pdf)
- [AQA assessment resources](https://www.aqa.org.uk/subjects/computer-science/gcse/computer-science-8525/assessment-resources)
- [June 2022 Paper 2](../../00%20-%20Past%20papers/Paper%202/AQA-85252-QP-JUN22.PDF) and [mark scheme](../../00%20-%20Past%20papers/Paper%202/AQA-85252-MS-JUN22.PDF)
- [June 2023 Paper 2](../../00%20-%20Past%20papers/Paper%202/AQA-85252-QP-JUN23.PDF) and [mark scheme](../../00%20-%20Past%20papers/Paper%202/AQA-85252-MS-JUN23.PDF)

The added 6–7 mark tasks are original consolidation and application practice. Mark values are tutor allocations rather than evidence that every topic has that exact mark value in official papers. Extended explanations need connected reasoning and, where requested, a justified judgement; a list of isolated words is insufficient.
