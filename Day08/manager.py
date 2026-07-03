"""
Manager Module
"""

from employee import Employee


class Manager(Employee):

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def display(self):
        print(
            f"{self.name} manages a team of "
            f"{self.team_size} and earns ₹{self.salary}"
        )