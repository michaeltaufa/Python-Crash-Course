"""
╔════════════════════════════════════════════════════════════════╗
║                    Python Script Template                      ║
╠════════════════════════════════════════════════════════════════╣
║  Author      : Michael Hikuleomtaufa                           ║
║  Created     : 2025-04-14                                      ║
║  Modified    : 2025-04-14                                      ║
║  Description : Program is focused on reading files.            ║
╚════════════════════════════════════════════════════════════════╝
"""
from pathlib import Path
import json

path = Path('NEW_numbers.json')

content = path.read_text()
numbers = json.loads(content)


print(f"\nThe following below is printed from {path}.")
print(numbers)
