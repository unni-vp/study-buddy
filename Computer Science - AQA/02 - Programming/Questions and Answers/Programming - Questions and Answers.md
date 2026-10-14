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

**29.** Write a Python function `make_code(surname, year)` that returns the first three characters of `surname` followed by the last two digits of `year`. Return `Invalid` if the surname has fewer than three characters. Assume `year` is an integer from 2000 to 2099. Preserve the surname's capitalisation and return the result rather than printing it.

**Answer:**

```python
def make_code(surname, year):
    if len(surname) < 3:
        return "Invalid"
    year_text = str(year)
    return surname[0:3] + year_text[2:4]
```

- The **length check** rejects short or empty surnames before slicing.
- **String conversion** makes the year available for substring extraction.
- Python slices **exclude the end index**: `[0:3]` selects the first three characters.
- **Concatenation** joins the two substrings. `make_code("Thompson", 2009)` returns `Tho09`.

**30.** In this seating plan, `0` means free and `1` means booked:

```python
seats = [[0, 1, 0, 1],
         [0, 0, 1, 1],
         [1, 0, 0, 0]]
```

Write a complete Python program that counts and outputs the free seats. Use **nested iteration**, rather than a built-in counting function, and make it work for other rectangular seating plans stored in `seats`.

**Answer:**

```python
seats = [[0, 1, 0, 1],
         [0, 0, 1, 1],
         [1, 0, 0, 0]]
free_count = 0

for row in seats:
    for seat in row:
        if seat == 0:
            free_count = free_count + 1

print(free_count)
```

The **outer loop** visits each row; the **inner loop** visits each seat in that row. Initialising the counter before both loops preserves the total across all rows. The program outputs **7**, once all rows have been checked.

**31.** This function should return the mean of a non-empty list of integer scores:

```python
def mean_score(scores):
    total = 0
    for index in range(1, len(scores)):
        total = total + scores[index]
    return total // len(scores)
```

Identify and explain two logic errors. Write a corrected function and give one test input with its expected result that shows the original function is wrong. Do not use `sum()`.

**Answer:**

- **Starting at index 1 skips the first score.** Lists begin at index 0.
- `//` performs integer division, so it can discard the fractional part of the mean. Use `/`.

```python
def mean_score(scores):
    total = 0
    for index in range(len(scores)):
        total = total + scores[index]
    return total / len(scores)
```

Test with `[2, 5]`. The expected mean is **3.5**; the original function returns **2**. The corrected function includes both scores and retains the fractional result.

## 7 marks

**32.** A bookshop awards loyalty credits using the number of books a customer buys and their complete years of membership. Write a Python program that:

- inputs both values as integers
- awards **3 credits per book** if the customer has been a member for **at least 4 years**
- otherwise awards **1 credit per book** if the customer buys **at least 12 books**
- otherwise awards **0 credits**
- outputs the number of credits awarded.

Only one rate applies. Assume both inputs are non-negative integers; no validation is needed. Use meaningful names and correct indentation.

**Answer:**

```python
books_bought = int(input("Books bought: "))
membership_years = int(input("Complete years of membership: "))

if membership_years >= 4:
    credits = books_bought * 3
else:
    if books_bought >= 12:
        credits = books_bought
    else:
        credits = 0

print(credits)
```

- **Nested selection** applies the book threshold only when the membership condition is false.
- `>=` includes the boundary: exactly 4 years gets the higher rate; exactly 12 books can qualify for the lower rate.
- **Mutually exclusive branches** prevent both rates being added together.

For 12 books and 3 years, the output is **12**. For 12 books and 4 years, it is **36**.

**33.** The following list stores school club names:

```python
clubs = ["chess", "drama", "coding", "music", "tennis"]
```

Write a complete Python program that inputs a club name and searches the list. It must output `True` if the name is present and `False` otherwise. Stop searching when a match is found or all items have been checked.

Write your own **linear search**. Do not use `in`, `.index()` or another built-in search. Matching is case-sensitive; the list does not need sorting.

**Answer:**

```python
clubs = ["chess", "drama", "coding", "music", "tennis"]
club_to_find = input("Club name: ")
index = 0
found = False

while index < len(clubs) and not found:
    if clubs[index] == club_to_find:
        found = True
    index = index + 1

print(found)
```

- The **index starts at 0** and stays below the list length before an item is accessed.
- `found` starts as `False` and changes only when an item matches.
- `and not found` stops another loop iteration after a match.
- Output is **outside the loop**, so the program gives one final result, including when the name is absent.

The last club, `tennis`, must still be checked. Entering `Tennis` outputs `False` because matching is case-sensitive.

**34.** Write a Python function called `read_score` with two parameters, `minimum` and `maximum`. It must:

- input an integer score
- repeatedly request another score while it is outside the inclusive range
- return the valid score to the calling program.

Use a local variable. Assume `minimum <= maximum` and that every input can be converted to an integer. Write the function only; do not use global variables.

**Answer:**

```python
def read_score(minimum, maximum):
    score = int(input("Score: "))
    while score < minimum or score > maximum:
        score = int(input("Enter a score in range: "))
    return score
```

- **Parameters** let the same function validate different ranges.
- The invalid condition uses `OR`: an input is invalid if it is below the minimum **or** above the maximum.
- **Re-entering inside the loop** lets an invalid value be replaced.
- `return` is after the loop, so only a valid score is returned. `score` is local to the function.

For a call with limits 0 and 100, `-1` and `101` are rejected; **0 and 100 are accepted**. This range check assumes integer input; checking whether text can be converted is a separate task.

**35.** Write a Python function `count_matches(words, target)` that returns how many times `target` occurs in the list `words`. Matching is case-sensitive. Check every item yourself; do not use `.count()` or another built-in counting/searching function.

Then write calling code that sets `words` to `["red", "blue", "red", "green", "red"]`, inputs the target, calls the function and outputs the returned count. The function must use a local counter.

**Answer:**

```python
def count_matches(words, target):
    matches = 0
    for word in words:
        if word == target:
            matches = matches + 1
    return matches

words = ["red", "blue", "red", "green", "red"]
target = input("Word to count: ")
answer = count_matches(words, target)
print(answer)
```

- **Parameters** pass the list and search term into the function.
- The counter is **local** and starts at 0 for each call.
- The loop checks **all items**, even after finding a match, because duplicates count.
- The function **returns** its result; the calling code prints it.

Searching for `red` outputs **3; `yellow` outputs 0**. An empty list also produces 0.

**36.** Write a Python function `next_letters(text)` that replaces each uppercase English letter with the next letter of the alphabet. `Z` must wrap round to `A`. For example, `AZ` becomes `BA`.

Assume the string contains only `A`–`Z`, or is empty. Use `ord()` and `chr()`, build a new string and return it. The character code of `A` is 65 and that of `Z` is 90.

**Answer:**

```python
def next_letters(text):
    result = ""
    for letter in text:
        code = ord(letter)
        if code == 90:
            code = 65
        else:
            code = code + 1
        result = result + chr(code)
    return result
```

- `ord()` converts a character to its code; `chr()` converts the new code back to a character.
- **Selection handles the boundary:** `Z` becomes `A`, rather than the character after `Z` in the character set.
- The result string starts empty and **accumulates every converted character**.
- The function returns after the loop. An empty input string returns an empty string.

## 9 marks

**37.** Write a Python authentication program using the stored username `learner` and stored password `Code27`. The program must:

- let the user enter a username and password on each attempt
- grant access only when **both** match the stored values exactly
- allow **at most 3 attempts**, stopping immediately after a successful attempt
- output `Access granted` after success, or `Access denied` after three failed attempts.

Each pair of entries counts as one attempt, including empty or incorrect entries. Use meaningful names and a Boolean flag. Do not print a stored password.

**Answer:**

```python
stored_username = "learner"
stored_password = "Code27"
attempts = 0
authenticated = False

while attempts < 3 and not authenticated:
    username = input("Username: ")
    password = input("Password: ")
    attempts = attempts + 1

    if username == stored_username and password == stored_password:
        authenticated = True

if authenticated:
    print("Access granted")
else:
    print("Access denied")
```

- **The counter starts at 0** and increases once for each pair of inputs.
- `attempts < 3` prevents a fourth attempt.
- `not authenticated` prevents another attempt after success.
- `AND` joins the two credential checks: one correct entry is insufficient.
- The final selection prints **one outcome**. A correct third attempt still grants access.

Changing `AND` to `OR` in the credential comparison would incorrectly allow access with only a correct username or only a correct password.

**38.** Write a Python program that accepts exactly **five valid test scores**, each an integer from **0 to 100 inclusive**. It must:

- request a replacement whenever a score is outside the range
- exclude rejected entries from all calculations
- calculate and output the mean of the five accepted scores
- count and output how many accepted scores are **50 or more**.

Assume each entry can be converted to an integer. Do not use a built-in function to calculate the total or mean.

**Answer:**

```python
total = 0
pass_count = 0

for count in range(5):
    score = int(input("Score 0 to 100: "))
    while score < 0 or score > 100:
        score = int(input("Enter 0 to 100: "))

    total = total + score
    if score >= 50:
        pass_count = pass_count + 1

mean = total / 5
print("Mean:", mean)
print("Passes:", pass_count)
```

- The **outer count-controlled loop** accepts five valid scores.
- The **inner validation loop** handles replacements without advancing to the next accepted score.
- The **total and pass count are updated after validation**, so rejected entries cannot affect either result.
- `>= 50` includes the pass boundary.
- **Real division** calculates the mean after all five scores have been accepted.

For accepted scores `0, 100, 49, 50, 75`, the outputs are **Mean: 54.8** and **Passes: 3**.

**39.** Write a Python program for a five-question addition quiz. For each question, it must:

- generate two new random integers from **1 to 12 inclusive**
- display both numbers and ask for their sum
- output `Correct` or `Incorrect` after checking the response
- award one point for a correct answer.

After all five questions, output the score and percentage correct. Assume every answer entered can be converted to an integer. Include any required import and use a count-controlled loop.

**Answer:**

```python
import random

correct_count = 0

for question_number in range(5):
    first_number = random.randint(1, 12)
    second_number = random.randint(1, 12)
    print(first_number, "+", second_number)
    answer = int(input("Sum: "))

    if answer == first_number + second_number:
        correct_count = correct_count + 1
        print("Correct")
    else:
        print("Incorrect")

percentage = correct_count / 5 * 100
print("Score:", correct_count)
print("Percentage:", percentage)
```

- `randint(1, 12)` includes both endpoints. Both calls are inside the loop, so each question gets a new pair.
- The **score is initialised once**, before the loop, and increases only for a correct response.
- **Selection** gives the appropriate feedback for every response.
- **The percentage uses the number of questions**, not the values of the random numbers.

Three correct answers give **3 points** and **60%**. A newly generated pair may repeat an earlier pair; random generation does not guarantee unique questions.

## Past-paper sources

The questions and answers on this page are original practice. The longer tasks are checked against the current programming requirements, with these official papers used to review task structure and marking approaches.

| Official source | Useful reference |
|---|---|
| [June 2022 Python Paper 1](../../00%20-%20Past%20papers/Paper%201/AQA-85251B-QP-JUN22.PDF#page=16) and [mark scheme](../../00%20-%20Past%20papers/Paper%201/AQA-85251-MS-JUN22.PDF#page=15) | Question 8: seven-mark conditional calculation using multiple inputs and conditions |
| [June 2023 Python Paper 1](../../00%20-%20Past%20papers/Paper%201/AQA-85251B-QP-JUN23.PDF#page=21) and [mark scheme](../../00%20-%20Past%20papers/Paper%201/AQA-85251-MS-JUN23.PDF#page=15) | Question 12.2: seven-mark linear search; Questions 6, 15 and 16 also inform authentication, subroutine and random/iteration practice |
| [Current specification](../../00%20-%20Specification/AQA-8525-specification-2027.pdf#page=12) | Programming requirements for the 2027 course; response format follows each question's instruction |
| [AQA assessment resources](https://www.aqa.org.uk/subjects/computer-science/gcse/computer-science-8525/assessment-resources) | Official paper and mark-scheme directory |

The two historical papers predate the 2027 revision, so content has been checked independently against the current specification. The new 9-mark questions are additional original practice with tutor mark allocations, not quotations from those papers or a prediction of future mark totals. The source sample is too small to support claims about how frequently a particular mark value appears.

The added 6–7 mark tasks are original consolidation and application practice. Mark values are tutor allocations rather than evidence that every topic has that exact mark value in official papers. Extended explanations need connected reasoning and, where requested, a justified judgement; a list of isolated words is insufficient.
