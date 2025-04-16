"""
Program Name: Chapter 10 Exercise 10-11 Favorite Number
Description:
    This program will prompt user for their favorite number.
    User json.dumps() to store this number in a file.
    Write a seperate program that reads and prints value
Name: Michael Taufa
Date: 2025-04-16
"""

from pathlib import Path
import json

path = Path('FINAL_exercise10-11.json')

print("Welcome to Exercise 10-11: Favorite Number")

program_status = True
while program_status:

    try:    
        user_favoriteNumber = input("\nWhat is your favorite number: ")
        user_favoriteNumber = int(user_favoriteNumber)

    except ValueError:
        print("Error: Please enter an integer.")

    else:
        print(f"{user_favoriteNumber} has been added to '{path}'.")
        content = json.dumps(user_favoriteNumber)
        path.write_text(content)
        program_status = False

print("Thank you, your favorite number has been added!")
