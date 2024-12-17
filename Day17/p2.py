import re

program = list(map(int, re.findall(r"\d+", open("input.txt").read())[3:]))

print(program)

def find(input, ans):
    if input == []: return ans
    for t in range(8):
        a = ans << 3 | t
        b = 0
        c = 0
        output = None

        def combo(op):
            if 0 <= op <=3: return op
            if op == 4: return a
            if op == 5: return b
            if op == 6: return c

        for cur in range(0, len(program) - 2, 2):
            instruction = program[cur]
            operand = program[cur + 1]
            if instruction == 1:
                b = b ^ operand
            elif instruction == 2:
                b = combo(operand) % 8
            elif instruction == 4:
                b = b ^ c
            elif instruction == 5:
                output = combo(operand) % 8
            elif instruction == 6:
                b = a >> combo(operand)
            elif instruction == 7:
                c = a >> combo(operand)
            if output == input[-1]:
                sub = find(input[:-1], a)
                if sub is None: continue
                return sub

print(find(program, 0))