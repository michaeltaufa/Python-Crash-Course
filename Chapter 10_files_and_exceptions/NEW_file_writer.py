"""
╔════════════════════════════════════════════════════════════════╗
║                    JSON File Writer                            ║
╠════════════════════════════════════════════════════════════════╣
║  Author      : Michael Hikuleomtaufa                           ║
║  Created     : 2025-04-14                                      ║
║  Modified    : 2025-04-14                                      ║
║  Description : Program is focused on using the json modules.   ║
╚════════════════════════════════════════════════════════════════╝
"""
from pathlib import Path
import json

numbers = [0, 1, 3, 5, 7, 11]

path = Path('NEW_numbers.json')

# NOTE: json.dumps() will take arugment and "CONVERT" 
contents = json.dumps(numbers)


# NOTE: AND THEN ... write_text() into the path
path.write_text(contents)
