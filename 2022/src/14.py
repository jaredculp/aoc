from copy import deepcopy

from common import sign

inputs = [x.strip() for x in open("2022/inputs/14.txt").readlines()]


rocks = set()
abyss = 0
for input in inputs:
    points = [complex(*[int(y) for y in x.split(",")]) for x in input.split(" -> ")]

    for i in range(len(points) - 1):
        a, b = points[i : i + 2]
        rocks.add(a)
        rocks.add(b)

        while a != b:
            c = b - a
            if c.real:
                a += sign(c.real)
            if c.imag:
                a += sign(c.imag) * 1j
            rocks.add(a)
            abyss = max(abyss, a.imag + 1)

sand = 0
source = 500
rocks_1 = deepcopy(rocks)
while source.imag <= abyss:
    down, left, right = source + 1j, source + 1j - 1, source + 1j + 1
    if down not in rocks_1:
        source = down
    elif left not in rocks_1:
        source = left
    elif right not in rocks_1:
        source = right
    else:
        rocks_1.add(source)
        sand += 1
        source = 500

print(sand)

sand = 0
source = 500
rocks_2 = deepcopy(rocks)
while 500 not in rocks_2:
    down, left, right = source + 1j, source + 1j - 1, source + 1j + 1
    if source.imag >= abyss:
        rocks_2.add(source)
        sand += 1
        source = 500
    elif down not in rocks_2:
        source = down
    elif left not in rocks_2:
        source = left
    elif right not in rocks_2:
        source = right
    else:
        rocks_2.add(source)
        sand += 1
        source = 500

print(sand)
