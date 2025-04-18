"""
Program Name: Chapter 10 Exercise 10-14 Verify User
Description:
    Create a 'remember_me.py' program that will get the user name.
    Modify the program to make sure the following:
        1. Old Username, print() welcome back
        2. New username, call New Username

    Challenge:
        Refactor the following code below to focus on single responsibilites.
        NOTE: Remember to break up code to have specific jobs/ functions

Name: Michael Taufa
Date: 2025-04-17
"""

from pathlib import Path
import json

def get_username(content):
    content = path.read_text()
    content_username = json.loads(content)

    return content_username 

def add_username(username):
    content = json.dumps(username)
    path.write_text(content)
    print(f"'{content}' has been added to '{path}'.")

    return username


path = Path('FINAL_exercise10.14_verifyUser.json')
print("\nWelcome to Exercise 10-14 Verify User Program.")


if path.exists():
    content_username = get_username(path)

    print(f"\nIs your username '{content_username}'?")
    user_verification = input(f"Type and enter Yes (y) or No (n): ")

    if user_verification == 'y':
        print(f"\nWelcome back '{content_username}'.")

    else:
        username = input("Enter your username: ")
        add_username(username)

else:
    username = input("Enter your username: ")
    add_username(username)


print("\nEnd of Program.")
