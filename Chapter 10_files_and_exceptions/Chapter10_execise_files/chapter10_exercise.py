"""
Program: Chapter 10-1 - Learning Python, Chapter 10-2 - Learning C 
Description:
    This program will be focused on executing exercises 10-1 and 10-2
Name: Michael Taufa
Date: 2025-03-31
"""

# SECTION - 10-1: Learning Python
    # 1. Open a blank file and write a few lines summarizing what you've learning in Python
    # 2. Save the file as 'learning_python.txt'
    # 3. Create a program that print() two times:
        # 3.1 - print the content
        # 3.2 - print() storing lines in a list and the looping over each line

# NOTE: Reference 'learning_python.txt'

from pathlib import Path

print("\nThis is Section: 10-1 - Learning Python\n")

path = Path('learning_python.txt')
content = path.read_text()

print("Below is the content printed:")
print(content.rstrip())


print("\nBelow is the content printed in a for loop + splitlines():\n")
lines = content.splitlines()
content_strip = ''

for line in lines:
    content_strip += line.lstrip()

print(content_strip)
print(len(content_strip))

# SECTION - 10-2: Learning C
    # Use replace() method to replace any word ina  string with a different word.
    # Use replace() method and replace 'Python' to 'C'

print("\nThis is Section: 10-2 - Learning C\n")

print("The following below is the content with 'Python' is being replace with 'C':\n")
print(content.replace('Python', 'C'))









