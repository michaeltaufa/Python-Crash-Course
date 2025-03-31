# For this program, we will be focused learning and understanding the
# concepts of 'Inheritance'.
    # This program has been created by Michael Taufa.

# SECTION - The '__init__' Method for a Child Class

print("\nFor this section will be focused on '__init__' Method for child class.")

    # The class 'Car' will be known as the 'Parent Class'.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptiveName(self):
        long_name = f'{self.year} {self.make} {self.model}'

        return long_name.title()

    def read_odometer(self):
        print(f"This vehicle has {self.odometer} miles.")

    def update_odometer(self, new_mileage):

        if self.odometer < new_mileage:
            self.odometer = new_mileage
        elif self.odometer == new_mileage:
            print("The mileage is {self.odometer} and will not change.")
        else:
            print("New mileage: {new_mileage} can't be rolled back.")

        return self.odometer

    def increment_odometer(self, miles):
        self.odometer += miles

        return self.odometer


    # We will focus on building a 'Child Class' based on the parent class
        # When creating a 'Child Class', you will need the following:
            # 1. Adding new attributes is similar to classes
                # NOTE: will need to add it to the "__init__"

            # 2. When creating new method, it is similar to clases

class Battery():
    def __init__(self, battery_size):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size} -kwh battery.")


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = Battery()


my_diselTruck = Car('dodge', 'ram', 2009)
print("\nThis is the output of the 'Parent Class':")
print(my_diselTruck.get_descriptiveName())


my_spaceX_car = ElectricCar('tesla', 'model y', 2020)
print("\nThis is the output of the 'Child Class':")
print(my_spaceX_car.get_descriptiveName())

my_spaceX_car.battery_size.describe_battery()


my_evCar = ElectricCar('rivion', 'x', 2025)
print("\nThis is the output of the 'Child Class':")
print(my_evCar.get_descriptiveName())


