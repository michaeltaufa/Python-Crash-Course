# For this program, we will practice nesting the following:
    # 1. Nesting dictionaries in a list
    # 2. Nesting a list in a dictionary
    # 3. Nesting a dictionary in a dictionary

# 1. Nesting dictionaries in a list:
    # 1.1: Create an empty list
    # 1.2: Create 15 dictionaries
    # 1.3: Print out list for each seperate element
    # 1.4: Bonus: Modify dictionaries within the list & print

print("\nThis is the start of the 1st Exercise.\n")

sheeps = []

for sheep in range(15):
    sheep = {'color': 'white', 'points': 5, 'speed': 'slow'}
    sheeps.append(sheep)

for sheep in sheeps:
    print(sheep)

print(f"\nThe number of elements located in 'sheeps' is {len(sheeps)}.\n")

for sheep in sheeps[0:5]:
    if sheep['color'] == 'white':
        sheep['color'] = 'light blue'
        sheep['points'] = 10
        sheep['speed']= 'medium'

for sheep in sheeps:
    print(sheep)

print("\nThis is the end of the 1st Exercise.\n")

# For this exercise, let's focus on nesting a list in a dictionary.
    # 1. Create a dictionary
    # 2. Nest a list in a dictionary

print("This is the start of the 2nd Exercise, 'Nesting List in a Dictionary'.\n")

elden_ring = {
        'rating': 5,
        'genre': 'souls game',
        'boss': ['margit the fell omen', 'starscrourage radahn', 'scarlet rott melania'],
        'price': 60,
        }

for elden_key, elden_values in elden_ring.items():
    print(f"{elden_key.title()}")

for boss in elden_ring['boss']:
    print(f"{boss.title()}")

# There is a difference in 'for loops'
    # For the following below, variable in a for loop to access list only works for dictionary with all lists.

favorite_programming = {
        'michael': ['python'],
        'tom': ['c++', 'c', 'java'],
        'kim': ['lua', 'javascript'],
        'sara': ['javascript']
        }

for name, languages in favorite_programming.items():
    print(f"\n{name.title()}'s favorite language is:")
    for language in languages:
        print(f"{language.title()}")

print("\nThis is the end of the 2nd Exercise.\n")

# For this next section, let's focus on nesting dictionaries in dictionaries.
    # 1. Create a dictioanry
    # 2. Nest 2 -3 dictionaries in a dictionary
    # 3. Print all values

print("\nThis is the start of 3rd Exercise: Nesting Dictionary in a Dictionary.\n")

users = {
        'johnjohn1010': {
            'first_name': 'john',
            'last_name': 'smith',
            'location': 'united states of america'
            },
        'Supersam5k': {
            'first_name': 'sam',
            'last_name': 'dilla',
            'location': 'france'
            }
        }
print(users)
print("\nBelow is reformatted in a 'for loop' to access all values invidivudally.\n")
# REMEMBER: Access information based on data type: 'list', 'dictionary', 'varible':
    # Dictionary: you will need a 'key' and 'value' varaibles
    # List: Need a variable to access list.
        # HINT: Accessing a list, sometimes need to specifiy key
    # Variable: Explicitly use variable or substitue variable to redeclare and access values.

for username, user_information in users.items():
    print(f"{username.title()}:")
    for information_key, information_value in user_information.items():
        print(f"{information_key.title()}: {information_value.title()}")
    print("-----------\n")

print("This is the end of the 3rd Exercise.\n")






