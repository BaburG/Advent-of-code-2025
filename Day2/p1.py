with open("input.txt") as file:
    lines = file.readlines()

sum = len(lines)
print(sum)

for line in lines:
    prev = None
    increasing = None
    for num in line.split(" "):
        num = int(num)
        if not prev:
            prev = num
            continue
        
        if num > prev and increasing == None:
            increasing = True
        elif increasing == None:
            increasing = False

        if abs(prev-num) == 0 or abs(prev-num) > 3:
            print(line, prev, num)
            sum = sum - 1
            break

        if (increasing and num < prev) or (not increasing and num > prev):
            print(line, prev, num)
            sum = sum - 1
            break
        prev = num

print(sum)
    
        