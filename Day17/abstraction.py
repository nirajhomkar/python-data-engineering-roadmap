"""
=========================================================
Python Data Engineering Roadmap
Day 17 : Abstraction

Topics Covered:
1. What is Abstraction
2. Abstract Base Class (ABC)
3. @abstractmethod
4. Abstract Class Rules
5. Vehicle Example
6. Employee Management Mini Project
7. Abstract Class with Normal Method

Author : Niraj Homkar
=========================================================
"""

from abc import ABC, abstractmethod

# =========================================================
# Program 1 : Basic Abstract Class
# =========================================================

print("=" * 50)
print("Program 1 : Basic Abstract Class")
print("=" * 50)


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car Started")


car = Car()
car.start()


# =========================================================
# Program 2 : Employee Management System
# =========================================================

print("\n" + "=" * 50)
print("Program 2 : Employee Management System")
print("=" * 50)


class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):

    def calculate_salary(self):
        print("Salary : 50000")


class PartTimeEmployee(Employee):

    def calculate_salary(self):
        print("Salary : 20000")


full = FullTimeEmployee()
part = PartTimeEmployee()

full.calculate_salary()
part.calculate_salary()


# =========================================================
# Program 3 : Abstract Class with Normal Method
# =========================================================

print("\n" + "=" * 50)
print("Program 3 : Abstract Class with Normal Method")
print("=" * 50)


class Animal(ABC):

    def eat(self):
        print("Eating")

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")


dog = Dog()

dog.eat()
dog.sound()

print("\n Day 17 Completed Successfully!")