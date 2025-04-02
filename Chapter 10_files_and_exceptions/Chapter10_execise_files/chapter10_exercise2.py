"""
Program: This program will be focused on exercise 10-4 and 10-5.
Description:
    This program will be focused on completing exercise Chapter 10-4 and
    Chapter 10-5.
Name: Michael Taufa
Date: 2025-04-01
"""

import pathlib

# SECTION - Exercise Chapter 10-4: Guest
    # Write a program that prompts the user for their Name
    # When they respond, write their name to a file called 'guest.txt'

print("\nSection is Chapter 10-4 Guest:")

path = pathlib.Path('guest.txt')

# print("\nWelcome to Exercise Chapter 10-4 Guest.")
user_name = input("Type and enter your name: ")
content = path.write_text(user_name)

# print(f"Thank you '{user_name.title()}'. Check 'guest.txt' to check your work. Section 10-4 is completed.")

print("\nSection is Chapter 10-5 Guest Book:")

path_guestBook = pathlib.Path('guest_book.txt')
guest_name_add = ''

print(f"\n{user_name.title()}, type and enter 'quit' to exit the program anytime.")

program_status = True
while program_status:

    print("\nPlease type and enter a guest name to add in 'guest_book.txt'")
    guest_name = input("Enter guest name: ")

    guest_name_add += f"{guest_name}\n" 

    if guest_name == 'quit':
            program_status = False

    else:
        path_guestBook.write_text(guest_name_add)
        print("Guest name has been added.")

    
print(f"\nThank you {user_name.title()}! Check 'guest_book.txt' to check your work. Section 10-5 is completed.")
