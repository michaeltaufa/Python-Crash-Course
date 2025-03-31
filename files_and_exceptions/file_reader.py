"""
Program: Read contents of file
Description:
    Program will read contents of a file.
Name: Michael Taufa
Date: 2025-03-31
"""
    # NOTE:
        # 'Path' could be the following:
            # 1. A function from a module
            # 2. A class from a class module
        # 'pathlib' is the module that is being imported to this file

from pathlib import Path


file_path = Path('testing_random_content.txt')
# NOTE: Intialize a variable to Path() and add file

contents = file_path.read_text().rstrip()
# NOTE: Intialize a variable 'contents' to variable 'path' and add method 'read_text()'

print(f"This this the following contents printed from the file: '{file_path}':\n")

# NOTE: LASTLY, print() contents from the file
print(contents)

print("\nThis is the end of the program.")
