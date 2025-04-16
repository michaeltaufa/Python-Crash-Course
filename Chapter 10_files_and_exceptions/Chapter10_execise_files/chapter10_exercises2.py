"""
Program: Chapter 10 - Exercises 10-6 and 10-7 
Description:
    This program is focused on completing execises 10-6 and 10-7.
Name: Michael Taufa
Date: 2025-04-08
"""

# SECTION - 10-6 Addition and 10-7 Addition Calculator:
    # Common problem with prompting is numerical input is when text
    # is provided vs numbers.
        # Create a program that prompts (2) numbers that is needed
        # Add the (2) numbers and print result
        # Create an ValueError is input is not number, print error message
        # Conduct testing for input
        # Wrap program in a while loop

print("\nWeclome to SECTION 10-6: Addition")
user_name = input("Please type and enter your name: ")

print(f"{user_name.title()}, let's start adding!")
program_status = True
number_checkStatus = True
while program_status:

    while number_checkStatus: 
        try:
            user_firstNumber = input(f"Enter your first number: ")
            user_firstNumber = int(user_firstNumber)
        except ValueError:
            print("Error: Input is not an integer.")
        else:
            number_checkStatus = False


    number_checkStatus = True

    while number_checkStatus:
        try:
            user_secondNumber = input(f"Enter your second number: ")
            user_secondNumber = int(user_secondNumber)
        except ValueError:
            print("Error: Input is not an integer.")
        else:
            number_checkStatus = False

    finalAnswer = (user_firstNumber + user_secondNumber)

    print(f"Calculation:\n{user_firstNumber} + {user_secondNumber} = {finalAnswer}")
    print("SECTION 10-6: Addition is COMPLETE")
    program_status = False
