mem = [list(map(int, line.split(","))) for line in open("input.txt").read().splitlines() ]

size = 70
n = 1024

grid = [[0] * (size + 1) for _ in range(size + 1)]

for i in range(n):
    c, r = mem[i]
    grid[r][c] = 1

seen = {(0,0)}
queue = [(0,0,0)]

while queue:
    r, c, s = queue.pop(0)
    if r == c == size:
            print(s)
            break
    for cr, cc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
        if cr < 0 or cc < 0 or cr > size or cc > size: continue
        if (cr, cc) in seen: continue
        if grid[cr][cc] == 1: continue
        seen.add((cr,cc))
        queue.append((cr,cc,s+1))
