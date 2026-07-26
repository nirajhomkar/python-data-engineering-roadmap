# 📘 Day 23 - Python `pathlib` Module

## 📅 Date
**Day 23 - Python for Data Engineering Roadmap**

---

# 🎯 Objective

Learn how to work with files and directories using Python's modern **`pathlib`** module.

Unlike `os.path`, `pathlib` provides an object-oriented and more readable way to work with file system paths.

---

# 📚 Topics Covered

- Importing `Path`
- `Path.cwd()`
- Creating `Path` objects
- `Path.exists()`
- `Path.is_file()`
- `Path.is_dir()`
- `Path.mkdir()`
- `mkdir(exist_ok=True)`
- `Path.rename()`
- Advantages of `pathlib` over `os.path`

---

# 📝 Theory

## 1. Importing Path

```python
from pathlib import Path
```

`Path` is a **class** available in Python's `pathlib` module.

---

## 2. Current Working Directory

```python
from pathlib import Path

print(Path.cwd())
```

Returns the current working directory.

Example Output:

```
D:\Coding\python-data-engineering-roadmap\Day23
```

---

## 3. Creating a Path Object

```python
from pathlib import Path

file = Path("employees.csv")
```

This does **not** create the file.

It only creates a **Path object** representing the file path.

---

## 4. Checking Whether a File Exists

```python
print(file.exists())
```

Returns:

- `True` → File exists
- `False` → File does not exist

---

## 5. Checking Whether It Is a File

```python
print(file.is_file())
```

Returns:

- `True` → It is a file.
- `False` → It is not a file.

---

## 6. Checking Whether It Is a Directory

```python
folder = Path("Reports")

print(folder.is_dir())
```

Returns:

- `True` → It is a directory.
- `False` → It is not a directory.

---

## 7. Creating a Directory

```python
folder = Path("Reports")

folder.mkdir()
```

Creates a new folder named **Reports**.

---

## 8. Preventing FileExistsError

```python
folder.mkdir(exist_ok=True)
```

If the folder already exists, Python will not raise an error.

---

## 9. Renaming a File or Folder

```python
folder.rename("Logs")
```

Renames **Reports** to **Logs**.

If the source file or folder does not exist, Python raises a **FileNotFoundError**.

---

# 💻 Practice Programs

## Program 1

```python
from pathlib import Path

print("Current Working Directory:")
print(Path.cwd())
```

---

## Program 2

```python
from pathlib import Path

file = Path("employees.csv")

print("Does employees.csv exist?")
print(file.exists())

print("Is employees.csv a file?")
print(file.is_file())
```

---

## Program 3

```python
from pathlib import Path

folder = Path("Reports")

folder.mkdir(exist_ok=True)

print("Reports folder created (or already exists).")

folder.rename("Logs")

print("Folder renamed to Logs.")
```

---

# 🛠 Mini Project - File Organizer

## Problem Statement

Create a folder named **Raw_Data**.

Inside it, create an empty file named:

```
sales.csv
```

Write a Python program to:

- Check whether `sales.csv` exists.
- Check whether it is a file.
- Rename it to `sales_2026.csv`.
- Print a success message.
- Display the contents of the `Raw_Data` folder.

---

## Sample Solution

```python
from pathlib import Path

folder = Path("Raw_Data")

file = folder / "sales.csv"

print("Does sales.csv exist?")
print(file.exists())

print("Is sales.csv a file?")
print(file.is_file())

if file.exists():
    new_file = file.rename(folder / "sales_2026.csv")
    print("File renamed successfully.")

print("\nContents of Raw_Data:")

for item in folder.iterdir():
    print(item.name)
```

---

# 🎤 Interview Questions

### 1. What is `Path`?

**Answer:** `Path` is a class in the `pathlib` module used to represent file system paths.

---

### 2. Why is `pathlib` preferred over `os.path`?

It provides a cleaner, object-oriented, and more readable way to work with files and directories.

---

### 3. What does `Path.cwd()` return?

It returns the current working directory.

---

### 4. What is the difference between `Path()` and `exists()`?

- `Path()` creates a Path object.
- `exists()` checks whether the path actually exists.

---

### 5. What does `exist_ok=True` do?

It prevents a `FileExistsError` if the directory already exists.

---

### 6. What happens if `rename()` is called on a file or folder that does not exist?

Python raises a **FileNotFoundError**.

---

# ⚠ Common Mistakes

### Incorrect

```python
file.isfile()
```

### Correct

```python
file.is_file()
```

---

### Incorrect

```python
file.iterdir()
```

`iterdir()` works only on directories.

---

### Correct

```python
folder.iterdir()
```

---

# 📌 Key Takeaways

- `Path` is a class for working with file paths.
- `Path.cwd()` returns the current working directory.
- `exists()` checks whether a path exists.
- `is_file()` checks if a path is a file.
- `is_dir()` checks if a path is a directory.
- `mkdir()` creates a new directory.
- `mkdir(exist_ok=True)` avoids `FileExistsError`.
- `rename()` renames files and directories.
- `pathlib` is cleaner and more readable than `os.path`.

---

# 📂 Folder Structure

```
Day23/
│── pathlib_practice.py
│── employees.csv
│── Logs/
│── README.md
```

---

# 📊 Progress

✅ Day 23 Completed

**Python Progress:** 23/50 Days Completed

---

## 📝 Git Commit Message

```text
Day 23: Learned Python pathlib module for file and directory operations
```

---

## 🚀 Next Lesson

**Day 24:** Advanced `pathlib` – Reading, Writing, and Navigating Files & Directories