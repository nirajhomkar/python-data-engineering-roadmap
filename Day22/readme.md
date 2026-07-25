# Day 22 - Python `os` Module

## 📚 Topics Covered

- `import os`
- `os.getcwd()`
- `os.listdir()`
- `os.mkdir()`
- `os.path.exists()`
- `os.chdir()`
- `os.path.isfile()`
- `os.path.isdir()`
- `os.rename()`

---

## 📝 Concepts Learned

### 1. `os.getcwd()`
Returns the current working directory.

```python
import os

print(os.getcwd())
```

---

### 2. `os.listdir()`
Returns a list of all files and folders in the current directory.

```python
print(os.listdir())
```

---

### 3. `os.mkdir()`
Creates a new directory.

```python
os.mkdir("Data")
```

---

### 4. `os.path.exists()`
Checks whether a file or folder exists.

```python
if os.path.exists("Data"):
    print("Folder already exists")
else:
    os.mkdir("Data")
```

---

### 5. `os.chdir()`
Changes the current working directory.

```python
os.chdir("Data")
```

---

### 6. `os.path.isfile()`
Checks whether the given path is a file.

```python
print(os.path.isfile("os_practice.py"))
```

---

### 7. `os.path.isdir()`
Checks whether the given path is a directory.

```python
print(os.path.isdir("Data"))
```

---

### 8. `os.rename()`
Renames a file or folder.

```python
os.rename("Data", "Raw_Data")
```

---

# 💻 Practice Program

```python
import os

print("Current Working Directory:")
print(os.getcwd())

print()

print("Files and Folders:")
print(os.listdir())

print()

if os.path.exists("Data"):
    print("Folder 'Data' already exists!")
else:
    os.mkdir("Data")
    print("Folder 'Data' created successfully!")

print()

print("Updated Files and Folders:")
print(os.listdir())

print()

print("Is os_practice.py a file?")
print(os.path.isfile("os_practice.py"))

print()

print("Is Data a directory?")
print(os.path.isdir("Data"))

print()

if os.path.exists("Data"):
    os.rename("Data", "Raw_Data")
    print("Folder renamed successfully!")

print()

print("Final Files and Folders:")
print(os.listdir())
```

---

# 🎯 Key Learnings

- The `os` module helps Python interact with the operating system.
- `os.getcwd()` returns the current working directory.
- `os.listdir()` lists files and folders.
- `os.mkdir()` creates a new directory.
- `os.path.exists()` prevents `FileExistsError`.
- `os.chdir()` changes the working directory.
- `os.path.isfile()` checks if a path is a file.
- `os.path.isdir()` checks if a path is a directory.
- `os.rename()` renames files or folders.

---

# 🚀 Mini Project

Created a Python program that:

- Displays the current working directory.
- Lists files and folders.
- Creates a new directory if it doesn't exist.
- Checks whether a path is a file or directory.
- Renames a directory.
- Displays the updated folder structure.

---

## 📌 Git Commit Message

```text
Day 22: Learned Python os module and performed file & directory operations
```