from itertools import product
from functools import cache

lines = open("input.txt").read().splitlines()



def compute_sequences(keypad):
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
            optimal = float("inf")
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
    return sequence


def solve(code, sequence):
    options = [sequence[(x,y)] for x, y in zip("A" + code, code)]
    return ["".join(x) for x in product(*options)]

door_keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"]
]

door_sequences = compute_sequences(door_keypad)

dir_keypad = [
    [None, '^', 'A'],
    ['<', 'v', '>']
]

dir_sequences = compute_sequences(dir_keypad)

dir_lengths = {key: len(value[0]) for key, value in dir_sequences.items()}

@cache
def compute_length(seq, depth=25):
    if depth == 1:
        return sum(dir_lengths[(x, y)] for x,y in zip("A"+ seq, seq))
    length = 0
    for x,y in zip("A" + seq, seq):
        length += min(compute_length(subseq, depth - 1) for subseq in dir_sequences[(x,y)])
    return length


score = 0

for line in lines:
    inputs = solve(line, door_sequences)
    length = min(map(compute_length, inputs))
    score += length * int(line[:-1])

print(score)
