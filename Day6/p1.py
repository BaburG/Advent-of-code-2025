with open("input.txt") as file:
    lines = file.readlines()

obs = []
start = []
startdir = [-1,0]
for row in range(len(lines)):
    for col in range(len(lines[0])-1):
        if lines[row][col] == "#":
            obs.append((row,col))
        elif lines[row][col] == "^":
            start = [row,col]

def turn(ls):
    if ls == [-1,0]:
        return [0,1]
    if ls == [0, 1]:
        return [1,0]
    if ls == [1,0]:
        return [0,-1]
    if ls == [0,-1]:
        return [-1,0]
    
max = len(lines) -1 

dir = startdir
cur = [start[0]+dir[0], start[1]+dir[1]]
sum = 1 

seen = []

print(cur)
while 0 <= cur[0] < max and 0 <= cur[1] < max:
    if (cur[0]+dir[0], cur[1]+dir[1]) in obs:
        dir = turn(dir)
    cur = [cur[0]+dir[0], cur[1]+dir[1]]
    

    print(cur)
    if cur not in seen:
        sum += 1
        seen.append(cur)

print(sum)



print(obs, start, dir)



