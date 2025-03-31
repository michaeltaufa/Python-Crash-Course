# This program will be focused on importing a class for
# Exercise 9-10 to practice importing classes

class Restaurant:
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


