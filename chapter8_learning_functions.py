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


# SECTION - Return Values
    # 'return' values are assist with large of the grunt work

    #SUB SECTION - 'Optional' Arguments 
        # Functions can be more versatile through integrating optional arguments

def full_name_format (first_name, last_name, middle_name = ''):
    first_name = str(first_name)
    last_name = str(last_name)
    middle_name = str(middle_name)

    if middle_name == '':
        full_name = f"\nYou full name is {first_name.title()} {last_name.title()}."

    else:
        full_name = f"\nYou full name is {first_name.title()} {middle_name.title()} {last_name.title()}."

    return full_name

user_fullName_program = True

while user_fullName_program:
    user_firstName = input("\nWhat is your first name: ")
    user_lastName = input(f"{user_firstName.title()}, what is your last name: ")

    user_middle_verification = input(f"{user_firstName.title()}, do you have a middle name? Enter the following (Yes 'y' or No 'n'): ")

    if user_middle_verification == 'y':
        user_middleName = input("Please enter your middle name: ")

    elif user_middle_verification == 'n':
        user_middleName = ''

    user_fullName_input = full_name_format(user_firstName, user_lastName, user_middleName)
    user_fullName_program = False

print(user_fullName_input)


# SECTION - Returning a 'Dictionay'
    # function() can 'return' any kind of value, including complicated.. 
    # data structures: lists and dictionaries

def build_person (first_name, last_name, age = None):
    person = {'first': first_name, 'last': last_name}

    # 
    if age:
        person['age'] = age
    else:
        person['age'] = None

    return person

# The following below is to test if function would 'add more values to dictionary', but did not.

musician = build_person('jimi', 'hendrix', age = 50)
print(f"Here is the musician dictionary: {musician}")

contentCreator = build_person('prime', 'time')
print(f"Here is the content creator dictionary: {contentCreator}")

athlete = build_person('marshawn', 'lynch', age = 38)
print(f"Here is the athlete dictionary: {athlete}")


