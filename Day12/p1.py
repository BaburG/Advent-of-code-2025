

grid = [list(row) for row in open("input.txt").read().splitlines()]

rows = len(grid)
cols = len(grid[0])

seen = set()

regions = []

for row in range(rows):
    for col in range(cols):
        if (row,col) in seen: continue
        seen.add((row,col))
        ch = grid[row][col]
        queue = [(row,col)]
        region = {(row,col)}
        while queue:
            r, c = queue.pop(0)
            region.add((r,c))
            for cr, cc in [(r + 1, c), (r - 1, c), (r, c +1), (r, c -1)]:
                if 0 <= cr < rows and 0 <= cc < cols:
                    if grid[cr][cc] == ch and (cr,cc) not in region:
                        region.add((cr,cc))
                        queue.append((cr,cc))
        seen |= region
        regions.append(region)





def calc_perimeter(region):
    ans = 0
    for slot in region:
        ans += 4
        r, c = slot
        for cr, cc in [(r + 1, c), (r - 1, c), (r, c +1), (r, c -1)]:
            if (cr, cc) in region:
                ans -= 1
    
    return ans


print(sum(len(region) * calc_perimeter(region) for region in regions))