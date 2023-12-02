from collections import defaultdict
from functools import reduce


lines = [l.strip() for l in open("2023/inputs/02.txt").readlines()]

part1 = 0
part2 = 0
for line in lines:
    game, info = line.split(":")
    _, num = game.split(" ")
    cubesets = info.split(";")

    valid = True
    max_counts = defaultdict(int)

    for cubeset in cubesets:
        cubes = cubeset.split(",")
        for cube in cubes:
            count, color = cube.strip().split(" ")
            count = int(count)

            if color == "red" and count > 12:
                valid = False
            if color == "green" and count > 13:
                valid = False
            if color == "blue" and count > 14:
                valid = False

            max_counts[color] = max(max_counts[color], count)

    if valid:
        part1 += int(num)

    part2 += reduce(lambda a, b: a * b, max_counts.values())

print(part1)
print(part2)
