# Relational databases and SQL

## Tables, records and fields

A **database** is an organised collection of data that can be stored, searched and updated. A **relational database** stores data in tables that can be linked through shared key values.

Think of a school library. One list describes pupils; another records their loans. A pupil's ID connects the person to the books they borrowed, without copying their full details onto every loan.

| Term | Plain meaning | Library example |
|---|---|---|
| **Table** | A collection of records about one kind of item | Pupils |
| **Record** | One row describing one item | The row for pupil 101 |
| **Field** | One named piece of information; a column | Name |
| **Data type** | The kind of value a field stores | Integer for YearGroup; text for Name |

Each record has values for the table's fields. A table with three pupils has **three records**, regardless of how many fields describe each pupil.

Choose data types that suit the information. A number used for counting may be an integer; a phone number is often text because leading zeroes matter and arithmetic is not needed.

### Counting what a table contains

In a pupil table, one record describes one pupil, while each field describes a property such as Name or YearGroup. Adding a new pupil adds a **row**. Adding a new property for all pupils adds a **column**.

A table's design defines the fields and their data types. A query result is a selected view of that data, so it can contain fewer rows or columns than the original table without removing the stored data.

## Primary and foreign keys

| Feature | Primary key | Foreign key |
|---|---|---|
| Purpose | **Uniquely identifies** a record within its own table. | **Links** a record to a primary-key value in another table. |
| Repeated values | Must not be repeated or missing in that table. | May repeat because several records can link to the same record elsewhere. |
| Library example | `Pupils.PupilID` identifies each pupil. | `Loans.PupilID` identifies which pupil made each loan. |


`LoanID` is also a primary key: it distinguishes separate loans, even if the same pupil borrows the same title again. A person’s name is usually a poor primary key because names can repeat or change.

![Pupils 101, 102 and 103 are identified by unique primary keys. Loans 501 and 502 both contain foreign-key PupilID 101, linking to Shreya. Loan 503 contains PupilID 102, linking to Amir. Pupil 103 has no loan in this example.](../Diagrams/linked-library-records.svg)

**Primary key:** identifies the row in this table. **Foreign key:** connects a row to another table. A field called `PupilID` can therefore be a primary key in Pupils and a foreign key in Loans.

A **composite primary key** uses a combination of fields when one field alone does not uniquely identify a record. For example, neither ClubID nor PupilID alone identifies a membership, but their combination can identify a pupil's membership of a particular club. An alternative design could give each membership its own unique MembershipID.

A foreign key can repeat: several loans may belong to pupil 101. What must be unique is the **primary key in the table it identifies**, not every field that happens to contain an ID.

## Reducing redundancy and inconsistency

**Data redundancy** means unnecessary duplication. **Data inconsistency** means different stored copies disagree.

Suppose every loan record stores the pupil's name and year group. When their year group changes, several rows need updating. Missing one leaves conflicting information.

With separate linked tables:

1. Store the pupil's name and year group **once in Pupils**.
2. Store their `PupilID` on each relevant loan.
3. Update the pupil's details in one record.
4. Retrieve those details when a query connects the tables.

This reduces repeated descriptive data and the risk of conflicting copies. Repeated **foreign-key values are intentional**: they provide the links. They are different from unnecessarily duplicating all of the pupil's details.

Good design supports consistency, but records must still be entered and updated correctly.

## Our example database

### Pupils

| PupilID | Name | YearGroup |
|---|---|---|
| 101 | Shreya | 10 |
| 102 | Amir | 11 |
| 103 | Mia | 10 |

`PupilID` is the primary key. The ID and year-group fields hold integers; Name holds text.

### Loans

| LoanID | PupilID | BookTitle | DaysLoaned |
|---|---|---|---|
| 501 | 101 | Macbeth | 14 |
| 502 | 101 | Geography | 21 |
| 503 | 102 | Atlas | 7 |

`LoanID` is the primary key. `PupilID` is a foreign key referencing Pupils. The query examples each start from these original tables.

## SELECT and FROM

**SQL** stands for **Structured Query Language**. It lets you retrieve and change database data.

| Clause | What it controls | Example |
|---|---|---|
| **SELECT** | Which fields/columns appear in the results. | `SELECT Name, YearGroup` |
| **FROM** | Which table or tables supply the data. | `FROM Pupils` |
| **WHERE** | Which records/rows meet the condition. | `WHERE YearGroup = 10` |
| **ORDER BY** | The order of the retrieved results. | `ORDER BY Name ASC` |


`SELECT *` means all fields. These clauses retrieve data; they do not change the stored records.

```sql
SELECT Name, YearGroup
FROM Pupils;
```

This retrieves each pupil's name and year group. It does not display PupilID because that field was not selected.

```sql
SELECT *
FROM Pupils;
```

This retrieves all three fields. Neither query changes the stored records.

**Keep the distinction clear:** SELECT chooses columns; a WHERE condition chooses which rows qualify.

SQL keywords such as `SELECT` are normally case-insensitive. Writing them in capitals makes the structure easier to see. Text-value matching can depend on the database's settings, so copy the spelling and capitalisation supplied by the task.

The asterisk in `SELECT *` means **all columns**. It does not mean “all matching words” or require a WHERE clause. With no WHERE condition, SELECT retrieves all rows from the named table.

## WHERE and combined conditions

**WHERE** filters records using a condition.

```sql
SELECT Name
FROM Pupils
WHERE YearGroup = 10;
```

**Result:** Shreya and Mia. Amir is excluded because his year group is 11.

### Comparisons and text values

- `=` means equal; `<>` means not equal.
- `<`, `>`, `<=` and `>=` compare values.
- Put text values in single quotes, such as `'Macbeth'`.
- Write numeric values without quotes, such as `10`.
- Use the table and field names from the question exactly.

SQL equality uses **`=`**, not Python's `==` or pseudocode's assignment arrow.

### AND and OR

```sql
SELECT Name
FROM Pupils
WHERE YearGroup >= 10 AND YearGroup <= 11;
```

**AND** requires both conditions to be true. All three pupils qualify because their year groups are within the inclusive range.

```sql
SELECT BookTitle
FROM Loans
WHERE DaysLoaned < 10 OR DaysLoaned > 20;
```

**OR** requires at least one condition to be true. Atlas qualifies through 7 days; Geography qualifies through 21 days. Macbeth, at 14 days, meets neither condition.

| Operator | When does a record qualify? | If only one condition is true |
|---|---|---|
| **AND** | Both conditions must be true. | The record is excluded. |
| **OR** | At least one condition must be true. | The record qualifies. |


Use brackets when combining AND and OR to make the intended grouping clear. Without ORDER BY, do not assume a particular result order.

## ORDER BY

**ORDER BY** sorts the retrieved results.

- **ASC:** ascending, such as A to Z or smallest to largest.
- **DESC:** descending, such as Z to A or largest to smallest.

```sql
SELECT Name
FROM Pupils
ORDER BY Name ASC;
```

**Result order:** Amir, Mia, Shreya.

```sql
SELECT BookTitle, DaysLoaned
FROM Loans
ORDER BY DaysLoaned DESC;
```

**Result order:** Geography — 21; Macbeth — 14; Atlas — 7.

Sorting changes the order of the query's results. It does not rewrite the original table's data. Put ORDER BY after WHERE when both are used.

### Filtering before displaying an ordered result

```sql
SELECT BookTitle, DaysLoaned
FROM Loans
WHERE DaysLoaned >= 14
ORDER BY DaysLoaned ASC;
```

| BookTitle | DaysLoaned |
|---|---|
| Macbeth | 14 |
| Geography | 21 |

The condition excludes Atlas because 7 is below 14. The remaining results are then shown from the smaller DaysLoaned value to the larger one. A field can be used for filtering or sorting even when it is not selected for display.

## Retrieving from two tables

To display pupils' names beside their book titles, retrieve fields from both tables and match the relevant key values.

```sql
SELECT Pupils.Name, Loans.BookTitle
FROM Pupils, Loans
WHERE Pupils.PupilID = Loans.PupilID
    AND Pupils.YearGroup = 10
ORDER BY Loans.BookTitle ASC;
```

Follow the query in three steps:

1. **Match the pupil IDs.** Loans 501 and 502 belong to pupil 101; loan 503 belongs to pupil 102.
2. **Keep year group 10.** Shreya's two loans remain. Amir is excluded; Mia has no matching loan.
3. **Display and sort.** Show the pupil's name and each matching title, sorted by title.

| Name | BookTitle |
|---|---|
| Shreya | Geography |
| Shreya | Macbeth |

The dot in `Pupils.Name` identifies **the table and its field**. This is especially useful when both tables contain a field named PupilID.

**Include the linking condition.** Otherwise a query using two tables may combine unrelated rows, pairing a pupil with somebody else's loan.

### Why the linking condition matters

The example has three pupil records and three loan records. Without a linking condition, combining both tables can produce **nine pairings**, including wrong combinations such as Mia with Amir's loan.

The condition **`Pupils.PupilID = Loans.PupilID`** keeps only pairs belonging to the same pupil. It is needed whenever these two tables are combined, even if every displayed field comes from just one of them.

A name from the pupil table can appear on several output rows because one pupil can have several loans. This repetition in query results does not mean the pupil's full details were unnecessarily copied into every stored loan record.

### Selecting data using a condition in the other table

```sql
SELECT Pupils.Name
FROM Pupils, Loans
WHERE Pupils.PupilID = Loans.PupilID
    AND Loans.DaysLoaned > 20;
```

The output is **Shreya**. The query needs Loans to test the borrowing duration, even though only a field from Pupils is displayed. Qualified names such as `Loans.PupilID` make it clear which table supplies a field.

## INSERT INTO and VALUES

**INSERT INTO** adds a new record. The field list and value list must correspond in the same order.

```sql
INSERT INTO Pupils (PupilID, Name, YearGroup)
VALUES (104, 'Lena', 11);
```

- A new pupil record is added; existing pupils remain.
- `104` is an unused primary-key value.
- `'Lena'` is text; `11` is an integer.
- There are three named fields and three matching values.

INSERT adds a record; it does not edit an existing record simply because the name is similar.

### Matching the order of fields and values

```sql
INSERT INTO Pupils (Name, YearGroup, PupilID)
VALUES ('Lena', 11, 104);
```

This adds the same new pupil as the earlier example, because the explicit field list matches the changed value order. The first supplied value belongs to Name, the second to YearGroup and the third to PupilID.

If the field list is omitted, every supplied value must follow the table's defined column order. Naming the fields makes the intended correspondence clear. A primary-key value already used by another record cannot identify a new record uniquely.

## UPDATE and SET

**UPDATE** changes existing records. **SET** specifies their new field values. **WHERE** restricts which records are changed.

```sql
UPDATE Pupils
SET YearGroup = 11
WHERE PupilID = 101;
```

Only Shreya's year group changes, from 10 to 11. Her name and primary key remain unchanged. The other pupils are unaffected.

Using a primary key in the condition is useful when exactly one record should change.

**Without WHERE, the change applies to every record in the table.**

A condition can match more than one record. For example:

```sql
UPDATE Pupils
SET YearGroup = 11
WHERE YearGroup = 10;
```

Both Shreya and Mia change to year group 11, while Amir was already in that group. UPDATE is not limited to one row; the condition determines which rows are affected.

More than one field can be changed in the same statement by separating the assignments with commas:

```sql
UPDATE Pupils
SET Name = 'Amir Khan', YearGroup = 12
WHERE PupilID = 102;
```

This changes two values in Amir's record without changing the primary key or creating a new pupil.

## DELETE FROM

**DELETE FROM** removes records that match a condition.

```sql
DELETE FROM Loans
WHERE LoanID = 502;
```

The Geography loan is removed. Shreya's pupil record and her Macbeth loan remain because those records are in different rows or tables.

- DELETE removes whole qualifying rows, rather than just clearing one field.
- **Without WHERE, all records in the named table are deleted.**
- The table itself still exists; removing its records is different from removing the table structure.

Use **`DELETE FROM`**, not `DELETE * FROM`. The asterisk belongs to SELECT when all fields are requested; DELETE already removes whole qualifying rows.

Deleting loan 502 changes the number of loan records from three to two. It does not delete a column or replace the book title with an empty value. To change just a field value, use UPDATE instead.

## Planning and checking a query

Before writing, identify the operation:

| Need | Command | Effect on stored records |
|---|---|---|
| Retrieve information | **SELECT** | No stored records change; results are returned. |
| Add a record | **INSERT INTO … VALUES** | Creates a new record with the supplied values. |
| Change values | **UPDATE … SET** | Edits fields in matching existing records. Without WHERE, all records are affected. |
| Remove records | **DELETE FROM** | Removes whole matching rows. Without WHERE, all rows are removed; the table remains. |


Then check:

1. **Fields:** which columns must be displayed or changed?
2. **Tables:** where is the information stored?
3. **Conditions:** which rows should qualify? For two tables, what key values must match?
4. **Order:** is a particular sort required?
5. **Accuracy:** are names, operators, quotes and values correct?

Trace the query against a few records. A correct-looking query can still answer the wrong question if its filter or linking condition is wrong.

## Sources

- [PMT Education: original Summary Notes](../Reference Materials/PMT - Summary Notes.pdf). Unmodified source retained with its printed attribution and licence.
- [AQA specification for first exams in 2027](../../00 - Specification/AQA-8525-specification-2027.pdf).
