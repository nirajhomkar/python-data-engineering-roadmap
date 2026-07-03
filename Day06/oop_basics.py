"""
Day 6 - Object-Oriented Programming (OOP)

Author: Niraj Homkar

Topics Covered:
1. Creating a Class
2. Constructor (__init__)
3. Creating Objects
4. Instance Variables
5. Methods
6. Updating Object Data
7. Returning Values from Methods
"""


# ----------------------------------------
# Employee Class
# ----------------------------------------

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"{self.name} earns ₹{self.salary}")

    def hike(self, amount):
        self.salary += amount

    def annual_salary(self):
        return self.salary * 12


# ----------------------------------------
# Creating Objects
# ----------------------------------------

emp1 = Employee("Niraj", 60000)
emp2 = Employee("Rahul", 70000)

print("=" * 40)
print("Employee Details")
print("=" * 40)

emp1.display()
emp2.display()

print("\n" + "=" * 40)
print("After Salary Hike")
print("=" * 40)

emp1.hike(5000)

emp1.display()

print("\n" + "=" * 40)
print("Annual Salary")
print("=" * 40)

print(f"{emp1.name}'s Annual Salary = ₹{emp1.annual_salary()}")

print("\nDay 6 Completed Successfully!")