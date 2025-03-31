name = input(f"Hello, please enter your name: ")
print(f"Welcome {name}, this is the program to test the input function.")

age = int(input(f"Please enter your age to see if you're eligible for discount: "))
if age >= 18:
    print(f"You're age is {age} and you are eligible!")
else:
    print(f"I apologize, but your age is {age} and you're not eligible.")