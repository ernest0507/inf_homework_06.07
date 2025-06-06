def dividers(n):
    divs = set()
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            divs.add(n // d)
            divs.add(d)
    return sorted(divs)

num = 700_000 + 1
count = 0
while count < 5:
    res = dividers(num)
    min_d = float('inf')
    for x in res:
        if x != 7 and x % 10 == 7 and min_d > x:
            min_d = x
    if min_d % 10 == 7:
        print(num, min_d)
        count += 1
    num += 1