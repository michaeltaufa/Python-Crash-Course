# For this program, we will complete exercises 7-8, 7-9, and 7-10.
    # This program has been created by Michael Taufa.

# SECTION - 7-8: Deli
    # Create a list called 'sandwich_order' and fill it with names of various sandwich-orders
    # Create an EMPTY LIST called 'finished_sandwichOrders'
        # Loop through list of sandwich order and print() = 'I made ....'
    # Move 'orders' to 'sandwiches_made'
        # print() = 'Order is complete...'

print("\nThis is the start of SECTION 7-8 Deli:")


sandwich_orders = ['tuna', 'marinara meatball', 'grilled cheese', 'vegetarian', 'roast beef']
finished_sandwichOrders = []


print("\nBelow is the current orders of sandwiches: ")
print(sandwich_orders)

print("\nBelow is the complete orders of sandwiches: ")
print(finished_sandwichOrders)

print("----------------------------")

while sandwich_orders:
    fillingOrder = sandwich_orders.pop()

    print(f"{fillingOrder.title()} is being made.")

    finished_sandwichOrders.append(fillingOrder)


print("\nBelow is the current orders of sandwiches: ")
print(sandwich_orders)

print("\nBelow is the complete orders of sandwiches: ")
print(finished_sandwichOrders)


# SECTION - 7-9: No Pastrami
   # Usign the list 'sandwich_orders', add 'pastrami' several times in the order.
   # Add code in beginning of program
   # print() = "There are no more pastrami lefts in the Deli
   # use 'while loop' to remove all instances
   # print() complete orders with NO PASTRAMI


print("\nThis is the start of SECTION 7-9 Pastrami:")

NewSandwich_orders = ['pastrami', 'tuna', 'marinara meatball','pastrami', 'grilled cheese', 'pastrami', 'vegetarian', 'roast beef']
NewFinished_sandwichOrders = []

print(f"\nHere is the current orders for sandwiches: {NewSandwich_orders}")
print(f"Here is the completed orders for sandwiches: {NewFinished_sandwichOrders}")

if 'pastrami' in NewSandwich_orders: 
    print("\nI am sorry, there is no more pastrami. Pastrami is not available at this time.\n")

    while 'pastrami' in NewSandwich_orders:
        NewSandwich_orders.remove('pastrami')

print("\nAll 'pastrami' orders have been removed.\n")

while NewSandwich_orders:

    # NewSandwich_orders.remove('pastrami')
        # NOTE:
            # There can be a bug placing a .remove() and .pop() next to each other
            # This can result in value not existing in list.

    fillingOrder = NewSandwich_orders.pop()
    print(f"{fillingOrder.title()} is being made.")

    NewFinished_sandwichOrders.append(fillingOrder)


print(f"\nHere is the current orders for sandwiches: {NewSandwich_orders}")
print(f"Here is the completed orders for sandwiches: {NewFinished_sandwichOrders}")



# SECTION - 7-10: Dream Vacation
    # Create a program that polls users about their dream vacation.
    # Create a block of code that will print out results

print("\nThis is the start of SECTION 7-10 Dream Vacation:")

users_dreamVacations = {}

program_dreamVacation_status = True

while program_dreamVacation_status:
    name = input("\nEnter your name: ")
    destination = input(f"\nWelcome {name.title()}, enter your 'Dream Destination' for vacation: ")

    users_dreamVacations[name] = destination

    complete_dreamVacation_status = input(f"\n{name.title()}, do you want to finish the poll? Press 'y' and ENTER: ")

    if complete_dreamVacation_status == 'y':
        program_dreamVacation_status = False

print("\n--------------- Poll Results ------------------")

for name, destination in users_dreamVacations.items():
    print(f"\n{name.title()} would like to go to {destination.title()}.")
















