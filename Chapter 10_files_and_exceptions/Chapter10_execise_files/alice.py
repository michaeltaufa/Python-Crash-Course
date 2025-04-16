"""
Program: Alice - Handle Files/ Errors
Description:
For this program, we will learn how to handle "FileNotFoundError" Exceptsions
Name: Michael Taufa
Date: 2025-04-04
"""

from pathlib import Path

print("Program has started.")

path = Path('alice.txt')

try:
    # NOTE: Method 'read_text(), it will default to encoding txt files via 'utf-8'
    # NOTE: Safe method to reading file that require encoding, best practice to specify

    contents = path.read_text(encoding = 'utf-8')

except:
    # NOTE: At the 'except' section, add the ErrorName

    FileNotFoundError
    print(f"Error: The file '{path}' does not exist.")

else:
    words = contents.split()
    number_words = len(words)
    print(f"The file {path} has about {number_words} words.")


print("Program has ended.")
