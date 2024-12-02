import re
from itertools import pairwise

input = open("2024/inputs/02.txt").readlines()
input = [[int(x) for x in re.findall(r"\d+", line)] for line in input]


def valid(line):
    pairs = list(pairwise(line))
    incr = all(a < b for a, b in pairs)
    decr = all(a > b for a, b in pairs)
    valid_step = all(1 <= abs(a - b) <= 3 for a, b in pairs)
    return (incr or decr) and valid_step


def remove_one(l):
    return [l[:i] + l[i + 1 :] for i in range(len(l))]


print(sum(valid(line) for line in input))
print(sum(any(valid(new_line) for new_line in remove_one(line)) for line in input))
