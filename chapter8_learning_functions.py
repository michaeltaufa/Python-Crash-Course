# For this program, we will focus on learning functions
    # This program has been created Michael Taufa.

# SECTION - Defining a Function:


# Below is defining a function:
    # 'def' will create Function
        # 'greet_user' will be the name to create functions
        # Indentation:
            # All lines of codes in functions will be part of the functions
            # Similar to 'if statements' and 'while loops'

def greet_user():
    """Display a simple greeting."""
    print("\nHello! Welcome to the 'Chapter 8' Defining Functions Program.")

# Called function and passed no argument to function
greet_user()


def greet_usernames(username):

    username = str(username)
    # str() will prevent errors when using method: .title()

    print(f"Hello {username.title()}!")

    # print(username + username)
        # Created to test 'username' if variable is converted to string

greet_usernames('tom')
greet_usernames('sara')
greet_usernames(19)


# SECTION - Arguments (Positional Arguments)
    # Keyword: Positional
        # Arguments are based on 'order of arguments'

def describe_pet(animal_type, pet_name):
    animal_type = str(animal_type)
    pet_name = str(pet_name)

    print(f"\nI have a {animal_type.title()}.")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}.")

describe_pet('lucky', 'dog')
describe_pet('dog', 'lucky')

# Practice using input() and pass arguments into functions
    # SUCCESS! - You can pass arguements of other variables into function

user_animalType = input(f"\nWhat type of pet do you have: ")
user_petName = input(f"Enter your pet's name: ")

describe_pet(user_animalType, user_petName)

# Practice using input() and pass arguments into functions and while loops
    # SUCCESS - Using functions in a while loop creates smaller blocks of code

pet_programStatus = True

while pet_programStatus:

    user_animalType = input(f"\nWhat type of pet do you have: ")
    user_petName = input(f"Enter your pet's name: ")

    describe_pet(user_animalType, user_petName)

    repeatProgram = input("\nDo you want to continue, press 'y' or 'n': ")

    if repeatProgram == 'n':
        pet_programStatus = False

# SECTION - Arguments (Keyword Arguments)
    # Keyword: 'Keyword' 
        # Regardless of order of arguments passed in functions
        # IMPORTANT: define argument in function

# NOTE: Use correct parameters and define with arguments
    # Order does NOT matter IF keywords are used.

describe_pet(animal_type = 'cat', pet_name = 'tom')
describe_pet(pet_name = 'lookiez', animal_type = 'owl')


# SECTION - 














