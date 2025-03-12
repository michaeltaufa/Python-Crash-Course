# For this program, we will focus on learning functions continued...
    # This program has been created Michael Taufa.


# SECTION - Returning a Dictionary (continued...)
    # For this program, we will practice 'returning dictionaries'
    # by using functions() to build and construct dictionaries


def build_yugiohCard (cardName, cardType = ''):
    # This function is focued on building a dictionary for 'each yugioh card'

    cardName = str(cardName)
    cardType = str(cardType)

    # Need to declare a dictionary for function to build 
    yugiohCard = {
            'Card Name': cardName,
            'Card Type': cardType,
            }

    if cardType == 'monster':
        yugiohCard['Card Name'] = cardName 
        yugiohCard['Card Type'] = 'monster' 

    elif cardType == 'spell':
        yugiohCard['Card Name'] = cardName 
        yugiohCard['Card Type'] = 'spell' 

    elif cardType == 'trap':
        yugiohCard['Card Name'] = cardName 
        yugiohCard['Card Type'] = 'trap' 

    # IMPORTANT to return dictionary 'yugioh' card
    return yugiohCard

darkMagician = build_yugiohCard('dark magician','monster')

blueEyesWhiteDragon = build_yugiohCard('blue eyes white dragon', 'monster')

potOfGreed = build_yugiohCard('pot of greed', 'spell')

mirrorForce = build_yugiohCard('mirror force', 'trap')

print(darkMagician)
print(blueEyesWhiteDragon)
print(potOfGreed)
print(mirrorForce)

# TESTING: Can you add a dictionary inside a list?
    # Add a yugioh card into user_deck
        # NOTES: With lists, you can use methods: such as .append()

print("\nNow, we are going to append dictionaries into a list.")

userYugiohDeck = [] 

userYugiohDeck.append(darkMagician)
userYugiohDeck.append(blueEyesWhiteDragon)
userYugiohDeck.append(potOfGreed)
userYugiohDeck.append(mirrorForce)

cardNumber = 1

for card in userYugiohDeck:

    # cardNumber = 1 NOTE: declaring iteration in 'for loop' will reset value to 1

    print(f"\nHere is {cardNumber} card:")
    cardNumber = 1 + cardNumber

    for card_Name, card_Type in card.items():
        print(f"{card_Name.title()} is {card_Type.title()}")


# SECTION - Using a function with a 'while' loop

def favoriteVideoGame_userPrint (favoriteVideoGame, videoGame_studio):
    favoriteVideoGame = str(favoriteVideoGame)
    videoGame_studio = str(videoGame_studio)

    favoriteGameStudio_Print = f"I like your answer! {favoriteVideoGame.title()} is a great game! Also, {videoGame_studio.title()} is a great studio!"

    print(favoriteGameStudio_Print)
    return favoriteVideoGame, videoGame_studio

while True:
    print("\nWelcome to the 'Favorite Video Game' program! To quit at any time, press 'q' and ENTER: ")
    user_favoriteVideoGame = input("What is your favorite video game: ")

    if user_favoriteVideoGame == 'q':
        break

    user_videoGame_studio = input("What is your favorite video game studio: ")

    if user_videoGame_studio == 'q':
        break

    favoriteVideoGame_userPrint(user_favoriteVideoGame, user_videoGame_studio)

print("The 'Favorite Video Game' Program is complete!")

# SECTION - Exercise 8-6: City Name 
    # For this exercise, create function() 'city_country()'
    # Function will take name of city, country
    # return print() statement

def city_country(cityName, countryName):
    cityName = str(cityName)
    countryName = str(countryName)

    print(f"{cityName.title()}, {countryName.title()}")

print(f"\nThis section is Exercise 8-6: City Name")
city_country('new york', 'united states of america')
city_country('santiago', 'chile')

# SECTION - Exercise 8-7: Album
    # For this exerice, create function make_album() that creates a dictionary
    # Dictonary should take the following: artist, album
    # return dictionary

    # call function 3 times, print dictionary

print(f"\nThis section is Exercise 8-7: Album")

def make_album(artistName, albumName, numberOfSongs = None):
    artistName = str(artistName)
    albumName = str(albumName)

    album = {
            'Artist Name': artistName,
            'Album Name': albumName,
            'Total Number of Songs': numberOfSongs,
            }

    if numberOfSongs:
        print(f"\nThis {albumName.title()} by {artistName.title()} has {numberOfSongs} a total songs.")

    else:
        print(f"\n{albumName.title()} is an album by {artistName.title()}.")

    return album

print(make_album('tupac', 'me against the world', 20))
print(make_album('kendrick lamar', 'good kid madd city'))
print(make_album(5, 'the numbers', 100))


# SECTION - Exercise 8-8: User Album
    # Continue on Exercise 8-7 with a 'while loop'
    # Add user input for Users on the make_album()
    # Add a 'quit' function to break while loop

print(f"\nThis section is Exercise 8-8: User Album")

while True:
    print("\n(At any time to exit, type 'q' and ENTER.)")
    
    user_artistName = input("Name your favorite music artist: ")

    if user_artistName == 'q':
        break

    user_albumName = input(f"Next, name your favorite album by {user_artistName.title()}: ")

    if user_albumName == 'q':
        break
    
    print("(If you don't know the number of songs, enter '0'.)")
    user_numberOfSongs = input(f"Lasty, enter how many songs is in the album.")

    if user_albumName == 'q':
        break

    make_album(user_artistName, user_albumName, user_numberOfSongs)

print("The 'Exercise 8-8: User Album' Program is complete!")


# SECTION - Passing a List:
    # Passing a list into a function will be needed depending on the needs

def greet_users(names):

    for name in names:
        message = f"Hello, {name.title()}"
        print(message)

userNames = ['hannah', 'ty', 'margot']

     










