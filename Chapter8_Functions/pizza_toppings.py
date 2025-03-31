# For this program, I will be testing out checking for special values in a list:
    # 1. I will use the 'If Statement' to check for certain values
    # 2. I will check for empty list
    # 3. I will check and compare using 2 different lists in a program.

requested_toppings = ['extra cheese', 'pepperoni', 'mushrooms', 'bell peppers']

print("\nThis is the start of the 'pizza program'.\n")

for requested_topping in requested_toppings:
    if requested_topping == 'bell peppers':
        print("We do not have 'bell peppers'.\n")
    else:
        print(f"Adding the following item: {requested_topping}." ) 

print("Your pizza is completed!\n")
print("This is the end of the 'pizza program'.\n")

# For this segment of the program, we will be checking for empty list.

print("This is the start of the 'Pizza Program: Empty List'.\n")

# Testing the empty list.

customer_requested_toppings = ['apple', 'pears', 'pineapples']

if customer_requested_toppings:
    for toppings in customer_requested_toppings:
        print(f"We have added {toppings}!\n")
else:
    print("The requested toppings is empty!\n")

print("Your pizza is completed!\n")
print("This is the end of the 'Pizza Program: Empty List'.\n")

# For this last segment of the code, we will compare 2 different list!

print("This is the start of the 'Pizza Program: Multiple List'.\n")

dominoes_pizza_toppins = ['pepperoni', 'mushrooms', 'pineapple', 'sausage']
customer_toppings = ['pepperoni', 'pineapple', 'bell peppers']

print(f"This is the toppings Dominoes have available: {dominoes_pizza_toppins}.\n")
print(f"This is the customer toppings: {customer_toppings}.\n")

print("We are building your pizza!\n")

# The biggest lession to takeaway from comparing multiple list is the variable used in a 'for loop'
    # Remember that the variable declared in the 'for loop' will be used to 
    # Compare between the two lists.

for toppings in customer_toppings: 
    if toppings in dominoes_pizza_toppins:
        print(f"{toppings.title()} has been added!")
    else:
        print(f"Sorry, {toppings.title()} is not available.")

print("\nYour pizza is complete!\n")

print("This is the ending of the 'Pizza Program: Multiple List'.\n")
