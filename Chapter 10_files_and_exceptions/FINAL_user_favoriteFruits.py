"""
Program Name: FINAL - Favorite Video Games 
Description:
    This program will focus on storing a list of video games in a json file. Lastly,
    there will be a conditional statement to test if the list of games have been
    stored.
Name: Michael Taufa
Date: 2025-04-16
"""

from pathlib import Path
import json

path = Path('FINAL_user_favoriteVideoGames.json')

user_videoGames = []

print("Welcome to the Video Game List Program!")
print("To exit program, type 'quit'.")

if path.exists():
    print("\nWe found your favorite list of video games:")
    content = path.read_text()
    content_videoGames = json.loads(content)

    for game in content_videoGames:
        print(f"{game.title()}")

else:
    program_status = True
    while program_status:

        user_videoGame = input("\nEnter your favorite video game: ")

        if user_videoGame == 'quit':
            program_status = False

        else:
            user_videoGames.append(user_videoGame)
            print(f"{user_videoGame.title()} has been added!")

    content = json.dumps(user_videoGames) 
    path.write_text(content)

print("\nEnd of Program.")











