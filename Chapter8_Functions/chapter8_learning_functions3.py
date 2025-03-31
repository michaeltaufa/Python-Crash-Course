# This program is a continued version of 'Learning Functions'.
    # This program has been created by Michael Taufa.

# SECTION - Passing a List:
    # Passing a list into a function will be needed depending on the needs

def greet_users(names):

    # When passing in 'lists', make sure parameters match
    for name in names:

        name = str(name) # This is added to ensure all values in a list will be stringify
        message = f"Hello, {name.title()}"

        print(message)

userNames = ['hannah', 'ty', 'margot', 5, 100, 1000, 'john']

greet_users(userNames)


print("\nThis is the start of the program: 'Modifying List'")

# SECTION - Modifying a List
    # When modifying a list, you can use a 'while loop', but we can also
    # reorganize into (2) functions
        # NOTE: When modufiying lists, remember .pop() and .append()

def approving_VideoGame_orders (pendingOrders, completedOrders):
    print("\nTransfering pending orders to completed orders.")

    while pendingOrders:
        videoGame_transfer = pendingOrders.pop()
        completedOrders.append(videoGame_transfer)
        print(f"{videoGame_transfer.title()} has been approved.")

def validate_VideoGame_orders(completedOrders):
    print("\nTransfering pending orders to completed orders.")
    
    for order in completedOrders:
        message = f"{order.title()} is completed."
        print(message)

pending_VideoGame_orders = ['john smith', 'tom johnsons', 'juan hernandez']
completed_VideoGames_orders = []

approving_VideoGame_orders(pending_VideoGame_orders, completed_VideoGames_orders)
validate_VideoGame_orders(completed_VideoGames_orders)

# SECTION - Preventing a Function from modifying a list
    # To prevent a function from modifying a list,
    # Use the 'slice function' to "send a copy of the list"
        # EXAMPLE: function_name(list_name[:])

# SECTION -  Passing Arbitary Number of Arguments
    # There will be instances when you won't know 
    # how many arguments will be passed into a function
    # When calling a function, use *argument as a parameter

print("\nThis section of the program is 'Passing Arbitary Number of Arguments': ")

def make_pizza(*toppings): 

#NOTE: *toppings will create a tuple, whether it has 1 value or 10 values
    print("\nNow adding the following pizza toppings: ")
    for topping in toppings:
        print(f"- {topping.title()}")

make_pizza('green peppers')
make_pizza('pepperoni', 'extra cheese', 'mushrooms')

# SECTION - Mixing Positional and Arbitrary Arguments
    # When adding mixture of arguments and parameters
    # Arbitary arguments will be last, "Think... collect left overs"

print("\nThis section of the program is 'Mixing Positional and Arbitary Arguments': ")

def creating_pizza(size, *toppings):
    print(f"The {size} inch pizza with the following toppings: ")

    for topping in toppings:
        print(f"- {topping.title()}")

creating_pizza(12, 'mushrooms', 'italian sausage')
creating_pizza(16, 'pepperoni', 'cheese', 'pineapples')


# SECTION - Using Arbitrary Keywood Arguments
    # Using 'Arbitrary Arguments' will help build key-value dictionary values
    # when there are unexpected arguments passed into the function

print("\nThis section of the program is 'Keyword Arbitary Arguments': ")

def build_profile(first_Name, last_Name, **userInfo):
    # userInfo = {}    < ---- NOTE: IMPORTANT

    # Adding this will not allow 'Arbitrary Keywood' values to append to object

    userInfo['first name'] = first_Name
    userInfo['last name'] = last_Name
    
    # 'return' statement will allow function to return value and store in variable...
    # IF assigned to a variable intially before calling function
    return userInfo

user_profile1 = build_profile('john', 'smith', age = 5, location = 'USA')
user_profile2 = build_profile('sam', 'sliderz', hobby = 'exercise', color = 'green')

print(user_profile1)
print(user_profile2)
