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





