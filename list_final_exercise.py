# For this program, I will be executing Chapter 5 Exercises.


# Create a list of 5 or more usernames and include username 'Admin'
    # Loop through lis to print greeting to each usernames
    # IF 'Admin' print message, 'Hello Admin, would you like to see status report?'

print("\nExercise 5-8 has started.\n")

usernames = ['johnbjohnson1000', 'CookieCutter', 'Admin', 'Red Wing Fighter', '3RTSzoom']

for names in usernames:
    if names == 'Admin':
        print(f"Hello Admin, would you like to see the status report?")
    else:
        print(f"Greetings '{names}', how are you doing?")

print("\nExercise 5-8 is completed!\n")

# Exercise 5-9: Add an 'if statement' to make sure the list is not empty.

print("Exercise 5-9 has stated.\n")

usernames_groupA = []

if usernames_groupA:
    for names in usernames_groupA:
        print(f"Hello {names}, how are you doing?\n")
else:
    print("There are no usernames in this list.\n")

print("Exercise 5-9 is completed!\n")

# Exercise 5-10: Checking usernames
    # Make a list of current_users
    # Make a list of new_users
    # Make sure there are 1 or 2 duplicates in both list
    # Loop through the list and print message 'Username is not availble', else 'Username is availble'
    # Ensure comparison is case insensitive

print("Exercise 5-10 has started.\n")

current_users = ['MikezTooRIPZ', '55_powerBACK', 'KungFUKenny', 'JaMarius_Cole', 'DraThor']
lower_case_current = [current_name.lower() for current_name in current_users]

new_users = ['greenLantern', 'KingSOFAR', 'mikeztooRIPZ','TitanMONSTER','jamarius_Cole']

print(f"This is the current_users list: {current_users}.\n")
print(f"This is the new_users list: {new_users}.\n")

# I had to create a new list for lower_case_current to modify list to lowercase for comparison.

for names in new_users:
    if names.lower() in lower_case_current:
        print(f"Sorry, {names} is not availble.\n")
    else:
        print(f"{names} is availble!\n")


print("Exercise 5-10 is completed.\n")


# Exercise 5-11: Ordinal Numbers
    # Create a number list of 1 - 9
    # Loop through the list
    # Create 'if elif else' statement for each number. Output should be 1st, 2nd, 3rd, etc...

print("Exercise 5-11 has started.\n")

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers_list:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print('3rd')
    else:
        print(f"{number}th")

print("\nExercise 5-11 is completed.\n")
