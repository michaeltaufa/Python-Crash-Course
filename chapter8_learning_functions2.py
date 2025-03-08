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

for card in userYugiohDeck:
    cardNumber = 1

    print(f"\nHere is {cardNumber} card:")
    cardNumber = 1 + cardNumber

    for card_Name, card_Type in card.items():
        print(f"{card_Name.title()} is {card_Type.title()}")











