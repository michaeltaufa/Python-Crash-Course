"""
Program: Exceptions
Description:
This program will be focused on learning Python's special object, 'exceptions', where
I will write 'exceptions through try-except block' to handle errors in a Python program 
and continue to execute the program.
Name: Michael Taufa
Date: 2025-04-02
"""

print("\nStart of program, 'Division Calculator':")

# SECTION - Handling the 'ZeroDivisionError' Exeception
    # For this section, we will execute the following: 'print(5/0)'
    # NOTE: For math, it is impossible to divide by 0

    # NOTE: When executing, the program receieved an error and return a traceback of the error
    # print(5/0)

# IMPORTANT: 'try-except blocks' is able to execute program 
# and handle errors that may occur


print("\nGive me (2) numbers and I will divide them.")
print("To exit the program, type and enter 'q'.")

program_status = True

while program_status:

    number_verification = True
    first_number = input("\nEnter your first number: ")

    while number_verification:
        if first_number == 'q':
            number_verification = False
            program_status = False

        else:

            try:
                first_number = int(first_number)
            except:
                print("You need to enter an integer!")
                first_number = input("Please enter a number: ")
            else:
                print(f"Your first number is {first_number}.")
                number_verification = False

    number_verification = True
    second_number = input("Enter your second number: ")

    while number_verification:
        if second_number == 'q':
            number_verification = False
            program_status = False
        else:

            try:
                second_number = int(second_number)
            except:
                print("You need to enter an integer!")
                second_number = input("Please enter a number: ")
            else:
                print(f"Your second number is {second_number}.")
                number_verification = False

    try:
        answer = (first_number/ second_number)
    except ZeroDivisionError:
        print("Error: You cannot divide by 0.")
    else:
        print(f"\n{first_number} divided by {second_number} is '{int(answer)}'")


    user_continueProgram = input("\n----------\nDo you want to calculate again?\nType and enter Yes (y) or No (n): ")

    if user_continueProgram == 'n':
        program_status = False



print("\nEnd of program.")
