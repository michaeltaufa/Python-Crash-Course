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
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restuarant's name is {self.restaurantName.title()} that serves {self.cuisineType.title()}.")

    def open_restaurant(self):
        print(f"{self.restaurantName.title()} is open.")

    def set_number_served(self, customerServed):
        self.number_served = customerServed

        return self.number_served

    def increment_number_served(self, incrementOrders):
        self.number_served += incrementOrders

        return self.number_served

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
        self.login_attempts = 0

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

    def increment_login_attempts(self, logins):

        if self.login_attempts <= 4:
            self.login_attempts += logins 
        else:
            print("\nLogin attempt has reached a limit of 5!")
            self.login_attempts = 5

        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0

        return self.login_attempts


user1 = User('james', 'smith', 28, 'dallas, tx', 'pizza')
user2 = User('sara', 'conley', 52, 'san francisco, ca', 'sushi')
user3 = User('kim', 'lee', 34, 'los angeles, ca', 'french fries')


user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()


user3.describe_user()
user3.greet_user()


# SECTION 9-4 Number Served:
    # Start program with 9-1
    # Add an attribute called number_served with default value = 0
    # Create an instance, change number, and print

print("\nSection 9-4 Number Served:")

restuarant5 = Restaurant('fogo de chao', 'brazilian steak house') 
print(f"The number of customers has been served is {restuarant5.number_served}.")

restuarant5.number_served = 10
print(f"The number of customers has been served is {restuarant5.number_served}.")

restuarant5.set_number_served(20)
print(f"The number of customers has been served is {restuarant5.number_served}.")

restuarant5.set_number_served(100)
print(f"The number of customers has been served is {restuarant5.number_served}.")

print("\nIncrement methods is being called:")

restuarant5.increment_number_served(200)
print(f"The number of customers has been served is {restuarant5.number_served}.")

restuarant5.increment_number_served(500)
print(f"The number of customers has been served is {restuarant5.number_served}.")

# SECTION 9-5 Login Attempts:
    # Add attribute 'login attempts' to Users
    # Create method focused on 'increments of login attempts' 
    # Create method focused on 'reset login attempts'
    # Create an instance, call increments method several times...
        # print value of login attempts and then call reset login attempts

print("\nSection 9-5 Login Attempts:")

user4 = User('jessie', 'khar', 28, 'dallas, tx', 'ice cream')

print(f"Log in attempt: {user4.login_attempts}")
user4.increment_login_attempts(1)
print(f"Log in attempt: {user4.login_attempts}")
user4.increment_login_attempts(1)
print(f"Log in attempt: {user4.login_attempts}")
user4.increment_login_attempts(1)
print(f"Log in attempt: {user4.login_attempts}")
user4.increment_login_attempts(1)
print(f"Log in attempt: {user4.login_attempts}")
user4.increment_login_attempts(1)
print(f"Log in attempt: {user4.login_attempts}")
user4.increment_login_attempts(1)
print(f"Log in attempt: {user4.login_attempts}")
user4.increment_login_attempts(1)

user4.reset_login_attempts()
print(f"Log in attempt: {user4.login_attempts}")

user4.increment_login_attempts(1)
print(f"Log in attempt: {user4.login_attempts}")
user4.increment_login_attempts(1)
print(f"Log in attempt: {user4.login_attempts}")

user4.reset_login_attempts()
print(f"Log in attempt: {user4.login_attempts}")





