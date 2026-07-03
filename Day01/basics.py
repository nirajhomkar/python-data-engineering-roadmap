"""
Day 1 - Python Basics

Topics Covered:
1. Variables
2. Data Types
3. User Input
4. Arithmetic Operators
5. Comparison Operators
6. Conditional Statements
7. Loops
"""

# Variables
name = "Niraj"
age = 22
city = "Bangalore"

print("Name:", name)
print("Age:", age)
print("City:", city)

print("-" * 30)

# Arithmetic Operators
a = 20
b = 10

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

print("-" * 30)

# Comparison Operators
print(a > b)
print(a < b)
print(a == b)

print("-" * 30)

# If-Else
salary = 60000

if salary > 50000:
    print("High Salary")
else:
    print("Average Salary")

print("-" * 30)

# List
numbers = [10, 20, 30, 40, 50]

print("Numbers:")
for number in numbers:
    print(number)

print("-" * 30)

# For Loop
for i in range(1, 6):
    print(i)

print("-" * 30)

# While Loop
count = 1

while count <= 5:
    print(count)
    count += 1

print("-" * 30)

print("Day 1 Completed Successfully!")