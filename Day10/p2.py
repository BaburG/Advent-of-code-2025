with open("input.txt") as file:
    grid = [line for line in file.read().splitlines()]


rows = len(grid)
cols = len(grid[0])


q = []


for row in range(rows):
    for col in range(cols):
        if grid[row][col] == "0":
            q.append((row, col, 0))


print(q)

count = 0

while q:
    r, c, num = q.pop()
    if num == 9:
        count += 1
        continue
    for dr in [ r - 1 , r + 1]:
        if 0 <= dr < rows:
            if grid[dr][c] != "." and int(grid[dr][c]) == num+1:
                q.append((dr, c, num+1))
    for dc in [ c - 1 , c + 1]:
        if 0 <= dc < cols:
            if grid[r][dc] != "." and int(grid[r][dc]) == num+1:
                q.append((r, dc, num + 1))


print(count)
    
