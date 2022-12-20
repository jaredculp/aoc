lava_cubes = {tuple(map(int, x.split(","))) for x in open("2022/inputs/18.txt")}


def sides(x, y, z):
    return {
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1),
    }


def within(x, y, z):
    return all([min_ <= x <= max_, min_ <= y <= max_, min_ <= z <= max_])


all_points = [s for c in lava_cubes for s in sides(*c)]
print(sum(1 if s not in lava_cubes else 0 for s in all_points))

min_, max_ = min(min(all_points)), max(max(all_points))

inside, outside = list(), set()
Q = [(min_, min_, min_)]
while Q:
    point = Q.pop()
    for side in sides(*point):
        if side in outside or not all(min_ <= s <= max_ for s in side):
            continue

        if side in lava_cubes:
            inside.append(side)
        else:
            outside.add(side)
            Q.append(side)
print(len(inside))
