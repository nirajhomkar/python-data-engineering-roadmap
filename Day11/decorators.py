"""
Day 11 - Decorators

Author: Niraj Homkar

Topics Covered:
1. Introduction to Decorators
2. Creating a Decorator
3. Timer Decorator
4. Login Required Decorator
"""

import time

# ----------------------------------------
# Decorator 1 : Program Started
# ----------------------------------------

print("=" * 50)
print("Decorator 1 : Program Started")
print("=" * 50)


def start_program(func):

    def inner():
        print("Program Started")
        func()

    return inner


@start_program
def greet():
    print("Hello Niraj")


greet()

# ----------------------------------------
# Decorator 2 : Timer
# ----------------------------------------

print("\n" + "=" * 50)
print("Decorator 2 : Timer")
print("=" * 50)


def timer(func):

    def inner():
        print("Function Started...")

        start = time.time()

        func()

        end = time.time()

        print(f"Execution Time : {end - start:.6f} seconds")
        print("Function Finished")

    return inner


@timer
def calculation():

    total = 0

    for i in range(1000000):
        total += i

    print("Calculation Completed")


calculation()

# ----------------------------------------
# Decorator 3 : Login Required
# ----------------------------------------

print("\n" + "=" * 50)
print("Decorator 3 : Login Required")
print("=" * 50)

logged_in = False


def login_required(func):

    def inner():

        if logged_in:
            func()
        else:
            print("Please Login First")

    return inner


@login_required
def view_balance():
    print("Your Balance is ₹50,000")


view_balance()

# ----------------------------------------
# Login Successful
# ----------------------------------------

print("\nChanging Login Status...\n")

logged_in = True

view_balance()

print("\nDay 11 Completed Successfully!")