# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#  For this program, I will practice using the input() and integrate with the following:
#                    1. Create a list
#                    2. Utilize an 'if statment' to create a flow.
#                    3. Concatenate variables with strings.
#
#  This program has been created by Michael Taufa
#  Date: 02-23-2025
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

name = input("Hello! Please enter your name: ")

age = input(f"\nHello {name.title()}, how old are you? ")

answer = input(f"\nTo confirm, {name.title()} are you {int(age)}? ")

print(f"\nThank you for confirming {name.title()} that you said '{answer.title()}' and that you are {int(age)} years old!")

michael_answers = []
michael_answers.append(name)
michael_answers.append(age)
michael_answers.append(answer)

age_answer = input(f"\nHello, let's test to see if you are old enough to drink. How old are you? >> ")
michael_answers.append(age_answer)

if int(age_answer) >= 21:
    print(f"\nCongratulations! You are {age_answer} years old. You are legal to drink alcohol.")
else:
    print(f"\nI am sorry, but you are not old enough to drink alcohol.")

decision_answer = input(f"\nNow, press 's' and press 'enter' to print all your anwers below. >> ")

if decision_answer == 's':
    for user_answer in michael_answers:
        print(user_answer)
else:
    print("I am sorry, the input is 'incorrect'.")

print("\nThis is the end of the program. Thank you! :)")

