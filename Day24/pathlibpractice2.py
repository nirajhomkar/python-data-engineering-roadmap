from pathlib import Path

file = Path("students.txt")

print(file.read_text())

print(type(file.read_text()))

file2 = Path("notes.txt")

file2.write_text("Content Written successfully")

print("\nReading the file")
print(file2.read_text())