"""
Program: Notes Manager
Description:
    Create a script that allows users to create and read text notes stored in a directory.
Name: Michael Taufa
Date: 2025-04-03
"""

import pathlib

path = pathlib.Path('notes_manager.txt')


print("\nWelcome to the Notes Manager Program!")
user_name = input("Type and enter your name: ")

print(f"\n{user_name.title()}, let begin by creating and writing your notes.")
print("Type and enter 'q' to finish writing your notes.")

user_notes_store = ''

program_status = True 
while program_status:

    user_notes = input("\nType here: ")

    if user_notes == 'q':
        program_status = False

    else:
        user_notes_store += f"{user_notes}\n"
        print("Note has been updated.")
        content_storeNotes = path.write_text(user_notes_store)


content_notesManagerFile = path.read_text()

print("\nYour notes have been added!\nBelow is your notes that you have added:\n")
print(content_notesManagerFile) 
