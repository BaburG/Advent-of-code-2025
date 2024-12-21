grid = [line for line in open("input.txt").read().splitlines()]

#print(*grid, sep="\n")

rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "S":
            break
    else:
        continue
    break

distances = [[-1] * cols for _ in range(rows)]
distances[r][c] = 0

q = [(r,c)]

while q:
    cr, cc = q.pop(0)
    for nr, nc in [(cr+ 1,cc), (cr-1,cc), (cr,cc+1), (cr,cc-1)]:
        if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
        if grid[nr][nc] == "#": continue
        if distances[nr][nc] != -1: continue
        distances[nr][nc] = distances[cr][cc] + 1
        q.append((nr,nc))

count = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "#": continue
        for radius in range(2, 21):
            for dr in range(radius + 1):
                dc = radius - dr
                for nr, nc in {(r+dr,c+dc), (r+dr, c-dc), (r-dr, c+dc), (r-dr, c-dc)}:
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
                    if grid[nr][nc] == "#": continue
                    if distances[r][c] - distances[nr][nc] >= 100 + radius:
                        count += 1

print(count)
#print(*distances, sep='\n')