"""
Program: Chapter 10 - Exercise 10-8 and 10-9
Description:
    This progrma is focused on completed exercises 10-8 Cats and Dogs
    and 10-9 Silent Cats and Dogs.
Name: Michael Taufa
Date: 2025-04-08
"""

from pathlib import Path

print("SECTION 10-8 and 10-9 is the start of the program.")

# SECTION 10-8 Cats and Dogs:
    # Create two files: cats.txt and dogs.txt
        # Store at least three names in each files
    # Write a program the prints the contents of each file
    # Wrap code in a 'try, except, else' code block for a 'FileNotFound' error
    # Move the file in different directory to ensure program works correctly

# SECTION 10-9 Silent Cats and Dogs:
    # Modify execept block that will "silently pass" if file is missing.

try:
    path_cat = Path('cats.txt')
    content_cat = path_cat.read_text()

except FileNotFoundError:
    # print(f"Sorry, the file '{path_cat}' was not found.")
    pass 

else:
    print("\nThe following names printed is 'cats.txt':")
    print(content_cat)


try:
    path_dog = Path('dogs.txt')
    content_dog = path_dog.read_text()

except FileNotFoundError:
    # print(f"Sorry, the file '{path_dog}' was not found.")
    pass

else:
    print("\nThe following names printed is 'dogs.txt':")
    print(content_dog)


print("SECTION 10-8 and 10-9 is COMPLETE.")
