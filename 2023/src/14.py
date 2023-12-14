input = open("2023/inputs/14.txt").readlines()


def tilt(input):
    for i in range(len(input) - 1):
        line, next_line = input[i : i + 2]

        for j in range(len(line)):
            if line[j] == "." and next_line[j] == "O":
                line = line[:j] + "O" + line[j + 1 :]
                next_line = next_line[:j] + "." + next_line[j + 1 :]
            input[i] = line
            input[i + 1] = next_line
    return input


def score(input):
    total = 0
    for i, line in enumerate(reversed(input)):
        total += (i + 1) * line.count("O")
    return total


def spin_cycle(input, do_rotate: bool = False):
    for _ in range(4):
        for _ in range(len(input)):
            input = tilt(input)
        if do_rotate:
            input = ["".join(x) for x in zip(*input[::-1])]
    return input


input = spin_cycle(input)
print(score(input))


seen_hashes = set()
cycles = dict()
for i in range(1000000000):
    input = spin_cycle(input, True)

    h = hash("".join(input))
    if h in seen_hashes:
        cycle_length = i - cycles[h]
        remaining = 1000000000 - i - 1
        offset = remaining % cycle_length
        for _ in range(offset):
            input = spin_cycle(input, True)
        break
    else:
        seen_hashes.add(h)
        cycles[h] = i
print(score(input))
