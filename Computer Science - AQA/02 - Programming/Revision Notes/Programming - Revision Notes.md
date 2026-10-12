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

- A **variable** is a named storage location whose value can change.
- A **constant** is a named value that should not change while the program runs.
- **Assignment** stores a value: pseudocode `score ← 0`; Python `score = 0`.
- Use meaningful identifiers such as `totalPrice`, not vague names such as `x`.

Choose types carefully. A telephone number is usually a string because it is not used in arithmetic and may begin with zero.

## Sequence, selection and iteration

The three basic control structures are:

- **Sequence:** instructions run in order.
- **Selection:** a condition chooses a route.
- **Iteration:** instructions repeat.

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

- A **one-dimensional array** stores an ordered list of values of the same kind.
- A **two-dimensional array** stores rows and columns, like a grid.
- An array element is accessed using an **index**. Check whether the given language or pseudocode starts indexing at 0 or 1.
- A **record** groups fields about one item, and its fields may have different data types.

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

- A **procedure** performs a task.
- A **function** returns a value to the calling code.
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

## Testing and error types

Testing checks whether an algorithm or program behaves as required.

| Test data | Meaning | For allowed range 1–10 |
|---|---|---|
| Normal | Typical valid value | 5 |
| Boundary | At and just outside limits | 0, 1, 10, 11 |
| Erroneous | Invalid type or format | `"five"` |

- A **syntax error** breaks the language's grammar and may stop translation or execution.
- A **logic error** allows the program to run but produces the wrong result.

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
