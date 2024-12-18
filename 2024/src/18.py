import heapq
import re

input = open("2024/inputs/18.txt").readlines()
input = [tuple(map(int, re.findall(r"\d+", line.strip()))) for line in input]

R = 71
C = 71
S = (0, 0)
E = (R - 1, C - 1)


def make_grid(size):
    grid = [["."] * C for _ in range(R)]
    for c, r in input[:size]:
        grid[r][c] = "#"
    return grid


def path(grid):
    q = [(0, S)]  # (cost, (r, c))
    visited = set()

    while q:
        cost, (r, c) = heapq.heappop(q)

        if (r, c) == E:
            return cost

        if (r, c) in visited:
            continue
        else:
            visited.add((r, c))

        neighbors = [
            (r - 1, c),
            (r + 1, c),
            (r, c - 1),
            (r, c + 1),
        ]

        for rr, cc in neighbors:
            if 0 <= rr < R and 0 <= cc < C and grid[rr][cc] != "#":
                heapq.heappush(q, (cost + 1, (rr, cc)))

    return None


print(path(make_grid(1024)))

for i, coord in enumerate(input, 1):
    if not path(make_grid(i)):
        print(",".join(str(c) for c in coord))
        break
