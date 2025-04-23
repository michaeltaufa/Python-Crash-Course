"""
Program Name: Employee Class
Description:
    This program will be focused on intializing class Employee.
Name: Michael Taufa
Date: 2025-04-23
"""

class Employee:

    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = int(salary)

    def give_raise(self, bonus_salary = 5_000):

        if bonus_salary == 5_000:
            self.salary = 5_000 + self.salary 
        else:
            self.salary = bonus_salary + self.salary

        print(f"Your new salary is {self.salary}.")
