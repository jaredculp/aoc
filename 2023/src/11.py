from itertools import combinations

input = [l.strip() for l in open("2023/inputs/11.txt").readlines()]

X = len(input[0])
Y = len(input)
exp_y = [y for y in range(Y) if all(input[y][x] == "." for x in range(X))]
exp_x = [x for x in range(X) if all(input[y][x] == "." for y in range(Y))]

galaxies = [(x, y) for x in range(X) for y in range(Y) if input[y][x] == "#"]
p1, p2 = 0, 0
for (x1, y1), (x2, y2) in combinations(galaxies, 2):

    def expansion(factor: int) -> int:
        X = range(*sorted([x1, x2]))
        Y = range(*sorted([y1, y2]))
        return (sum(x in exp_x for x in X) + sum(y in exp_y for y in Y)) * factor

    d = abs(x1 - x2) + abs(y1 - y2)
    p1 += d + expansion(1)
    p2 += d + expansion(1000000 - 1)
print(p1)
print(p2)
