import re

with open("input.txt") as file:
    text = file.read()


text = text.split("do()")

enabled = []

for seg in text:
    enabled.append(seg.split("don't()")[0])

text = ''.join(enabled)



pattern = r"mul\((\d+),(\d+)\)"

match = re.findall(pattern, text)

sum = 0

for x,y in match:
    sum += int(x)*int(y)

print(sum)