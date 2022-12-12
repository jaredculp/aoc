import re
from itertools import accumulate

inputs = [x.strip() for x in open("2022/inputs/10.txt").readlines()]

adds = []
for i, input in enumerate(inputs):
    addx = re.match(r"addx (-?\d+)", input)

    adds.append(0)
    if addx:
        adds.append(int(addx.group(1)))


total = 0
sprite = ""
for i, x in enumerate(accumulate([1] + adds)):
    total += (i + 1) * x if (i + 1) in [20, 60, 100, 140, 180, 220] else 0
    sprite += "#" if i % 40 - x in [-1, 0, 1] else '.'

print(total)
print("\n".join(sprite[i:i+40] for i in range(0, len(sprite), 40)))
