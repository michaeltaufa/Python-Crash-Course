"""
Program: Write a Story .txt file
Description:
    This program will be focused on writing as many lines as possible
    on the a text window.
Name: Michael Taufa
Date: 2025-04-01
"""

import pathlib

path = pathlib.Path('write_story.txt')

print("\nWelcome to the 'write a story' program.")
user_name = input("Please enter your name: ")

print(f"{user_name.title()}, quit the program at anytime and type and enter 'quit' to leave.\nBegin to enter your story!")

content = ''


program_status = True
while program_status:

    story_content = input("\nType here: ")

    content += f"{story_content}\n"

    if story_content == 'quit':
        program_status = False
    else:
        print("Content has been added.")
        path.write_text(content)

print("Program is completed. Check you work at 'write_story.txt'")




