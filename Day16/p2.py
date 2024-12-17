import heapq
from collections import deque

grid = [list(line) for line in open('input.txt').read().splitlines()]

rows = len(grid)
cols = len(grid[0])

for row in range(rows):
    for col in range(cols):
        if grid[row][col] == "E":
            end = (row,col)
        if grid[row][col] == "S":
            start = (row,col)


sr, sc = start
lowest_cost = {(sr, sc, 0, 1):0}
pq = [(0, sr, sc, 0, 1)]
best_cost = float("inf")
backtrack = {}
ends = set()


while pq:
    cost, r, c, dr, dc = heapq.heappop(pq)
    
    if cost > lowest_cost.get((r,c,dr,dc), float("inf")): continue
    
    if (r,c) == end:
        if cost > best_cost: break
        best_cost = cost
        ends.add((r,c,dr,dc))
    for ccost, cr, cc, cdr, cdc in [(cost + 1, r + dr, c + dc, dr,dc), (cost + 1000, r, c, -dc, dr), (cost + 1000, r, c, dc, -dr)]:
        if grid[cr][cc] == "#": continue
        if ccost > lowest_cost.get((cr, cc, cdr, cdc), float("inf")): continue
        if ccost < lowest_cost.get((cr, cc, cdr, cdc), float("inf")):
            backtrack[(cr, cc, cdr, cdc)] = set()
            lowest_cost[(cr, cc, cdr, cdc)] = ccost
        backtrack[(cr, cc, cdr, cdc)].add((r,c,dr,dc))
        heapq.heappush(pq, (ccost, cr, cc, cdr, cdc))


states = deque(ends)
seen = set(ends)

while states:
    key = states.popleft()
    for last in backtrack.get(key, []):
        if last in seen: continue
        seen.add(last)
        states.append(last)

print(len({ (r,c) for r,c, _ ,_ in seen}))