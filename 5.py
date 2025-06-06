def f(N):
    num = bin(N)[2:]
    if num.count('1') % 2 == 0:
        num = '10' + num[2:] + '0'
    else:
        num = '11' + num[2:] + '1'
    return int(num, 2)

ans = []
for N in range(27 + 1, 1000):
    ans.append(f(N))
print(min(ans))
