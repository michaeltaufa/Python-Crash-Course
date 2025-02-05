# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#   This program is design to build a list, sor in a 'for loop', and test on 'conditional statements'
#       Disclaimer: Conditional Statements have not been studied for Python. 
#       This program will test all the knowledge I have learned from python and applied.
#
#   This program has been created by Michael Taufa
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

print("\n\nThis is the start of the 'Project1' program.\n")

number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_under = []
number_over = []

print("'for loop' has started.\n")

for value in number_list:
    if value >= 6:
        number_over.append(value)
    elif value < 5:
        number_under.append(value)

print("'for loop' has been completed.\n")

if number_under == [0, 1, 2, 3, 4] and number_over == [5, 6, 7, 8, 9, 10]:
    print("Values have been successfully added to new list:\n")
    print(f"Success: This is the values for number_over: {number_over}.\n")
    print(f"Success: This is the values for number_under: {number_under}.\n")
elif number_over == [5, 6, 7, 8, 9, 10]:
    print(f"Warning: values for number_over: {number_over} Completed!")
    print("Error: 'number_under' did not successfully append.\n")
elif number_under == [0, 1, 2, 3, 4]:
    print(f"Warning: values for number_under: {number_under} Completed!")
    print("Error: 'number_over' did not successfully append.\n")

print("This is the end of the 'Project1' program.\n")