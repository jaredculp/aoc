import json

inputs = [
    [json.loads(y) for y in x.split("\n") if y != ""]
    for x in open("2022/inputs/13.txt").read().split("\n\n")
]


def compare(a, b) -> bool:
    """
    Negative # indicates a < b  (ordered)
    Zero       indicates a == b (continue)
    Positive # indicates a > b  (unordered)
    """
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    elif isinstance(a, int) and isinstance(b, list):
        return compare([a], b)
    elif isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])
    else:
        for aa, bb in zip(a, b):
            diff = compare(aa, bb)
            if diff:
                return diff
        # zip will stop once one list is exhausted, so check the sizes, since
        # all elements are equal up to this point
        return len(a) - len(b)


indices, lt2, lt6 = 0, 1, 2
for i, (a, b) in enumerate(inputs):
    if compare(a, b) < 0:
        indices += i + 1

    for x in [a, b]:
        if compare(x, [[2]]) < 0:
            lt2 += 1
        if compare(x, [[6]]) < 0:
            lt6 += 1

print(indices)
print(lt2 * lt6)
