# This program is focused on creating functions and practice importing into another file.
    # This program has been created by Michael Taufa.

def greeting_user(firstName, lastName):
    greet_user_message = f"Hello {firstName.title()} {lastName.title()}."

    return greet_user_message

    # Function will return 'greet_user_message' to greet user


def user_legalDrinkingAge(age):
    age_eligibility = False
    user_ageMessage = ''

    if age >= 21:
        user_ageMessage = "Congratulations, you are old enough to purchase alcohol."
        age_eligibility = True
    else:
        user_ageMessage = "I am sorry, but you are not old enough to purchase alcohol."

    return age_eligibility, user_ageMessage

    # Function will check user if they are eligible to purchase alcohol.


def build_userProfile(firstName, lastName, **userProfile):
    userProfile['first name'] = firstName
    userProfile['last name'] = lastName
    
    return userProfile
    
    #  Function will collection information on user to build dictionary.
