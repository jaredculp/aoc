import re
from functools import reduce
from operator import mul

f = open("inputs/2015/02.txt")
lines = [x.strip() for x in f.readlines()]

paper = 0
ribbon = 0
for line in lines:
    match = re.search(r"(\d+)x(\d+)x(\d+)", line)
    l, w, h = [int(x) for x in match.groups()]
    small_l, small_w = sorted([l, w, h])[:2]
    smallest_side = reduce(mul, [small_l, small_w])

    paper += 2 * l * w + 2 * w * h + 2 * h * l + smallest_side
    ribbon += 2 * small_l + 2 * small_w + l * w * h

print("part1: ", paper)
print("part2: ", ribbon)
