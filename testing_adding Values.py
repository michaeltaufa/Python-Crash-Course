# For this program, we will be focused on adding values in lists, dictionaries, and classes.
    # This program has been created by Michael Taufa.


favoriteFoods = []


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def format_carName(self):
        formatted_carName = f"{self.year} {self.make} {self.model}"

        return formatted_carName.title()


def build_userProfile(firstName, lastName, age, location):
    userInfo = {}

    userInfo['first name'] = firstName
    userInfo['last name'] = lastName
    userInfo['age'] = age 
    userInfo['location'] = location 

    return userInfo


print("\nWelcome to the the 'Add Values' program!")

user_name = input("Enter and type your name: ")
user_name = str(user_name)

program_status = True

while program_status:

    user_carMake = input(f"\nFirst, {user_name.title()} what is the make of your car: ")
    user_carModel = input(f"{user_name.title()}, enter what is the model of your car: ")
    user_carYear = input("Lastly, what is the year of you car: ")

    user_car = Car(user_carMake, user_carModel, user_carYear)
    confirm_userCar = user_car.format_carName()

    print(f"This is your vehicle: {confirm_userCar}")

    user_verification = input(f"{user_name.title()}, enter Yes (y) or No (n) if this is correct: ")

    if user_verification == 'y':
        program_status = False
    else:
        program_status = True


print(f"\n{user_name.title()}, now we are going to collect a list of your favorite foods!")

program_status = True

while program_status:
    user_favoriteFood = input(f"{user_name.title()}, enter and type your favorite food: ")

    favoriteFoods.append(user_favoriteFood)

    print("\nHere is the list of your favorite foods:")
    for food in favoriteFoods:
        print(f" -{food.title()}")


    # Reusing 'user_verification'
    user_verification = input(f"\nDid you want to add more foods, enter Yes (y) or No (n): ")

    if user_verification == 'y':
        program_status = True 
    else:
        program_status = False 


print(f"\n{user_name.title()}, now we are going to create a user profile!")


program_status = True

while program_status:
    user_firstName = user_name

    user_lastName = input("We already have your first name.\nEnter your last name: ")
    user_age = input("Gotchu, how old are you: ")
    user_location = input("Lastly, where are you located: ")

    print(build_userProfile(user_firstName, user_lastName, user_age, user_location))

    program_status = False


print("\nThis is the end of the program.")
