"""
Program Name: Testing a Function (name_function.py)
Description: This program will be focused on importing the module:
    'name_function.py' and building a program to practice building
    unit testing.
Name: Michael Taufa
Date: 2025-04-18
"""

from name_function import get_formatted_name

def test_first_last_name():
    # NOTE: Declare variable and intialize function, pass argumentments
    test_format_name = get_formatted_name('michael', 'taufa')

    # NOTE: 'assert' will be the FINAL ANSWER function is testing for
    # The assertion will be that 'test_first_last_name' will == 'Michael Taufa'.
    
    assert test_format_name == 'Michael Taufa'

def test_first_middle_last():
    test_format_middle_name = get_formatted_name('monkey', 'luffy', 'dragon')
    assert test_format_middle_name == 'Monkey Dragon Luffy'

