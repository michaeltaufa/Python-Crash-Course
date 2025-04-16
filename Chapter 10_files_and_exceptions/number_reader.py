"""
Program: Number Reader JSON
Description:
    This program will be focused on reading data in JSON files and
    learn how to use the JSON module.
Name: Michael Taufa
Date: 2025-04-10
"""

from pathlib import Path
import json

path = Path('numbers.json')

"""
REMEMBER: P.I.C.
    P - Path
        * Create a pathway for a file
    I - Intialize
        * Intialize content using json.dumps() or json.loads()
    C - Commit
        * Commit to writing into a file or console/ print()
"""

# NOTE: Intialize content by reading text on "path from the file"
content = path.read_text()

# NOTE: Intialize a variable
    # IMPORTANT - Due to json file, use json.loads() to unpack json file
    # Lastly, pass arugment of the content into function
numbers = json.loads(content)

# NOTE: print() to show work
print(numbers)
