# This program will be primarily be focused on learning 'Dictionaries' for Python.

print("\nChapter 6: Dictionaries - Program has started.\n")

# Dictionary is a collection of 'key-value' pairs:
    # Syntax: Dictionaies are used with curly braces '{ }'
    # Single Quotes <'  '> are used WITH Colons < : >
    # Values are paired

alien_0 = {'color': 'green', 'points': 5}
print("This is the dictionary value for alien_0:")
print(alien_0['color'].title())
print(alien_0['points'])

print("\nThis is the dictionary value for alien_1:")
alien_1 = {'color': 'yellow', 'points': 10}
print(alien_1['color'])
print(alien_1['points'])

print("\nThis is the dictionary value for alien_2:")
alien_2 = {'color': 'red', 'points': 15}
print(alien_2['color'])
print(alien_2['points'])

print(f"\n\nI am going to access the dictionary: alien_2, where the points is {alien_2['points']} .\n")
