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
