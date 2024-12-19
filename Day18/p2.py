mem = [list(map(int, line.split(","))) for line in open("input.txt").read().splitlines() ]

size = 70


def check(n):

    grid = [[0] * (size + 1) for _ in range(size + 1)]

    for i in range(n):
        c, r = mem[i]
        grid[r][c] = 1


    seen = {(0,0)}
    queue = [(0,0)]

    while queue:
        r, c = queue.pop(0)
        if r == c == size:
                return True
        for cr, cc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
            if cr < 0 or cc < 0 or cr > size or cc > size: continue
            if (cr, cc) in seen: continue
            if grid[cr][cc] == 1: continue
            seen.add((cr,cc))
            queue.append((cr,cc))

    return False

# # Brute Force
# for i in range(len(mem)):
#     if not check(i):
#         print(*mem[i-1], sep=',')
#         break


#Binary Search
low = 0
high = len(mem) - 1
while low < high:
    mid = (low + high) // 2
    if check(mid):
         low = mid + 1
    else:
         high = mid
print(*mem[low-1], sep=',')
