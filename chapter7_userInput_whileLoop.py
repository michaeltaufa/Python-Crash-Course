# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#  For this program, I will practice using the input() and integrate with the following:
#                    1. Create a list
#                    2. Utilize an 'if statment' to create a flow.
#                    3. Concatenate variables with strings.
#
#  This program has been created by Michael Taufa
#  Date: 02-23-2025
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

name = input("\nWelcome to the 'chapter7_userInput()' program. Please enter your name: ")

user_age = input(f"\nHello {name.title()}! Let's collect some information. Please enter your age: ")

user_sportsTeam = input(f"\nWow I didn't know you are {user_age} years old! One last question.\nWhat is your favorite NFL sports team? ")

user_information_input = []

user_information_input.append(name)
user_information_input.append(user_age)
user_information_input.append(user_sportsTeam.title())

print(f"\nAlright {name.title()}, lets quickly print out all this information you shared:")

for user_info in user_information_input:
    print(user_info)

user_answer_key = input(f"\n{name.title()}, if the information you submitted is correct, please press 'x' to contunue.  ")
user_decision = True 

while user_decision == True:
    if user_answer_key == 'x': 
        user_decision = False
        print(f"\nSuccessful!")
        print(f"{name.title()}, you did it! Go '{user_sportsTeam.title()}'! Program is complete!")
        break
    else:
        print("\nThis is an invalid entry. Please press 'x' to continue:  ")

    user_answer_key = input(f"Let's try again. Press 'x' to continue:   ")


print(f"Congratulations! Program is complete!\n")
