"""
Program Name: Testing a Function (Names.py)
Description: This program will be focused on importing the module:
    'name_function.py' and building a program to practice building
    unit testing.
Name: Michael Taufa
Date: 2025-04-18
"""
from pathlib import Path
import json
from name_function import get_formatted_name

path = Path('names_data.json')

usernames_list = []


print("\nWelcome to the 'names.py Program'!\nType and enter 'q' to end the program.")
while True:
    user_firstName = input("Enter your first name: ")
    if user_firstName == 'q':
        break

    user_lastName = input("Enter your last name: ")
    if user_lastName == 'q':
        break

    formatted_name = get_formatted_name(user_firstName, user_lastName)
    usernames_list.append(formatted_name)

    username_content = json.dumps(usernames_list)
    path.write_text(username_content)

    print(f"Formatted name: {formatted_name} has been added.")
    print("\nNew Round: ")



