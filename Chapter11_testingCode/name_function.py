"""
Program Name: Testing a Function
Description:
    This program will be a module used to import into the following file:
    'names.py'. 
Name: Michael Taufa
Date: 2025-04-18
"""

def get_formatted_name(first, last, middle = ''):

    if middle:
        full_name = f"{first} {middle} {last}"

    else:
        full_name = f"{first} {last}"

    return full_name.title()
