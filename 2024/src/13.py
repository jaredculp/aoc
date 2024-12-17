import re

games = [
    [tuple(map(int, re.findall(r"\d+", x))) for x in line.splitlines()]
    for line in open("2024/inputs/13.txt").read().split("\n\n")
]


def cramer(game, offset=0):
    # https://en.wikipedia.org/wiki/Cramer%27s_rule
    (ax, ay), (bx, by), (px, py) = game
    px += offset
    py += offset

    det_a = ax * by - bx * ay
    if det_a == 0:
        return None

    a, a_remainder = divmod(px * by - py * bx, det_a)
    b, b_remainder = divmod(ax * py - ay * px, det_a)

    if a_remainder or b_remainder or a < 0 or b < 0:
        return None

    return 3 * a + b


print(sum(cramer(game) or 0 for game in games))
print(sum(cramer(game, offset=10000000000000) or 0 for game in games))
