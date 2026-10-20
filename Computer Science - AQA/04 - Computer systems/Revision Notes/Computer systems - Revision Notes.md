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

| Software | Main purpose | Examples |
|---|---|---|
| **System software** | Manages computer resources and provides a platform for applications. | Operating system, device drivers and utility programs. |
| **Application software** | Performs tasks for the end user. | Word processor or image editor. |


An **operating system** manages:

- processors and scheduling
- memory allocation
- input/output devices and drivers
- applications and files
- users, permissions and security

**Utility software** maintains, protects or configures a system. Examples include backup tools, anti-malware software, compression tools and disk-management utilities.

## High-level and low-level languages

A high-level language expresses a problem in human-readable statements. Low-level languages work much closer to a processor’s instructions.

- **Machine code** is binary that a particular processor instruction set executes directly.
- **Assembly language** uses mnemonics, with roughly one assembly instruction for one machine-code instruction.

| Feature | High-level language | Low-level language |
|---|---|---|
| Readability | Human-readable statements and abstractions. | Machine code uses binary; assembly uses mnemonics close to machine instructions. |
| Development | Usually quicker to write, test and maintain. | Usually harder to create and maintain. |
| Portability | Usually portable between processor types after suitable translation. | Processor-specific instructions limit portability. |
| Hardware control | Less direct control over hardware. | Close control can be useful in embedded systems. |
| Efficiency | Convenient abstractions may add overhead. | Can be carefully tailored for efficient hardware use, but this is not automatic. |

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

| CPU change | Why it can improve performance | What limits the benefit? |
|---|---|---|
| Higher **clock speed** | More clock cycles each second. | Heat, architecture and other bottlenecks. |
| More **cores** | More instructions or tasks can be processed at the same time. | Software must be able to use the additional cores. |
| Larger **cache** | More frequently used data and instructions can be kept close to the CPU. | The benefit depends on how much slower main-memory access is avoided. |


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

Secondary storage keeps programs and data for the long term. Both magnetic and solid-state storage are **non-volatile**.

### Magnetic and solid-state storage

| Feature | Magnetic storage | Solid-state storage |
|---|---|---|
| How data is stored | Magnetises areas of a surface. | Uses electronic circuits. |
| Moving parts | Usually has moving parts. | No moving parts; quiet in operation. |
| Performance | Often slower to access data. | Usually faster and energy-efficient. |
| Physical durability | Moving parts can make it more vulnerable to shock. | Often more durable when a device is moved or knocked. |
| Cost and limits | Often high capacity at low cost per gigabyte. | Often costs more per gigabyte and has limited write endurance. |


### Local and cloud storage

Cloud storage uses **remote servers**, which contain magnetic and/or solid-state devices. Cloud is a location and service arrangement, rather than a third physical storage technology.

| Feature | Local storage | Cloud storage |
|---|---|---|
| Location | On a device or storage system at the user’s site. | On remote servers managed through a provider. |
| Access | Local files can be used without an internet connection. | Usually depends on a network/internet connection and the provider’s service. |
| Sharing | Users must arrange access or transfer copies. | Supports access from different locations, sharing and collaboration. |
| Capacity and cost | Capacity is limited by owned equipment; expansion may need new hardware. | Capacity can scale, but subscriptions or other ongoing costs may apply. |
| Backup and control | Users organise backups and protect their equipment. | Off-site copies can help recovery, but backup arrangements and permissions still matter. |
| Limitations | Loss, damage or theft at the site can affect local copies. | Outages, privacy/security concerns and slow transfers of large files can affect use. |

## Embedded systems

An **embedded system** is a computer built into a larger device to perform a dedicated or limited set of functions.

| Feature | Embedded system | General-purpose computer |
|---|---|---|
| Purpose | Built into a larger device for a dedicated or limited set of functions. | Designed to run many user-selected applications. |
| Resources | Memory, power and processing are chosen around its specific job and may be limited. | Resources support a wider range of tasks. |
| Examples | Washing-machine controller, car engine-control unit or smart thermostat. | Laptop used for writing, programming and browsing. |


## Sources

- AQA GCSE Computer Science 8525 specification, section 3.4.
