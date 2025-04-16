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

content = path.read_text()
favorite_number = json.loads(content)

print(f"Your favorite number is {favorite_number}.\nThis number was extracted from '{path}'.")
