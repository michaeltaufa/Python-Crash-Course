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

