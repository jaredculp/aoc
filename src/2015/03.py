from dataclasses import dataclass

input = open("inputs/2015/03.txt").read()


@dataclass(frozen=True)
class House:
    x: int
    y: int


x, y = 0, 0
houses = {House(0, 0)}

x1, y1, x2, y2 = 0, 0, 0, 0
robo_houses = {House(0, 0)}
for i, dir in enumerate(input):
    if dir == "^":
        y += 1
    elif dir == "v":
        y -= 1
    elif dir == ">":
        x += 1
    elif dir == "<":
        x -= 1
    houses.add(House(x, y))

    if i % 2 == 0:
        if dir == "^":
            y1 += 1
        elif dir == "v":
            y1 -= 1
        elif dir == ">":
            x1 += 1
        elif dir == "<":
            x1 -= 1
    else:
        if dir == "^":
            y2 += 1
        elif dir == "v":
            y2 -= 1
        elif dir == ">":
            x2 += 1
        elif dir == "<":
            x2 -= 1
    robo_houses.add(House(x1, y1))
    robo_houses.add(House(x2, y2))


print("part1: ", len(houses))
print("part2: ", len(robo_houses))
