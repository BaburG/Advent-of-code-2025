from functools import cache

with open('input.txt') as file:
    nums = list(map(int,file.read().split(" ")))

blink = 75

@cache
def count(num, steps):
    if steps == 0:
        return 1
    if num == 0:
        return count(1, steps - 1)
    length = len(str(num))
    if length % 2 == 0:
        return count((num // (10 ** (length//2))), steps - 1) + count((num % (10 ** (length//2))), steps - 1)
    return count(num * 2024, steps - 1)

print(sum(count(stone, blink) for stone in nums))