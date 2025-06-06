file = open('09_17672.txt')
count = 0
for line in file:
    nums = sorted([int(x) for x in line.split()])
    if nums[0] + nums[3] < nums[1] + nums[2]:
        count += 1
print(count)

