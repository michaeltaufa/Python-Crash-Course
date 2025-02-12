print("\nThis is the start of the 'Dictionary Exercises' Program.\n")

# 6-1 Person:
    # Use a dictionary to store information about a person you know:
        # first_name, last_name, age, city, etc.
        # Print each information seperately

lucky = {'first_name': 'lucky', 'last_name': 'rosete', 'city': 'san jose', 'weight': 12, 'favorite_food': 'chicken nuggets'}

print(f"There is a dog name {lucky['first_name'].title()} {lucky['last_name'].title()}.\n")
print(f"Lucky is from {lucky['city'].title()} and she weighs {lucky['weight']} lbs.\n")
print(f"Lucky's favorite food is {lucky['favorite_food'].title()}.\n")

# 6-2 Favorite Numbers:
    # Create a dictionary with 5 people and their favorite numbers

friends_favoriteNumbers = {
        'michael': 24,
        'john': 7,
        'kathy': 100,
        'sandra': 12,
        'sam': 3,
        'eric': 1,
        }

print(f"Michael's favorite number is {friends_favoriteNumbers['michael']}.\n")
print(f"John's favorite number is {friends_favoriteNumbers['john']}.\n")
print(f"Kathy's favorite number is {friends_favoriteNumbers['kathy']}.\n")
print(f"Sandra's favorite number is {friends_favoriteNumbers['sandra']}.\n")
print(f"Sam's favorite number is {friends_favoriteNumbers['sam']}.\n")
print(f"Eric's favorite number is {friends_favoriteNumbers['eric']}.\n")

# 6-3 Glossary:
    # Think of 5 programming words learned in previous chapters

programming_glossary = {
        'list': 'A list of elements or values stored in a list.',
        'boolean': 'A value that is either true or false.',
        'integer': 'A whole number.',
        'for loop': 'A function that can conduct a function through a loop.',
        'string': 'A string of letters and characters that can be formed in a sentence.'
        }
print(f"List:\n{programming_glossary['list']}\n")
print(f"Boolean:\n{programming_glossary['boolean']}\n")
print(f"Integer:\n{programming_glossary['integer']}\n")
print(f"For Loop:\n{programming_glossary['for loop']}\n")
print(f"String:\n{programming_glossary['string']}\n")

print("This is the end of the 'Dictionary Exercises' Program.\n")
