

file = open("input.txt", "r").read().strip()


files = {}
fileID = 0
blank = []
pos = 0


for i, ch in enumerate(file):
    x = int(ch)
    if i % 2 == 0:
        files[fileID] = (pos, x)
        fileID += 1
    else:
        if x != 0: blank.append((pos, x))
    pos += x


while fileID > 0:
    fileID -= 1
    pos, size = files[fileID]

    for i, (start, length) in enumerate(blank):
        if start >= pos:
            blank = blank[:i]
            break
        if size <= length:
            files[fileID] = (start, size)
            if size == length:
                blank.pop(i)
            else:
                blank[i] = (start+size, length - size)
            break


checksum = 0

for fileID, (pos, size) in files.items():
    for x in range(pos, pos+size):
        checksum += fileID * x

print(checksum)