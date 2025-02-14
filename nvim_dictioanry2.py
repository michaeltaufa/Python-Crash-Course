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
