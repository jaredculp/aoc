from collections import Counter
from functools import reduce
from itertools import combinations_with_replacement, permutations
from operator import mul
from typing import Dict, Optional

inputs = [x.strip() for x in open("inputs/2015/15.txt").readlines()]

items = dict()
for input in inputs:
    item, rest = input.split(": ")
    props = [y for x in rest.split(", ") for y in x.split(" ")]
    # turn [a 1 b 2] into {a: 1, b: 2}
    props = dict(zip(props[::2], props[1::2]))
    items[item] = props
ingredients = items.keys()


def score(
    amounts: Dict[str, int], target_calories: Optional[int] = None
) -> int:
    calories = 0
    for item, amount in amounts.items():
        calories += amount * int(items[item]["calories"])

    if target_calories and calories != target_calories:
        return 0

    scores = []
    for prop in {"capacity", "durability", "flavor", "texture"}:
        total = 0
        for item, amount in amounts.items():
            total += amount * int(items[item][prop])
        scores.append(max(0, total))
    return reduce(mul, scores)


part_1, part_2 = 0, 0
for c in combinations_with_replacement(ingredients, 100):
    item_amounts = Counter(c)

    part_1 = max(score(item_amounts), part_1)
    part_2 = max(score(item_amounts, 500), part_2)

print("part1: ", part_1)
print("part2: ", part_2)
