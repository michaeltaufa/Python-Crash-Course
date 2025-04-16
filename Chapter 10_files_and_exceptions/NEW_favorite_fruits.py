"""
╔════════════════════════════════════════════════════════════════╗
║                    Python Script Template                      ║
╠════════════════════════════════════════════════════════════════╣
║  Author      : Michael Hikuleomtaufa                           ║
║  Created     : 2025-04-15                                      ║
║  Modified    : 2025-04-15                                      ║
║  Description : Program is focused on user input for fruits.    ║
╚════════════════════════════════════════════════════════════════╝
"""

from pathlib import Path
import json


path = Path('NEW_user_favoriteFruits.json')

user_fruits = []

print("Welcome to the favorite fruits program!")
print("Type 'quit' to exit program.")

program_status = True
while program_status:

    user_favoriteFruits = input("\nType and enter your favorite fruits: ")

    if user_favoriteFruits == 'quit':
        program_status = False
    else:
        user_fruits.append(user_favoriteFruits)
        print(f"{user_favoriteFruits.title()} has been added.")

content = json.dumps(user_fruits)
path.write_text(content)

print("\nProgram has ended.")
