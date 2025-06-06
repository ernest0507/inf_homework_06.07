def F(x, y, z, w):
    return int((z <= (not (y <= x))) or w)


print('x y z w | F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if not F(x, y, z, w):
                    print(x, y, z, w, '|', F(x, y, z, w))
