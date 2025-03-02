# For this program, we will add all the Chapter 7 exercises in this program.


# Section 7-1: Rental Car
    # Create a program that ask user what car they are seraching for

user_carPrompt = "\nHello, I notice you are shopping for a car today."
user_carPrompt += "\nPlease type which car you are looking for: "

user_carAnswer = input(user_carPrompt)
print(f"\nLet me see and check if we have a '{user_carAnswer.title()}'.")


# Section 7-2: Restaurant Seating
    # Ask user how many people are in their group
    # If there are more than 8, user will have to wait

user_dinnerGroup = input("\nWelcome to dinner. Enter how many guests are in your group: ")
user_dinnerGroup = int(user_dinnerGroup)

if user_dinnerGroup >= 8:
    print("\nSorry, we do not have a table available at this time.")
else:
    print("\nPlease follow me, I will escort you to your table.")

# Section 7-3: Multiple of Ten
    # Ask the user for a number
    # Check number if it is a multiple of 10

user_numberPrompt = input("\nPlease enter a number to check if it is a multiple of 10: ")

user_numberPrompt = int(user_numberPrompt)

if user_numberPrompt % 10 == 0:
    print(f"\n{user_numberPrompt} is a multiple of 10!")
else:
    print(f"\n{user_numberPrompt} is NOT a multiple of 10.")


# Section 7-4: Pizza Toppings
    # Write a loop that prompts the user to enter series of pizza Toppings
    # Print out all pizza Toppings
    # Add a 'quit' prompt to exit while loop


user_pizzaToppingsPrompt = "\nType and enter a pizza topping."
user_pizzaToppingsPrompt += "\nIf you are done, enter 'quit' when you are finished: "

pizza_programStatus = True

while pizza_programStatus:

    pizzaPrompt = input(user_pizzaToppingsPrompt)

    if pizzaPrompt == 'quit':
        break
    else:
        print(f"{pizzaPrompt.title()} has been added.")

print("\nThis is the end of the Section 7-4: Pizza Toppings.")


# Section 7-5: Movie Ticket
    # Create a 'while loop' and ask user's age.
        # Create prompt of price of movie ticket based on age

        # Age < 3: Ticket is free
        # Age > 3 and Age < 12: Ticket is $10
        # Age > 12: Ticket is $15

user_movieTicketPrice = "\nWelcome to the Cinemax4K! To exit, type 'quit'."
user_movieTicketPrice += "\nEnter your age to reveal the price of your ticket: "

movie_programStatus = True

while movie_programStatus:

    user_movieAge = input(user_movieTicketPrice)



    if user_movieAge == 'quit':
        break

    # Comparison:
        # input() is NOT taking string input
        # input() is skipped to else statement and getting error

    elif user_movieAge != int: 
        print("\nInvalid Input.")
        continue


    else:
        user_movieAge = int(user_movieAge)



    if int(user_movieAge) <= 3:
        print("\nCongratulations! Your ticket will be free.")

    elif (int(user_movieAge) >= 4) and (int(user_movieAge) <= 12):
        print("\nYour ticket price will be $12.00")

    elif (int(user_movieAge) >= 13):
        print("\nYour ticket price will be $15.00")

print("\nThis is the end of the Section 7-5: Movie Ticket.")





