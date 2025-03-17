# For this program, we will be focused on completing Chapter 9
# exercise for Classes.
    # This program has been created by Michael Taufa.

# SECTION 9-1 Restaurant:
    # Make a class called Restaurant
    # Attributes: Restaurant Name, Cuisine Type
    # Methods:
        # describe_restairant = print attributes
        # open_restaurant = print restaurant is open

print("\nSection 9-1 Restaurant:")

class Restaurant:
    def __init__ (self, restaurantName, cuisineType):
        self.restaurantName = restaurantName
        self.cuisineType = cuisineType

    def describe_restaurant(self):
        print(f"The restuarant's name is {self.restaurantName.title()} that serves {self.cuisineType.title()}.")

    def open_restaurant(self):
        print(f"{self.restaurantName.title()} is open.")

restaurant1 = Restaurant('mcdonalds', 'american fast food')

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

# SECTION 9-2 Three Restaurants:
    # Create (3) different instances from the class
    # Call describe_restaurant() for each restaurant

print("\nSection 9-2 Three Restaurant:")

restaurant2 = Restaurant('santos', 'japanesse')
restaurant3 = Restaurant('town', 'american diner')
restaurant4 = Restaurant('cha cha cha', 'carribean')

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3.describe_restaurant()
restaurant3.open_restaurant()

restaurant4.describe_restaurant()
restaurant4.open_restaurant()

# SECTION 9-3 Users:
    # Make class called User
    # Create (2) attributes: firstName, lastNamea
    # Add several other attributes required in a profile

    # Methods:
        # Create method that describes User 
        # Create a method that greet the User 

    # Lastly, create several instances and call both methods for each user

print("\nSection 9-3 Users:")

class User:

    def __init__(self, firstName, lastName, age, location, favoriteFood):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.location = location
        self.favoriteFood = favoriteFood

    def describe_user(self):
        gender = ''

        if (self.firstName == 'james') or (self.firstName == 'kim'):
            gender = 'he'
        else:
            gender = 'she'

        print(f'\nThis is {self.firstName.title()} {self.lastName.title()}.')
        print(f'{gender.title()} is located in {self.location.title()} and is age {self.age}.')


    def greet_user(self):
        print(f"Good afternoon and Welcome {self.firstName.title()} {self.lastName.title()}!")


user1 = User('james', 'smith', 28, 'dallas, tx', 'pizza')
user2 = User('sara', 'conley', 52, 'san francisco, ca', 'sushi')
user3 = User('kim', 'lee', 34, 'los angeles, ca', 'french fries')


user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()


user3.describe_user()
user3.greet_user()





