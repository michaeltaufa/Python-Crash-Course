"""
Program Name: Exercise Chapter 10-12: Favorite Number Remembered
Description:
    Combine the two programs from exercise 10-11 Favorite Number.
    If the number is already stored, report the number to user.
    IF NOT, prompt user for favoirte number and store it in file.
    Run program twice to see if it works.
Name: Michael Taufa
Date: 2025-04-17
"""

from pathlib import Path
import json

path = Path('FINAL_chapter10.12_data.json')

if path.exists():
    content = path.read_text()
    favorite_number = json.loads(content)
    print(f"Welcome back! I remember that your favorite number is {favorite_number}.")

else:
    print("Welcome to Exercise Chapter 10-12 Favorite Number Remembered!")

    program_status = True
    while program_status:
            
        try:
            user_favoriteNumber = input("\nEnter your favoirte number: ")
            user_favoriteNumber = int(user_favoriteNumber)

        except ValueError:
            print("Error: Please enter an integer.")

        else:
            content = json.dumps(user_favoriteNumber)
            path.write_text(content) 
            print(f"{user_favoriteNumber} has been added.")
            program_status = False

print("End of Program.")







