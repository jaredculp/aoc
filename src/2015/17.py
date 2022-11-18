from itertools import combinations

inputs = [int(x.strip()) for x in open("inputs/2015/17.txt").readlines()]

combos = []
for i in range(1, len(inputs) + 1):
    for p in combinations(inputs, i):
        if sum(p) == 150:
            combos.append(p)

print("part1: ", len(combos))

min_containers = len(min(combos, key=lambda x: len(x)))
print("part2: ", len([x for x in combos if len(x) == min_containers]))
