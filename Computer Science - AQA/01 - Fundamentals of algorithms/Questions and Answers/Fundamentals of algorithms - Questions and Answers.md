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
