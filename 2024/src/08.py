from collections import defaultdict
from itertools import combinations

input = [x.strip() for x in open("2024/inputs/08.txt").readlines()]
R = len(input)
C = len(input[0])

antennas = defaultdict(list)
for r in range(R):
    for c in range(C):
        if (antenna := input[r][c]) and antenna != ".":
            antennas[antenna].append((r, c))

antinodes_1 = set()
antinodes_2 = set()
for antenna, positions in antennas.items():
    for (r1, c1), (r2, c2) in combinations(positions, 2):
        dr = r2 - r1
        dc = c2 - c1

        if 0 <= r1 - dr < R and 0 <= c1 - dc < C:
            antinodes_1.add((r1 - dr, c1 - dc))
        if 0 <= r2 + dr < R and 0 <= c2 + dc < C:
            antinodes_1.add((r2 + dr, c2 + dc))

        while 0 <= r1 < R and 0 <= c1 < C:
            antinodes_2.add((r1, c1))
            r1 -= dr
            c1 -= dc

        while 0 <= r2 < R and 0 <= c2 < C:
            antinodes_2.add((r2, c2))
            r2 += dr
            c2 += dc

print(len(antinodes_1))
print(len(antinodes_2))
