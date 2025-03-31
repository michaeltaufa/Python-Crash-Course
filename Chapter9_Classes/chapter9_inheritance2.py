# For this program, we will be focused on learning more on inhertiance though
# modifying attributes, creating instances for attributes, and more.
    # This program has been created by Michael Taufa.


class Car(): # 'Parent Class' - Car
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def format_carName(self):
        formatted_name = f"{self.make} {self.model}"

        return formatted_name.title()

myCar = Car('chrysler', 'town & country', 2012)
print(myCar.format_carName())


# SECTION - Instances as attributes
    # GOAL:
        # 1. Create an attribute as an instance
        # 2. Call the attribute into a class to be used.

    # NOTE:
        # IMPORTANT for attributes to as default values to pass arguements
        # when calling the functions and attributes

class Battery():
    def __init__(self, battery_size = 40, battery_level = 100):
        self.battery_size = battery_size
        self.battery_level = battery_level

    def display_batterySize(self):
        message_batterySize = f"The size of the battery is {self.battery_size} -kWh battery."

        return message_batterySize

    def display_batteryLevel(self):
        message_battery_level = f"Battery: {self.battery_level}%"

        return message_battery_level

    def display_rangeMiles(self):
        if self.battery_level == 100:
            miles = 300
        elif self.battery_level <= 50:
            miles = 150

        message_rangeMiles = f"Battery {self.battery_level}% Range: {miles} miles."

        return message_rangeMiles



class Tires():
    def __init__(self, tire_pressure = 60, tire_size = 30):
        self.tire_pressure = tire_pressure
        self.tire_size = tire_size

    def display_tirePressure(self):
        message_tirePressure = f"The pressure of all tires is {self.tire_pressure} PSI."

        return message_tirePressure

    def display_tireSize(self):
        message_tireSize = f"The size of the tires is {self.tire_size}."

        return message_tireSize


class electricCar(Car): # 'Child Class' - Electric Car
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        # When intializing an attribute in a class...
            # 1. 'self.battery' will be a unique attribute name for class
            # 2. When intializing the attribute, call the 'Attribute/ Instances'

        self.battery = Battery()
        self.tires = Tires()

    
my_electricCar = electricCar('tesla', 'model y', 2020)
print(my_electricCar.format_carName())


print("\nThis section will be focused on 'Calling attributes as instances'.\n")
print(my_electricCar.format_carName())
print(my_electricCar.battery.display_batterySize())
print(my_electricCar.battery.display_batteryLevel())
print(my_electricCar.tires.display_tirePressure())
print(my_electricCar.tires.display_tireSize())
print(my_electricCar.battery.display_rangeMiles())
