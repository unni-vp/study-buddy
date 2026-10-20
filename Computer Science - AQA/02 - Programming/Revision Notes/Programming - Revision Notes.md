# Programming

## Data types, variables and constants

A **data type** tells the computer what kind of value is stored and which operations make sense.

| Type | Meaning | Example |
|---|---|---|
| Integer | Whole number | `27` |
| Real | Number with a fractional part | `3.75` |
| Boolean | `True` or `False` | `loggedIn = True` |
| Character | One character | `'A'` |
| String | Sequence of characters | `"Shreya"` |

| Named value | Can it change while the program runs? | Example |
|---|---|---|
| **Variable** | It is a **named storage location** whose value can change. | `score` changes as points are earned. |
| **Constant** | It is intended to stay the same. | `MAX_ATTEMPTS` stores the allowed number of guesses. |

- **Assignment** stores a value: pseudocode `score ← 0`; Python `score = 0`.
- Use meaningful identifiers such as `totalPrice`, not vague names such as `x`.

Choose types carefully. A telephone number is usually a string because it is not used in arithmetic and may begin with zero.

### Choosing and updating values

A numeric value such as `12` can be added to another number. The string `"12"` is text, so it must be converted before doing that calculation. A Boolean stores a truth value rather than the words `"True"` or `"False"`.

In Python, both single and double quotation marks can enclose a string. Python represents a single character as a string of length 1. Other languages may provide a separate character type.

```python
score = 4
score = score + 3
MAX_SCORE = 20
```

The second assignment reads the old value, adds 3 and stores **7** back in `score`. Assignment does not mean that both sides must already be equal. Capital letters are a Python convention for constants; they do not stop a programmer from reassigning the name.

Initialise a **counter** before counting events, and a **total** before adding values. Otherwise the program has no reliable starting value.

## Sequence, selection and iteration

The three basic control structures are:

| Structure | What happens | Example |
|---|---|---|
| **Sequence** | Instructions run in order. | Read a price, calculate a total, then display it. |
| **Selection** | A condition chooses which route runs. | Display a discount only if the customer qualifies. |
| **Iteration** | A block of instructions repeats. | Process every item in a shopping basket. |


### Selection

```python
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```

Selection can be **nested**: one decision sits inside another.

### Count-controlled iteration

Use a `for` loop when the number of repetitions is known.

```text
FOR count ← 1 TO 5
    OUTPUT count
ENDFOR
```

### Condition-controlled iteration

Use `WHILE` when the condition is checked before the loop. It may run zero times.

```python
password = input("Password: ")
while password != "correct":
    password = input("Try again: ")
```

Use `REPEAT ... UNTIL` or `DO ... WHILE` when the body must run at least once because the condition is checked at the end.

| Loop | When does the body run? | When is it useful? |
|---|---|---|
| **FOR** | A set number of repetitions in a count-controlled loop. | Process five scores when the number of repetitions is known. |
| **WHILE** | Condition checked **before** the body; repeats while true. It may run zero times. | Keep asking while the current input is invalid. |
| **REPEAT … UNTIL** | Condition checked **after** the body; stops when true. Runs at least once. | Ask for input, then check whether it is valid. |
| **DO … WHILE** | Condition checked **after** the body; repeats while true. Runs at least once. | Ask for input, then repeat while it is invalid. |


The last two forms check at the same point but use **opposite stopping logic**. Python does not have a built-in `REPEAT ... UNTIL` or `DO ... WHILE` statement.

### Following the chosen branch

In an `if`/`elif`/`else` chain, the first true condition selects one branch. For age 20, the `Adult` branch runs and the remaining branches are skipped. Two independent `if` statements can both run, so they do not always mean the same thing as an `if`/`elif` chain.

A nested decision is checked only if its outer branch is reached:

```python
if member:
    if age < 18:
        price = 3
    else:
        price = 5
else:
    price = 8
```

Here, the age check affects **members only**. Indentation shows which decision owns each branch.

### Counting repetitions accurately

```python
total = 0
for number in range(1, 6):
    total = total + number
print(total)
```

Python's `range(1, 6)` includes 1 but excludes 6, so the body runs **five times** and the total is **15**. The pseudocode `FOR count ← 1 TO 5` includes both endpoints. Check the convention before translating a loop.

A condition-controlled loop needs something that can change its condition. In the password example, new input can eventually make the condition false. Forgetting that update could create an **infinite loop**.

### A loop inside another loop

```python
for row in range(2):
    for column in range(3):
        print(row, column)
```

For each outer-loop value, the inner loop runs from the beginning. This prints **six pairs**, from `(0, 0)` to `(1, 2)`. It does not run only 2 + 3 times.

A post-condition loop runs its body before testing. In `REPEAT ... UNTIL valid`, the loop stops when `valid` becomes true. In `DO ... WHILE invalid`, it continues while `invalid` remains true.

## Operators and expressions

### Arithmetic

| Operation | Pseudocode | Python example |
|---|---|---|
| Addition | `+` | `a + b` |
| Subtraction | `-` | `a - b` |
| Multiplication | `*` | `a * b` |
| Real division | `/` | `11 / 2` gives `5.5` |
| Integer division | `DIV` | `11 // 2` gives `5` |
| Remainder | `MOD` | `11 % 2` gives `1` |

`MOD` is useful for divisibility and alternating patterns: `number MOD 2 = 0` means even.

### Relational and Boolean operations

Relational operators compare values: equal, not equal, `<`, `>`, `<=` and `>=`.

- `NOT` reverses a Boolean value.
- `AND` is true only when both conditions are true.
- `OR` is true when at least one condition is true.

Use brackets to make combined conditions clear.

### Reading expressions

Multiplication and division are evaluated before addition and subtraction unless brackets change the order. For example, `(4 + 2) * 3` is 18, while `4 + 2 * 3` is 10.

For positive whole numbers, `17 DIV 5` is **3**, and `17 MOD 5` is **2**. The quotient counts complete groups, while the remainder tells you what is left. A number is divisible by 5 when `number MOD 5 = 0`.

| Comparison | Python example | Result when `score` is 8 |
|---|---|---|
| Equal to | `score == 8` | `True` |
| Not equal to | `score != 8` | `False` |
| Less than | `score < 8` | `False` |
| Greater than | `score > 8` | `False` |
| Less than or equal to | `score <= 8` | `True` |
| Greater than or equal to | `score >= 8` | `True` |

Python uses `=` to assign a value and **`==` to test equality**. A comparison produces a Boolean that can control selection or iteration.

### Combining conditions

| A | B | A AND B | A OR B |
|---|---|---|---|
| False | False | False | False |
| False | True | False | True |
| True | False | False | True |
| True | True | True | True |

`NOT False` is true, and `NOT True` is false.

To accept ages from 11 to 18 inclusive, both limits must hold: **`age >= 11 and age <= 18`**. Using `or` here accepts every age: an age below 11 still satisfies `age <= 18`.

To reject an age outside that range, use **`age < 11 or age > 18`**. One broken limit is enough to make the input invalid.

## Arrays and records

A **data structure** organises related data.

| Structure | How it organises data | Suitable example |
|---|---|---|
| **One-dimensional array** | An ordered list of values of the same kind, accessed by index. | A list of 30 test scores. |
| **Two-dimensional array** | Values arranged in rows and columns, accessed using two indices. | A grid of seats. |
| **Record** | Named fields about one item; fields may have different data types. | One pupil’s name, date of birth and attendance status. |


Check whether the given language or pseudocode starts indexing at **0 or 1**.

```text
RECORD Student
    name : String
    yearGroup : Integer
    present : Boolean
ENDRECORD
```

Use an array for 30 test scores. Use a record for one pupil's name, date of birth and attendance status.

### Accessing and changing a one-dimensional array

```python
scores = [7, 9, 4]
scores[1] = 10
total = 0
for index in range(len(scores)):
    total = total + scores[index]
print(total)
```

Python lists use indices starting at 0. The assignment changes the second score, so the final list is `[7, 10, 4]` and the total is **21**. An index identifies a position; it is not the value stored at that position.

An array is taught as a collection of the same data type. A Python list is used here to implement that idea, although Python also permits mixed-type lists.

### Rows, columns and records

```python
seats = [["A", "B", "C"], ["D", "E", "F"]]
print(seats[1][2])
seats[0][1] = "Booked"
```

The first index selects the **row**, and the second selects the **column**. The output is `F`. Updating row 0, column 1 replaces `B`, leaving the other cells unchanged.

To visit every seat, use one loop for rows and a nested loop for columns. Keep both indices within their valid ranges.

A record groups fields describing **one entity**. For example, a pupil record can hold a string name, integer year group and Boolean attendance value. A program could store many pupil records in an array: the array selects the pupil, and the field name selects the fact about that pupil.

## Input and output

- Input collects data, often from the keyboard.
- Output displays information to the user.
- Convert input to the required type before calculations.

```python
age = int(input("Age: "))
print("Next year you will be", age + 1)
```

Python's `input` returns a **string**, even if the user types digits. Convert with `int` for a whole number or `float` for a real value when the task needs arithmetic. A prompt tells the user what to enter, but the program still needs to store the returned input.

`print("Next year you will be", age + 1)` outputs both a label and the calculated result. Output does not automatically save a value for later use.

## Working with strings

A string is a sequence of characters. Positions identify individual characters, while a substring contains a selected sequence of characters.

Use `text = "BIOLOGY"` in these examples:

| Operation | Python | Result and explanation |
|---|---|---|
| Find the length | `len(text)` | The result is 7, because every character counts. |
| Access a position | `text[2]` | The result is `"O"`, because indexing starts at 0. |
| Find a position | `text.find("LOG")` | The result is 3, the start index of that sequence. It returns −1 if absent. |
| Extract a substring | `text[1:4]` | The result is `"IOL"`. Indices 1, 2 and 3 are included; index 4 is excluded. |
| Concatenate strings | `"Bio" + "logy"` | The result is `"Biology"`. A space is added only if one is supplied. |

`"7" + "2"` gives `"72"`, while `int("7") + int("2")` gives **9**. Converting a string to a number changes the operation from joining text to arithmetic.

| Conversion | Python example | Result |
|---|---|---|
| String to integer | `int("42")` | The integer 42. |
| String to real | `float("3.5")` | The real value 3.5. |
| Number to string | `str(42)` | The string `"42"`. |
| Character to code | `ord("A")` | The character code 65. |
| Code to character | `chr(65)` | The character `"A"`. |

A conversion requires suitable input. The string `"four"` cannot be converted using `int`. Character codes represent characters, so the code of the digit `"7"` is not the number 7.

## Random numbers

Random-number generation can simulate dice, choose quiz questions or create unpredictable game events. You do not need to explain how pseudo-random numbers are generated.

```python
import random
die = random.randint(1, 6)
```

Check whether both endpoints are included in the language or function stated in the question.

Python's `random.randint(1, 6)` can return any integer from **1 to 6 inclusive**. It returns one value per call; it does not return the whole range.

Store the result if later decisions must use the same throw:

```python
import random
die = random.randint(1, 6)
print("You rolled", die)
if die == 6:
    print("Take another turn")
```

Generating a second number inside the condition could test a different throw from the one displayed. Repeated calls can also produce the same number by chance. Random does not mean “a new value every time”.

## Subroutines and structured programming

A **subroutine** is a named block of code called from elsewhere.

| Feature | Procedure | Function |
|---|---|---|
| Main purpose | Carries out a task without returning a useful result to the caller. | Calculates and returns a value to the calling code. |
| Example | Display a menu. | Calculate a rectangle’s area. |
| Using the result | Call it to perform the action. | Use its returned value in an expression or assignment. |


Python uses `def` for both styles of subroutine.
- A **parameter** passes data into a subroutine.
- A **return value** passes a result out.
- A **local variable** exists only while its subroutine runs and is accessible only there.

```python
def rectangle_area(width, height):
    area = width * height       # local variable
    return area
```

Advantages include reuse, less repeated code, easier testing, easier maintenance and clearer decomposition.

**Structured programming** builds a program from small modules with clear interfaces. Parameters, local variables and return values reduce unwanted dependence between modules.

### Passing values in and returning a result

```python
def rectangle_area(width, height):
    area = width * height
    return area

first_area = rectangle_area(4, 6)
print(rectangle_area(3, 5))
```

`width` and `height` are **parameters**. The first call supplies 4 and 6 as arguments, so `first_area` receives **24**. The second call supplies different values and prints **15**.

`return` sends a result back to the caller and ends that function call. Printing displays text but does not provide the same returned result. A returned value can be assigned, passed to another call or used directly in an expression.

The local `area` belongs to the function call. Code outside the function should use the returned value rather than try to read `area` directly. Local names help prevent one module accidentally changing another module's working data.

### Why structure helps

A reusable function can replace several copies of the same calculation. One correction then fixes every call, instead of leaving slightly different copies to maintain. Each module can be tested separately with known inputs and expected outputs.

Clear parameters and return values state what a module needs and provides. They also let different programmers develop separate modules, provided those interfaces agree.

## Validation and authentication

**Validation** checks that input is sensible and follows rules. It does not prove that the input is factually correct.

Common checks include:

- range check, such as 1 to 10
- length check, such as at least 8 characters
- presence check, ensuring a string is not empty

```python
age = int(input("Age 11 to 18: "))
while age < 11 or age > 18:
    age = int(input("Enter 11 to 18: "))
```

**Authentication** checks identity, for example by comparing a username and password with stored values. In exam programming tasks, plain-text values may be used; real systems should store passwords securely.

| Check | Question it answers | Example |
|---|---|---|
| **Validation** | Does the input follow the required rules? | An entered age lies between 11 and 18. It could still be an untrue age. |
| **Authentication** | Is this user’s claimed identity accepted? | The supplied username and password match an account. |

### Applying the right check

| Rule | Suitable check | Why this is useful |
|---|---|---|
| A username must be supplied. | Check `username != ""`. | A presence check rejects an empty string. |
| A code must contain exactly six characters. | Check `len(code) == 6`. | A length check rejects codes that are too short or too long. |
| A score must be from 0 to 20. | Check `0 <= score <= 20`. | A range check rejects values outside the limits. |

Validation cannot prove that a plausible value is true. An entered score of 12 passes the range check even if the student's actual score was 15.

In the age example, `int` conversion happens before the range test. That example assumes numeric input; it does not handle someone typing `hello`. A robust solution must address the invalid inputs specified in its task, rather than claiming one range check handles every possible error.

Authentication needs the supplied details to match the **same account**. If a username matches one record and a password matches another, that does not authenticate either user. Use `AND` when both matching credentials are required.

## Testing and error types

Testing checks whether an algorithm or program behaves as required.

| Test data | Meaning | For allowed range 1–10 |
|---|---|---|
| Normal | Typical valid value | 5 |
| Boundary | At and just outside limits | 0, 1, 10, 11 |
| Erroneous | Invalid type or format | `"five"` |

| Error | What goes wrong | Example |
|---|---|---|
| **Syntax error** | The code breaks the language’s grammar and may stop translation or execution. | Missing `:` after a Python `if` condition. |
| **Logic error** | The program runs but produces the wrong result. | Adding two side lengths when the task requires multiplying them for area. |


For every test, state the input, reason for choosing it, expected result and actual result. Correct errors, then retest affected and previously working paths.

### A test plan with expected results

Suppose a program must accept whole-number scores from 1 to 10 and reject other input.

| Test input | Reason for choosing it | Expected result |
|---|---|---|
| `5` | This is normal valid data. | Accept it. |
| `0` | This is just below the lower boundary. | Reject it. |
| `1` | This is the lowest permitted value. | Accept it. |
| `10` | This is the highest permitted value. | Accept it. |
| `11` | This is just above the upper boundary. | Reject it. |
| `"five"` | This is erroneous text for a whole-number field. | Reject it without continuing as if it were a valid score. |

Decide the expected result **before running the test**, then record what actually happened. If 10 is rejected, inspect comparisons such as `score < 10`, which incorrectly leave out the permitted endpoint.

A syntax error prevents the code from being understood correctly, such as a missing colon. A logic error may allow the program to run, so tests must expose the wrong behaviour. After a correction, rerun the failed test and relevant earlier tests to check that the fix has not broken working behaviour.

## Exam coding checklist

- Use the response form requested: Python, pseudocode or flowchart.
- Use meaningful identifiers and suitable data types.
- Initialise totals, counters and flags before use.
- Check loop boundaries and whether an endpoint is included.
- Indent nested selection and iteration clearly.
- Use `=` for assignment in Python and `==` for comparison.
- Test normal, boundary and erroneous inputs.

## Sources

- AQA GCSE Computer Science 8525 specification, section 3.2.

- [PMT Education: original Summary Notes](../Reference Materials/PMT - Summary Notes.pdf). Unmodified source retained with its printed attribution and licence.
- [AQA specification for first exams in 2027](../../00 - Specification/AQA-8525-specification-2027.pdf).
