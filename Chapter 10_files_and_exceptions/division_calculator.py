"""
Program: Exceptions
Description:
This program will be focused on learning Python's special object, 'exceptions', where
I will write 'exceptions through try-except block' to handle errors in a Python program 
and continue to execute the program.
Name: Michael Taufa
Date: 2025-04-02
"""

print("\nStart of program.")

# SECTION - Handling the 'ZeroDivisionError' Exeception
    # For this section, we will execute the following: 'print(5/0)'
    # NOTE: For math, it is impossible to divide by 0

    # NOTE: When executing, the program receieved an error and return a traceback of the error
    # print(5/0)

# IMPORTANT: 'try-except blocks' is able to execute program 
# and handle errors that may occur

try:
    print(5/0)
except ZeroDivisionError:
    print("You cannot divide by 0.")






print("\nEnd of program.")
