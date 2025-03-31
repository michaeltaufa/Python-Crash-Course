


user_favroiteGames = []

user_name = input("\nWelcome! Enter your name to continue: ")

program_status = True

user_promptGames = input(f"\n{user_name.title()}, if you are done adding games, type 'quit' and ENTER.\nNow, let's add your favorite games to the list: ")

while program_status == True:

    if user_promptGames == 'quit':

        if len(user_favroiteGames) == 0:
            print(f"\n{user_name.title()}, you don't have any games on your list!")

        else:
            break

    else:
        user_favroiteGames.append(user_promptGames)
        print(f"\n{user_promptGames.title()} has beed added to your list.")


    print(f"\nHere is the updated list: {user_favroiteGames}")

    user_promptGames = input("\nIf you are done, type 'quit' and ENTER.\nEnter your favorite video games to the list: ")


print(f"\nGreat! Here is the list of games added to your list:")
print(user_favroiteGames)



