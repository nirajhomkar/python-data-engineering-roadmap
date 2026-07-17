"""
=========================================================
Python Data Engineering Roadmap
Day 15 : Inheritance

Topics Covered:
1. Parent Class
2. Child Class
3. Inheritance
4. is-a Relationship
5. Constructor in Inheritance
6. super()
7. Method Overriding
8. Vehicle Management Mini Project

Author : Niraj Homkar
=========================================================
"""

# =========================================================
# Program 1 : Basic Inheritance
# =========================================================

print("=" * 50)
print("Program 1 : Basic Inheritance")
print("=" * 50)


class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.bark()


# =========================================================
# Program 2 : Constructor Inheritance using super()
# =========================================================

print("\n" + "=" * 50)
print("Program 2 : Constructor Inheritance")
print("=" * 50)


class Person:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name : {self.name}")


class Student(Person):

    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def student_info(self):
        print(f"Name : {self.name}")
        print(f"Roll No : {self.roll_no}")


student = Student("Niraj", 101)

student.display()
student.student_info()


# =========================================================
# Program 3 : Method Overriding
# =========================================================

print("\n" + "=" * 50)
print("Program 3 : Method Overriding")
print("=" * 50)


class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog barks")


dog = Dog()
dog.sound()


# =========================================================
# Program 4 : Vehicle Management Mini Project
# =========================================================

print("\n" + "=" * 50)
print("Program 4 : Vehicle Management System")
print("=" * 50)


class Vehicle:

    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print(f"Brand : {self.brand}")


class Car(Vehicle):

    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display(self):
        super().display()
        print(f"Model : {self.model}")


car = Car("Toyota", "Fortuner")

car.display()


print("\n Day 15 Completed Successfully!")