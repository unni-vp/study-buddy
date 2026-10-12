# Computer systems

## Hardware, software and Boolean logic

- **Hardware** is the physical equipment in a computer system.
- **Software** is the programs and data that tell hardware what to do.
- Hardware needs software instructions; software needs hardware on which to run.

Boolean logic uses values that are either 0/1 or False/True.

| A | B | AND | OR | XOR |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

`NOT` reverses one input. `XOR` is true when the two inputs are **different**.

For a circuit with several gates, calculate intermediate outputs one gate at a time. AQA notation may use `.` for AND, `+` for OR, `⊕` for XOR and an overbar for NOT.

## System and application software

- **System software** manages computer resources and provides a platform for applications.
- **Application software** performs end-user tasks, such as word processing or image editing.

An **operating system** manages:

- processors and scheduling
- memory allocation
- input/output devices and drivers
- applications and files
- users, permissions and security

**Utility software** maintains, protects or configures a system. Examples include backup tools, anti-malware software, compression tools and disk-management utilities.

## High-level and low-level languages

### High-level languages

- Use human-readable statements and abstractions.
- Usually portable between processor types after suitable translation.
- Faster to write, test and maintain.
- Give less direct control over hardware.

### Low-level languages

- **Machine code** is binary executed directly by a particular processor instruction set.
- **Assembly language** uses mnemonics and has roughly a one-to-one relationship with machine-code instructions.
- Low-level programs can give close hardware control and may be efficient, but are harder to create and are processor-specific.
- Assembly is useful for embedded systems or direct hardware control.

## Translators

Code written in a high-level or assembly language must be translated before the processor can execute it.

| Translator | What it does | Typical use |
|---|---|---|
| Compiler | Translates a whole high-level program into machine code and produces executable/object code | Distributing a finished program and running it repeatedly |
| Interpreter | Reads high-level statements and calls suitable machine-code routines as the program runs; it does not directly create a machine-code program | Development, testing and interactive execution |
| Assembler | Translates assembly language, normally one instruction to one machine-code instruction | Low-level and embedded code |

A compiler can take time before the first run, but the translated program can run without translating each statement again. An interpreter can stop at the first encountered error and supports quick testing, but needs the interpreter when running.

## CPU components

The **central processing unit (CPU)** executes program instructions.

- **Arithmetic logic unit (ALU):** calculations and logical comparisons.
- **Control unit (CU):** coordinates the fetch-decode-execute cycle and sends control signals.
- **Clock:** produces timing signals that synchronise operations.
- **Registers:** tiny, very fast storage locations inside the CPU.
- **Buses:** collections of wires carrying data or signals between components.
- **Main memory:** stores active instructions and data for direct CPU access.

## Fetch-decode-execute cycle

Think of the CPU as repeatedly collecting and following instruction cards:

1. **Fetch:** get the next instruction from main memory into the CPU.
2. **Decode:** the control unit works out what the instruction means.
3. **Execute:** carry out the instruction, possibly reading or writing data.
4. Repeat continuously.

The clock keeps operations in step, while buses carry instructions, data and control signals.

## CPU performance

- Higher **clock speed** allows more clock cycles per second, but heat and architecture limit the benefit.
- More **processor cores** allow more instructions or tasks to be processed at the same time when software can use them.
- Larger **cache** keeps more frequently used instructions and data close to the CPU, reducing slower main-memory access.

Do not claim that doubling one feature always doubles performance. Workload, software, architecture and other bottlenecks matter.

## Memory types

| Type | Volatile? | Purpose |
|---|---|---|
| Register | Yes | Immediate values and instructions inside the CPU |
| Cache | Yes | Frequently used data/instructions close to the CPU |
| RAM | Yes | Active programs and data in main memory |
| ROM | No | Instructions or data that must persist, such as startup firmware |

**Volatile** memory loses its contents without power. **Non-volatile** memory keeps them.

Main memory is directly accessible by the CPU, apart from cache and registers which are treated separately here. Secondary storage is non-volatile and not directly accessed by the CPU.

## Secondary and cloud storage

Secondary storage is needed for long-term storage of programs and data.

### Magnetic storage

Stores data by magnetising areas of a surface, usually with moving parts. It often offers high capacity at low cost but is slower and more vulnerable to shock.

### Solid-state storage

Uses electronic circuits with no moving parts. It is fast, quiet, durable and energy-efficient, but often costs more per gigabyte and has limited write endurance.

### Cloud storage

Stores data on remote servers that use magnetic and/or solid-state storage.

Advantages include access from different locations, sharing, off-site backup and scalable capacity. Disadvantages include dependence on internet access and the provider, ongoing costs, privacy/security concerns and slower transfer for large files.

## Embedded systems

An **embedded system** is a computer built into a larger device to perform a dedicated or limited set of functions.

Examples include a washing-machine controller, car engine-control unit and smart thermostat. A general-purpose laptop runs many user-selected applications, while an embedded system is designed around its specific job, often with limited memory, power and processing.

## Sources

- AQA GCSE Computer Science 8525 specification, section 3.4.
