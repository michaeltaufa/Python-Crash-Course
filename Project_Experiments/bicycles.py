# Lesson: List
    #This lesson focus on creating/ accessing lists on Python.

bicycles = ['white bicycle', 'red bicycle', 'blue bicycle', 'green bicycle']

print(f"{bicycles}")
print(bicycles[0].upper(), bicycles[1].title(), bicycles[2].title())
print(f"This is the first element in the list: {bicycles[1].title()}.\n")

# Special Syntax: Access last element
    # To access last element, use '-1'
    # Also, intervals of '-1' will access elements in a list backwards

fruit = ['apple', 'mango', 'kiwi', 'pineapple', 'blueberry', 'strawberry', 'banana', 'watermeleon']
special_syntax = '-1'
fruit_message = f"\nTo access the last element in the list: {fruit[-1].title()}, I would need\nto utilize the special syntax {special_syntax}.\n"

print(fruit_message)