# For this program, we will focus on completing Exercises 6-7 to 6-12:

# Exercise 6-7: People
    # Make (3) Dictionaries representing different people
    # Store all Dictionaries in one list
    # Loop and print all values in Dictionaries
    
print("\nThis is the start of Exercise 6-7: People\n")

michael_smith = {
        'first_name': 'michael',
        'last_name': 'smith',
        'location': 'redwood city',
        }

kim_johnson = {
        'first_name': 'kim',
        'last_name': 'johnson',
        'location': 'san francisco',
        }

tom_einstein = {
        'first_name': 'tom',
        'last_name': 'einstein',
        'location': 'oakland'
        }

people = [michael_smith, kim_johnson, tom_einstein]

for person in people:
    first_name = person['first_name']
    last_name = person['last_name']
    location = person['location']
    print(f"Hello, my name is {first_name.title()} {last_name.title()} and I am from {location.title()}.")

print("\nThis is the end of Exercise 6-7: People\n")


# Exercise 6-8: Pets
    # Make (4) dictionaries representing a different pet
    # Dictionary should include: 'type of animal', 'owner', etc.
    # Store in a list
    # print() all values

print("This is the start of Exercise 6-8: Pets\n")

slow_poke_mike = {
        'type_animal': 'turtle',
        'owner_name': 'sam lokenberg', 
        'pet_name': 'slow poke mike',
        }



johnny_too_fast = {
        'type_animal': 'rabbit',
        'owner_name': 'tim duncan',
        'pet_name': 'johhny too fast',
        }

big_rock = {
        'type_animal': 'cat',
        'owner_name': 'tommy nicks',
        'pet_name': 'big rock',
        }

thunder = {
        'type_animal': 'dog',
        'owner_name': 'nick bloomsberg',
        'pet_name': 'thunder',
        }

pets = [slow_poke_mike, johnny_too_fast, big_rock, thunder]

for pet in pets:
    animal_type = pet['type_animal']
    owner_name = pet['owner_name']
    pet_name = pet['pet_name']
    print(f"{owner_name.title()} has a {animal_type} named {pet_name.title()}.")

print("\nThis is the end of Exercise 6-8: Pets\n")

# Exercise 6-9: Favorite Places
    # Create dictionary called favorite_places
    # Inside the dictionary, add a location and name associated with person
    # Loop through dictionary and print all values
print("This is the start of Exercise 6-9: Favorite Places\n")

favorite_places = {
        'tokyo': 'sara',
        'france': 'nate',
        'spain': 'tom',
        'china': 'tim',
        }
for location, name in favorite_places.items():
    print(f"{name.title()}'s favorite place to visit is {location.title()}.")

print("\nThis is the end of Exercise 6-9: Favorite Places\n")

# Exercise 6-10: Favorite Numbers
    # Create a dictionary of people having a list of favorite Numbers
    # print() all values

print("This is the start of Exercise 6-10: Favorite Numbers\n")

favorite_users_numbers = {
        'michael': [7, 24, 1],
        'tim': [3, 5],
        'kathy': [10],
        'alex': [11, 2, 9],
        'pauline': [1],
        }

for names, numbers in favorite_users_numbers.items():
    print(f"This is the list of {names.title()}'s favorite numbers:")
    print(f"List of numbers: {numbers}\n")

print("\nThis is the end of Exercise 6-10: Favorite Numbers.\n")

# Exercise 6-11: Cities
    # Create a dictionary called 'cities'
    # 'keys' will be the name of the cities
    # Nest a dictionary for each cities for the following: population, country, key fact

print("This is the start of Exercise 6-11: Cities\n")

cities = {
        'san francisco': {
            'country': 'united states of america',
            'population': 100_000,
            'fact': "The Golden Gate Bridge was originally suppose to be painted black and yellow.",
            },
        'paris': {
            'country': 'france',
            'population': 50_000,
            'fact': "There is only 1 stop sign in Paris.",
            },
        'hong kong': {
            'country': 'china',
            'population': 150_000,
            'fact': "Hong Kong has the most skyscrappers than any other cities in the world.",
            }
        }

for city, city_information in cities.items():
    country = city_information['country']
    population = city_information['population']
    fun_fact = city_information['fact']
    print(f"{city.title()} is located in {country.title()} and has a population of {population}.\nHere is a fun fact about {city.title()}: {fun_fact}.\n")

print("This is the end of Exercise 6-11: Cities\n")

# Exercise 6-12: Extensions
    # Recreate the program, Exercise 5-7 Favorite Fruits, and add additional features.
    # Creat a list of (3) favorite Fruits
    # Create an 'if else statement'
    # Add dicitionary features, clean the format of the output.

print("This is the start of Exercise 6-12: Exetensions\n")

favorite_fruits = {
        'apple': {
            'color': 'red',
            'size': 'small',
            'calories': 30
            },
        'mango': {
            'color': 'orange',
            'size': 'medium',
            'calories': 40,
            },
        'watermelon': {
            'color': 'green',
            'size': 'large',
            'calories': 45,
            },
        }

for fruit_name, fruit_information in favorite_fruits.items():
    fruit_color = fruit_information['color']
    fruit_size = fruit_information['size']
    fruit_calories = fruit_information['calories']

    if (fruit_name == 'watermelon'):
        print(f"I am not a fan of {fruit_name.title()} because of the following:\nI don't like how {fruit_name} is the color '{fruit_color}'. Also, the fruit is '{fruit_size}' and has a total amount of '{fruit_calories}' calories.")
    else:
        print(f"I love eating {fruit_name.title()} because they are good!\n")

print("\nThis is the end of Exercise 6-12: Extensions.\nThis is the end of the program.\n")
