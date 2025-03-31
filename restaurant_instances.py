# This program will be focused on importing a class for
# Exercise 9-10 to practice importing classes

import restaurant_class_modules

print("\nThis is the start of the program for Exercise 9-10: Imported Restaurant")

iceCream_shop1 = restaurant_class_modules.IceCreamStand('coldstones', 'san francisco, ca') 

print(iceCream_shop1.restaurantName.title())
print(iceCream_shop1.display_iceCreamFlavors())

print("\nThis is the end of the program for Exercise 9-10: Imported Restaurant")
