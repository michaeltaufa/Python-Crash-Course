# For this program, we will be focused on building programs based on exercised provided in Chapter 8.
    # This program has been created by Michael Taufa.

print("\nThis section of the program is Chapter 8-1 Message:")

# SECTION - 8-1: Message
    # Define a function called display_message
        # print() = Tell everyone what you are learning.

def display_message(chapter8_topic):
    chapter8_topic = str(chapter8_topic)
    print(f"For this chapter, I am learning {chapter8_topic.title()}.")

topic1 = "functions"
topic2 = "arguments"
topic3 = "parameters"

display_message(topic1)
display_message(topic2)
display_message(topic3)


# SECTION - 8-2: Favorite Book
    # Define a function called favorite_book()
    # Include a parameter, title

print("\nThis section of the program is Chapter 8-2 Favorite Book:")

def favorite_book(title):
    title = str(title)
    print(f"My favorite book that I am reading is {title.title()}.")

favorite_book('python crash course')
favorite_book('harry potter')
favorite_book('atomic habits')


# SECTION - 8-3: T-Shirt
    # Create function called make_shirt()
    # Pass (2) arguments: size and message/ logo of shirt

print("\nThis section of the program is Chapter 8-3 T-Shirt:")

def make_shirt(shirt_size, shirt_content):

    shirt_size = str(shirt_size)
    shirt_content = str(shirt_content)

    print(f"The size of this shirt is a {shirt_size.title()}")
    print(f"The content of the shirt displays, '{shirt_content}'.")

make_shirt('medium', 'I love coding!')
make_shirt('large', 'Coffee Please')


# SECTION - 8-4: Large Shirts
    # Modify make_shirt function to the following:
        # Default Message = 'I love Python'
        # Large and Medium shirts will have default message 

        # Any size shirt will have different message  

print("\nThis section of the program is Chapter 8-4 Large Shirts:")

def make_pythonShirt(shirt_size, shirt_content):
    shirt_size = str(shirt_size)
    shirt_content = str(shirt_content)

    if (shirt_size == 'large') or (shirt_size == 'medium'):
        shirt_content = "I love Python!"

    print(f"The size of my shirt is {shirt_size.title()} that says '{shirt_content}'.")

make_pythonShirt('medium', 'I hate Python')
make_pythonShirt('small', 'I also love Python!')


# SECTION - 8-5: Cities
    # Create function() called describe_cities()
    # Arguments: name of city, name of country
    
    # Give country a default value
        # Call function 3 
        # Call function once with no default value

print("\nThis section of the program is Chapter 8-5 Cities:")

def describe_cities(cityName, countryName = 'United States of America'):
    cityName = str(cityName)
    countryName = str(countryName)


    if cityName == 'paris' or cityName == 'tokyo' or cityName == 'rome':
        print(f"{cityName.title()} is not located in the {countryName.title()}")

    else:
        print(f"{cityName.title()} is located in {countryName.title()}.") 

describe_cities('redwood city')
describe_cities('rome')
describe_cities('dallas')


# SECTION - 8-9: Messages
    # Make a list containing a series of short text messages
    # Pass list into function show_message() and print message

print("\nThis section of the program is Chapter 8-9 Messages:")

text_messages = ['hello world!', 'i like coding in python :)', 'routines are great exercise']

def show_message(list_messages):
    for message in list_messages:
        print(f"{message.title()}")

show_message(text_messages)



# SECTION - 8-10: Sending Messages 
    #

















 





