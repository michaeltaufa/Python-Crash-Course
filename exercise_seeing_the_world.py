# 3-8 Exercise:
    # For this exercise, I will practice using sorted() function, sort() method(), len(), and reverse.

dream_destinations = ['japan', 'australia', 'united kingdom', 'switzerland', 'tonga']
print("\nThis is the original order:")
print(dream_destinations)

print("\nThis is the 'sorted() function order':")
print(sorted(dream_destinations))

print("\nThis is the original order:")
print(dream_destinations)

print("\nThis is the reverse order by 'sorted() function':")
print(sorted(dream_destinations, reverse=True))

print("\nThis is the original order:")
print(dream_destinations)

print("\nThis is the reversed with the 'revsere() method':")
dream_destinations.reverse()
print(dream_destinations)

print("\nThis is the original order after 'reverse() method':")
dream_destinations.reverse()
print(dream_destinations)

print("\nThis is the alphabetical order by 'sort()':")
dream_destinations.sort() # sort() method will arrange list in alphabetical PERMANETLY
print(dream_destinations)

print("\nThis is the reverse alphabetical order by 'sort()':")
dream_destinations.sort(reverse=True)
print(dream_destinations)

print(f"\nThe total elements in this list is '{len(dream_destinations)}'.")