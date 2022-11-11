import re

inputs = [x.strip() for x in open("inputs/2015/6.txt").readlines()]

size = 1000
lights = [[0] * size for _ in range(size)]

for input in inputs:
    matches = re.search(r"([a-z\s]+) (\d+),(\d+) through (\d+),(\d+)", input)
    command, x1, y1, x2, y2 = matches.groups()

    for x in range(int(x1), int(x2) + 1):
        for y in range(int(y1), int(y2) + 1):
            if command == "turn on":
                lights[y][x] |= 1
            elif command == "toggle":
                lights[y][x] ^= 1
            elif command == "turn off":
                lights[y][x] &= 0

print("part1: ", sum(sum(x) for x in lights))

lights = [[0] * size for _ in range(size)]
for input in inputs:
    matches = re.search(r"([a-z\s]+) (\d+),(\d+) through (\d+),(\d+)", input)
    command, x1, y1, x2, y2 = matches.groups()

    for x in range(int(x1), int(x2) + 1):
        for y in range(int(y1), int(y2) + 1):
            if command == "turn on":
                lights[y][x] += 1
            elif command == "toggle":
                lights[y][x] += 2
            elif command == "turn off":
                if lights[y][x] > 0:
                    lights[y][x] -= 1

print("part2: ", sum(sum(x) for x in lights))
