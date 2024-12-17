import re
from math import prod

input = open("2024/inputs/14.txt").readlines()
input = [list(map(int, re.findall(r"-?\d+", line))) for line in input]
C = 101
R = 103

tl = {(rr, cc) for rr in range(R // 2) for cc in range(C // 2)}
tr = {(rr, cc) for rr in range(R // 2) for cc in range(C // 2 + 1, C)}
bl = {(rr, cc) for rr in range(R // 2 + 1, R) for cc in range(C // 2)}
br = {(rr, cc) for rr in range(R // 2 + 1, R) for cc in range(C // 2 + 1, C)}
quadrants = [tl, tr, bl, br]


def run(t):
    grid = [[0] * C for _ in range(R)]
    for point in input:
        c, r, dc, dr = point
        new_r = (r + dr * t) % R
        new_c = (c + dc * t) % C
        grid[new_r][new_c] += 1

    return prod(sum(grid[r][c] for r, c in quad) for quad in quadrants)


print(run(100))
print(min(((i, run(i)) for i in range(R * C)), key=lambda x: x[1])[0])
