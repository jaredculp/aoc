import re

inputs = [x.strip() for x in open("2022/inputs/04.txt").readlines()]

full = 0
part = 0
for input in inputs:
    a, b, c, d = map(int, re.findall(r"\d+", input))

    x = set(range(a, b + 1))
    y = set(range(c, d + 1))

    if x - y == set() or y - x == set():
        full += 1

    if x & y != set():
        part += 1

print(full)
print(part)
