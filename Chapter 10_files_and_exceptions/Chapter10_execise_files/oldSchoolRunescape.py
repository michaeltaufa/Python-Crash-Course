"""
Program: Old School Runescape - Skills
Description:
    This program is focused on reading the content of 'oldSchoolRunescape.txt' and
    'oldSchoolRunescape_1string.txt'. Lastly, the goal is to print() the content to 
    display.
Name: Michael Taufa
Date: 2025-04-04
"""
from pathlib import Path

path_oldSchool = Path('oldSchoolRunescape.txt')
path_oldSchool_1string = Path('oldSchoolRunescape_1string.txt')

content_oldSchool = path_oldSchool.read_text()
content_oldSchool_1string = path_oldSchool_1string.read_text()

"""
print("\nThe following content printed is 'oldSchoolRunescape.txt':")
print(content_oldSchool)

print("\nThe following content printed is 'oldSchoolRunescape_1string.txt':")
print(content_oldSchool_1string)
"""


