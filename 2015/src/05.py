input = [x.strip() for x in open("2015/inputs/05.txt").readlines()]

nice = 0
for string in input:
    vowels = len([x for x in string if x in {"a", "e", "i", "o", "u"}]) >= 3

    prev = string[0]
    repeated = False
    for x in string[1:]:
        if x == prev:
            repeated = True
            break
        prev = x

    substrings = not any([x in string for x in {"ab", "cd", "pq", "xy"}])

    if all([vowels, repeated, substrings]):
        nice += 1

print(nice)

nice = 0
for string in input:
    pairs = set()
    a = string[0]
    for b in string[1:]:
        pairs.add(f"{a}{b}")
        a = b

    pair_match = False
    for pair in pairs:
        first_match = string.find(pair)
        if first_match >= 0:
            second_match = string.find(pair, first_match + 2)
            if second_match >= 0:
                pair_match = True
                break

    a, b, c = string[0:3]
    sandwich_match = False
    for x in string[3:]:
        if a == c and a != b:
            sandwich_match = True
            break
        a, b, c = b, c, x
    else:
        if a == c and a != b:
            sandwich_match = True

    if pair_match and sandwich_match:
        nice += 1

print(nice)
