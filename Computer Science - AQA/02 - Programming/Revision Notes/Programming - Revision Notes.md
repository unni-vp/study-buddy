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

## Input, output and strings

- Input collects data, often from the keyboard.
- Output displays information to the user.
- Convert input to the required type before calculations.

```python
age = int(input("Age: "))
print("Next year you will be", age + 1)
```

String operations you must recognise:

- **length**: number of characters
- **position**: location of a character or substring
- **substring**: selected part of a string
- **concatenation**: joining strings
- character ↔ character-code conversion
- string ↔ integer or real conversion

In Python, examples include `len(text)`, `text[1:4]`, `first + last`, `ord('A')`, `chr(65)`, `int("42")` and `str(42)`.

## Random numbers

Random-number generation can simulate dice, choose quiz questions or create unpredictable game events. You do not need to explain how pseudo-random numbers are generated.

```python
import random
die = random.randint(1, 6)
```

Check whether both endpoints are included in the language or function stated in the question.

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
