# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                     
#      Program Name: Alien Boolean Exercise                         
#      Author: Michael Taufa                                          
#      Description: This program will study 'If statements' and dive deeper
#                   into exploring boolean expression, comparison, and more
#                   for testing knowledge on conditional statements.                                                     
#                                                                     
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 5-3, 5-4, 5-5:
    # Create variable = alien_color and assign to color: green, red, yellow
    # Choose another alien and add to if-else chain
    # Create if-elif-else chain with all 3 colors 
    
    
print("\nThis is the start of the 'Alien Boolean' Exercise.\n")

alien_color = 'blue'

if alien_color == 'green':
    score = 5
    print(f"You shot down a '{alien_color.title()} Alien' and earned '{score}' points!\n")
elif alien_color == 'yellow':
    score = 10
    print(f"You shot down a '{alien_color.title()} Alien' and earned '{score}' points!\n")
elif alien_color == 'red':
    score = 15
    print(f"You shot down a '{alien_color.title()} Alien' and earned '{score}' points!\n")
else:
    score = 0
    print(f"You shot the '{alien_color.title()} Alien' and is worth '{score}' points!\n")
    
# 5-6: Stages of Life:
    # Write if-elif-else chain on stages of persons life
        # age = 2: person is a baby
        # age = 2 - 4: person is a toddler
        # age = 4 -13: person is a kid
        # age = 13 - 20: person is a teenager
        # age = 20 - 65: person is an adult
        # age = 65 or older: person is an elderly

print(f"This is the start of the 'Stages of Life' program section.\n")

age = 20

if (age <= 2) and (age > 0):
    stage_life = 'baby'
elif (age >= 3) and (age <= 4):
    stage_life = 'toddler'
elif (age >= 5) and (age <= 13):
    stage_life = 'kid'
elif (age >= 14) and (age <= 20):
    stage_life = 'teenager'
elif (age >= 21) and (age <= 65):
    stage_life = 'adult'
elif (age >= 66):
    stage_life = 'elderly'

print(f"I can see that you are '{age}' years old and considered a '{stage_life}'.\n")

# 5-7: Favorite Fruit
    # Make list of favorite fruits
    # Check if fruits is in your list with seiries of indepenedent statements
     
print(f"This is the start of the 'Favorite Fruit' program section.\n")

favorite_fruits = ['mango', 'apple', 'kiwi', 'blueberry', 'strawberry']

print(f"This is the list of my favorite fruits: {favorite_fruits}.\nLet's check if these fruits is on the list.\n")

if 'mango' in favorite_fruits:
    print("Mango was found in your list of fruits.\n")

if 'apple' in favorite_fruits:
    print("Apple was found in your list of fruits.\n")
    
if 'kiwi' in favorite_fruits:
    print("Kiwi was found in your list of fruits.\n")

if 'blueberry' in favorite_fruits:
    print("Bluerry was found in your list of fruits.\n")

if 'strawberry' in favorite_fruits:
    print("Strawberry was found in your list of fruits.\n")
    
print("This is the end of the 'Favorite Fruit' program section.\n")

