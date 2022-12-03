import string
from typing import List

inputs = [x.strip() for x in open("2022/inputs/03.txt").readlines()]


def intersection(*lists: List[str]) -> str:
    return set.intersection(*map(set, lists)).pop()


def get_score(x: str) -> int:
    return string.ascii_letters.index(common) + 1


score = 0
for input in inputs:
    mid = len(input) // 2
    a, b = input[:mid], input[mid:]

    common = intersection(a, b)
    score += get_score(common)

print(score)

score = 0
for i in range(0, len(inputs), 3):
    a, b, c = inputs[i : i + 3]
    common = intersection(a, b, c)
    score += get_score(common)

print(score)
