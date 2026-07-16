"""
Day 14 - Object Oriented Programming (OOP)

Author : Niraj Homkar

Topics Covered:
1. Class
2. Object
3. Constructor (__init__)
4. self
5. Instance Variables
6. Methods
7. __str__()
8. Class Variables
9. Bank Account Mini Project
"""

# ==========================================
# Program 1 : Creating a Class and Object
# ==========================================

print("=" * 50)
print("Program 1 : Student Class")
print("=" * 50)


class Student:

    college = "JSPM University"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def greet(self):
        print(f"Hello, I am {self.name}")
        print(f"My Roll Number is {self.roll_no}")

    def __str__(self):
        return f"Student(Name={self.name}, Roll No={self.roll_no})"


student1 = Student("Niraj", 101)
student2 = Student("Rahul", 102)

student1.greet()
print()

student2.greet()
print()

print(student1)
print(student2)

print("\nCollege :", Student.college)

# ==========================================
# Program 2 : Employee Class
# ==========================================

print("\n" + "=" * 50)
print("Program 2 : Employee Class")
print("=" * 50)


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name : {self.name}")
        print(f"Salary : ₹{self.salary}")

    def annual_salary(self):
        print(f"Annual Salary : ₹{self.salary * 12}")


employee1 = Employee("Niraj", 50000)
employee2 = Employee("Rahul", 70000)

employee1.display()
employee1.annual_salary()

print()

employee2.display()
employee2.annual_salary()

# ==========================================
# Program 3 : Bank Account Mini Project
# ==========================================

print("\n" + "=" * 50)
print("Program 3 : Bank Account")
print("=" * 50)


class BankAccount:

    bank_name = "State Bank of India"

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} Deposited Successfully")
        print(f"Current Balance : ₹{self.balance}")

    def withdraw(self, amount):

        if self.balance >= amount:
            self.balance -= amount
            print(f"₹{amount} Withdrawn Successfully")
            print(f"Current Balance : ₹{self.balance}")

        else:
            print("Insufficient Balance")

    def display(self):
        print("\n===== Account Details =====")
        print(f"Bank : {self.bank_name}")
        print(f"Account Holder : {self.account_holder}")
        print(f"Balance : ₹{self.balance}")


account = BankAccount("Niraj", 10000)

account.deposit(5000)
print()

account.withdraw(3000)
print()

account.display()

print("\nDay 14 Completed Successfully!")