from itertools import product

lines = open("input.txt").read().splitlines()

door_keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"]
]

dir_keypad = [
    [None, '^', 'A'],
    ['<', 'v', '>']
]


def solve(code, keypad):
    pos = {}
    for r in range(len(keypad)):
        for c in range(len(keypad[r])):
            if keypad[r][c] is not None: pos[keypad[r][c]] = (r,c)
    sequence = {}
    for x in pos:
        for y in pos:
            if x == y:
                sequence[(x,y)] = ["A"]
                continue
            possible = []
            q = [(pos[x], "")]
            optimal = 999
            while q:
                (r,c), moves = q.pop(0)
                for nr, nc, nm in [(r-1,c,"^"), (r+1, c, "v"), (r, c-1, "<"), (r,c+1,">")]:
                    if nr < 0 or nc < 0 or nr >= len(keypad) or nc >= len(keypad[0]): continue
                    if keypad[nr][nc] is None: continue
                    if keypad[nr][nc] == y:
                        if optimal < len(moves) +1 : break
                        optimal = len(moves) + 1
                        possible.append(moves + nm + "A")
                    else:
                        q.append(((nr,nc), moves + nm))
                else:
                    continue
                break
            sequence[(x,y)] = possible
    options = [sequence[(x,y)] for x, y in zip("A" + code, code)]
    return ["".join(x) for x in product(*options)]

score = 0

for line in lines:
    robot1 = solve(line, door_keypad)
    possible_robot2 = []
    for seq in robot1:
        possible_robot2 += solve(seq, dir_keypad)
    minlen = min(map(len, possible_robot2))
    robot2 = [seq for seq in possible_robot2 if len(seq) == minlen]
    possible_robot3 = []
    for seq in robot2:
        possible_robot3 += solve(seq, dir_keypad)
    minlen = min(map(len, possible_robot3))
    robot3 = [seq for seq in possible_robot3 if len(seq) == minlen]

    length = len(robot3[0])
    complexity = length * int(line[:-1])
    score += complexity

print(score)
