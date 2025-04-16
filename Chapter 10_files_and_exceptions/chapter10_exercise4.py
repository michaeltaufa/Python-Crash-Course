"""
Program: Chapter 10 - Exercise 10-10 Common Words 
Description:
    Visit 'Project Gutenberg' and find and download a couple texts.
    Use the method count() to find out how manyu times a word or phrase appears
    in a string.

Name: Michael Taufa
Date: 2025-04-08
"""
from pathlib import Path

path = Path('theGreatGatsby.txt')
content = path.read_text()
countWord_the = content.lower().count(' the ')

print(f"\nFile: {path}")
print(f"The approximate count of the word 'the' is {countWord_the}.")



path_oldSchoool = Path('oldSchoolRunescape.txt')
content_oldSchoolRunescape = path_oldSchoool.read_text()
countWord_slayer = content_oldSchoolRunescape.lower().count('slayer')

print(f"\nFile: {path_oldSchoool}")
print(f"The approximate count of the word 'the' is {countWord_slayer}.")
