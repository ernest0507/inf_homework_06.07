def to6(x):
    res = []
    while x > 0:
        res.append(str(x % 6))
        x //= 6
    return ''.join(res[::-1])

for x in range(1, 2030 + 1):
    a = to6(6**260 + 6**160 + 6**60 - x)
    if a.count('0') == 202:
        print(x)



