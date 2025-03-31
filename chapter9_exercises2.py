# For this program, we will be focused on completing the exercises in
# for Chapter 9 Inheritance
    # This program has been completed by Michael Taufa.

print("\nThis is SECTION 9-6: Ice Cream Stand")

# SECTION - Exercise 9-6: Ice Cream Stand
    # Write a class called 'IceCreamStand' that inherits from class Restaurant class
    # Add an attribute called 'flavors' for ice cream flavors
    # Create method() that displays flavors of ice cream flavors 
    # Create an instances of IceCreamStand and call method

class Restaurant():
    def __init__(self, restaurantName, location):
        self.restaurantName = restaurantName
        self.location = location


class IceCreamStand(Restaurant):
    def __init__(self, restaurantName, location):
        super().__init__(restaurantName, location)
        self.ice_creamFlavors = ['chocolate', 'vanilla', 'strawberry']


    def display_iceCreamFlavors(self):
        print("\nThis is the following available ice cream flavors:")

        for flavor in self.ice_creamFlavors:
            print(f"{flavor.title()}")

        print("Contact Store Manager to request more ice cream flavors.")

baskin_robins = IceCreamStand('baskin robins', 'dallas, tx')
print(baskin_robins.restaurantName.title())
print(baskin_robins.location.title())
baskin_robins.display_iceCreamFlavors()


print("\nThis is SECTION 9-7: Admin")
# SECTION - Exercise 9-7: Admin
    # Create class Admin that inherits User Class
    # Add attribute 'Privileages' that stores list
        # List = ['can add post', 'can delete post', 'can ban user']
        # Create a method that will display all Privileages
    # Create an instances and call method


class User():
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def display_userName(self):
        print(f"{self.firstName.title()} {self.lastName.title()}")


class special_Privileges():
    def __init__(self, privileges = ['Add Post', 'Delete Post', 'Ban User']):
        self.privileges = privileges 

    def display_specialPrivileages(self):

            print("The following is all Special Privileages:")

            for privileage in self.privileges:
                print(f"-{privileage}")


class Admin(User):
    def __init__(self, firstName, lastName, age):
        super().__init__(firstName, lastName, age)
        self.privileages = ['Can add posts', 'Can delete post', 'Can ban user']
        self.special = special_Privileges()

    def display_adminPrivileages(self):

        print("The following is all Admin Privileages:")

        for privileage in self.privileages:
            print(f"-{privileage}")

master_admin = Admin('michael', 'smith', 25)
master_admin.display_adminPrivileages()


print("\nThis is SECTION 9-8: Privileages")
# SECTION - Exercise 9-8: Privileages
    # Write a seperate Privileges class as an Instance
    # Store a list of strings similar to 9-7

special_admin = Admin('john', 'lee', 30)
special_admin.special.display_specialPrivileages()


print("\nThis is SECTION 9-9: Battery Upgrade")
# SECTION - Exercise 9-9: Battery Upgrade
    # Use final version of electric car class
    # Add method to Battery() called 'upgrade battery()
        # Check 'battery_size' and set capcitiy to '85'


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_formatCarName(self):
        print(f"{self.year} {self.make.title()} {self.model.title()}")


class electric_Car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()



class Battery():
    def __init__(self, battery_size = 50):
        self.battery_size = battery_size

    def display_batterySize(self):
        print(f"Battery: {self.battery_size}%")

    def display_rangeMiles(self):
        if self.battery_size <= 85:
            miles = 150
            print(f"Battery: {self.battery_size}% range is {miles} miles.")
        elif self.battery_size >= 85:
            miles = 300 
            print(f"Battery: {self.battery_size}% range is {miles} miles.")

    def upgrade_battery(self):
        if self.battery_size <= 85:
            self.battery_size = 85
            print(f"Battery is upgraded to {self.battery_size}.")
        else:
            print(f"Battery upgraded is not needed.")


my_firstEV = electric_Car('tesla', 'model y', 2014)

my_firstEV.battery.display_rangeMiles()

my_firstEV.battery.upgrade_battery()

my_firstEV.battery.display_rangeMiles()


print("\nProgram: Chapter 9 Exercises 2 is completed.")
