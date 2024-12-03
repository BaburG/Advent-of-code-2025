import re

with open("input.txt") as file:
    text = file.read()



pattern = r"mul\((\d+),(\d+)\)"

match = re.findall(pattern, text)

sum = 0

for x,y in match:
    sum += int(x)*int(y)

print(sum)