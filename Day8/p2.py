file = open("input.txt")

grid = []

for line in file.readlines():
    grid.append(line.strip())

rows = len(grid)
cols = len(grid[0])

nodes = {}

for i, line in enumerate(grid):
    for j, ch in enumerate(line):
        if ch == ".": continue
        if ch not in nodes:
            nodes[ch] = []
        nodes[ch].append((i,j))


antinodes = set()

for list in  nodes.values():
    for i in range(len(list)):
        for j in range(len(list)):
            if i == j: continue
            r1, c1 = list[i]
            r2, c2 = list[j]
            
            dr = r2 - r1
            dc = c2 - c1

            r = r1
            c = c1

            while 0 <= r < rows or 0 <= c < cols:
                antinodes.add((r,c))
                r += dr
                c += dc


sum = 0


for r,c in antinodes:
    if 0 <= r < rows and 0 <= c < cols:
        sum += 1


print(sum)