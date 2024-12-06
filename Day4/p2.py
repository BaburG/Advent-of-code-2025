data = []

with open('input.txt') as file:
    lines = file.readlines()
    for line in lines:
        row = list(line.strip())
        data.append(row)




starts = []

for i in range(1, len(data)-1):
    for j in range(1, len(data[0])-1):
        if data[i][j] == "A":
            starts.append((i,j))

print(starts)

sum = 0


for x,y in starts:
    corners = data[x-1][y-1] + data[x+1][y-1] + data[x+1][y+1] + data[x-1][y+1]
    if corners in ["MMSS","SMMS", "SSMM", "MSSM"]:
        sum += 1

print(sum)