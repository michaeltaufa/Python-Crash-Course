# For this program, we will be focused on 'Storing Functions in Modules'
    # This program has been created Michael Taufa

# SECTION - Importing an Entire Modules

# import printing_modules
    # COMPLETED
# from printing_modules import greeting_user
    # COMPLETED
# from printing_modules import greeting_user as gusers
    # COMPLETED
# import printing_modules as pm
    # COMPLETED

import printing_modules
from pizza_modules import build_pizza, label_pizza, user_pizzaOrder
    # NOTE: Importing specific functions will not require calling module



# NOTE: When importing modules, spelling is IMPORTANT!
    # This will also impact calling functions as well.

build_pizza(12, 'italian sausage', 'cheese', 'mushrooms')
build_pizza(18, 'pepperoni', 'extra cheese', 'pineapples')

print("\nFor this next section, we will call out other functions from the module.")

label_pizza('michael', 20, 'redwood city')
label_pizza('john', 10, 'fort worth')

user1 = user_pizzaOrder('michael', 'smith', location = 'redwood city', discount = False)
user2 = user_pizzaOrder('john', 'lee', location = 'fort worth', discount = True)

print(user1)
print(user2)


print("\nFor this next section, we will call out other functions from the 'printing_modules'.")

user1 = pm.greeting_user('james', 'conway')

print(user1)
