# Chapter 4: Working with List
    # For this chapter, we will be learning for loops, similar to for/ while loops  in JavaScript and C.
    
    # Using 'for loops' it is important to declare/ intialize a variable relative to the list (Singular vs Plural)
    # Also, curly braces is replaced with indents/ indentations
    # Example: list = cats, variable = cat, list = yugioh_monsters, variable = yugioh_monster_name

magicians = ['dark magician', 'dark magician girl', 'dark magician of chaos']
for magician_names in magicians:
    print(f"{magician_names.title()}, that was a great trick!")
    print(f"Now, {magician_names.title()} attack directly!\n")
    

    
yugioh_dragons = ['blue eyes white dragon', 'red eyes black dragon', 'blue eyes ultimate dragon']
for dragon_name in yugioh_dragons:
    print(f"I summon the {dragon_name.title()} in attack position!")
    print(f"{dragon_name.title()}, use your dragon breath and attack directly!\n")
    
# This print() statement shows end of program.
print("All the Magicians and Dragons have finished!\n")