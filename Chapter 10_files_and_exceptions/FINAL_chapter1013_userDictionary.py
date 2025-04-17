"""
Program Name: Exercise Chapter 10-13: User Dictionary 
Description:
    Create a program that will be asking for 3 pieces of information:
    'username', 'location', 'age'
    Next, store information collected from user into dictionary.
    Write dictionay into a json and print summary of information
Name: Michael Taufa
Date: 2025-04-17
"""

from pathlib import Path
import json

path = Path('userInformation_dictionary.json')


if path.exists():
    content = path.read_text()
    user_content = json.loads(content)

    print(f"\nThis is {user_content['first name'].title()} information:\n")

    for info in user_content.values():
        print(f"{info}")

else:
    print("\nWelcome to Chapter 10-13 User Dictionary!")
    user_name = input("First, what is your name: ")
    user_location = input("Next, where are you from: ")

    user_age = input("Lastly, what is your age: ")
    user_age = int(user_age)

    user = {
            'first name': user_name,
            'location': user_location,
            'age': user_age,
            }

    content = json.dumps(user)
    path.write_text(content)
    print(f"'{path}' has been updated.")

print("End of Program.")
