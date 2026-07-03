"""
Day 7 - Inheritance & Polymorphism

Author: Niraj Homkar

Topics Covered:
1. Inheritance
2. Parent Class
3. Child Class
4. super()
5. Method Overriding
6. Polymorphism
"""

# ----------------------------------------
# Parent Class
# ----------------------------------------

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"{self.name} earns ₹{self.salary}")


# ----------------------------------------
# Child Class - Data Engineer
# ----------------------------------------

class DataEngineer(Employee):

    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def display(self):
        print(
            f"{self.name} is a Data Engineer, "
            f"earns ₹{self.salary} and knows {self.language}"
        )


# ----------------------------------------
# Child Class - Manager
# ----------------------------------------

class Manager(Employee):

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def display(self):
        print(
            f"{self.name} manages a team of "
            f"{self.team_size} and earns ₹{self.salary}"
        )


# ----------------------------------------
# Creating Objects
# ----------------------------------------

emp = Employee("Amit", 50000)
de = DataEngineer("Niraj", 65000, "Python")
manager = Manager("Rahul", 90000, 10)

print("=" * 40)
print("Method Overriding")
print("=" * 40)

emp.display()
de.display()
manager.display()

print("\nDay 7 Completed Successfully!")