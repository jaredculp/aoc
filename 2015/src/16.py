inputs = [x.strip() for x in open("2015/inputs/16.txt").readlines()]

sues = dict()
for input in inputs:
    num, *rest = input.split(": ")
    _, num = num.split(" ")

    props = [y for x in " ".join(rest).split(", ") for y in x.split(" ")]
    # turn [a 1 b 2] into {a: 1, b: 2}
    props = dict(zip(props[::2], props[1::2]))

    sues[num] = {k: int(v) for k, v in props.items()}

search = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

for sue, props in sues.items():
    if all(k not in props or v == props[k] for k, v in search.items()):
        sues.pop(sue)
        print("part1: ", sue)
        break

for sue, props in sues.items():
    if all(
        k not in props
        or (k in {"cats", "trees"} and props[k] > v)
        or (k in {"pomeranians", "goldfish"} and props[k] < v)
        or (v == props[k])
        for k, v in search.items()
    ):
        print("part2: ", sue)
