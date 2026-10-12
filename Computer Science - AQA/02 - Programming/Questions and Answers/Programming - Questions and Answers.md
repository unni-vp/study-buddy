# Programming questions & answers

## 1 mark

**1.** Name the data type used for `True` or `False`.

**Answer:** Boolean.

**2.** Which arithmetic operation gives the remainder after division?

**Answer:** MOD.

**3.** What is a parameter?

**Answer:** Data passed into a subroutine when it is called.

**4.** Name the error type in a program that runs but gives the wrong result.

**Answer:** Logic error.

**5.** Which data structure stores named fields that may have different data types?

**Answer:** Record.

**6.** What does concatenation do?

**Answer:** Joins strings together.

## 2 marks

**7.** Explain the difference between a variable and a constant.

**Answer:**

- A variable's stored value can change while the program runs.
- A constant is a named value intended to remain unchanged.

**8.** Explain the difference between integer division and real division for 11 divided by 2.

**Answer:**

- Integer division produces the quotient **5**.
- Real division produces **5.5**.

**9.** Explain the difference between a `WHILE` loop and a `REPEAT ... UNTIL` loop.

**Answer:**

- `WHILE` tests its condition before the body, so the body may run zero times.
- `REPEAT ... UNTIL` tests after the body, so the body runs at least once.

**10.** Give two advantages of meaningful identifier names.

**Answer:**

- They make the purpose of stored values or subroutines clear.
- They make code easier to read, debug and maintain.

**11.** Explain the difference between validation and authentication.

**Answer:**

- Validation checks whether input follows stated rules.
- Authentication checks whether a user is who they claim to be.

**12.** State two features of local variables.

**Answer:**

- They normally exist only while their subroutine is executing.
- They are accessible only inside that subroutine.

**13.** Give one suitable use for a one-dimensional array and one for a two-dimensional array.

**Answer:**

- A one-dimensional array could store a list of test scores.
- A two-dimensional array could store seats in rows and columns.

**14.** Explain why a telephone number should normally be stored as a string.

**Answer:** It is not used in arithmetic and may contain a leading zero that an integer would remove.

## 3 marks

**15.** State the result of `17 DIV 5`, `17 MOD 5` and `17 / 5`.

**Answer:**

- `17 DIV 5 = 3`.
- `17 MOD 5 = 2`.
- `17 / 5 = 3.4`.

**16.** Write a Python condition that is true when `age` is from 11 to 18 inclusive.

**Answer:**

```python
age >= 11 and age <= 18
```

Both boundary values are included.

**17.** Describe three advantages of using subroutines.

**Answer:**

- A subroutine can be reused instead of duplicating code.
- It can be tested separately.
- It makes a large program easier to understand and maintain.

**18.** Select normal, boundary and erroneous test data for an integer input allowed from 1 to 10.

**Answer:**

- Normal: 5.
- Boundary: 0, 1, 10 and 11.
- Erroneous: a non-integer such as `"hello"`.

**19.** Explain how parameters, local variables and return values create a clear subroutine interface.

**Answer:**

- Parameters specify the data entering the subroutine.
- Local variables keep temporary data inside it.
- A return value provides its result to the calling routine.

**20.** Write Python that inputs a name, removes no characters, and outputs `Hello ` followed by the name.

**Answer:**

```python
name = input("Enter your name: ")
message = "Hello " + name
print(message)
```

**21.** Explain the result of `NOT (score >= 50 AND submitted)` when `score` is 70 and `submitted` is `False`.

**Answer:**

- `score >= 50` is True, while `submitted` is False.
- `True AND False` is False.
- `NOT False` is **True**.

## 4 marks

**22.** Write Python that inputs five integers and outputs their total.

**Answer:**

```python
total = 0
for count in range(5):
    number = int(input("Number: "))
    total = total + number
print(total)
```

**23.** Write pseudocode that repeatedly inputs a mark until it is from 0 to 100 inclusive.

**Answer:**

```text
mark ← USERINPUT
WHILE mark < 0 OR mark > 100
    OUTPUT "Enter 0 to 100"
    mark ← USERINPUT
ENDWHILE
```

**24.** Write a function that accepts width and height and returns the area of a rectangle.

**Answer:**

```python
def rectangle_area(width, height):
    area = width * height
    return area
```

The two values enter as parameters and the calculated value is returned.

**25.** Explain how you would test a password routine requiring at least eight characters and a non-empty username.

**Answer:**

- Use a normal valid username and a password longer than eight characters.
- Test passwords of exactly 8 and 7 characters as boundary values.
- Test an empty username and an empty password.
- Record expected and actual acceptance or rejection for each test.

**26.** A program contains `if score = 10 print("Win")`. Identify likely errors and give a corrected Python version.

**Answer:**

- Python comparison uses `==`, not assignment `=`.
- The condition needs a colon.
- The output statement must be indented.

```python
if score == 10:
    print("Win")
```

## 6 marks

**27.** Design an algorithm that inputs ten temperatures, then outputs the mean and the highest temperature.

**Answer:**

```text
total ← 0
highest ← USERINPUT
total ← highest
FOR count ← 2 TO 10
    temperature ← USERINPUT
    total ← total + temperature
    IF temperature > highest THEN
        highest ← temperature
    ENDIF
ENDFOR
mean ← total / 10
OUTPUT mean
OUTPUT highest
```

The first input safely initialises `highest`; every value contributes to the total and is compared with the current highest.

**28.** Explain how structured programming improves the development of a large program.

**Answer:**

- Decomposition separates the problem into modules with identifiable tasks.
- Subroutines avoid repeated code and can be reused.
- Meaningful names and clear sequence, selection and iteration improve readability.
- Parameters show required inputs; return values show outputs.
- Local variables reduce accidental changes to other parts of the program.
- Modules can be developed, tested and corrected separately before integration.
