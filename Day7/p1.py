with open("input.txt") as file:
    lines = file.read().splitlines()


def possible(target, array):
    if len(array) == 1:
        return target == array[-1]
    if target % array[-1] == 0 and possible(target // array[-1], array[:-1]):
        return True
    if target > array[-1] and possible(target - array[-1], array[:-1]):
        return True
    return False

sum = 0

for line in lines:
    target = int(line.split(": ")[0])
    nums = list(map(int,line.split(": ")[1].split(" ")))
    if possible(target, nums): sum += target
    print(target, " -> ", nums)

print(sum)