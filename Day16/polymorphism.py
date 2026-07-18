"""
=========================================================
Python Data Engineering Roadmap
Day 16 : Polymorphism

Topics Covered:
1. What is Polymorphism
2. Method Overloading (Python Approach)
3. Duck Typing
4. Operator Overloading
5. Magic (Dunder) Methods
6. Notification System Mini Project

Author : Niraj Homkar
=========================================================
"""

# =========================================================
# Program 1 : Basic Polymorphism
# =========================================================

print("=" * 50)
print("Program 1 : Basic Polymorphism")
print("=" * 50)


class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# =========================================================
# Program 2 : Method Overloading (Python Approach)
# =========================================================

print("\n" + "=" * 50)
print("Program 2 : Method Overloading")
print("=" * 50)


class Calculator:

    def add(self, a, b, c=0):
        return a + b + c


calc = Calculator()

print("Addition of Two Numbers :", calc.add(5, 10))
print("Addition of Three Numbers :", calc.add(5, 10, 15))


# =========================================================
# Program 3 : Duck Typing
# =========================================================

print("\n" + "=" * 50)
print("Program 3 : Duck Typing")
print("=" * 50)


class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


def make_sound(animal):
    animal.sound()


dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)


# =========================================================
# Program 4 : Operator Overloading
# =========================================================

print("\n" + "=" * 50)
print("Program 4 : Operator Overloading")
print("=" * 50)

print("5 + 3 =", 5 + 3)
print("'Hello' + 'World' =", "Hello " + "World")
print("[1, 2] + [3, 4] =", [1, 2] + [3, 4])


# =========================================================
# Program 5 : Notification System (Mini Project)
# =========================================================

print("\n" + "=" * 50)
print("Program 5 : Notification System")
print("=" * 50)


class Notification:

    def send(self):
        print("Sending Notification...")


class Email(Notification):

    def send(self):
        print("Email Sent")


class SMS(Notification):

    def send(self):
        print("SMS Sent")


def notify(service):
    service.send()


email = Email()
sms = SMS()

notify(email)
notify(sms)

print("\n Day 16 Completed Successfully!")