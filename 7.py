size = 1024 * 960
n = 32
speed = 1_474_560
time = 140

for i in range(1, 1000):
    if (size * i) * n / speed <= time:
        print(2**i)

