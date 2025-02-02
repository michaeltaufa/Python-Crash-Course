# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
#   This program has been created by Michael Taufa.
#
#   This program is to test the 'for loop' and 'range() function':
#       # 1.
#           # The magicians program shows the last value that is saved at the end of the 'for loop' AFTER
#           # the loop has finished.
#        
#       # 2.
#           # The number_range, number_ list is to test the output of 'range() function'
#           # print(range()) will print the output of range()
#           #           VS.
#           # print(list(range())) will print the list of all values within the range()
#       # 3.
#           # The last part of the program consist of executing the exercises provided in the 'for loop' and 'range() function'.
#           # The difficult concept to grasp is 'list comprehension', where generate a list in "one line of code"
#           # Key takeaway is to think key word 'list', syntax is same + simplify lines of code
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

print("This is the start of the 'magicians for loop' program.")

magicians = []
magicians.append('James')
magicians.append('Sarah')
magicians.append('Cat')

for names in magicians:
    print(names)
print(f"This is the last output for variable: 'names' = '{names}'.\n")

magicians.append('Tom')

for names in magicians:
    print(names)
print(f"This is the last output for variable: 'names' = '{names}'.")

print("This is the end of the 'magicians for loop' program.\n")

print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
print("This is the start of the 'range test' program:\n")

number_range = range(0,6)
number_list = list(range(0,6))

for value in number_range:
    print(value)
print(f"This is the end of 'number_range. This is the value: {number_range}.\n")
    
for value in number_list:
    print(value)
print(f"This is the end of 'number_list. This is the value: {number_list}.\n")

print("This is the end of the 'range test' program.")
print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
print("This is the last section of the program to execute exercise programs in Python Crash Course.\n\n")

exercise_set = list(range(0,21))
for value in exercise_set:
    print(value)
print("This is the end of the 1st exercise.\n")

# exercise_set = list(range(0,1_000_001))
# for value in exercise_set:
    # print(value)
# print("This is the end of the 2nd exercise.\n")

for value in exercise_set:
    print(value)
print(f"The minimum value is: {min(exercise_set)}.")
print(f"The maximum value is: {max(exercise_set)}.")
print(f"The sum of range(0,1_000_000) is: {sum(exercise_set)}.")
print("This is the end of the 3rd exercise.\n")

exercise_set = list(range(1, 21, 2))
for value in exercise_set:
    print(value)
print("This is the end of the 4th exercise.\n")

exercise_set = list(range(3, 31, 3))
for value in exercise_set:
    print(value)
print("This is the end of the 5th exercise.\n")

cube_set = list(range(0,11))
for value_cube in cube_set:
    cube = value_cube ** 3
    print(cube)
print("This is the end of the 6th exercise.\n")

# This is the hardest concept to understand and master.
    # List comprehension is condensing the for loop into 2 lines of code. Is this 'refectoring'?
cube_comprehension = [value * 3 for value in range(0,11)]
print(cube_comprehension)
print("This is the end of the 7th exercise.\n")