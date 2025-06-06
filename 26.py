file = open('26_17687.txt')
N = int(file.readline())
prices = sorted([int(x) for x in file], reverse=True)
file.close()

total1 = sum(prices[(N // 9):])
total2 = sum(prices)
for i in range(8, N - (N % 9), 9):
    total2 -= prices[i]

print(total1, total2)
