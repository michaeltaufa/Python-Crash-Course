"""
Program: Exercise 9-14 Lottery, 9-15 Lottery Analysis
Description:
        This program will be focused on executing Exercise 9-14 and 9-15
        from Chapter 9 Classes.
Name: Michael Taufa
Date: 2025-03-31
"""

import random


# SECTION - 9-14 Lottery:
    # Make a list or tuple of a series of 10 numbers and 5 letters
    # Randomly select 4 numbers and letters from the list
    # print() message that any ticket matching these 4 numbers or letters wins the prize


print("\nThis is the start of Exercuse: 9-14 Lottery")

draw_pool = ['1', 's', 'B', '8', '100', '31', 'W', 'z', 'P', 'f', '21', '19', '3', '55', '47', '83']

# draw_machine = random.choice(draw_pool)

golden_ticket = ['s', 'P', '21', '3']

print(f"The winning numbers is '{golden_ticket}.\n")

draw_machine = random.choice(draw_pool)

if draw_machine in golden_ticket:
    print(f"Congratulations! '{draw_machine}' was drawn and you win the prize!")
else:
    print(f"I am sorry. You drawn a '{draw_machine}' and did not win.")


# SECTION - 9-15 Lottery Analysis:
    # Make a list or tuple called my_ticket
    # Create a loop that keeps pulling numbers until your ticket wins
    # print() message reporting how times the loop run

print("\nThis is the start of Exercuse: 9-15 Lottery Analysis")

golden_ticket.sort()
draw_round = 1
my_ticket = []
program_status = True


while program_status: 
    if my_ticket == golden_ticket:
        program_status = False
        break

    print(f"\nRound: {draw_round}")

    draw_machine = random.choice(draw_pool)

    if (draw_machine in golden_ticket) and (draw_machine not in my_ticket):
        my_ticket.append(draw_machine)
        my_ticket.sort()
        print(f"Congratulations! '{draw_machine}' was drawn and added to ticket!")
        print(f"This is currently your ticket: {my_ticket}.")

    elif (draw_machine in golden_ticket) and (draw_machine in my_ticket):
        print(f"You already have {draw_machine}.")

    else:
        print(f"I am sorry. You drawn a '{draw_machine}' and is not added to the ticket.")

    draw_round = draw_round + 1


print(f"Congratulations! You won the lottery!\nGolden Numbers: {golden_ticket}\nLottery Ticket: {my_ticket}\nNumber of Attempts: {draw_round - 1}")
