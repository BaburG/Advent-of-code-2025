with open('input.txt') as file:
    chunks = file.read().split('\n\n')
    grid = [list(line) for line in chunks[0].splitlines()]
    commands = "".join(chunks[1].splitlines())

rows = len(grid)
cols = len(grid[0])

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "@":
            start = (i,j)
            break


r, c = start

for command in commands:
    dr, dc = { ">": (0, 1), "^": (-1, 0), "<": (0, -1), "v": (1, 0)}[command]
    infront = [(r,c)]
    cr = r
    cc = c
    go = True
    while True:
        cr = cr + dr
        cc = cc + dc
        if grid[cr][cc] == "O":
            infront.append((cr,cc))
            continue
        if grid[cr][cc] == ".":
            break
        if grid[cr][cc] == "#":
            go = False
            break

    if not go:
        continue
    grid[r][c] = "."
    grid[r + dr][c + dc] = "@"
    if len(infront) > 1:
        lr, lc = infront.pop()
        grid[lr + dr][lc + dc] = "O"
    r += dr
    c += dc


print(sum(100 * i+j for i in range(rows) for j in range(cols) if grid[i][j] == "O"))



