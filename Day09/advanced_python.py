"""
Day 9 - Advanced Python

Author: Niraj Homkar

Topics Covered:
1. Lists
2. Tuples
3. Sets
4. Dictionaries
5. List Comprehension
6. Lambda Functions
7. map()
8. filter()
"""

# ----------------------------------------
# Lists
# ----------------------------------------

print("=" * 40)
print("Lists")
print("=" * 40)

numbers = [10, 20, 30, 40, 50]

print("All Numbers:")

for num in numbers:
    print(num)

# ----------------------------------------
# Even Numbers
# ----------------------------------------

print("\n" + "=" * 40)
print("Even Numbers")
print("=" * 40)

for num in numbers:
    if num % 2 == 0:
        print(num)

# ----------------------------------------
# Sum of Numbers
# ----------------------------------------

print("\n" + "=" * 40)
print("Sum of Numbers")
print("=" * 40)

total = 0

for num in numbers:
    total += num

print(f"Total = {total}")

# ----------------------------------------
# Tuples
# ----------------------------------------

print("\n" + "=" * 40)
print("Tuples")
print("=" * 40)

cities = ("Bangalore", "Pune", "Hyderabad")

for city in cities:
    print(city)

# ----------------------------------------
# Sets
# ----------------------------------------

print("\n" + "=" * 40)
print("Sets")
print("=" * 40)

languages = {"Python", "Java", "Python", "SQL"}

print(languages)

# ----------------------------------------
# Dictionary
# ----------------------------------------

print("\n" + "=" * 40)
print("Dictionary")
print("=" * 40)

employee = {
    "name": "Niraj",
    "salary": 60000,
    "city": "Bangalore"
}

for key, value in employee.items():
    print(f"{key} : {value}")

# ----------------------------------------
# Square Numbers (Normal Loop)
# ----------------------------------------

print("\n" + "=" * 40)
print("Square Numbers (Loop)")
print("=" * 40)

numbers = [1, 2, 3, 4, 5]

squares = []

for num in numbers:
    squares.append(num * num)

print(squares)

# ----------------------------------------
# List Comprehension
# ----------------------------------------

print("\n" + "=" * 40)
print("List Comprehension")
print("=" * 40)

squares = [num * num for num in numbers]

print(squares)

# ----------------------------------------
# Even Numbers using List Comprehension
# ----------------------------------------

print("\n" + "=" * 40)
print("Even Numbers using List Comprehension")
print("=" * 40)

numbers = [10, 15, 20, 25, 30]

evens = [num for num in numbers if num % 2 == 0]

print(evens)

# ----------------------------------------
# Lambda Function
# ----------------------------------------

print("\n" + "=" * 40)
print("Lambda Function")
print("=" * 40)

square = lambda num: num * num

print(square(5))

# ----------------------------------------
# map()
# ----------------------------------------

print("\n" + "=" * 40)
print("map()")
print("=" * 40)

numbers = [10, 20, 30, 40]

double = list(map(lambda num: num * 2, numbers))

print(double)

# ----------------------------------------
# filter()
# ----------------------------------------

print("\n" + "=" * 40)
print("filter()")
print("=" * 40)

numbers = [10, 20, 30, 40, 50]

greater = list(filter(lambda num: num > 25, numbers))

print(greater)

print("\nDay 9 Completed Successfully!")