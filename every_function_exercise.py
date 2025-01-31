# 3-10: Every Function
    # For this exercisem create a list of anything and use all functions and methods introduced in Chapter 3:
    # Part 1:
        # Functions:
            # len(), sorted(), 'del statement'

    # Part 2:
        # Methods:
            # append(), insert(), pop(), remove(), sort(), reverse()
            
            
programming_languages = ['javascript', 'python', 'lua', 'C++', 'java']
print(f"\nThe total number of programming languages I want to learn is {len(programming_languages)}.")

print(f"\nThe programming languages I want to learn is {sorted(programming_languages)}.")

del programming_languages[0]
del programming_languages[0]
del programming_languages[0]
del programming_languages[0]
del programming_languages[0]
print(len(programming_languages))

programming_languages.append('python')
programming_languages.append('C++')
programming_languages.append('C')
programming_languages.append('javascript')
programming_languages.insert(2, 'java')
programming_languages.insert(1, 'C#')
print(f"\nI want to learn these languages: {programming_languages}.")

languages_not_interested = programming_languages.pop(1), programming_languages.pop(2)
print(f"\nI am not interested in learning these languages: {languages_not_interested}.")
print(f"\nI want to learn these languages: {programming_languages}.")


ignore_languages = programming_languages.remove('javascript'), programming_languages.remove('C++') # remove() will not store value
print(f"\nI want to ignore these languages: {ignore_languages}.") # Returns 'None'

print(f"\nI want to focus on these languages: {programming_languages}.")
programming_languages.reverse()
print(programming_languages)