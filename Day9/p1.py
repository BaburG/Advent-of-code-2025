disk = []
fileID = 0

file = open("input.txt", "r").read().strip()



for i, ch in enumerate(file):
    x = int(ch)
    if i % 2 == 0:
        disk += [fileID] * x
        fileID += 1
    else:
        disk += [-1] * x


blank = [x for x, ch in enumerate(disk) if ch == -1]

for i in blank:
    while disk[-1] == -1:
        disk.pop()
    if i > len(disk): continue
    if disk[i] != -1: continue
    
    disk[i] = disk.pop()

checksum = sum(i * x for i,x in enumerate(disk))

print(checksum)