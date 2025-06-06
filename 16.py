from sys import setrecursionlimit
setrecursionlimit(3000)

def F(n):
    if n == 1:
        return 1
    return (n - 1) * F(n - 1)


print((F(2024) // 7 - F(2023)) // F(2022))


F = [0] * 2025
for n in range(2025):
    if n == 1:
        F[n] = 1
    else:
        F[n] = (n - 1) * F[n - 1]

print((F[2024] // 7 - F[2023]) // F[2022])

