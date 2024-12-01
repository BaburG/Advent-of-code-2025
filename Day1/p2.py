
right = {}
left = []

with open('input.txt') as file:
    lines = file.readlines()
    for line in lines:
        line = line.split("   ")
        left.append(int(line[0]))
        num = int(line[1])
        if num not in right:
            right[num] = 0
        right[num] += 1


sum = 0

for i in range(len(left)):
    if left[i] in right:
        sum = sum + left[i] * right[left[i]]
    

print(sum)