# Dinner Guest List Exercise:

# Exericise 3-4:
    # Create a list guests to attend dinner
dinner_guest_list = ['Mom', 'Dad', 'Kalolaine', 'Melvin', 'Bebee']

print(f"\nHere is the list for the current guest that will attend dinner: {dinner_guest_list}.")

# Exercise 3-5:
    # Modify guest that is not able to make to dinner.
print(f"\n'{dinner_guest_list[4]}' shared that she is not able to make it to dinner tonight.")

dinner_guest_list[4] = 'Edd'

print(f"\nHere is the updated list for the dinner: {dinner_guest_list}.")

# Exericise 3-6:
    # Add 3 more additional guests to the list.
print("\nI have reserved a bigger dinner table and I would need to add 3 more guest to celebrate!")

dinner_guest_list.insert(0,'Pou')
dinner_guest_list.insert(2, 'Siua')
dinner_guest_list.append('Lua')

print(f"\nHere is the updated list for guest attending to dinner: {dinner_guest_list}.")

# Exercise 3-7: 
    # I will have to remove guest from the dinner list. The table only has space for 2 people.
    
print("\nI have learned that only 2 guests can only attend to dinner due to table reservation constraints.")

guest_no_dinner1 = dinner_guest_list.pop()
print(f"\nI am sorry {guest_no_dinner1}, but there is no space on the table.")

guest_no_dinner2 = dinner_guest_list.pop()
print(f"\nI am sorry {guest_no_dinner2}, but there is no space on the table.")

guest_no_dinner3 = dinner_guest_list.pop()
print(f"\nI am sorry {guest_no_dinner3}, but there is no space on the table.")

guest_no_dinner4 = dinner_guest_list.pop()
print(f"\nI am sorry {guest_no_dinner4}, but there is no space on the table.")

guest_no_dinner5 = dinner_guest_list.pop()
print(f"\nI am sorry {guest_no_dinner5}, but there is no space on the table.")

guest_no_dinner6 = dinner_guest_list.pop()
print(f"\nI am sorry {guest_no_dinner6}, but there is no space on the table.")

print(f"\nHere is the updated guest list: {dinner_guest_list}.")

del dinner_guest_list[1]
del dinner_guest_list[0]
print(f"\nDinner has been cancelled. Here is the list: '{dinner_guest_list}'.")