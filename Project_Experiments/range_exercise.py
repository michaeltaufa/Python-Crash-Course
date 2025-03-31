# This program will practice the function 'range()' when handling in a 'for loop'

    # The 'range()' will print series of numbers, but 'off by 1' due to index position.

for numbers in range(0,6):
    print(f"This is the {numbers} iteration.")
print("This is the end of the 'for loop'.\n")

    # Pass '1' argument in 'range() function'    

for numbers in range(4):
    print(f"'One Arguement Test': This is the {numbers} iteration.")
print("This is the end of the 'One Argument Test'.\n")

    # The 'list() function' wrapped in a range() function can fill out a list (array)

random_list_of_numbers = list(range(0, 100, 10))
for numbers in random_list_of_numbers:
    print(numbers)
print(f"This is the total list: {random_list_of_numbers}.\n")

final_squareroot = []
for values in range(0, 11):
    square = values ** 2 # Created temporary variable to store value in range
    final_squareroot.append(square)
    print(final_squareroot)
print(f"This is the final list: {final_squareroot}.\n")

    # Simple Statistics can be practiced with Python using min(), max(), and sum(), and can create function for averages.

data_digits = [5, 9, 23, 0, -4, 77, 1000, 523, -45]
print(f"This is the list of data_digits: {data_digits}.")
print(f"This is the min values: '{min(data_digits)}'.")
print(f"This is the max value: '{max(data_digits)}'.")
print(f"This is the sum of all values: '{sum(data_digits)}'.")
average_data_digits = round(sum(data_digits)/len(data_digits))
print(f"This is the average for list 'data_digits': '{average_data_digits}'.\n")