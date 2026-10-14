# Fundamentals of algorithms questions & answers

## 1 mark

**1.** Define an algorithm.

**Answer:** A sequence of steps that can be followed to complete a task.

**2.** What is decomposition?

**Answer:** Breaking a problem into smaller sub-problems with identifiable tasks.

**3.** What is abstraction?

**Answer:** Removing unnecessary detail from a problem.

**4.** Which search algorithm requires the data to be sorted?

**Answer:** Binary search.

**5.** Name the flowchart shape used for a decision.

**Answer:** Diamond.

**6.** What proves that a bubble sort has finished?

**Answer:** A complete pass with no swaps.

## 2 marks

**7.** Explain the difference between an algorithm and a program.

**Answer:**

- An algorithm is the logical sequence of steps used to solve a problem.
- A program is an implementation of an algorithm in a programming language.

**8.** Give one advantage and one disadvantage of linear search.

**Answer:**

- It works on unsorted data and is simple to implement.
- It may need to check every item, so it can be slow on a large list.

**9.** Explain why binary search is normally faster than linear search on a large sorted list.

**Answer:**

- Binary search compares the target with the middle item.
- It discards half of the remaining search area after each comparison.

**10.** State the input and output of an algorithm that receives three test scores and calculates their mean.

**Answer:**

- Input: the three test scores.
- Output: their calculated mean.

**11.** Give two rules for drawing a clear flowchart decision.

**Answer:**

- Use a diamond for the condition.
- Label its outgoing branches clearly, for example Yes and No.

**12.** Explain one way abstraction helps when designing a route-planning algorithm.

**Answer:** It removes irrelevant details, such as building colours, so the algorithm can focus on locations, connections and journey costs.

## 3 marks

**13.** Trace this algorithm and give its output: `total ← 1`; for `n` from 1 to 3, set `total ← total × n`; output `total`.

**Answer:**

- After n = 1, total = 1.
- After n = 2, total = 2; after n = 3, total = 6.
- The output is **6**.

**14.** Describe how a linear search finds a target.

**Answer:**

- Start at the first item and compare it with the target.
- Move through the items one at a time until a match is found.
- Stop with not found if the end of the list is reached.

**15.** A sorted list is `[4, 9, 13, 18, 25, 31, 40]`. Describe the first three comparisons made by a binary search for 31.

**Answer:**

- Compare with 18, the middle item; 31 is larger, so discard the lower half.
- Compare with 31 in the upper half.
- The target is found, so no third comparison is needed.

**16.** Perform the first complete pass of bubble sort on `[7, 3, 5, 2]` in ascending order.

**Answer:**

- Swap 7 and 3 → `[3, 7, 5, 2]`.
- Swap 7 and 5 → `[3, 5, 7, 2]`.
- Swap 7 and 2 → `[3, 5, 2, 7]`.

**17.** Describe the main stages of merge sort.

**Answer:**

- Repeatedly split the list until each sublist contains one item.
- Compare items while merging neighbouring sublists into sorted order.
- Continue merging until one sorted list remains.

**18.** Explain how decomposition could be used when developing a quiz program.

**Answer:**

- Split the program into tasks such as getting a question, checking an answer and updating the score.
- Develop or test each smaller task separately.
- Combine the completed parts through clear inputs and outputs.

## 4 marks

**19.** Compare linear search and binary search.

**Answer:**

- Linear search checks items one by one and works on unsorted data.
- Binary search checks a middle item and repeatedly halves the search area.
- Binary search requires sorted data.
- Binary search is usually faster for a large sorted list; linear search may be more suitable when the list is small or unsorted.

**20.** Compare bubble sort and merge sort.

**Answer:**

- Bubble sort compares neighbouring items and swaps those in the wrong order.
- Merge sort splits the data and merges sublists in order.
- Bubble sort is simple but may make many comparisons and swaps.
- Merge sort is generally faster for large lists but requires extra temporary memory.

**21.** Write pseudocode that inputs five numbers and outputs the largest.

**Answer:**

```text
largest ← USERINPUT
FOR count ← 2 TO 5
    number ← USERINPUT
    IF number > largest THEN
        largest ← number
    ENDIF
ENDFOR
OUTPUT largest
```

**22.** Explain how a trace table helps determine the purpose of an unfamiliar algorithm.

**Answer:**

- Choose suitable input data and record the initial variable values.
- Follow one instruction at a time in the correct control-flow order.
- Record every change, including each loop iteration and decision outcome.
- Use the final values and output pattern to state what the algorithm does.

## 6 marks

**23.** A school must repeatedly search a large list of sorted student IDs. Evaluate whether it should use linear search or binary search.

**Answer:**

- Binary search is suitable because the IDs are already sorted.
- It checks the middle ID and removes half of the remaining list after each comparison.
- This usually needs far fewer comparisons than linear search on a large list.
- Linear search could find an item near the start quickly, but its worst case checks every ID.
- Keeping the list sorted may require work when IDs are added, but the list is searched repeatedly, so that cost is outweighed by faster searches.
- Therefore binary search is the better choice for this situation.

**24.** Describe a systematic method for creating and checking an algorithm for a ticket-price calculator.

**Answer:**

- Decompose the problem into input, validation, price selection, discount calculation and output.
- Abstract away details that do not affect price.
- Define required inputs and expected outputs, then write pseudocode or the requested representation.
- Use sequence, selection and any required iteration with meaningful identifiers.
- Trace the algorithm using normal, boundary and invalid values.
- Correct any logic errors and confirm every route produces the required price or error message.

**25.** Trace this algorithm for inputs `4, 0, -2, 6, -1`, in that order. Record the total and count after each value is processed, state the final outputs and explain the role of `-1`.

```text
total ← 0
count ← 0
number ← USERINPUT
WHILE number ≠ -1
    IF number > 0 THEN
        total ← total + number
        count ← count + 1
    ENDIF
    number ← USERINPUT
ENDWHILE
OUTPUT total
OUTPUT count
```

**Answer:**

| Input | Total | Count | Action |
|---|---|---|---|
| 4 | 4 | 1 | Add and count the positive value |
| 0 | 4 | 1 | Ignore |
| -2 | 4 | 1 | Ignore |
| 6 | 10 | 2 | Add and count the positive value |
| -1 | 10 | 2 | Stop before the loop body |

The final outputs are **10** and **2**. The value **-1 is a sentinel**: it signals the end of input and is not included in the calculations. The algorithm totals and counts **positive** inputs, rather than all values before the sentinel.

**26.** Apply ascending bubble sort to `[5, 1, 4, 2]`. On each pass, compare adjacent items from left to right, stopping one position earlier on the next pass because the largest remaining item has reached its final position. Stop early if a pass makes no swaps.

Show the list after every complete pass. Explain the swaps in the first pass and why the algorithm stops.

**Answer:**

- Compare **5 and 1**, then swap: `[1, 5, 4, 2]`.
- Compare **5 and 4**, then swap: `[1, 4, 5, 2]`.
- Compare **5 and 2**, then swap: `[1, 4, 2, 5]`.

| Complete pass | List | Swaps |
|---|---|---|
| 1 | `[1, 4, 2, 5]` | 3 |
| 2 | `[1, 2, 4, 5]` | 1 |
| 3 | `[1, 2, 4, 5]` | 0 |

Each pass moves the **largest remaining item to the end of the unsorted part**. A pass with no swaps shows that the remaining adjacent pairs are already in order, so no further pass is needed.

**27.** Show how merge sort puts `[8, 3, 7, 1]` into ascending order. Show the splitting and merging stages, and explain the comparisons in the final merge.

**Answer:**

| Stage | Sublists |
|---|---|
| Split once | `[8, 3]` and `[7, 1]` |
| Split into single items | `[8]`, `[3]`, `[7]`, `[1]` |
| Merge neighbouring single items | `[3, 8]` and `[1, 7]` |
| Final merge | `[1, 3, 7, 8]` |

During the final merge, compare the first unused item in each sorted sublist:

- **3 versus 1:** take 1.
- **3 versus 7:** take 3.
- **8 versus 7:** take 7.
- The second sublist is now empty, so copy the remaining **8**.

The merge works because **each input sublist is already sorted**. It does not simply join the two sublists without checking their order.

## 7 marks

**28.** Design a pseudocode algorithm that inputs integers until `0` is entered. Zero is the stopping signal and must not be counted. Negative integers are valid data.

Output the number of data values and the largest one. If the first input is 0, output `No data` instead. Do not assume the largest value is positive.

**Answer:**

```text
count ← 0
number ← USERINPUT
WHILE number ≠ 0
    IF count = 0 THEN
        largest ← number
    ELSE
        IF number > largest THEN
            largest ← number
        ENDIF
    ENDIF
    count ← count + 1
    number ← USERINPUT
ENDWHILE
IF count = 0 THEN
    OUTPUT "No data"
ELSE
    OUTPUT count
    OUTPUT largest
ENDIF
```

**Initialising from the first data value** handles a sequence containing only negatives. The sentinel is tested before counting or comparing. The final selection avoids using an undefined largest value when there were no data values.

For inputs `-8, -3, 0`, the outputs are **2** and **-3**. For input `0`, the only output is **No data**.

**29.** The list `values` is already sorted in ascending order and `target` is already stored. Write Python that performs a **binary search** and outputs `True` if the target exists, or `False` if it does not. Do not use a built-in searching function. Your solution must also work for an empty list.

**Answer:**

```python
low = 0
high = len(values) - 1
found = False

while low <= high and not found:
    middle = (low + high) // 2
    if values[middle] == target:
        found = True
    elif target < values[middle]:
        high = middle - 1
    else:
        low = middle + 1

print(found)
```

- **Integer division** selects a valid middle index.
- The comparison discards the half that cannot contain the target, **excluding the middle item already checked**.
- `low <= high` allows the final remaining item to be checked and stops when the search area is empty.
- An empty list starts with `high = -1`, so the loop never accesses an item and outputs `False`.

For `[4, 9, 13, 18, 25, 31, 40]` and target `31`, the comparisons are **18, then 31**. For target `26`, they are **18, 31, 25**, then the search area becomes empty.

## Past-paper sources

Original practice questions and tutor answers. Longer questions use tutor practice mark allocations, with independent checks against the current specification. They are not official marked questions or a prediction of future paper structure.

- [Current specification](../../00%20-%20Specification/AQA-8525-specification-2027.pdf)
- [AQA assessment resources](https://www.aqa.org.uk/subjects/computer-science/gcse/computer-science-8525/assessment-resources)
- [June 2022 Paper 1](../../00%20-%20Past%20papers/Paper%201/AQA-85251B-QP-JUN22.PDF) and [mark scheme](../../00%20-%20Past%20papers/Paper%201/AQA-85251-MS-JUN22.PDF)
- [June 2023 Paper 1](../../00%20-%20Past%20papers/Paper%201/AQA-85251B-QP-JUN23.PDF) and [mark scheme](../../00%20-%20Past%20papers/Paper%201/AQA-85251-MS-JUN23.PDF)

The added 6–7 mark tasks are original consolidation and application practice. Mark values are tutor allocations rather than evidence that every topic has that exact mark value in official papers. Extended explanations need connected reasoning and, where requested, a justified judgement; a list of isolated words is insufficient.
