import functools

file = open("input.txt")

rules = []

for line in file:
    if line.isspace(): break
    rules.append(list(map(int, line.split("|"))))

mem = {}

for x,y in rules:
    mem[(x,y)] = -1
    mem[(y,x)] = 1

def valid(update):
    for i in range(len(update)):
        for j in range(i+ 1, len(update)):
            key = (update[i],update[j])
            if key in mem and mem[key] == 1:
                return False
    return True

def compare(x,y):
    return mem.get((x,y), 0)

sum = 0


for line in file:
    update = list(map(int, line.split(",")))
    if valid(update): continue
    update.sort(key=functools.cmp_to_key(compare))
    sum += update[len(update) // 2]
    



print(sum)