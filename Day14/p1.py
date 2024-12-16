with open("input.txt") as file:
    robots = [ [list(map(int, line.lstrip("p=").split(' v=')[0].split(','))), list(map(int, line.lstrip("p=").split(' v=')[1].split(',')))] for line in file.read().splitlines()]

width = 101
height = 103

map = []

t = 100

for robot in robots:
    px, py = robot[0]
    dx, dy = robot[1]
    map.append(((px + dx * t)% width, (py + dy * t)%height))

first = len([(x, y) for x,y in map if x < width//2 and y < height//2])
second = len([(x, y) for x,y in map if x < width//2 and y > height//2])
third = len([(x, y) for x,y in map if x > width//2 and y > height//2])
fourth = len([(x, y) for x,y in map if x > width//2 and y < height//2])

print( first * second * third * fourth)