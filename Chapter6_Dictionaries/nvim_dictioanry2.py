# For this program, we will be learning more detail about dictionaries.

print("\nThis is the start of the program: Chapter 5 - Dictionary.")

# Let's first create a dictionary!
print("\nFirst, we are going to print the values for 'souls_monster':")
souls_monster = {'color': 'green', 'point': 5}
print(souls_monster['color'])
print(souls_monster['point'])

# Next, we are going to modify values.
print("\nNow, lets modify values for dictionary.\n")
print(f"\nThe color of the 'souls_monster' is {souls_monster['color'].title()}.")
souls_monster['color'] = 'red' 
print(f"\nThe new color of the 'souls_monster' is {souls_monster['color'].title()}.")
souls_monster['color'] = 'green'

# Now, we are going to do the following:
    # 1. Add new values to the dictionary
    # 2. Modify values to the dictionary by creating a 'if statement'

souls_monster['x_position'] = 0
souls_monster['y_position'] = 25
souls_monster['movement_class'] = 'medium'

print("\nLet's print out the new following values that was added:\n")
print(f"The 'x_position' value is {souls_monster['x_position']}.")
print(f"The 'y_position' value is {souls_monster['y_position']}.")
print(f"The class value is {souls_monster['movement_class']}.")

if souls_monster['movement_class'] == 'slow':
    x_increment = 1
    souls_monster['color'] = 'blue'
elif souls_monster['movement_class'] == 'medium':
    x_increment = 2
    souls_monster['color'] = 'yellow'
elif souls_monster['movement_class'] == 'fast':
    x_increment = 3
    souls_monster['color'] = 'flashing red'

# IMPORTANT: Store new value by redeclaring position.
souls_monster['x_position'] = souls_monster['x_position'] + x_increment

print(f"\nWatch out! The monster's color is {souls_monster['color'].title()}!")
print(f"Souls Monster's new position is {souls_monster['x_position']}.\n")


# Lets build a dictionary with similar objects.
    # BONUS: We are going to attempt to conduct a poll system.

favorite_programming_languages = {
        'michael': 'python',
        'jen': 'javascript',
        'alex': 'C',
        'john': 'C++',
        'tom': 'C++',
        'sam': 'javascript',
        'khan': 'javascript',
        'edward': 'C',
        'sarah': 'javascript',
        'kim': 'python',
        'phil': 'java',
        'mike': 'java',
        }

tom_langauge = favorite_programming_languages['tom'].title()
print(f"Tom's favorite programming language is {tom_langauge}.\n")

sarah_language = favorite_programming_languages['sarah'].title()
print(f"Sara's favorite programming language is {sarah_language}.\n")

print("\nThis is the start for 'loop' through a dictionary.\n")
print(favorite_programming_languages)

# For this section, let's focus on looping dictionaries.
    # When creating a 'for loop', you will need to have (2) variables to acces 'key' and 'value'
    # Let's first focus on creating a 'for loop' for a previous dictionary that was declared.
    # For this example, we will use the method 'items()'

print("\nHere is the output for looping through a dictionary:\n")
for name, language in favorite_programming_languages.items():
    print(f"Hello, my name is {name.title()} and my favorite programming language is {language.title()}.")

# Next, we will focus on using the method 'key()' to focus on grabbing the values ONLY for the key:
    # Using (1) variavble in a 'for loop' will be the default to grabbing 'keys' value.

print("\nHere is the output for looping through a dictionary for 'keys':\n")

for name in favorite_programming_languages.keys():
    print(f"The following is the value for 'key': {name.title()}.")

# For this next example, we will compare a Dictionary with a List:
    # Remember the fundamentals, declare main variable used for both dictionary and list.


print("\nHere is the output for looping through a dictionary while comparing to a list.\n")

best_friends = ['mike', 'khan']
for name in favorite_programming_languages.keys():
    print(f"Hello {name.title()}!")

    if name in best_friends:
        # When grabbing a 'key value', redeclare dictionary with same variable used in 'for loop'
        language = favorite_programming_languages[name].title()
        print(f"One of my best friends is {name.title()}! Are you still programming in {language}?")

# For this next section, I'm going to focus on looping through a dictionary key's in order.
    # Let's test to see the 'sorted()' function executed.

print("\nThis section of the program is focused on sorted 'keys' in a dictionary.\n")

favorite_souls_games = {
        'michael': 'elden ring',
        'jacob': 'bloodborne',
        'sarah': 'bloodborne',
        'tom': 'dark souls',
        'caitlyn': 'dark souls 2',
        }

# IMPORTANT: For functions such as sorted(), you can insert dictionary + method.

for name, game in sorted(favorite_souls_games.items()):
    print(f"{name.title()} : {game.title()}")

# For this section, we will focus on accessing the 'Values' in a dictioanry:

print("\nFor this next section, I will focus on accessing 'Values'.\n")

for game in favorite_souls_games.values():
    print(f"{game.title()}")

print("Now, let's practice sorting 'Values' from a dictionary.\n")

print("Let's print out all the Fromsoftware Games:\n")
for game in sorted(favorite_souls_games.values()):
    print(f"{game.title()}.")

# Now let's try using the 'set()' function to prevent duplicates:
    # Use the dictionary: favorite_programming_languages

print(f"\nFor this section, we are prevent duplicates using 'set()\n")

for language in sorted(set(favorite_programming_languages.values())):
    print(f"{language.title()}")

# Nesting:
    # For this section, we will focus on nesting dictionaries, list, and etc.
    # First, we will create a list and nest a dictionary.

print("\nFor this section, we will focus on nesting dictionaries in a list:\n")

alien_0 = {'color': 'green', 'points': 5, 'speed': 'slow'}
alien_1 = {'color': 'yellow', 'points': 10, 'speed': 'medium'}
alien_2 = {'color': 'red', 'points': 15, 'speed': 'fast'}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print("\nFor this next section, we will experiment appending a list with a dictionary:\n")

# Create an empty list:
bears = []

# Make 10 bears:
    # Use the range() function:

for new_bears in range(10):
    new_bears = {'color': 'brown', 'points': 5, 'speed': 'slow'}
    bears.append(new_bears)

# Check work:
    # Print all elements in the list and print the length of the list.

for yellow_bear in bears[0:3]:
    if yellow_bear['color'] == 'brown':
        yellow_bear['color'] = 'yellow'
        yellow_bear['points'] = 10
        yellow_bear['speed'] = 'medium'
    elif yellow_bear['color'] == 'yellow':
        yellow_bear['color'] = 'red'
        yellow_bear['points'] = 15
        yellow_bear['speed'] = 'fast'

for bear in bears:
    print(bear)

print(f"\nThe length of the list is {len(bears)}.\n")

print("\nFor the next section, we will focus on building a list in a dictionary.\n")

pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese']
        }

print(f"You ordered a '{pizza['crust'].title()}' crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(topping.title())

favorite_video_games = {
        'michael': ['dark souls remastered', 'elden ring', 'orcarina of time'],
        'jen': ['orcarina of time'],
        'kim': ['call of duty'],
        'john': ['dark souls remastered', 'elden ring']
        }
# IMPORTANT: When printing lists within dictionary with 'title()' function:
    # Use (2) variables to access 'Values' and then 'Lists'

for name, games in favorite_video_games.items():
    print(f"{name.title()} favorite games is the following:")
    for game in games:
        print(f"\t{game.title()}")

