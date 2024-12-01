
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

sum = 0

for i in range(len(right)):
    sum = sum + abs(left[i] - right[i])

print(sum)