from pathlib import Path

path = Path('oldSchoolRunescape_1string.txt')
content = path.read_text()

print("\nBelow is the content printed:")
print(content)

print("\nBelow is the content printed from a for loop:")
lines = content.splitlines()
for line in lines:
    print(line)
