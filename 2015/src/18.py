from copy import deepcopy
from typing import List, Optional

inputs = [x.strip() for x in open("2015/inputs/18.txt").readlines()]
dimension = len(inputs[0]) - 1
corners = [(0, 0), (dimension, 0), (0, dimension), (dimension, dimension)]


def setup_lights(sticky: Optional[bool] = False) -> List:
    lights = []
    for i, input in enumerate(inputs):
        lights.append([1 if x == "#" else 0 for x in input])

    if sticky:
        for corner in corners:
            lights[corner[1]][corner[0]] = 1
    return lights


def neighbors(x: int, y: int) -> List:
    n = [
        (x - 1, y),
        (x + 1, y),
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]

    valid_n = []
    for i, x in enumerate(n):
        if x[0] < 0 or x[1] < 0 or x[0] > dimension or x[1] > dimension:
            continue

        valid_n.append(x)
    return valid_n


def update_lights(lights, sticky: Optional[bool] = False):
    new_lights = deepcopy(lights)
    for y, _ in enumerate(lights):
        for x, _ in enumerate(lights[y]):
            n = sum(lights[n[1]][n[0]] for n in neighbors(x, y))
            if sticky and (x, y) in corners:
                continue

            if lights[y][x] == 1:
                if n not in {2, 3}:
                    new_lights[y][x] = 0
            elif n == 3:
                new_lights[y][x] = 1
    return new_lights


def run(sticky: Optional[bool] = False):
    lights = setup_lights(sticky)
    for _ in range(100):
        lights = update_lights(lights, sticky)

    return sum(map(sum, lights))


print(run())
print(run(True))
