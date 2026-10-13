# Relational databases and SQL questions & answers

## 1 mark

**1.** What is a database?

**Answer:** An organised collection of data.

**2.** What is one row of a database table called?

**Answer:** Record.

**3.** What is one column of a database table called?

**Answer:** Field.

**4.** Which key uniquely identifies each record in a table?

**Answer:** Primary key.

**5.** Which key can link a record to a primary key in another table?

**Answer:** Foreign key.

**6.** Which SQL keyword sorts the rows in a result?

**Answer:** ORDER BY.

**7.** Which SQL symbol selects all fields?

**Answer:** *.

**8.** Name a suitable data type for the whole-number field YearGroup.

**Answer:** Integer.

**9.** Name a suitable data type for a person's name.

**Answer:** Text/string.

## 2 marks

**10.** Explain a relational database.

**Answer:**

- It stores data in **related tables**.
- Tables can be linked by matching a foreign key to a primary key.

**11.** Explain why a person's name is usually a poor primary key.

**Answer:**

- Different people can have the same name.
- A primary key must identify each record uniquely, so a unique ID is more suitable.

**12.** In Pupils(PupilID, Name) and Loans(LoanID, PupilID, BookTitle), identify the primary key of Loans and its foreign key.

**Answer:**

- **Primary key:** LoanID.
- **Foreign key:** PupilID, linking to the pupil identified in Pupils.

**13.** Explain why the same PupilID may appear in several Loan records.

**Answer:**

- One pupil may borrow several books.
- Each loan has a unique LoanID but uses the same foreign key to identify that pupil.

**14.** Explain the difference between data redundancy and data inconsistency.

**Answer:**

- **Redundancy** is unnecessary duplication of data.
- **Inconsistency** occurs when copies disagree, for example two different addresses for the same pupil.

**15.** The table Pupils has fields PupilID, Name and YearGroup. Write SQL to display only Name and YearGroup for every pupil.

**Answer:**

```sql
SELECT Name, YearGroup
FROM Pupils;
```

**16.** Pupils has a field YearGroup. Write SQL to return all fields for pupils in Year 10.

**Answer:**

```sql
SELECT *
FROM Pupils
WHERE YearGroup = 10;
```

**17.** Pupils has fields PupilID and Name. Write SQL to list the names in alphabetical order.

**Answer:**

```sql
SELECT Name
FROM Pupils
ORDER BY Name ASC;
```

**18.** Pupils contains Shreya in Year 10, Amir in Year 11 and Mia in Year 10. What names are returned by this query?

```sql
SELECT Name
FROM Pupils
WHERE YearGroup = 10
ORDER BY Name DESC;
```

**Answer:** Shreya, then Mia.

## 3 marks

**19.** Explain how linking a pupil table to a loan table can reduce inconsistency.

**Answer:**

- Store the pupil's name once in the pupil table.
- Each loan stores the **PupilID foreign key**, rather than another copy of the name.
- A name change is made in one record, avoiding conflicting copies in different loan records.

**20.** Pupils has fields PupilID, Name and YearGroup. Write SQL to select names in Years 10 or 11.

**Answer:**

```sql
SELECT Name
FROM Pupils
WHERE YearGroup = 10 OR YearGroup = 11;
```

**21.** Loans has fields LoanID, PupilID, BookTitle and DaysLoaned. Write SQL to return BookTitle for loans lasting at least 14 days but no more than 21 days.

**Answer:**

```sql
SELECT BookTitle
FROM Loans
WHERE DaysLoaned >= 14 AND DaysLoaned <= 21;
```

**22.** Explain why this condition cannot match any record: YearGroup = 10 AND YearGroup = 11.

**Answer:**

- One record has one value for YearGroup.
- **AND** requires both conditions to be true, but that value cannot be both 10 and 11.
- Use **OR** to match either year group.

**23.** Pupils has fields PupilID, Name and YearGroup. Insert pupil 104, named Lena, in Year 11.

**Answer:**

```sql
INSERT INTO Pupils (PupilID, Name, YearGroup)
VALUES (104, 'Lena', 11);
```

**24.** Pupils has fields PupilID, Name and YearGroup. Change pupil 101's YearGroup to 11.

**Answer:**

```sql
UPDATE Pupils
SET YearGroup = 11
WHERE PupilID = 101;
```

**25.** Loans has a primary key LoanID. Write SQL to delete only loan 502.

**Answer:**

```sql
DELETE FROM Loans
WHERE LoanID = 502;
```

## 4 marks

**26.** An administrator runs this query by mistake. Explain its effect and show a corrected version that affects only pupil 101.

```sql
UPDATE Pupils
SET YearGroup = 11;
```

**Answer:**

The missing **WHERE** means every record is updated, so all pupils are assigned Year 11. A condition using the unique primary key limits the change to the intended pupil.

```sql
UPDATE Pupils
SET YearGroup = 11
WHERE PupilID = 101;
```

**27.** Loans has fields LoanID, PupilID, BookTitle and DaysLoaned. Write SQL to show BookTitle and DaysLoaned for loans longer than 7 days, longest first.

**Answer:**

```sql
SELECT BookTitle, DaysLoaned
FROM Loans
WHERE DaysLoaned > 7
ORDER BY DaysLoaned DESC;
```

**28.** A pupil table has records (101, Shreya), (102, Amir), (103, Mia). A loan table has matching PupilID values 101, 101 and 102. Describe the rows produced by matching Pupils.PupilID to Loans.PupilID, and explain why the match matters.

**Answer:**

- Shreya appears in **two matching rows**, one for each loan.
- Amir appears in **one matching row**.
- Mia has **no matching loan**, so does not appear in this matching result.
- Matching the keys links each loan to the correct pupil; without a linking condition, unrelated pupil and loan rows could be combined.

## 6 marks

**29.** Pupils(PupilID, Name, YearGroup) links to Loans(LoanID, PupilID, BookTitle, DaysLoaned). Write SQL to return each Year 10 pupil's Name and borrowed BookTitle. Sort by BookTitle alphabetically.

**Answer:**

```sql
SELECT Pupils.Name, Loans.BookTitle
FROM Pupils, Loans
WHERE Pupils.PupilID = Loans.PupilID
AND Pupils.YearGroup = 10
ORDER BY Loans.BookTitle ASC;
```

The first condition **links the tables**. The second selects the required pupils. Qualified field names distinguish which table each field belongs to.

**30.** A library stores a pupil's name and address separately in every loan record. Explain the problems and recommend a relational design.

**Answer:**

- Repeating the same pupil details creates **redundancy**, increasing storage and repeated data-entry work.
- If some copies are updated but others are not, records become **inconsistent**.
- Store PupilID, name and address once in a pupil table, using PupilID as its primary key.
- Store each borrowing event in a loan table with a unique LoanID.
- Include PupilID as a foreign key in the loan table to associate the borrowing with the pupil.
- Updating one pupil record then changes the details used by all matching queries, while keeping individual loans separate.

## Past-paper sources

These are original practice questions and tutor answers. Question types were checked against AQA Paper 2 from June 2022 and June 2023 and the revised course content. The marks are practice allocations. No frequency ranking is claimed from this two-paper sample.

- [June 2022 question paper](../../00%20-%20Past%20papers/Paper%202/AQA-85252-QP-JUN22.PDF)

- [June 2022 mark scheme](../../00%20-%20Past%20papers/Paper%202/AQA-85252-MS-JUN22.PDF)

- [June 2023 question paper](../../00%20-%20Past%20papers/Paper%202/AQA-85252-QP-JUN23.PDF)

- [June 2023 mark scheme](../../00%20-%20Past%20papers/Paper%202/AQA-85252-MS-JUN23.PDF)

- [Official AQA assessment resource directory](https://www.aqa.org.uk/subjects/computer-science/gcse/computer-science-8525/assessment-resources)
