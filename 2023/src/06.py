import re
import math

input = [l for l in open("2023/inputs/06.txt").readlines()]

# -x^2 + time * x - distance = 0
# quadratic formula: a=-1, b=7, c=-9
times, distances = [[int(x) for x in re.findall(r"\d+", i)] for i in input]
total = 1
for time, distance in zip(times, distances):
    total *= sum(1 if time * x - x**2 > distance else 0 for x in range(time))
print(total)

time, distance = [int("".join(re.findall(r"\d+", i))) for i in input]
root_1 = (time + math.sqrt(time**2 - 4 * distance)) / 2
root_2 = (time - math.sqrt(time**2 - 4 * distance)) / 2
roots = sorted(int(x) + 1 for x in [root_1, root_2])
print(len(range(*roots)))
