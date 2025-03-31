# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
#   This program has been created by Michael Taufa.
#
#   This program is to learn the following:
#       1. Learn how to slice a list
#       2. Learn how to loop through a list that is slice
#       3. Copying a list
#
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:4])

# Answer: florence - WRONG (Forgot 'Michael', counting up to 4 elements)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:3])

# Answer: martina, michael - RIGHT

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# Answer: charles, martina, michael - RIGHT

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:2])

# Answer: charles, martina - RIGHT

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

# Answer: martina, michael, florence, eli - WRONG (Counted an extra element, start counting a index position 0)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:1])

# Answer: 0 - RIGHT

print("\n\n\n")
print("This is the second program to test slicing.")

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[4:])

# Answer: eli - RIGHT

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

# Answer: charles, martina, michael, florence - RIGHT

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

# Answer: michael, florence, eli - RIGHT
    # slice - (start: stop: step) => start -3, stop 0 => include all values left over

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:-2])

# Answer: 0 - WRONG (Reverse slice? Sliced out flornece, eli printed: charles, martina, michael?)
    # slice - (start: stop: step) => start 0, stop -2 => include all values left over

print('\n\nThis is the start of the program.\n')
    
yugioh_spellcasters = []
yugioh_spellcasters.append('dark magician')
yugioh_spellcasters.append('dark magician girl')
yugioh_spellcasters.append('dark magician of chaos')
yugioh_spellcasters.append('time wizard')
yugioh_spellcasters.append('thousand eye restrict')

for spellcaster in yugioh_spellcasters[1:4]:
    print(f"This is the test for [1:4]. Output: {spellcaster}")
print('\nThis is the end of the program.')


print('\n\nThis is the start of the program.\n')

favorite_video_games = ["legend of zelda: orcarina of time", "legend of zelda: majora's mask", "legend of zelda: twilight princess"]
sister_favorite_video_games = favorite_video_games[:]

print(f"This is my list of favorite video games: {favorite_video_games}.\n")
print(f"This is my sister's list of favorite video games: {sister_favorite_video_games}.\n")

favorite_video_games.append('dark souls')
favorite_video_games.append('elden ring')
sister_favorite_video_games.append('persona 5')
sister_favorite_video_games.append('okami')

print(f"This is my list of favorite video games: {favorite_video_games}.\n")
print(f"This is my sister's list of favorite video games: {sister_favorite_video_games}.\n")