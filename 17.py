file = open('17_17680.txt')
nums = [int(x) for x in file]
melem = min([x for x in nums if x > 0 and x % 41 == 0])
file.close()

ans = []
for i in range(len(nums) - 1):
    a, b = nums[i:i + 2]
    rule1 = a != b
    rule2 = abs(a - b) % melem == 0
    if rule1 and rule2:
        ans.append(a + b)

print(len(ans), max(ans))
