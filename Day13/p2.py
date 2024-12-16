with open('input.txt') as file:
    chunks = file.read().split("\n\n")


data = []

sum = 0

for chunk in chunks:
    lines = chunk.split("\n")
    ax, ay = list(map(int, lines[0].lstrip("Button A: X+").split(", Y+")))
    bx, by = list(map(int, lines[1].lstrip("Button B: X+").split(", Y+")))
    px, py = list(map(int, lines[2].lstrip("Prize: X=").split(", Y=")))

    px += 10000000000000
    py += 10000000000000

    i = (px * by - py * bx) / (ax * by - ay * bx)
    j = (px - ax * i) / bx

    if i % 1 == j % 1 == 0:
        sum += i*3 + j


print(int(sum))
