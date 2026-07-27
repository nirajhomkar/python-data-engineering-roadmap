# 📘 Day 24 - Python `pathlib` (Reading & Writing Files)

## 📅 Date
Day 24 - Python for Data Engineering Roadmap

---

# 🎯 Objective

Learn how to read and write text files using the `pathlib` module.

---

# 📚 Topics Covered

- Path.read_text()
- Path.write_text()
- Reading file contents
- Writing data to files
- Overwriting existing files
- Creating files if they do not exist
- Mini Project - Student Report Generator

---

# 📝 Theory

## Reading a File

```python
from pathlib import Path

file = Path("students.txt")

print(file.read_text())
```

### Output

```
Niraj
Rahul
Priya
Anjali
```

`read_text()` reads the complete file and returns a **string**.

---

## Return Type

```python
content = file.read_text()

print(type(content))
```

Output

```
<class 'str'>
```

---

## Writing to a File

```python
from pathlib import Path

file = Path("notes.txt")

file.write_text("Python for Data Engineering")
```

If the file does not exist, Python creates it.

If it already exists, Python overwrites the existing content.

---

# 💻 Practice Program

```python
from pathlib import Path

file = Path("students.txt")

print(file.read_text())

print(type(file.read_text()))

file2 = Path("notes.txt")

file2.write_text("Content Written Successfully")

print("\nReading the file")

print(file2.read_text())
```

---

# 🛠 Mini Project

Student Report Generator

Read student marks from `marks.txt` and generate a report in `report.txt`.

---

# 🎤 Interview Questions

### What does `read_text()` return?

It returns the complete file content as a **string**.

---

### What does `write_text()` do?

It writes data to a file.

If the file exists, it overwrites the content.

---

### Can `write_text()` append data?

No.

`write_text()` always overwrites the file.

---

### Difference between `read_text()` and `write_text()`

- `read_text()` → Reads data
- `write_text()` → Writes data

---

# 📌 Key Takeaways

- `read_text()` returns a string.
- `write_text()` creates or overwrites files.
- `pathlib` provides simple methods for file handling.
- File transformation is one of the first steps of an ETL pipeline.

---

# 📂 Folder Structure

```
Day24/
│── marks.txt
│── students.txt
│── notes.txt
│── studentReportGenerator.py
│── pathlibpractice2.py
│── README.md
```

---

# 📈 Progress

✅ Day 24 Completed

Python Progress : 24/50 Days Completed

---

## Git Commit Message

```
Day 24: Learned pathlib read_text() and write_text() with Student Report Generator
```