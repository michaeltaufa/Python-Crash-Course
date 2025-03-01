# Strings

#name = "michael scott, johnny manziel, and miffy woosh"

# The method, '.title()' will change all words within string to be uppercase
# print(name.title())

# print("\nThis is the original string:")
# first_name = "JaCK, MichAEL, saMANTHA, erIC, ANThony\n"
# print(first_name)

# print("This is the lower() method used:")
# print(first_name.lower())

# print("This is the upper() method used:")
# print(first_name.upper())

first_name = "michael"
last_name = "jordan"

full_name1 = f"{first_name} {last_name}"

greeting_message = f"Hello, {full_name1.title()}!"


program_language1 = "JavaScript"
program_language2 = "C"
program_language3 = "Python"

print(f"\nHere is the list of programming languages I have learned:\n\t{program_language1}\n\t{program_language2}\n\t{program_language3}\n")


user_prompt = input(" ")

if user_prompt != " ":
    print(user_prompt)
