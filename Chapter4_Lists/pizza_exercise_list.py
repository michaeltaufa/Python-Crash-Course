# Exercise 4-1:  
    # Think of three kinds of pizzas. Store names in list, use 'for loop' to print each name
favorite_pizza_store = []
favorite_pizza_store.append('papa johns')
favorite_pizza_store.append('pizza hut')
favorite_pizza_store.insert(1,'dominoes')
favorite_pizza_store.append('roundtable')

for pizza_name in favorite_pizza_store:
    print(pizza_name.title())
    

# Modify 'for loop' and print a sentence using    
for pizza_name in favorite_pizza_store:
    print(f"In {pizza_name.title()}, they have great pizza!\n")
    
print("There are a lot of varieties of pizza.")
print("I prefer pepperoni pizza.")
print("The Meatlovers pizza is really good too!\n\n\n")

# Exercise 4-2:
    # Think of a list of animals that have a similar characteristic
    
animals_birds_list = []
animals_birds_list.append('parrot')
animals_birds_list.append('eagle')
animals_birds_list.append('hawk')
animals_birds_list.insert(0, 'falcon')

for bird_name in animals_birds_list:
    print(f"I think {bird_name.title()} would make a great pet!\n")
print("Honestly, all these birds would make a great pet!")