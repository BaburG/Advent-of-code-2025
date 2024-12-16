expand = { "#" : "##",
            "O" : "[]",
            "." : "..",
            "@" : "@."}

with open('input.txt') as file:
    chunks = file.read().split('\n\n')
    grid = [list("".join(expand[char] for char in line)) for line in chunks[0].splitlines()]
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
    go = True
    for cr, cc in infront:
        nr = cr + dr
        nc = cc + dc
        ch = grid[nr][nc]
        if (nr, nc) in infront: continue
        if ch == "[":
            infront.append((nr,nc))
            infront.append((nr,nc + 1))
            continue
        if ch == "]":
            infront.append((nr,nc))
            infront.append((nr,nc - 1))
        if ch == "#":
            go = False
            break

    if not go:
        continue

    copy = [list(row) for row in grid]
    grid[r][c] = "."
    grid[r + dr][c + dc] = "@"
    for x, y in infront[1:]:
        grid[x][y] = "."
    for x, y in infront[1:]:
        grid[x + dr][y + dc] = copy[x][y]
    r += dr
    c += dc



print(sum(100 * i+j for i in range(rows) for j in range(cols) if grid[i][j] == "["))



