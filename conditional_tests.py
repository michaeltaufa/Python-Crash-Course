# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                     
#      Program Name: Conditional Tests                         
#      Author: Michael Taufa                                          
#      Description: This program will study 'If statements' and dive deeper
#                   into exploring boolean expression, comparison, and more
#                   for testing knowledge on conditional statements.                                                     
#                                                                     
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Test for equality and inequality with strings
print("\n5-2.1: Test for equality and inequality with strings.\n")

favortie_video_games = ['Path of Exile 2', 'Call of Duty', 'Elden Ring', 'Personal 5']

for game in favortie_video_games:
    if (game == 'Path of Exile 2') or (game == 'Elden Ring'):
        print(f"This is {(game == 'Path of Exile 2') or (game == 'Elden Ring')}, I like playing {game}.\n")
    else:
        print(f"No, this is {(game == 'Path of Exile 2') or (game == 'Elden Ring')}, I don't like playing {game}.\n")
        
# Test using the lower() method        
print("\n5-2.2: Test using the lower() method:\n\n")
    
print(favortie_video_games[0].lower())
print(favortie_video_games[1].lower())
print(favortie_video_games[2].lower())
print(favortie_video_games[3].lower())

for game in favortie_video_games:
    if (game == 'Path of Exile 2') or (game == 'Elden Ring'):
        print(f"This is {(game == 'Path of Exile 2') or (game == 'Elden Ring')}, I like playing {game}.\n")
    else:
        print(f"No, this is {(game == 'Path of Exile 2') or (game == 'Elden Ring')}, I don't like playing {game}.\n")
        
# *** Note: Despite modifying strings to all lower(), boolean conditional statement executed true regardless of case sensitivity.
    # This was not expected, learned something new.
    
# Conduct numerical tests:
print("\n5-2.3: Numerical tests involves equality, inequality, greater than or less than, or equal to, etc.\n\n")

teenager_age = [15, 16, 17, 18]
young_adult_age = [21, 22, 23, 24]
adult_age = [40, 41, 42, 43]
elderly_age = [70, 71, 72, 73]
children_age = [1, 2, 3, 4]

for drinking_age in teenager_age:
    if drinking_age < 21:
        print(f"This age: '{drinking_age}' is not old enough to buy alcohol.\n")
    elif drinking_age >= 21 and drinking_age < 70:
        print(f"This age '{drinking_age}' is old enough to buy alcohol.\n")
    elif drinking_age >= 70:
        print(f"Oh my gosh, this age is '{drinking_age}', you have beend drinking for a long time!\n")
    else:
        print(f"I don't know where to sort this age: '{drinking_age}'.\n")
        
for drinking_age in young_adult_age:
    if drinking_age < 21:
        print(f"This age: '{drinking_age}' is not old enough to buy alcohol.\n")
    elif drinking_age >= 21 and drinking_age < 70:
        print(f"This age '{drinking_age}' is old enough to buy alcohol.\n")
    elif drinking_age >= 70:
        print(f"Oh my gosh, this age is '{drinking_age}', you have beend drinking for a long time!\n")
    else:
        print(f"I don't know where to sort this age: '{drinking_age}'.\n")
        
for drinking_age in adult_age:
    if drinking_age < 21:
        print(f"This age: '{drinking_age}' is not old enough to buy alcohol.\n")
    elif drinking_age >= 21 and drinking_age < 70:
        print(f"This age '{drinking_age}' is old enough to buy alcohol.\n")
    elif drinking_age >= 70:
        print(f"Oh my gosh, this age is '{drinking_age}', you have beend drinking for a long time!\n")
    else:
        print(f"I don't know where to sort this age: '{drinking_age}'.\n")
        
for drinking_age in elderly_age:
    if drinking_age < 21:
        print(f"This age: '{drinking_age}' is not old enough to buy alcohol.\n")
    elif drinking_age >= 21 and drinking_age < 70:
        print(f"This age '{drinking_age}' is old enough to buy alcohol.\n")
    elif drinking_age >= 70:
        print(f"Oh my gosh, this age is '{drinking_age}', you have beend drinking for a long time!\n")
    else:
        print(f"I don't know where to sort this age: '{drinking_age}'.\n")
for drinking_age in children_age:
    if drinking_age < 21:
        print(f"This age: '{drinking_age}' is not old enough to buy alcohol.\n")
    elif drinking_age >= 21 and drinking_age < 70:
        print(f"This age '{drinking_age}' is old enough to buy alcohol.\n")
    elif drinking_age >= 70:
        print(f"Oh my gosh, this age is '{drinking_age}', you have beend drinking for a long time!\n")
    else:
        print(f"I don't know where to sort this age: '{drinking_age}'.\n")

# Create an If Else If Statement for following:
    # Admissions - anyone under age 4 is free
    # Admissions - anyone between the age 4 to age 18 is $25
    # Admissions - anyone over the age 18 is $40
            
print("This section of the program will be focused on 'If Else If Statements'.\n")

age = 19

if age < 4:
    print(f"Your age is '{age}' and your admissions is free.\n")
elif (age >= 4) and (age <= 18):
    print(f"Your age is '{age}' and your admissions is $25.\n")
elif (age >= 19):
    print(f"Your age is '{age}' and your admissions is $40.\n")
    
# This verision of code is much easier to modify due to simplicity.
    # 1 print() statement to edit vs. 3 print() statements

if age < 4:
    price = 0
elif (age >= 4) and (age <= 18):
    price = 25
elif (age >= 19):
    price = 40
    
print(f"Your age is '{age}' and your admissions is '${price}'.\n")

# Lets test speficific conditions with a pizza example:

request_pizza_toppings = ['mushrooms', 'anchovies', 'sausage', 'extra cheese', 'extra pepperoni']

if 'mushrooms' in request_pizza_toppings:
    print('Mushrooms has been added!\n')
    
if 'anchovies' in request_pizza_toppings:
    print('Anchovies has been added\n')
    
if 'sausage' in request_pizza_toppings:
    print('Sausage has been added!\n')
    
if 'extra cheese' in request_pizza_toppings:
    print('Extra Cheese has been added!\n')
    
if 'extra pepperoni' in request_pizza_toppings:
    print('Extra Pepperoni has been added!\n')

print('We have received your toppings! We are now making your pizza!\n')