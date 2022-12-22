import re

*map, _, moves = open("2022/inputs/22.txt").readlines()

tiles = set()
walls = set()

for j, y in enumerate(map):
    for i, x in enumerate(y):
        if x == ".":
            tiles.add(complex(i, j))
        elif x == "#":
            walls.add(complex(i, j))

position = complex(map[0].index("."), 0)
direction = complex(1, 0)


for move in re.findall(r"\d+|[LR]", moves):
    if move == "L":
        direction *= -1j
    elif move == "R":
        direction *= 1j
    else:
        for _ in range(int(move)):
            new_position = position + direction

            if new_position not in tiles | walls:
                if direction == 1j:  # up
                    new_position = complex(
                        position.real,
                        min(x.imag for x in tiles | walls if x.real == position.real),
                    )
                if direction == -1j:  # down
                    new_position = complex(
                        position.real,
                        max(x.imag for x in tiles | walls if x.real == position.real),
                    )
                if direction == -1:  # left
                    new_position = complex(
                        max(x.real for x in tiles | walls if x.imag == position.imag),
                        position.imag,
                    )
                if direction == 1:  # right
                    new_position = complex(
                        min(x.real for x in tiles | walls if x.imag == position.imag),
                        position.imag,
                    )

            if new_position in tiles:
                position = new_position

print(
    int(
        1000 * (position.imag + 1)
        + 4 * (position.real + 1)
        + [1, -1j, -1, 1j].index(direction)
    )
)
