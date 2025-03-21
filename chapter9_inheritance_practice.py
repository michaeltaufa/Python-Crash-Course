# For this progam, we  will be focused on building Classes, inheritance, and more.
    # This program has been created by Michael Taufa.

class VideoGame:

    def __init__(self, title, studio, price):
        self.title = title
        self.studio = studio
        self.price = int(price) 

    def format_videoGameTitle(self):
        format_title = f"{self.title}"

        return format_title.title()

    def price_adjustment(self, adjustment):
        self.price += adjustment 

        return self.price


# NOTE: The definition below is to check variable is int or str
    # '.isdigit()' is a method to check variable and return True or False

def check_variableInt(number):
    checkNumber = number.isdigit() 
    verification_status = ''

    if checkNumber == True: 
        verification_status = True
    else:
        verification_status = False 

    return verification_status


print("\nWelcome to Program to practice building classes with user inputs.")


program_status = True

while program_status:
    user_name = input("Enter your name to start: ")
    user_name = str(user_name)

    user_favoriteVideo = input(f"{user_name.title()}, enter a title of a video game you would create: ")
    user_favoriteVideo = str(user_favoriteVideo)

    user_VideoGameStudio = input("Now, enter the name of your studio: ")
    user_VideoGameStudio = str(user_VideoGameStudio)

    user_VideoGame_price = input("Lastly, enter the price of your video game: ")

    mini_program_status = True
    while mini_program_status:

        verfication_number = check_variableInt(user_VideoGame_price)

        if verfication_number == False:
            print("Invalid Input!")
            user_VideoGame_price = input("Please enter the price of your video game: ")

        else:
            mini_program_status = False


    user_videoGame = VideoGame(user_favoriteVideo, user_VideoGameStudio, user_VideoGame_price)
    print(f"\nBelow is the following information of your game:")
    print(f"{user_videoGame.format_videoGameTitle()}.")
    print(f"{user_videoGame.studio.title()}")
    print(f"The game is priced at {user_videoGame.price}")


    user_discount = input("\nNow, enter how much adjust the price: ")

    mini_program_status = True
    while mini_program_status:

        # verfication_number1 = user_discount.isdigit()
        # print(verfication_number1)
        try:
            verfication_number1 = int(user_discount)
            mini_program_status = False 

        except ValueError:
            print("Invalid Input!")
            user_discount = input("Please enter a valid number: ")

    """
        if verfication_number1 == False:
            print("Invalid Input!")
            user_discount = input("Please enter a valid number: ")

        else:
            user_discount = int(user_discount)
            mini_program_status = False
        
        user_videoGame.price_adjustment(user_discount)
    """

    user_videoGame.price_adjustment(verfication_number1)
    print(f"The game is priced at {user_videoGame.price}")


    program_status = False


print("\nThe program has ended and is complete.")
