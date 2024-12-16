with open('input.txt') as file:
    nums = list(map(int,file.read().split(" ")))

blink = 25

#print(f'Initial arrangement:\n {nums}')


for i in range(blink):
    #print(f"blink {i+1}")
    newnums = []

    for num in nums:
        length = len(str(num))
        if num ==  0:
            newnums.append(1)
        elif length % 2 == 0:
            newnums.append(int(num // (10 ** (length/2))))
            newnums.append(int(num % (10 ** (length /2))))
        else:
            newnums.append(num * 2024)
    
    nums = newnums
    #print(f'Arrangement after {i+1} blinks:\n {nums}')


print(len(nums))