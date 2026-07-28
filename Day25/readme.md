# Day 25 – Python Pathlib: File Organizer

## 📖 Overview

Today I learned how to work with Python's `pathlib` module to manage files and directories efficiently. I explored different methods for navigating folders, searching files, deleting files/directories, and moving files.

To apply these concepts, I built a **File Organizer** that automatically sorts files into folders based on their file extensions.

---

## 📚 Concepts Covered

- `Path()`
- `iterdir()`
- `glob()`
- `rglob()`
- `name`
- `stem`
- `suffix`
- `is_file()`
- `mkdir()`
- `unlink()`
- `rmdir()`
- `rename()`

---

## 🛠️ Mini Project – File Organizer

### Features

- Scans the Downloads folder.
- Detects file types using file extensions.
- Creates destination folders automatically if they do not exist.
- Moves files into their respective folders.

### Supported File Types

| Extension | Folder |
|-----------|--------|
| `.pdf` | PDFs |
| `.txt` | TextFiles |
| `.csv` | CSVs |
| `.py` | Python |
| `.png` | Images |
| `.jpg` | Images |

---

## 💡 Key Learnings

- `iterdir()` iterates through all files and folders in a directory.
- `glob()` searches files matching a pattern in the current directory.
- `rglob()` searches files recursively in all subdirectories.
- `suffix` returns the file extension.
- `name` returns the complete file name.
- `stem` returns the filename without the extension.
- `mkdir(exist_ok=True)` creates a directory only if it does not already exist.
- `unlink()` deletes a file.
- `rmdir()` removes an empty directory.
- `rename()` can rename or move files to another location.

---

## 🚀 What I Built

A Python program that:

1. Reads all files inside the Downloads folder.
2. Identifies each file's extension.
3. Creates folders for different file types.
4. Moves each file into the appropriate folder automatically.

This project helped me understand practical file handling and automation using Python.

---

## 📈 Skills Improved

- Python File Handling
- Pathlib Module
- File System Automation
- Directory Management
- Conditional Logic
- Writing Clean Python Code

---

## 📌 Git Commit

```
Day 25: Mastered pathlib and built a File Organizer using Path objects
```

---

## 🎯 Next Goal

Continue learning Python for Data Engineering by exploring more advanced modules and building real-world automation projects.