from itertools import combinations

from matplotlib.path import Path

input = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""".splitlines()
# input = open("2025/inputs/09.txt").readlines()
input = [[int(xx) for xx in x.split(",")] for x in input]


def area(a, b):
    x1, y1 = a
    x2, y2 = b
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])
    return (x2 - x1 + 1) * (y2 - y1 + 1)


print(max(area(a, b) for a, b in combinations(input, 2)))

polygon = Path(input)


def inside(a, b):
    x1, y1 = a
    x2, y2 = b
    corners = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
    return all(polygon.contains_point(c) for c in corners)


print(max(area(a, b) for a, b in combinations(input, 2) if inside(a, b)))

# Y = max(point[1] for point in input) + 1
# X = max(point[0] for point in input) + 1
# print(X, Y)
# G = [[0] * X for _ in range(Y)]
#
#
# for (x1, y1), (x2, y2) in pairwise(input + [input[0]]):
#     if y1 == y2:
#         for x in range(min(x1, x2), max(x1, x2) + 1):
#             G[y1][x] = 1
#     if x1 == x2:
#         for y in range(min(y1, y2), max(y1, y2) + 1):
#             G[y][x1] = 1
# #
# # for y in range(Y):
# #     inside = False
# #     for x in range(X):
# #         if G[y][x] == 1 and not inside:
# #             inside = not inside
# #
# #         if inside:
# #             G[y][x] = 1
# #
# #
# # def area2(a, b):
# #     x1, y1 = a
# #     x2, y2 = b
# #     x1, x2 = sorted([x1, x2])
# #     y1, y2 = sorted([y1, y2])
# #
# #     if any(G[y1][x] == 0 for x in range(x1, x2 + 1)):
# #         return 0
# #
# #     if any(G[y][x1] == 0 for y in range(y1, y2 + 1)):
# #         return 0
# #
# #     return (x2 - x1 + 1) * (y2 - y1 + 1)
# #
# #
# # print(max(area2(a, b) for a, b in combinations(input, 2)))
