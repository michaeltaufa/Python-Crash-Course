"""
Program: Number Writer JSON
Description:
    This program will be focused on storing data in JSON files and
    learn how to use the JSON module.
Name: Michael Taufa
Date: 2025-04-10
"""

from pathlib import Path
import json


"""
REMEMBER: P.I.C.
    P - Path
        * Create a pathway for a file
    I - Intialize
        * Intialize content using json.dumps() or json.loads()
    C - Commit
        * Commit to writing into a file or console/ print()
"""


numbers = [1, 3, 5, 7, 9, 11]

# NOTE: Always establish a path to file/ create a file
path = Path('numbers.json')

# NOTE: Intialize variable and use json function, json.dumps() and pass
    # data/ argument into function
content = json.dumps(numbers)

# NOTE: Lastly, write text to the path and pass content into function
path.write_text(content)
