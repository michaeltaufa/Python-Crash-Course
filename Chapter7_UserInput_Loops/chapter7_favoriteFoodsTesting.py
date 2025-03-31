# This program has been created by Michael Taufa

# For this program, we will test using a 'while loop' with lists.
    # 1. Create a list of foods from user
    # 2. Add food with input()
    # 3. Add to the list



# Section - Introduction:

userName_prompt = input("\nWelcome to the program. What is your name: ")
print(f"Nice to meet you {userName_prompt.title()}!")

user_favoriteFoods = []

userMinimum_food = True 


# Section - Add Food to list:

while userMinimum_food:

    if len(user_favoriteFoods) == 5:
        break
    else:
        food_userInput = input(f"\n{userName_prompt.title()}, add your favorite food to the list: ")

        user_favoriteFoods.append(food_userInput)
        print(f"{food_userInput.title()} has been added.")


print("\nYour food list is complete! Here is the list:")
print(user_favoriteFoods)

print(f"\n{userName_prompt.title()}, now its time to empty your list.")


# During testing, comment variable below to test 'if statement variable' redeclares value outside of local scope:
    # IMPORTANT: new value gets modified and carried into the rest of the program!
    
# userMinimum_food = True


# Section - Remove Food from list

while userMinimum_food:
    user_inputRemove = input("\nPress 'x' to remove a food from your list: ")

    if user_inputRemove == 'x':

        removedFood = user_favoriteFoods.pop()
        print(f"{removedFood.title()} has been removed.")

        if len(user_favoriteFoods) == 0:
            break

    else:
        print(f"Incorrect Input! Please try again.")

print("\nAll the food has been removed in your list: ")
print(user_favoriteFoods)
print("\nProgram is completed, thank you for your participation.")
