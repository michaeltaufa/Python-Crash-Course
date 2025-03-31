# For this program, we will be focused on building modules and importing
# to other files.
    # This program has been created Michael Taufa

def build_pizza(size, *toppings):
    print(f"\nBelow is the toppings for the {size}' pizza that is going to be created: ")

    for topping in toppings:
        print(f"- {topping.title()} has been added")

    print("Pizza is complete!")

# SECTION - Create various functions
    # Import specific functions into program

def label_pizza(name, price, location):
    name = str(name)
    location = str(location)
    price = int(price)

    print(f"\n{name.title()}, your pizza cost {price} and will be delivered to {location.title()}.")


def user_pizzaOrder(firstName, lastName, **userInfo):
    userInfo['firstName'] = firstName
    userInfo['lastName'] = lastName

    return userInfo


def user_alcoholOrder(age, firstName, lastName):
    age_eligible = False 

    if age >= 21:
        print(f"\nCongratulations, {firstName.title()} {lastName.title()} you are eligble to order alcohol.")
        age_eligible = True
    else:
        print(f"\nI am sorryy {firstName.title()} {lastName.title()}, but you are not eligble to order alcohol.")

    return age_eligible
