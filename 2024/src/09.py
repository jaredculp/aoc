from collections import Counter

input = open("2024/inputs/09.txt").read().strip()
# input = "2333133121414131402"


def parse():
    id = 0
    output = []
    for i, x in enumerate(input):
        n = int(x)
        if i % 2 == 0:
            output += [id] * n
            id += 1
        else:
            output += [None] * n
    return output


def part1():
    output = parse()
    swap = len(output) - 1
    for i, x in enumerate(output):
        if x is not None:
            continue

        while swap > i and output[swap] is None:
            swap -= 1

        output[i] = output[swap]
        output[swap] = None
    return output


def part2():
    output = parse()
    locations = dict()
    for i, x in enumerate(output):
        if x not in locations:
            locations[x] = i

    counts = Counter(x for x in output if x is not None)
    for x in reversed(counts.keys()):
        count = counts[x]
        location = locations[x]
        for i in range(len(output) - count + 1):
            if i > location:
                break
            if output[i : i + count] == [None] * count:
                output[locations[x] : locations[x] + count] = [None] * count
                output[i : i + count] = [x] * count
                break

    return output


print(sum(i * int(x) for i, x in enumerate(part1()) if x))
print(sum(i * int(x) for i, x in enumerate(part2()) if x))
