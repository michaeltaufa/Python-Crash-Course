"""
Program Name: Chapter 10 Exercise 10-14 Verify User
Description:
    Create a 'remember_me.py' program that will get the user name.
    Modify the program to make sure the following:
        1. Old Username, print() welcome back
        2. New username, call New Username
Name: Michael Taufa
Date: 2025-04-17
"""

from pathlib import Path
import json


path = Path('FINAL_exercise10.14_verifyUser.json')

if path.exists():
    content = path.read_text()
    content_username = json.loads(content)

    print(f"Welcome back '{content_username}'.\nYou information was extracted successfully from '{path}'!")

else:
    print("Welcome to Exercise 10-14 Verify User Program.")

    username = input("Enter your username: ")
    content = json.dumps(username)
    path.write_text(content)
    print(f"'{content}' has been added to '{path}'.")
