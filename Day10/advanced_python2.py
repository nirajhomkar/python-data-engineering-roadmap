"""
Day 10 - Advanced Python (Part 2)

Author: Niraj Homkar

Topics Covered:
1. enumerate()
2. zip()
3. *args
4. **kwargs
5. Iterators
6. Generators (yield)
"""

# ----------------------------------------
# enumerate()
# ----------------------------------------

print("=" * 40)
print("enumerate()")
print("=" * 40)

languages = ["Python", "SQL", "Pandas", "PySpark"]

for index, language in enumerate(languages, start=1):
    print(f"{index}. {language}")

# ----------------------------------------
# zip()
# ----------------------------------------

print("\n" + "=" * 40)
print("zip()")
print("=" * 40)

subjects = ["Python", "SQL", "Pandas"]
marks = [95, 90, 98]

for subject, mark in zip(subjects, marks):
    print(f"{subject} : {mark}")

# ----------------------------------------
# *args
# ----------------------------------------

print("\n" + "=" * 40)
print("*args")
print("=" * 40)

def add(*numbers):
    total = 0

    for num in numbers:
        total += num

    return total

print("Sum =", add(10, 20))
print("Sum =", add(10, 20, 30))
print("Sum =", add(10, 20, 30, 40))


def find_max(*numbers):
    maximum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

    return maximum

print("Maximum =", find_max(10, 50, 20, 90, 40))

# ----------------------------------------
# **kwargs
# ----------------------------------------

print("\n" + "=" * 40)
print("**kwargs")
print("=" * 40)

def employee_details(**details):
    for key, value in details.items():
        print(f"{key} : {value}")

employee_details(
    name="Niraj",
    role="Data Engineer",
    salary=60000,
    city="Bangalore"
)

# ----------------------------------------
# Iterators
# ----------------------------------------

print("\n" + "=" * 40)
print("Iterators")
print("=" * 40)

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# ----------------------------------------
# Generators
# ----------------------------------------

print("\n" + "=" * 40)
print("Generators (yield)")
print("=" * 40)

def generate_numbers():
    for num in range(1, 6):
        yield num

generator = generate_numbers()

for number in generator:
    print(number)

print("\nDay 10 Completed Successfully!")