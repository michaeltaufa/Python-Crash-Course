# For this program, I will practice building a 'Rock, Paper, Scissor' game.
    # To build a 'Rock, Paper, Scissor', we will need to the following:
        # 1. Computer to generate moves:
            # Create a RNG and associate with move set: Rock, Paper, Scissor
        # 2. Create user move set:
        # 3. Results: create a comparison of move set: Rock, Paper, Scissor
        # 4. Create user input to link move set

import random

# Section: Start Program

user_name = input(f"\nWelcome to the 'Rock, Paper, Scissor' game.\nTo get started, enter your name: ")
start_game_prompt = input(f"\nWelcome {user_name.title()}! To start the game, press 'x' and ENTER to begin: ")

user_StartGame = True

while user_StartGame == True:
    if start_game_prompt == 'x':
        break
    else:
        start_game_prompt = input(f"\nIncorrect Input!\n{user_name.title()}, press 'x' and ENTER to begin: ")


# Section: Generate Computer Move

computerMove = ''
computer_random_number = random.randint(1,100)

if (computer_random_number >= 0) and (computer_random_number <= 33):
    computerMove = 'rock'
elif (computer_random_number >= 34) and (computer_random_number <= 66):
    computerMove = 'paper'
elif (computer_random_number >= 67) and (computer_random_number <= 100):
    computerMove = 'scissor'

# Section: User Move

userMove_pending = True 
userMove = ''
userMove_input = input(f"\n{user_name.title()}, Choose your move and press the following: Rock (r/R), Paper (p/P), or Scissor (s/S):  ") 

while userMove_pending == True:

    if (userMove_input == 'r' or userMove_input == 'R'): 
        userMove = 'rock'
        break
    elif (userMove_input == 'p' or userMove_input == 'P'):
        userMove = 'paper'
        break
    elif (userMove_input == 's' or userMove_input == 'S'):
        userMove = 'scissor'
        break
    else:
        userMove_input = input(f"\nIncorrect Input!\n{user_name.title()}, Choose your move and press the following: Rock (r/R), Paper (p/P), or Scissor (s/S):  ")

# Section: Print Results

game_results = ''

if (userMove == 'rock' and computerMove == 'rock') or (userMove == 'paper' and computerMove == 'paper') or (userMove == 'scissor' and computerMove == 'scissor'):
    game_results = 'tie'
elif (userMove == 'rock' and computerMove == 'paper') or (userMove == 'paper' and computerMove == 'scissor') or (userMove == 'scissor' and computerMove == 'rock'):
    game_results = 'Computer wins'
elif (userMove == 'rock' and computerMove == 'scissor') or (userMove == 'paper' and computerMove == 'rock') or (userMove == 'scissor' and computerMove == 'paper'):
    game_results = f"{user_name.title()} wins"

print("\n\n- - - - - - - - - - - - - - - - - - - - - ")
print(f"{user_name.title()}, this is the results:\n")
print(f"This is {user_name.title()}'s move: {userMove.title()}")
print(f"The Computer rolled a '{computer_random_number}', pulling a '{computerMove.title()}'")
print(f"\nThe result is '{game_results}'!")
print("- - - - - - - - - - - - - - - - - - - - -\n ")

print("\nThis is the end of the game.\n")
