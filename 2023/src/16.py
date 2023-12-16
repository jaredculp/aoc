import sys

sys.setrecursionlimit(10_000)

input = [x.strip() for x in open("2023/inputs/16.ex").readlines()]
input = [x.strip() for x in open("2023/inputs/16.txt").readlines()]
X = len(input[0])
Y = len(input)


def travel(x, y, dx, dy, seen):
    global input
    if not 0 <= x < X or not 0 <= y < Y or (x, y, dx, dy) in seen:
        return {(x, y) for x, y, *_ in seen}

    seen.add((x, y, dx, dy))

    u = dx == 0 and dy == -1
    d = dx == 0 and dy == 1
    l = dx == -1 and dy == 0
    r = dx == 1 and dy == 0

    position = input[y][x]
    if position == "/":
        if u:
            dx = 1
            dy = 0
        elif d:
            dx = -1
            dy = 0
        elif l:
            dx = 0
            dy = 1
        elif r:
            dx = 0
            dy = -1
    elif position == "\\":
        if u:
            dx = -1
            dy = 0
        elif d:
            dx = 1
            dy = 0
        elif l:
            dx = 0
            dy = -1
        elif r:
            dx = 0
            dy = 1
    elif position == "|" and (l or r):
        return travel(x, y - 1, 0, -1, seen) | travel(x, y + 1, 0, 1, seen)
    elif position == "-" and dx == 0 and dy != 0:
        return travel(x - 1, y, -1, 0, seen) | travel(x + 1, y, 1, 0, seen)

    return travel(x + dx, y + dy, dx, dy, seen)


print(len(travel(0, 0, 1, 0, set())))
