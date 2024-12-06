file = open("input.txt")

rules = []

for line in file:
    if line.isspace(): break
    rules.append(list(map(int, line.split("|"))))

mem = {}

for x,y in rules:
    mem[(x,y)] = True
    mem[(y,x)] = False

def valid(update):
    for i in range(len(update)):
        for j in range(i+ 1, len(update)):
            key = (update[i],update[j])
            if key in mem and not mem[key]:
                return False
    return True

sum = 0

for line in file:
    update = list(map(int, line.split(",")))
    if valid(update):
        sum += update[len(update)//2]

print(sum)