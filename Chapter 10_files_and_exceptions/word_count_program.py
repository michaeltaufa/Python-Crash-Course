"""
Program Name: Word Count Program
Description:
This program will be focused on working with multiple files in reading and 
analyzing the content.
Name: Michael Taufa
Date: 2025-04-04
"""

from pathlib import Path

def count_words(path):
    try:
        contents = path.read_text(encoding = 'utf-8')

    except FileNotFoundError:
        print(f"File {path} does not exist.")

    else:
        words = contents.split()
        number_words = len(words)
        print(f"The file {path} was about {number_words} words.")

# path = Path('alice.txt')
# count_words(path)

filenames = ['alice.txt', 'little_women.txt', 'moby_dick.txt', 'siddhartha.txt', 'resident_evil4.txt']

for filename in filenames:
    path = Path(filename)
    count_words(path)
