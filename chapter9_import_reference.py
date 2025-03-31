# For this proggram, we will be focused on learning how to import classes that
# is similar 'importing modules/ functions'
    # This program has been created by Michael Taufa


# NOTE: When importing modules/ classes, import file name
    # DON'T worry about file extension: '.txt, .py, etc...'

from chapter9_importingClasses import Car
from chapter9_importingClasses import electricCar 



print("\nThis is instances: 'my_newCar':")
my_newCar = Car('dodge', 'challenger', 2014)
print(my_newCar.display_carName())


print(my_newCar.display_odometer())
my_newCar.odometer = 100
print(my_newCar.display_odometer())



print("\nThis is instances: 'my_electricCar':")

my_electricCar = electricCar('tesla', 'model y', 2018)
print(my_electricCar.display_carName())
print(my_electricCar.battery.display_RangeMiles())
