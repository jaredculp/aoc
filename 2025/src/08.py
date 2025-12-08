import math
from itertools import combinations

input = open("2025/inputs/08.txt").readlines()


def distance(a: tuple[int, ...], b: tuple[int, ...]) -> float:
    p1, p2, p3 = a
    q1, q2, q3 = b

    return math.sqrt((p1 - q1) ** 2 + (p2 - q2) ** 2 + (p3 - q3) ** 2)


def update(a: tuple[int, ...], b: tuple[int, ...]):
    find = lambda x: next((c for c in circuits if x in c), None)
    if (c1 := find(a)) and (c2 := find(b)) and c1 != c2:
        c1 |= c2
        circuits.remove(c2)


boxes = [tuple(int(xx) for xx in x.split(",")) for x in input]
circuits = [{p} for p in boxes]
distances = sorted((distance(a, b), a, b) for a, b in combinations(boxes, 2))

for _, a, b in distances[:1000]:
    update(a, b)

largest = sorted([len(c) for c in circuits], reverse=True)
print(math.prod(largest[:3]))

for _, a, b in distances[1000:]:
    update(a, b)
    if len(circuits) == 1:
        print(a[0] * b[0])
        break
