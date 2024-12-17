import re

a, b, c, *program = map(int, re.findall(r"\d+", open("input.txt").read()))

cur = 0
output = []


def combo(operand):
    if 0 <= operand <=3: return operand
    if operand == 4: return a
    if operand == 5: return b
    if operand == 6: return c


while cur < len(program):
    instruction = program[cur]
    operand = program[cur + 1]
    if instruction == 0:
        a = a >> combo(operand)
    elif instruction == 1:
        b = b ^ operand
    elif instruction == 2:
        b = combo(operand) % 8
    elif instruction == 3:
        if a != 0:
            cur = operand
            continue
    elif instruction == 4:
        b = b ^ c
    elif instruction == 5:
        output.append(combo(operand) % 8)
    elif instruction == 6:
        b = a >> combo(operand)
    elif instruction == 7:
        c = a >> combo(operand)

    cur += 2

print(*output, sep=',')
