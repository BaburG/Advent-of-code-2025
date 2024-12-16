with open("input.txt") as file:
    robots = [ [list(map(int, line.lstrip("p=").split(' v=')[0].split(','))), list(map(int, line.lstrip("p=").split(' v=')[1].split(',')))] for line in file.read().splitlines()]

width = 101
height = 103



n = len(robots)

for i in range(1000000):
    map = set()
    for robot in robots:
        px, py = robot[0]
        dx, dy = robot[1]
        map.add(((px + dx * i)% width, (py + dy * i)%height))
    if len(map) == n:
        print(i)
        #uncomment to see christmas tree
        # print("FOUND", i)
        # for i in range(width):
        #     for j in range(height):
        #         if (j,i) in map:
        #             print("o", end="")
        #         else:
        #             print(".", end='')
        #     print()
        break

