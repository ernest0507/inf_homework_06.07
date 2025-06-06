def f(A, x, y):
    rule1 = (x + y) <= 24
    rule2 = y <= (x - 2)
    rule3 = y >= A
    return rule1 or rule2 or rule3

for A in range(500):
    flag = True
    for x in range(700):
        for y in range(700):
            if not f(A, x, y):
                flag = False

    if flag:
        print(A)



