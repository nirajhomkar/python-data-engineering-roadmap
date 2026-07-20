"""
=========================================================
Python Data Engineering Roadmap
Day 18 : Encapsulation

Topics Covered:
1. Public Members
2. Protected Members
3. Private Members
4. Name Mangling
5. @property
6. Mini Project - Bank Account

Author : Niraj Homkar
=========================================================
"""

# ==========================================================
# Public Member
# ==========================================================

class Student:

    def __init__(self, name):
        self.name = name


student = Student("Niraj")
print("Public Member")
print(student.name)

print("-" * 50)


# ==========================================================
# Protected Member
# ==========================================================

class Employee:

    def __init__(self, salary):
        self._salary = salary


employee = Employee(50000)
print("Protected Member")
print(employee._salary)

print("-" * 50)


# ==========================================================
# Private Member (Name Mangling)
# ==========================================================

class Person:

    def __init__(self, age):
        self.__age = age


person = Person(22)

print("Private Member using Name Mangling")
print(person._Person__age)

print("-" * 50)


# ==========================================================
# @property Example
# ==========================================================

class Result:

    def __init__(self):
        self.__marks = 0

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid Marks")


result = Result()

result.marks = 90
print("@property Example")
print(result.marks)

result.marks = 120
print(result.marks)

print("-" * 50)


# ==========================================================
# Mini Project : Bank Account System
# ==========================================================

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited Successfully")
        else:
            print("Invalid Deposit Amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid Withdrawal Amount")
        elif amount <= self.__balance:
            self.__balance -= amount
            print("Withdraw Successfully")
        else:
            print("Insufficient Balance")


account = BankAccount("Niraj", 10000)

print("Account Holder :", account.name)
print("Balance :", account.balance)

account.deposit(5000)
print("Balance :", account.balance)

account.withdraw(3000)
print("Balance :", account.balance)

account.withdraw(20000)
print("Balance :", account.balance)