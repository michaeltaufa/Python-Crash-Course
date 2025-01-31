# List
    # Focus on adding, removing, and modifying elements in a list

fromsoftware_souls_games = ['Demon Souls', 'Dark Souls', 'Dark Souls 2', 'Dark Souls 3']
print(fromsoftware_souls_games)

# Modify - How to modify elements in the lists
    # We are redeclaring variable in list

fromsoftware_souls_games[0] = 'UPDATE: Demon Souls Remake' 
print(fromsoftware_souls_games)

# Append - The easiest way to add elements in the list at the end.

fromsoftware_souls_games.append('Bloodborne') # Use 'append()' method 
print(fromsoftware_souls_games)

fromsoftware_non_souls_games = []
fromsoftware_non_souls_games.append('Sekiro: Shadows Die Twice') 
fromsoftware_non_souls_games.append('Elden Ring')
fromsoftware_non_souls_games.append('Armored Core 6')
fromsoftware_non_souls_games.append('Elden Ring Nightreign')

non_souls_message = f"These are the following FS non-souls games {fromsoftware_non_souls_games}."
print(non_souls_message)

# Insert - To insert elements in a current list, use 'insert()' => specify index position, string
    # Example: list.insert(0, 'apples')
    
call_of_duty_games = ['Call of Duty: Modern Warefare 2', 'Call of Duty: Modern Warefare 3']
call_of_duty_games.insert(0, 'Call of Duty Modern Warefare')

missing_cod_titles_message = f"The game that was missing on the list is '{call_of_duty_games[0]}' and so I inserted this element and here is the full list:\n{call_of_duty_games}."
print(missing_cod_titles_message)

# Remove - There are 2 ways to remove elements in a list
    # 1. 'del' statement:
        # Use this method if "you know the exact index postion" element that needs to be removes
            # REMEMBER: del is statement, NOT method
    # 2. 'pop()' method: 
        # Use this method to remove element at the end of the list
        
game_of_the_year_titles = ['Elden Ring', 'Baldurs Gate 3','Assasins Creed: Valhalla', 'AstroBot', 'Starfield']
print(f"Before: {game_of_the_year_titles}")

del game_of_the_year_titles[2]
print(f"After: {game_of_the_year_titles}")

print(f"Now, since Valhalla was removed, we need to remove {game_of_the_year_titles[3]} because this game was not nominated.\nHere is before {game_of_the_year_titles}")

updated_goty_titles = game_of_the_year_titles.pop()
print(f"Game removed: '{updated_goty_titles}'")
print(f"After: {game_of_the_year_titles}")