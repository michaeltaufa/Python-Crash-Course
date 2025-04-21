"""
Program Name: Testing a Function (Names.py)
Description: This program will be focused on importing the module:
    'name_function.py' and building a program to practice building
    unit testing.
Name: Michael Taufa
Date: 2025-04-18
"""

from name_function import get_formatted_name

print("\nWelcome to the 'names.py Program'!\nType and enter 'q' to end the program.")
while True:
    user_firstName = input("Enter your first name: ")
    if user_firstName == 'q':
        break

    user_lastName = input("Enter your last name: ")
    if user_lastName == 'q':
        break

    formatted_name = get_formatted_name(user_firstName, user_lastName)
    print(f"Here if your formatted name: {formatted_name}")
    print("\n\nNew Round: ")
