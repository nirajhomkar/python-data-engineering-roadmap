"""
Day 12 - Exception Handling

Author: Niraj Homkar

Topics Covered:
1. try
2. except
3. Multiple except
4. else
5. finally
6. raise
"""

# ==========================================
# Program 1 : Basic Exception Handling
# ==========================================

print("=" * 50)
print("Program 1 : Basic Exception Handling")
print("=" * 50)

try:
    num = int(input("Enter a number: "))
    print("Result :", 100 / num)

except:
    print("Something went wrong!")

print("Program Ended")


# ==========================================
# Program 2 : Multiple Exceptions
# ==========================================

print("\n" + "=" * 50)
print("Program 2 : Multiple Exception Handling")
print("=" * 50)

try:
    num = int(input("Enter another number: "))
    print("Result :", 100 / num)

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Please enter only numbers.")

else:
    print("Everything executed successfully!")

finally:
    print("Finally block executed.")

print("Program Ended")


# ==========================================
# Program 3 : Raise Exception
# ==========================================

print("\n" + "=" * 50)
print("Program 3 : Raise Exception")
print("=" * 50)

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise ValueError("Age must be at least 18.")

    print("Account Created Successfully")

except ValueError as e:
    print(e)

finally:
    print("Thank you for using our application.")

print("Program Ended")


# ==========================================
# Day Completed
# ==========================================

print("\nCongratulations! Day 12 Completed Successfully!")