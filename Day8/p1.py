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
        for j in range(i+1, len(list)):
            r1, c1 = list[i]
            r2, c2 = list[j]
            dr = r2 - r1
            dc = c2 - c1
            antinodes.add((r1-dr, c1-dc))
            antinodes.add((r2+dr, c2+dc))

sum = 0


for r,c in antinodes:
    if 0 <= r < rows and 0 <= c < cols:
        sum += 1


print(sum)