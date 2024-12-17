import heapq

grid = [list(line) for line in open('test.txt').read().splitlines()]

rows = len(grid)
cols = len(grid[0])

for row in range(rows):
    for col in range(cols):
        if grid[row][col] == "E":
            end = (row,col)
        if grid[row][col] == "S":
            start = (row,col)


sr, sc = start
seen = {(sr, sc, 0, 1)}
pq = [(0, sr, sc, 0, 1)]

while pq:
    cost, r, c, dr, dc = heapq.heappop(pq)
    seen.add((r, c, dr, dc))
    if (r,c) == end:
        print(cost)
        break
    for ccost, cr, cc, cdr, cdc in [(cost + 1, r + dr, c + dc, dr,dc), (cost + 1000, r, c, -dc, dr), (cost + 1000, r, c, dc, -dr)]:
        if grid[cr][cc] == "#": continue
        if (cr, cc, cdr, cdc) in seen: continue
        heapq.heappush(pq, (ccost, cr, cc, cdr, cdc))

print(len(seen))

