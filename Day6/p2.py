with open("input.txt") as file:
    grid = list(map(list,file.read().splitlines()))




for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "^":
            start = (r,c,-1,0)



r, c, dr, dc = start

path = set()


while True:
    path.add((r,c))
    if 0 > r + dr  or r + dr >= len(grid) or 0 > c + dc or c + dc >= len(grid[0]): break
    if grid[r + dr][c + dc] == "#":
        dc, dr = -dr, dc
    r += dr
    c += dc


r, c, dr, dc = start





def loopcheck(grid, start):
    cr, cc, cdr, cdc = start

    seen = set()

    while True:
        seen.add((cr,cc,cdr,cdc))
        if 0 > cr + cdr  or cr + cdr >= len(grid) or 0 > cc + cdc or cc + cdc >= len(grid[0]):
            return False
        if grid[cr + cdr][cc + cdc] == "#":
            cdc, cdr = -cdr, cdc
        else:
            cr += cdr
            cc += cdc
        if (cr,cc,cdr,cdc) in seen:
            return True

count = 0

for x,y in path:
    #if grid[x][y] == ".":
    grid[x][y] = "#"
    if loopcheck(grid, start): 
        count += 1
    grid[x][y] = "."




print(count)