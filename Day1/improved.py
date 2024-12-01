

right = []
left = []

with open('input.txt') as file:
    lines = file.readlines()
    for line in lines:
        line = line.split("   ")
        left.append(int(line[0]))
        right.append(int(line[1]))

right.sort()
left.sort()

a = [left, right]

print("part 1 ", sum(abs(x-y) for x, y in zip(*a)))

print("part 2 ", sum( x* right.count(x) for x in left))