# For this program, we will focus on the last part of Chapter 7.
    # Learn to use 'while' loops with Lists and Dictionaries 
        # This program has been created by Michael Taufa

# SECTION - Moving Items from One List to Another:
    # IMPORTANT NOTES:
        # To transfer from one list to another list:
            # 1. Create a variable that will 'hold' a value
            # 2. Use methods:
                # .pop() and .append() and pass 'value'
        # Create a small program to practice transfering values to different lists.


print("\nStart of the program: 'Moving Items to Different Lists'\n")

unconfirmed_users = ['alice', 'brian', 'candance', 'john', 'michael']
confirmed_users = []

    # unconfirmed_users = True, when contains values.
        # When unconfirmed_users = [], with no values will result to 'False'

while unconfirmed_users:

    # 'current_user' can be used to transfer with temporarily variable 

    current_user = unconfirmed_users.pop()
    
    # Transfering variable to 'new list' with append() 

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)



print("\nThe following users have been confirmed:")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())


print(f"\nThis is the 'unconfirmed_users': {unconfirmed_users}")
print(f"This is the 'confirmed_users': {confirmed_users}\n")




# SECTION - Removing 'specific values' in a list with a 'while loop'
    # Using 'while loops' can scan a list and remove a value UNTIL False

print("\nStart of the program: 'Removing 'Specific Values' in a List.")

    # Here is a list of numbers. There are duplicates of '56'
        # Now, we will remove the int 56 duplicates from the list

number_lists = [3, 56, 1, 56, 90, 67, 28, 36, 46, 56, 9, 79, 60, 56]

print(f"\nBefore: {number_lists}")

while (56 in number_lists):
    # NOTE:
        # Using method: .remove() will permanately remove value VS.
        # using .pop(), where a value can be stored and used

    number_lists.remove(56)

print(f"\nAfter: {number_lists}")


