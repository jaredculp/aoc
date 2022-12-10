from math import prod

inputs = [x.strip() for x in open("2022/inputs/08.txt").readlines()]

X = len(inputs[0])
Y = len(inputs)
XS = range(1, X - 1)
YS = range(1, Y - 1)


def neighbors(x, y):
    return [
        (inputs[xx][y] for xx in reversed(range(x))),
        (inputs[xx][y] for xx in range(x + 1, X)),
        (inputs[x][yy] for yy in reversed(range(y))),
        (inputs[x][yy] for yy in range(y + 1, Y)),
    ]


def check_tree(x, y):
    return any(all(n < inputs[x][y] for n in ns) for ns in neighbors(x, y))


def count(predicate, iterable):
    total = 0
    for i in iterable:
        total += 1
        if not predicate(i):
            break

    return total


def score_tree(x, y):
    return prod(count(lambda n: n < inputs[x][y], ns) for ns in neighbors(x, y))


edges = X * 2 + Y * 2 - 4
print(edges + sum(check_tree(x, y) for x in XS for y in YS))
print(max(score_tree(x, y) for x in XS for y in YS))
