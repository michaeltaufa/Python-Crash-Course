# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
#   This program has been created by Michael Taufa.
#   
#   This program is to practice and test using slices.
#
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 4-10:
    # Practice using slices in different segments in the list below:
print("\nExercise 4-10:\n")
    
nfl_teams = ['san francisco 49ers', 'seattle seahawks', 'arizona cardinals', 'los angeles rams', 'kansas chiefs', 'baltimore ravens']

print(f"\nHere is the list: {nfl_teams}.\n\n")
print(f"The first three items in the list is {nfl_teams[0:3]}.\n")
print(f"The three items in the middle is {nfl_teams[2:5]}.\n")
print(f"The last three items in the list is {nfl_teams[-3:]}.\n")

# 4-11:
    # Make a copy of a list do the following:
        # 1. Add a new item in the original list
        # 2. Add a new different in the new list
        # 3. print() both list to show different list
        
print("\nExercise 4-11:\n")

favorite_music_artist = ['kendrick lamar', 'j. cole', 'drake']
friends_favorite_music_artist = favorite_music_artist[:]

favorite_music_artist.insert(1,'sza')
friends_favorite_music_artist.append('beyonce')

print(f"\nThis is my list of favorite music artist:{favorite_music_artist}.")
print(f"\nThis is my friends list of favorite music artist:{friends_favorite_music_artist}.")

# 4-12:
    # print a list with 'for loop'
    # Bonus: Practice looping with a slice
    
print("\nExercise 4-12:\n")

print("This is my favorite music artists for top 3:")
for artist in favorite_music_artist[0:3]:
    print(artist)
print("This is the end of my list.\n\n")
    
print("This is my friend's top 3 least favorite music artist in his list:")
for artist in friends_favorite_music_artist[-3:]:
    print(artist)
print("This is the end of my friend's list.\n\n")