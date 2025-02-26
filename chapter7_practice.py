# For this program, we will practice running examples from Chapter 7.





# input () functions:
    # When creating an input, you can assign to a variable.

message = input("\nTell me something, and I will repeat it back to you: ")
print(message)

    # The 'input()' is a function that you can pass a variable inside.
        # EXAMPLE: Create a prompt and pass prompt inside input()

prompt = "\nIf you share your name, we can personalize the message you see. Don't believe me?"
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name.title()}")

# PRACTICE SECTION: input() functions

prompt_gameStart = "\n\nWelcome to the TEXT GAME! To start enter your name: "
userName_game = input(prompt_gameStart)

print(f"\nWelcome {userName_game.title()}! Thank you entering your name.")





# int () function:
    # This function is IMPORTANT to take user inputs and convert into intgers
    # IMPORTANT: Errors will be received trying to compare strings to integers

age_message = f"\n{userName_game.title()}, let's see if you are old enough to buy alcohol."
age_message += "\nHow old are you: "

userAge = input(age_message)
userAge = int(userAge)

if userAge >= 21:
    print(f"\nCongratulations {userName_game.title()}! You are old enough to buy alcohol.")
else:
    print(f"\nI am sorry {userName_game.title()}. You are not old enought to buy alcohol.")



