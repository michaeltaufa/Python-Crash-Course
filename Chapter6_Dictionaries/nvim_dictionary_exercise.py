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

# For this next section of the program, we will focus on building more programs through the Exercises provided.

# 6-4: Glossary 2:
    # Create a to print put all the dictionary terms from '6-3 Glosssary' at line 16.

programming_glossary['dictionary'] = 'A collection of information paired through key-values.'
programming_glossary['f string'] = 'A way to concatenate strings with variables.'
programming_glossary['math operations'] = 'Math operations to execute logic through PEMDAS.'
programming_glossary['print function'] = 'A function to print out text.'
programming_glossary['sorted()'] = 'A python built in function to sort out strings in order.'

print("This next section is focused on Exercise: 6-4.\n")

for term, description in sorted(programming_glossary.items()):
    print(f"{term.title()}: {description}.")

# 6-5 Rivers:
    # Make a dictionaty containing three major rivers and the count related to the river.

print("\nThis next section is focused on Exercise 6-5:\n")

river_dictionary = {
        'mississippi': 'united states of america',
        'nile': 'egypt',
        'amazon': 'columbia',
        }

for river, country in river_dictionary.items():
    print(f"The '{river.title()}' river runs through the country: {country.title()}.")

for river in river_dictionary.keys():
    print(f"This is the output of keys: {river.title()}.")

for country in river_dictionary.values():
    print(f"This is the output of values: {country.title()}.")

# 6-6: Polling:
   # Create a list of people WHO should take a 'favorite language poll'
   # Create a seperate list of people who are 'in the list' and 'not in the list'

print("\nThis next section is focused on Exercise 6-6:\n")

favorite_programmingLanguages = {
        'michael': 'python',
        'sara': 'javascript',
        'kim': 'C++',
        'sam': 'python',
        'aaron': 'java',
        }

language_poll_roser = ['michael', 'alex', 'tom', 'kim', 'sam', 'keith', 'aaron']

for name in language_poll_roser:
    if name in favorite_programmingLanguages:
        language = favorite_programmingLanguages[name]
        print(f"{name.title()}, thank you for your participation. You answer was language: {language.title()}.")
    else:
        print(f"{name.title()}, you did not take the poll. You are invited to take the poll.")
