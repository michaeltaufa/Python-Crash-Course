"""
╔════════════════════════════════════════════════════════════════╗
║                    Python Script Template                      ║
╠════════════════════════════════════════════════════════════════╣
║  Author      : Michael Hikuleomtaufa                           ║
║  Created     : 2025-04-15                                      ║
║  Modified    : 2025-04-15                                      ║
║  Description : Program is reading on user input for fruits.    ║
╚════════════════════════════════════════════════════════════════╝
"""

from pathlib import Path
import json

path = Path('NEW_user_favoriteFruits.json')

content = path.read_text()
fruits = json.loads(content)

print(f"The following is the content printed from '{path}':")
print(fruits)
