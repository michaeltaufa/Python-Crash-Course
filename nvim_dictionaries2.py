# For this program, we will be focused on learning more on dictionaries on Python.

# When creating dictionary with multiple similar objects, it should be formatted neatly.
    # For dictionary with multple objects that is similar should be formatted in a list.

print("\nThis is the start of the 'for loop' for dictionary.")

favorite_programming_languages = {
        'michael': 'python',
        'sam': 'javascript',
        'tom': 'C++',
        'kelly': 'java',
        'tori': 'C',
        }

# Looping through a 'Dictionary':
    # When creating a 'for loop' variables used is 'key, value'
    # Method: 'items()' will be used to return a list.

for key, value in favorite_programming_languages.items():
    print("\nThis is an object:")
    print("This is the Key: " + key.title())
    print("This is the Value: " + value.title())

print("\nThis is the end of the 'for loop' for dictionary.\n")
