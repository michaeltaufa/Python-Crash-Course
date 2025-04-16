"""
Program: Exercise 1: Sum of Even Numbers in a Range
Description:
    Write a program that asks the user for (2) numbers and print() sum 
Name: Michael Taufa
Date: 2025-04-10
"""

from pathlib import Path
import json

path = Path('chatGPT_exercise.json')


programStatus = True
numberCheck_status = True

while programStatus:

    while numberCheck_status:
        try:
            user_firstNumber = input("Enter first number: ")
            user_firstNumber = int(user_firstNumber)

        except TypeError:
            print("Error: Input is not an integer.")

        else:
            print(f"{user_firstNumber} was added.")
            numberCheck_status = False

    numberCheck_status = True

    while numberCheck_status:
        try:
            user_secondNumber = input("Enter second number: ")
            user_secondNumber = int(user_secondNumber)

        except TypeError:
            print("Error: Input is not an integer.")

        else:
            print(f"{user_secondNumber} was added.")
            numberCheck_status = False


    answer = (user_firstNumber + user_secondNumber)
    print(f"The calculation is {answer}.")
    programStatus = False

content = json.dumps(answer) 
path.write_text(content)
