# For this proggram, we will be focused on learning how to import classes that
# is similar 'importing modules/ functions'
    # This program has been created by Michael Taufa

# Reference the file 'chapter9_import_reference.py'

# This porgram will be focused on creating the program based on 'imported classes'
# from 'chapter9_importingClasses.py'
    # NOTE: File names are important! Make sure these names are reflective!


# Parent Class:
    # Car

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def display_carName(self):
        message_carName = f"{self.year} {self.make} {self.model}"

        return message_carName.title()

    def display_odometer(self):
        message_odometer = f"{self.odometer} miles"

        return message_odometer


# Attributes:
    # Tires
    # Battery

class Tires:
    def __init__(self, tire_size = 30, tire_PSI = 40):
        self.tire_size = tire_size 
        self.tire_PSI = tire_PSI 

    def display_tirePSI(self):
        message_tirePSI = f"Tire Pressure: {self.tire_PSI} PSI"

        return message_tirePSI

class Electric_Battery:
    def __init__(self, battery_size = 0, battery_energyLevel = 100):
        self.battery_size = battery_size 
        self.battery_energyLevel = battery_energyLevel 

    def display_batteryEnergy(self):
        message_batteryEnergyLevel = f"Battery: {self.battery_energyLevel}"

        return message_batteryEnergyLevel

    def display_RangeMiles(self):

        if self.battery_energyLevel == 100:
            range_miles = 350
        elif self.battery_energyLevel == 50:
            range_miles = 125
        else:
            range_miles = 0

        message_rangeMiles = f"Battery: {self.battery_energyLevel}%\n{range_miles} miles"

        return message_rangeMiles

# Child Classes:
    # Electric Car 

class electricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Electric_Battery()
        self.tires = Tires()
