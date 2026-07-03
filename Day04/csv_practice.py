"""
Day 4 - CSV Handling

Author: Niraj Homkar

Topics Covered:
1. csv.reader()
2. csv.DictReader()
3. Reading Columns
4. Filtering Data
5. Calculating Total Salary
"""

import csv

# ----------------------------------------
# Reading using csv.reader()
# ----------------------------------------

print("=" * 40)
print("Reading using csv.reader()")
print("=" * 40)

with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# ----------------------------------------
# Reading using csv.DictReader()
# ----------------------------------------

print("\n" + "=" * 40)
print("Reading using csv.DictReader()")
print("=" * 40)

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(f"{row['name']} earns ₹{row['salary']}")

# ----------------------------------------
# Employees from Bangalore
# ----------------------------------------

print("\n" + "=" * 40)
print("Employees from Bangalore")
print("=" * 40)

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["city"] == "Bangalore":
            print(row["name"])

# ----------------------------------------
# Employees earning more than 60000
# ----------------------------------------

print("\n" + "=" * 40)
print("Employees earning more than 60000")
print("=" * 40)

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if int(row["salary"]) > 60000:
            print(f"{row['name']} earns ₹{row['salary']}")

# ----------------------------------------
# Total Salary
# ----------------------------------------

print("\n" + "=" * 40)
print("Total Salary")
print("=" * 40)

total = 0

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total += int(row["salary"])

print(f"Total Salary = ₹{total}")

print("\n" + "=" * 40)
print("Average Salary")
print("=" * 40)

average=0

with open("employees.csv","r") as file:
    reader=csv.DictReader(file)
    count=0
    for row in reader:
        average+=int(row["salary"])
        count+=1

if count > 0:
    average /= count

print(f"Average Salary = ₹{average:.2f}")

print("\nDay 4 Completed Successfully!")