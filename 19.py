# def f(x, p):
#     if x >= 67 and p == 3:
#         return True
#     elif x < 67 and p == 3:
#         return False
#     elif x >= 67:
#         return False
#     else:
#         if p % 2 == 0:
#             return f(x + 1, p + 1) or f(x + 3, p + 1) or f(x * 2, p + 1)
#         else:
#             return f(x + 1, p + 1) and f(x + 3, p + 1) and f(x * 2, p + 1)
#
#
# for S in range(1, 66):
#     if f(S, 1):
#         print(S)


# def f(x, p):
#     if x >= 67 and p == 4:
#         return True
#     elif x < 67 and p == 4:
#         return False
#     elif x >= 67:
#         return False
#     else:
#         if p % 2 == 0:
#             return f(x + 1, p + 1) and f(x + 3, p + 1) and f(x * 2, p + 1)
#         else:
#             return f(x + 1, p + 1) or f(x + 3, p + 1) or f(x * 2, p + 1)
#
#
# for S in range(1, 66):
#     if f(S, 1):
#         print(S)


def f(x, p):
    if x >= 67 and (p == 3 or p == 5):
        return True
    elif x < 67 and p == 5:
        return False
    elif x >= 67:
        return False
    else:
        if p % 2 == 0:
            return f(x + 1, p + 1) or f(x + 3, p + 1) or f(x * 2, p + 1)
        else:
            return f(x + 1, p + 1) and f(x + 3, p + 1) and f(x * 2, p + 1)


for S in range(1, 66):
    if f(S, 1):
        print(S)