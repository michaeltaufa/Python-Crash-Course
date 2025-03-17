# For this program, we will cover learning how to build classes and
# Object Oriented Program for Python.
# Lasty, we will learn how to import classes, similar to importing modules
    # This program has been created by Michael Taufa


# SECTION - Creating and Using Classes
    # Below is a simple example of creating a class

class Dog:
    # By convention, class names have captial names:

    # This will initialize 'name' and 'age' attributes
        # '__init__' is a special method for class to create and define
        # attributes in classes.

        # __init__ will always start with 'self', followed with other
        # parameters to define attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")
        # Simulate function of dog is sitting.

    def roll_over(self):
        print(f"{self.name} rolled over!")
        # Simulate function of dog is rolling over.


# Now, we will create an instance based on a class that was define above
    # Naming conventions is IMPORTANT.
        # Dog() is a class
        # 'my_dog' is an instance of class 'Dog()'
    
my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age}.")

# To call methods from 'Dog()', first you need to call the following:
    # Name of the instance => 'my_dog'
    # Name of the method => 'sit()' or 'roll_over()'

    # NOTE: Important to initialize 'my_dog' to class
        # Then pass arguments into class

my_dog.sit()
my_dog.roll_over()

print("\nThis next section is focused on practicing making random classes Car.")

# SECTION - Practice making random Classes

class Car:
    # First, initialize the attribute of a class.
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    # Second, we add methods that this class can perform.

    def fastDriving(self):
        print(f"The {self.make.title()} {self.model.title()} is driving fast.") 

    def slowDriving(self):
        print(f"The {self.make.title()} {self.model.title()} is driving slow.") 

# Next, we initialize an instance using class Car.
car1 = Car('toyota', 'tacoma', 'grey')
car2 = Car('tesla', 'model y', 'white')

# Lasty, we can call the instances 'car1' and 'car2'
car2.fastDriving()
car1.slowDriving()

# We can access instances through 'dot notation'
print(f"The {car1.make.title()} {car1.model.title()} color is {car1.color.title()}.")
print(f"The {car2.make.title()} {car2.model.title()} color is {car2.color.title()}.")

print("\nThis next section is focused on another class, Football Sports Team.")

class FootballSportsTeam:

    def __init__(self, city, teamName):
        self.city = city
        self.teamName = teamName

    def team_win(self):
        print(f"The {self.city.title()} {self.teamName.title()} has won!")

    def team_lost(self):
        print(f"The {self.city.title()} {self.teamName.title()} has lost!")


footballTeam1 = FootballSportsTeam('san francisco', '49ers')
footballTeam2 = FootballSportsTeam('los angeles', 'charger')
footballTeam3 = FootballSportsTeam('baltimore', 'ravens')

footballTeam1.team_win()

# print(footballTeam1.team_win())
    # This print statement will do the following:
        # 1. Conduct print statement from function

        # 2. Conduct print statement, result is none because..
            # There are no return statement

footballTeam3.team_lost()
footballTeam2.team_lost()

my_dog.name


print("\nThis next section is focused... ") 











