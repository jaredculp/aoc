from collections import deque
from functools import lru_cache

inputs = {tuple(map(int, x.split(","))) for x in open("2022/inputs/18.txt")}
inputs = {
    tuple(map(int, x.split(",")))
    for x in """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
""".splitlines()
}


def sides(point):
    x, y, z = point
    return [
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1),
    ]


p1 = 0
for i in inputs:
    for s in sides(i):
        if s not in inputs:
            p1 += 1

print(p1)

all_points = [sides(p) for p in inputs]
min_x = min(p[0] for p in all_points)[0]
max_x = max(p[0] for p in all_points)[0]
min_y = min(p[1] for p in all_points)[1]
max_y = max(p[1] for p in all_points)[1]
min_z = min(p[2] for p in all_points)[2]
max_z = max(p[2] for p in all_points)[2]


@lru_cache(maxsize=None)
def inside(point):
    Q = deque()
    Q.append(point)
    while Q:
        p = Q.popleft()

        for x, y, z in sides(p):
            if (
                min_x <= x <= max_x
                and min_y <= y <= max_y
                and min_z <= z <= max_z
            ):
                for s in sides(p):
                    Q.append(s)

    return i


print(flood((-1, -1, -1)))
