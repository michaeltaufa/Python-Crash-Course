# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                     
#      Program Name: 'If Statements' Chaopter                         
#      Author: Michael Taufa                                          
#      Description: This program will study 'If statements' and dive deeper
#                   into exploring boolean expression, comparison, and more.                                                     
#                                                                     
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

print("\nThis is the start of of the 'If Statement' Chapter.\n")

# Checking Values in a list:
    # Check values is "IN A LIST" using 'in'

video_games = ['resident evil 4 remastered', 'dark souls 3', 'horizon zero dawn', 'call of duty: black ops 4']

print(f"List: {video_games}.\n")

print(f"I am checking if Dark Souls 3 is in the list: {'dark souls 3' in video_games}.\n")

print(f"I am checking if Pokemon is in the list: {'pokemon' in video_games}.\n")

# Checking Values in a list:
    # Check values is "NOT IN A LIST" using 'not'

print("This is to check values 'not' in the list.\n")

bad_game = 'Dragon Age: Veilguard'

print(f"The game to check on list is {bad_game}.\n")

if bad_game not in video_games:
    print(f"{bad_game} is not on my favorite list of video games.\n")
else:
    print(f"I made a mistake. {bad_game} is on the list.\n")
    
    
