"""
Program Name: Chapter 9, Exercise 9-13 to 9-16
Description:
    This program is focused on executing Chapter 9 exercises from the focused on
    Python Standard Library exercises
Name: Michael Taufa
Date: 2025-03-29
"""

import random

print("\nSection - Exercise 9-13: Dice")
# Make a class Dice
    # Add 1 attribute called 'Sides' with value 6
    # Create method() called roll_dice() that prints random number 1 and 'sides of dice'
    # Roll dice 10 times 

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll_dice(self):
        random_dice_roll = random.randint(1, self.sides)
        print(f"The dice rolled a {random_dice_roll}.")


dice_6sides = Dice(6)

print("\nThis is the 6 sides dice:")
dice_6sides.roll_dice()
dice_6sides.roll_dice()
dice_6sides.roll_dice()
dice_6sides.roll_dice()
dice_6sides.roll_dice()
dice_6sides.roll_dice()
dice_6sides.roll_dice()
dice_6sides.roll_dice()
dice_6sides.roll_dice()
dice_6sides.roll_dice()

dice_10sides = Dice(10)
dice_20sides = Dice(20)

print("\nThis is the 10 sides dice:")
dice_10sides.roll_dice()
dice_10sides.roll_dice()
dice_10sides.roll_dice()
dice_10sides.roll_dice()
dice_10sides.roll_dice()
dice_10sides.roll_dice()
dice_10sides.roll_dice()
dice_10sides.roll_dice()
dice_10sides.roll_dice()
dice_10sides.roll_dice()

print("\nThis is the 20 sides dice:")
dice_20sides.roll_dice()
dice_20sides.roll_dice()
dice_20sides.roll_dice()
dice_20sides.roll_dice()
dice_20sides.roll_dice()
dice_20sides.roll_dice()
dice_20sides.roll_dice()
dice_20sides.roll_dice()
dice_20sides.roll_dice()
dice_20sides.roll_dice()


print("\nSection - Exercise 9-14: Lottery")
# Create a list or tuple containing series of 10 numbers & 5 letters
    # Randomly select 4 letters/ numbers from list
    # print() message that any ticket matching values wins lottery

random_numbers_letters = [4, 8, 9, 10, 'A', 'c', 'P', 'W', 100, 41, 72, 35]

random_draw = random.choice(random_numbers_letters)

if (random_draw == 8) or (random_draw == 'P') or (random_draw == 10) or (random_draw == 100):
    print(f"You win the lottery! Here is what you draw: {random_draw}")
else:
    print(f"I am sorry. You did not win the lottery. Here is what you draw: {random_draw}")


print("\nSection - Exercise 9-15: Lottery Analysis")
# Use a loop to see how hard it might be to win the lottery:
    # Create a list/ tupple called 'my_ticket'
    # Create a loop that keeps pulling numbers until you ticket wins
    # print() a report how many times loop had to run to = wining ticket


