"""
Day 8 - Encapsulation

Author: Niraj Homkar

Topics Covered:
1. Private Variables
2. Deposit
3. Withdraw
4. Getter Method
"""


class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Balance = ₹{self.__balance}")

    def withdraw(self, amount):

        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Balance = ₹{self.__balance}")
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance


account = BankAccount(1500)

print("=" * 40)
print("Bank Account")
print("=" * 40)

account.deposit(500)

account.withdraw(300)

print(f"Current Balance = ₹{account.get_balance()}")

print("\nDay 8 Completed Successfully!")