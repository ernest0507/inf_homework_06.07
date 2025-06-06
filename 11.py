import math

alph = 10 + 26 + 450
n = 575
i = 9
mem = 100
for length in range(1, 1000):
    if math.ceil(length * i / 8) * n >= mem * 1024:
        print(length)
        break
