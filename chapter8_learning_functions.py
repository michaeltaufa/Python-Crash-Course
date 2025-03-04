# For this program, we will focus on learning functions
    # This program has been created Michael Taufa.

# SECTION - Defining a Function:


# Below is defining a function:
    # 'def' will create Function
        # 'greet_user' will be the name to create functions
        # Indentation:
            # All lines of codes in functions will be part of the functions
            # Similar to 'if statements' and 'while loops'

def greet_user():
    """Display a simple greeting."""
    print("\nHello! Welcome to the 'Chapter 8' Defining Functions Program.")

# Called function and passed no argument to function
greet_user()


def greet_usernames(username):

    username = str(username)
    # str() will prevent errors when using method: .title()

    print(f"Hello {username.title()}!")

    # print(username + username)
        # Created to test 'username' if variable is converted to string

greet_usernames('tom')
greet_usernames('sara')
greet_usernames(19)








