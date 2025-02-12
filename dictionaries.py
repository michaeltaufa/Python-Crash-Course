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

# Adding 'New Values' for dictionary
    # When adding new values ....
    # Call dictionary followed by key-value pairs

print("This is the Dictionary alien_2 before:")
print(alien_2)

alien_2['x_position'] = 0
alien_2['y_position'] = 25

print("This is the Dictionary alien_2 after:")
print(alien_2)

# Starting out with an 'Empty Dictionary'

alien_special = {}

alien_special['color'] = 'rainbow'
alien_special['points'] = 100

print(f"\nLet's see if we can print this new dictionary called alien_special: {alien_special}.\n")

# Modifying values in Dictionaries

print(f"The color of the 'alien_special' is {alien_special['color']}.\n")

alien_special['color'] = 'neon rainbow'

print(f"The NEW color of the 'alien_special' is {alien_special['color']}.\n")

alien_special['color'] = 'rainbow'

# Modifying Values (Continues)
    # Let's  adjust 'alien_special' x poition to move to the right
    # First, build an 'if statement'
        # NOTE:
            # When modifying dictionaries, you can create 'if statements' to modify values.

alien_special['x_position'] = 0
alien_special['y_position'] = 25
alien_special['speed'] = 'slow'

print(f"Before Modifying x_position: {alien_special['x_position']}.\n")

if alien_special['speed'] == 'slow':
    x_increment = 1 
elif alien_special['speed'] == 'medium':
    x_increment = 2
elif alien_special['speed'] == 'fast':
    x_increment = 3

alien_special['x_position'] = alien_special['x_position'] + x_increment

print(f"After Modifying x_position: {alien_special['x_position']}.\n")

# Adding 'Same Objects' in Dictionaries:

favorite_languages ={
        'michael': 'python',
        'jen': 'javascript',
        'scott': 'C',
        'john': 'C++',
        'katie': 'python'
        }

print(f"Michael's favorite programming language is {favorite_languages['michael'].title()}.\n")
