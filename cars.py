# This Exercise, we are learning sorting elements in a list
    # sort() method vs. sorted() function
    
marvel_hero_names = ['captain america', 'iron man', 'thor', 'hulk', 'black widow', 'hawkeye']
print("\nHere is the original sorted list:")
print(marvel_hero_names)

# sort() method will PERMANETLY sort list

# marvel_hero_names.sort()
# print(marvel_hero_names)


# marvel_hero_names.sort(reverse=True)
# print(marvel_hero_names)


# sorted() function will TEMPORARYOLY sort the list, but values at original positions
print("\nHere is the sorted() function list:")
print(sorted(marvel_hero_names))


print("\nHere is the original sorted list:")
print(marvel_hero_names)

print("\nHere is the sorted() function list in reverse:")
print(sorted(marvel_hero_names, reverse=True))
    # REMEMBER: For functions, you will need to pass arguments in parameters. NOT SAME as methods.
    
print("\nHere is the original sorted list:")
print(marvel_hero_names)