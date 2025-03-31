# This program is an exercise to practice adding, removing, and modifying elements within a list.


vehicles_owned_lifetime = []
vehicles_owned_lifetime.append('Isuzu Rodeo')
vehicles_owned_lifetime.append('Dodge Challenger')
vehicles_owned_lifetime.append('Chevrolet Camaro')
vehicles_owned_lifetime.append('Chrysler Town & County')

print(f"These were the vehicles I owned: {vehicles_owned_lifetime}. After reviewing my list, I realized that I did not own a '{vehicles_owned_lifetime[2]}'. I will make the corrections.\n")

del vehicles_owned_lifetime[2]
print(f"Here is the updated list on the cars I have owned {vehicles_owned_lifetime}.\n")

traded_car = vehicles_owned_lifetime.pop(0)
print(f"Here is an updated list of the cars in my lifetime: {vehicles_owned_lifetime}. {traded_car} was removed because it was traded to my aunt.\n")

accident_car = vehicles_owned_lifetime.pop(0)
print(f"The last update that I will need to make is that the '{accident_car}' was involved into an accident. Here is the updated list of current vehicles I am driving: {vehicles_owned_lifetime}.")


print(f"I want to trade-in my {vehicles_owned_lifetime} for a dream car.")

vehicles_owned_lifetime[0] = 'Tesla Model Y'

print(f"The dream car I would like to own is {vehicles_owned_lifetime}.")


# Review Notes:
    # 1. pop() and 'del' statment is identical in terms of removing elements, BUT most important takeaway is the using pop() method can store and reuse elements VS. 'del' elements permanently
    
    # 2. append() works like magic and can dynamically add elements in a list 'unsorted', but list is able to store multiply values within a list
    
    # 3. Don't forget that pop() will remove elements at the end of the list, providing a more dynamic programming.
    
    # 4. 'f strings' is powerful to get accurate input/ output from variable/ list changes.
    
    # 5. You can modify list through 'dream_car = list[0]', but you cannot store values similar to pop() because the changes is permanent.