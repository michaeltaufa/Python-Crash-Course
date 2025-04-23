"""
Program Name: Test Employee Class 
Description: Program to test 'employee_class'
Name: Michael Taufa
Date: 2025-04-23
"""
import pytest
from employee_class import Employee


# NOTE: When creating and using fixtures:
    # Main Point is to create an instance through a Class
    # Pass instance as an argument in each test
    # Overall, this will help test larger projects with larger scale tests

@pytest.fixture
def supervisor_employee():
    supervisor_employee = Employee('john', 'martinez', 10_000)
    return supervisor_employee



def test_give_default_raise(supervisor_employee):
    test_salary = supervisor_employee.give_raise()
    assert test_salary == print(f"Your new salary is 10000.")


def test_give_custom_raise(supervisor_employee):
    test_salary_employee2 = supervisor_employee.give_raise(3_000)
    assert test_salary_employee2 == print(f"Your new salary is 8000.")
