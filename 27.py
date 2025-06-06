# from math import dist
#
# def centroid(c):
#     n = len(c)
#     min_s_dist, ind = float('inf'), 0
#     for i in range(n):
#         s = 0
#         for j in range(n):
#             s += dist(c[i], c[j])
#         if min_s_dist > s:
#             min_s_dist = s
#             ind = i
#     return c[ind]
#
#
# c1, c2 = [], []
# file = open('27_A.txt')
# for line in file:
#     x, y = [float(i.replace(',', '.')) for i in line.split()]
#     if x > 0:
#         c1.append([x, y])
#     else:
#         c2.append([x, y])
#
# x1, y1 = centroid(c1)
# x2, y2 = centroid(c2)
# print(abs((x1 + x2) / 2 * 10_000), abs((y1 + y2) / 2 * 10_000))
# Ответ: 10592 6300


# from math import dist
#
#
# def centroid(c):
#     n = len(c)
#     min_s_dist, ind = float('inf'), 0
#     for i in range(n):
#         s = 0
#         for j in range(n):
#             s += dist(c[i], c[j])
#         if min_s_dist > s:
#             min_s_dist = s
#             ind = i
#     return c[ind]
#
#
# c1, c2, c3 = [], [], []
# file = open('27_B.txt')
# for line in file:
#     x, y = [float(i.replace(',', '.')) for i in line.split()]
#     if y >= -x:
#         c1.append([x, y])
#     elif x < -5:
#         c2.append([x, y])
#     else:
#         c3.append([x, y])
#
# x1, y1 = centroid(c1)
# x2, y2 = centroid(c2)
# x3, y3 = centroid(c3)
# print(abs((x1 + x2 + x3) / 3 * 10_000), abs((y1 + y2 + y3) / 3 * 10_000))
# Ответ: 15981 37287
