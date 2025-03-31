# This program will be focused on 'tupple' exercises

buffet_food = ('bbq chicken', 'kbbq shortribs', 'sushi', 'pizza', 'brisket')

print(f"\nThis is the list of food: {buffet_food}.\n")
for food in buffet_food:
    print(f"We are serving {food}.")
print("\n'for loop' is completed.\n")

# Attempt to change value in tupple
# buffet_food[0] = 'vegan chicken'
# print(buffet_food)

buffet_food = ('vegan meat' , 'vegan eggs' , 'vegan fish', 'vegan pork', 'vegan milk')

print(f"\nThis is the new list of food focused on vegan theme: {buffet_food}.\n")
for food in buffet_food:
    print(f"We are serving {food}.")
print("\n'for loop' is completed.\n")