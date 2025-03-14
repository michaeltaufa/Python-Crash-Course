# For this program, we will be focused on building modules and importing
# to other files.
    # This program has been created Michael Taufa

def build_pizza(size, *toppings):
    print(f"\nBelow is the toppings for the {size}' pizza that is going to be created: ")

    for topping in toppings:
        print(f"- {topping.title()} has been added")

    print("Pizza is complete!")

