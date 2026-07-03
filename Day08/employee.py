"""
Day 8 - Modules

Author: Niraj Homkar

Employee Module
"""


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"{self.name} earns ₹{self.salary}")