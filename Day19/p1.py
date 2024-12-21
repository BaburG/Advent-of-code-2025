from functools import cache

lines = open("input.txt").read().splitlines()

patterns = set(lines[0].split(", "))
max_len = max(map(len, patterns))

@cache
def obtainable(design):
    if design == "": return True
    for i in range(min(len(design), max_len) + 1):
        if design[:i] in patterns and obtainable(design[i:]):
            return True
    #print("NOT POSSIBLE")
    return False

count = 0
total = len(lines[2:])

for i, design in enumerate(lines[2:]):
    if obtainable(design):
        count += 1
    #print()

print(count)