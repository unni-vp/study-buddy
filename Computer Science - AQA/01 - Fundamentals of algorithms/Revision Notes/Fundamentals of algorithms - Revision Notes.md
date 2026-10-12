# Fundamentals of algorithms

## Algorithms and problem solving

An **algorithm** is a **sequence of steps that can be followed to complete a task**. Think of it as a precise recipe: the ingredients are the inputs, the method is the processing, and the finished dish is the output.

- A **program** is an implementation of an algorithm in a programming language.
- The same algorithm can be implemented in Python, another language or hardware.
- A good algorithm is unambiguous, finishes after a finite number of steps and produces the required output for valid inputs.

### Decomposition and abstraction

- **Decomposition** breaks a large problem into smaller sub-problems with identifiable jobs.
- **Abstraction** removes detail that is not needed for the current problem.

For a school-booking system, decomposition might separate login, room search and booking. Abstraction might store whether a room is available without modelling its wall colour.

## Representing algorithms

You may be asked for **pseudocode**, **program code** or a **flowchart**. Follow the form named in the question.

### Pseudocode

Pseudocode expresses the logic without depending on one real programming language.

```text
OUTPUT "Enter a temperature"
temperature ← USERINPUT
IF temperature < 0 THEN
    OUTPUT "Freezing"
ELSE
    OUTPUT "Not freezing"
ENDIF
```

### Python

```python
temperature = float(input("Enter a temperature: "))
if temperature < 0:
    print("Freezing")
else:
    print("Not freezing")
```

### Flowcharts

| Shape | Meaning |
|---|---|
| Oval | Start or stop |
| Rectangle | Process or calculation |
| Parallelogram | Input or output |
| Diamond | Decision with labelled branches |
| Arrow | Direction of control flow |

Keep each decision as a question with clear outcomes such as **Yes/No**.

## Inputs, processing, outputs and trace tables

- **Input:** data supplied to an algorithm.
- **Processing:** calculations, comparisons or changes made to the data.
- **Output:** information produced by the algorithm.

A **trace table** records variable values as an algorithm runs. Work one instruction at a time and create a new row whenever a tracked value changes.

```text
total ← 0
FOR number ← 1 TO 3
    total ← total + number
ENDFOR
OUTPUT total
```

| number | total after addition |
|---:|---:|
| 1 | 1 |
| 2 | 3 |
| 3 | 6 |

The output is **6**. Do not guess the purpose from variable names; prove it from the instructions and trace.

## Comparing efficiency

More than one algorithm may solve the same problem. For this course, compare **time efficiency**: how the number of steps or time taken changes for the same input.

- Compare algorithms using the **same task and data**.
- An algorithm that performs fewer operations will usually finish faster.
- Formal Big O notation is not required.
- A method may be fast for one kind of data but unsuitable for another.

## Linear search

A **linear search** checks items in order until the target is found or every item has been checked.

```text
found ← False
index ← 0
WHILE index < LENGTH(items) AND found = False
    IF items[index] = target THEN
        found ← True
    ELSE
        index ← index + 1
    ENDIF
ENDWHILE
```

- Works on **sorted or unsorted** data.
- Simple and suitable for small lists.
- In the worst case, it checks every item.

## Binary search

A **binary search** repeatedly checks the middle item and discards half of the remaining search area.

1. Check the middle item.
2. If it is the target, stop.
3. If the target is smaller, continue in the lower half.
4. If the target is larger, continue in the upper half.
5. Repeat until found or no items remain.

The data **must be sorted**. Binary search is usually much faster than linear search for a large sorted list because the search area halves each step.

## Bubble sort

A **bubble sort** repeatedly compares neighbouring items and swaps them when they are in the wrong order.

Example: `5, 2, 4`

- Compare 5 and 2 → swap: `2, 5, 4`
- Compare 5 and 4 → swap: `2, 4, 5`
- A pass with no swaps proves the list is sorted.

It is simple but can require many comparisons and swaps, especially for a large or reverse-ordered list.

## Merge sort

A **merge sort** uses decomposition:

1. Repeatedly split the list into smaller lists until each contains one item.
2. Merge neighbouring lists while placing items into order.
3. Continue merging until one sorted list remains.

Merge sort is generally more time-efficient than bubble sort for large lists, but it needs extra memory to hold temporary lists.

## Search and sort comparisons

| Pair | Must-know comparison |
|---|---|
| Linear vs binary search | Linear works on unsorted data; binary needs sorted data but removes half the search area each step |
| Bubble vs merge sort | Bubble repeatedly swaps neighbours; merge sort splits then merges ordered sublists |
| Efficiency | Describe the number of checks, comparisons or swaps for the stated data |

When explaining an algorithm, state the **starting condition**, the **repeated action**, how the search area or list changes, and the **stopping condition**.

## Sources

- AQA GCSE Computer Science 8525 specification, section 3.1.
