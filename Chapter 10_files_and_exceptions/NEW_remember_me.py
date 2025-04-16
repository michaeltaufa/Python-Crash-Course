"""
╔════════════════════════════════════════════════════════════════╗
║                    Python Script Template                      ║
╠════════════════════════════════════════════════════════════════╣
║  Author      : Michael Hikuleomtaufa                           ║
║  Created     : 2025-04-15                                      ║
║  Modified    : 2025-04-15                                      ║
║  Description : Program is focused on practicing json module.   ║
╚════════════════════════════════════════════════════════════════╝
"""
from pathlib import Path
import json

path = Path('username.json')

if path.exists():
    content = path.read_text()
    username = json.loads(content)
    print(f"Welcome back {username.title()}!")

else:
    print("Welcome to the 'remember_me' Program.")
    username = input("Type and enter your name: ")

    content = json.dumps(username) 
    path.write_text(content)


print("End of program.")
