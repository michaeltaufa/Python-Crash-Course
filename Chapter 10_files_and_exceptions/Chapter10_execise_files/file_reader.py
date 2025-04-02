"""
Program: Read contents of file
Description:
    Program will read contents of a file.
Name: Michael Taufa
Date: 2025-03-31
"""

from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

# SECTION - Accessing a File's line:
    # method() splitlines() will break a long string into individual lines

pi_string = ''

for line in contents.splitlines():
    pi_string += line.lstrip()

print(pi_string[:50])


