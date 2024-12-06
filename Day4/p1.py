data = []

with open('input.txt') as file:
    lines = file.readlines()
    for line in lines:
        row = list(line.strip())
        data.append(row)


max = len(data)

starts = []

for i, row in enumerate(data):
    for j, char in enumerate(row):
        if char == "X":
            starts.append((i,j))

print(starts)

sum = 0


for x,y in starts:
    dirs = [(-1,-1),(-1,0),(0,-1),(-1,1),(1,-1),(1,0),(0,1),(1,1)]
    for i, j in dirs:
        word = "XMAS"
        for k in range(1,4):
            cx = x + i*k
            cy = y + j*k
            
            if cx < 0 or cx >= max or cy < 0 or cy >= max:
                break
            if data[cx][cy] != word[k]:
                break
            if k == 3:
                sum += 1

print(sum)