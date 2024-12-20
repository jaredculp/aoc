from collections import deque
from itertools import combinations

input = open("2024/inputs/20.txt").readlines()

grid = [list(r.strip()) for r in input]
R = len(grid)
C = len(grid[0])

sr, sc, er, ec = -1, -1, -1, -1
for r in range(R):
    for c in range(C):
        if grid[r][c] == "S":
            sr, sc = r, c
        if grid[r][c] == "E":
            er, ec = r, c

q = deque([(sr, sc)])
d = {(sr, sc): 0}
while q:
    r, c = q.popleft()
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        rr, cc = r + dr, c + dc
        if not (0 <= rr < R and 0 <= cc < C) or grid[rr][cc] == "#" or (rr, cc) in d:
            continue
        q.append((rr, cc))
        d[(rr, cc)] = d[(r, c)] + 1


p1 = p2 = 0
for (p, i), (q, j) in combinations(d.items(), 2):
    manhattan = abs(p[0] - q[0]) + abs(p[1] - q[1])
    if manhattan == 2 and j - i - manhattan >= 100:
        p1 += 1
    if manhattan < 21 and j - i - manhattan >= 100:
        p2 += 1
print(p1)
print(p2)
