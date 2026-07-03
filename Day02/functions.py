"""
Day 2 - Python Functions

Author: Niraj Homkar

Topics Covered:
1. Function Definition
2. Parameters
3. Return Statement
4. Default Arguments
5. Keyword Arguments
6. *args
7. **kwargs
"""

# Simple Function
def greet():
    print("Welcome to Python!")

greet()

print("-" * 40)

# Function with Parameters
def add(a, b):
    print(f"Sum = {a + b}")

add(10, 20)

print("-" * 40)

# Function with Return Value
def multiply(a, b):
    return a * b

result = multiply(5, 4)
print(f"Multiplication = {result}")

print("-" * 40)

# Default Argument
def employee(name, city="Bangalore"):
    print(f"{name} works in {city}")

employee("Niraj")
employee("Rahul", "Pune")

print("-" * 40)

# Keyword Arguments
def student(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

student(age=22, name="Niraj")

print("-" * 40)

# *args (Variable Number of Arguments)
def total_salary(*salaries):
    total = sum(salaries)
    print(f"Total Salary = {total}")

total_salary(50000, 60000, 70000)

print("-" * 40)

# **kwargs (Variable Keyword Arguments)
def employee_details(**details):
    for key, value in details.items():
        print(f"{key} : {value}")

employee_details(
    name="Niraj",
    salary=60000,
    city="Bangalore"
)

print("-" * 40)

print("Day 2 Completed Successfully!")