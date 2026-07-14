"""
Day 13 - File Handling

Author: Niraj Homkar

Topics Covered:
1. Read File
2. Write File
3. Append File
4. with open()
5. read()
6. readline()
7. readlines()
8. Student Record Management System
"""

# ==========================================
# Program 1 : Read a File
# ==========================================

print("=" * 50)
print("Program 1 : Read File")
print("=" * 50)

try:
    with open("students.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("students.txt file not found.")

print()


# ==========================================
# Program 2 : Write to a File
# ==========================================

print("=" * 50)
print("Program 2 : Write File")
print("=" * 50)

with open("sample.txt", "w") as file:
    file.write("Welcome to Python File Handling")

print("Data written successfully.\n")


# ==========================================
# Program 3 : Append to a File
# ==========================================

print("=" * 50)
print("Program 3 : Append File")
print("=" * 50)

with open("sample.txt", "a") as file:
    file.write("\nLearning Data Engineering")

print("Data appended successfully.\n")


# ==========================================
# Student Record Management System
# ==========================================

def add_student():
    name = input("Enter Student Name: ")

    with open("students.txt", "a") as file:
        file.write(f"{name}\n")

    print("Student Added Successfully!\n")


def view_students():

    try:
        with open("students.txt", "r") as file:

            print("\n===== Students =====")

            for line in file:
                print(line.strip())

            print()

    except FileNotFoundError:
        print("No student records found.\n")


# ==========================================
# Main Menu
# ==========================================

while True:

    print("===== Student Record System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!\n")

print("\nDay 13 Completed Successfully!")