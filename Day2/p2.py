with open("input.txt") as file:
    lines = [list(map(int, line.strip().split(" "))) for line in file.readlines()]

sum = 0

def safe(line):
    temp = []
    for i in range(len(line)-1):
        temp.append(line[i+1] - line[i])
    line = temp
    return all( 1 <= x <= 3 for x in line) or all( -1 >= x >= -3 for x in line)

for line in lines:
    if any(safe(line[:n]+line[n+1:]) for n in range(len(line))):
        sum += 1

print(sum)
    
        