input = [x.strip() for x in open("2023/inputs/18.txt").readlines()]


# https://11011110.github.io/blog/2021/04/17/picks-shoelaces.html
def pick_shoelace(ps, n):
    a = 0

    for i in range(len(ps) - 1):
        x1, y1 = ps[i]
        x2, y2 = ps[(i + 1) % n]
        a += x1 * y2 - x2 * y1

    return int(a / 2 + 1 - n / 2 + n)


def add_point(p, d, x):
    c = {
        "L": (-1, 0),
        "R": (1, 0),
        "U": (0, -1),
        "D": (0, 1),
    }[d]

    return (p[0] + c[0] * x, p[1] + c[1] * x)


b = 0
ps = [(0, 0)]
for line in input:
    d, x, *_ = line.split()
    x = int(x)
    b += x
    ps.append(add_point(ps[-1], d, x))
print(pick_shoelace(ps, b))

b = 0
ps = [(0, 0)]
for line in input:
    *_, hex = line.split()
    hex = hex.replace("(", "").replace(")", "").replace("#", "")
    d = {0: "R", 1: "D", 2: "L", 3: "U"}[int(hex[-1])]
    x = int(hex[:-1], 16)
    b += x
    ps.append(add_point(ps[-1], d, x))
print(pick_shoelace(ps, b))
