# This program has been created by Michael Taufa
    # For this program, we will focus on practicing 'while loops' in Chapter 7

#SECTION - While Loops:
    # When creating a while loop, IMPORTANT to have a base case
    # EXAMPLE: When is the 'while loop' is going to end? 

current_number = 1

while current_number <= 5:
    print(current_number)

    # This is how to do an iteration of (+1)
    current_number = current_number + 1

# While Loops (continued):
    # Let's create a prompt to allow users to quit a while loop.

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""

# TIP: '!=' means 'not equal to...'
    # Ask: Are these numbers different?
        # Yes = True (Statement that holds a difinitive truth)
        # No = False (Contradictory Statement)

# Using a Flag:
    # A flag will be help maintain 'while loops' and programs much more manageable. 

program_statusActive = True

while program_statusActive:

    message = input(prompt)

    if message == 'quit':
        program_statusActive = False

        # print() statement below is executed after flag has been set to False.

        print("\nThis line of code is in the 'if statement'.")
    else:
        print(message)

    # Also, this print() statement below is executed after flag been set to False
    print("\nThis line of code is in the 'while loop'.")


# SECTION - Using 'break' to exit:
    # 'break' can be used to used to direct the flow of a program
    # ALSO, it can be used to control which lines of code can be executed.

    # Lastly, 'break' can be used on 'for loops'


program_statusActive = True

print("\nThis is the start of the 2nd 'while' loop.")

while program_statusActive:

    message = input(prompt)

    if message == 'quit':
        print("This program 'break' out of while loop.")
        break
    elif message == '903':
        print("Secret code number: 903 has been typed. This program will 'break' out of the while loop")
        break
    else:
        print(message)


# SECTION - 'continue' loop
    # Use a 'continue' loop to return to the beginning of the loop
print("\nThe section 'continue' has started.")

current_number = 0

while current_number <= 10:
    current_number = current_number + 1

    if current_number % 2 == 0:
        continue

    # Testing to see if we can print '12'
        # UPDATE: Does not print '12' due to while statement

    elif current_number == 11:
        continue

    print(current_number)







print("\nThe program has ended.")
