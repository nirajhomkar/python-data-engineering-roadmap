"""
Day 3 - File Handling

Author: Niraj Homkar

Topics Covered:
1. Reading a File
2. Reading Line by Line
3. Writing to a File
4. Appending to a File
5. File Modes
"""

# -----------------------------
# Reading an Entire File
# -----------------------------

with open("employees.txt", "r") as file:
    content = file.read()
    print(content)

print("-" * 40)

# -----------------------------
# Reading Line by Line
# -----------------------------

with open("employees.txt", "r") as file:
    for line in file:
        print(line.strip())

print("-" * 40)

# -----------------------------
# Writing to a File
# -----------------------------

with open("output.txt", "w") as file:
    file.write("Welcome to Python File Handling\n")
    file.write("This file was created using Python.\n")

print("Data written successfully!")

print("-" * 40)

# -----------------------------
# Appending Data
# -----------------------------

with open("output.txt", "a") as file:
    file.write("Appending a new line.\n")

print("Data appended successfully!")

print("-" * 40)

print("Day 3 Completed Successfully!")