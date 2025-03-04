# For this program, we will focus on the last part of Chapter 7.
    # Learn to use 'while' loops with Lists and Dictionaries 
        # This program has been created by Michael Taufa

# SECTION - Moving Items from One List to Another:
    # IMPORTANT NOTES:
        # To transfer from one list to another list:
            # 1. Create a variable that will 'hold' a value
            # 2. Use methods:
                # .pop() and .append() and pass 'value'
        # Create a small program to practice transfering values to different lists.


print("\nStart of the program: 'Moving Items to Different Lists'\n")

unconfirmed_users = ['alice', 'brian', 'candance', 'john', 'michael']
confirmed_users = []

    # unconfirmed_users = True, when contains values.
        # When unconfirmed_users = [], with no values will result to 'False'

while unconfirmed_users:

    # 'current_user' can be used to transfer with temporarily variable 

    current_user = unconfirmed_users.pop()
    
    # Transfering variable to 'new list' with append() 

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)



print("\nThe following users have been confirmed:")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())


print(f"\nThis is the 'unconfirmed_users': {unconfirmed_users}")
print(f"This is the 'confirmed_users': {confirmed_users}\n")

# SECTION - Removing 'specific values' in a list with a 'while loop'
    # Using 'while loops' can scan a list and remove a value UNTIL False

print("\nStart of the program: 'Removing 'Specific Values' in a List.")

    # Here is a list of numbers. There are duplicates of '56'
        # Now, we will remove the int 56 duplicates from the list

number_lists = [3, 56, 1, 56, 90, 67, 28, 36, 46, 56, 9, 79, 60, 56]

print(f"\nBefore: {number_lists}")

while (56 in number_lists):
    # NOTE:
        # Using method: .remove() will permanately remove value VS.
        # using .pop(), where a value can be stored and used

    number_lists.remove(56)

print(f"\nAfter: {number_lists}")


print("\nThis section of the program will be focused on practicing utilizing 'while loops' & lists + dictionaries.")


# Build a program that transfers pizza orders that are 'unconfirmed' to 'confirmed' using a while loop
   # Create (2) lists
   # Create a variable that will be used to hold the value
   # REMEMBER:
        # The difference between remove() and pop()
        # How to use the append()
        # Question: Can you use push()? Does it exist in Python?
        # print() output

pizzaOrders_unconfirmed = ['jen', 'benjamin', 'samuel', 'john']
pizzaOrders_confirmed = []

    # Flag is not needed for while loop. List with values = True, Lists no values = False

# program_pizzaStatus = True

print("\nPizza Unconfirmed Orders:")
print(pizzaOrders_unconfirmed)

print("\nPizza Confirmed Orders:")
print(pizzaOrders_confirmed)


while pizzaOrders_unconfirmed:
        pizzaOrders_transfer = pizzaOrders_unconfirmed.pop()

        print(f"{pizzaOrders_transfer.title()} has been transfered.")

        pizzaOrders_confirmed.append(pizzaOrders_transfer)


print("\nPizza orders has been transfered successfully:")
print(pizzaOrders_confirmed)

print("\nUnconfirmed Pizza Orders:")
print(pizzaOrders_unconfirmed)



# SECTION - Filling a dictionary with User Input
    # 1. Create a user input that would correlate with each other. Key:Values
    # 2. Create a variable that would organize values based on dictioanry format

    # Create a poll for video games

favorite_videoGames = {}

poll_videoGames = True


while poll_videoGames:
    name = input("\nEnter your name: ")
    video_game = input("\nEnter your favorite video game: ")


    # Study how does the format of user input is stored in dictionaries
    favorite_videoGames[name] = video_game

    endPoll_program = input("\nIf you want to end the poll, press 'y' or 'Y': ")

    if (endPoll_program == 'y') or (endPoll_program == 'Y'):
        poll_videoGames = False


print("\nCongratulations! The poll is completed. Below is the results: \n")

for name, game in favorite_videoGames.items():
    print(f"{name.title()}'s favorite video game is {game.title()}.")

