import re
from itertools import permutations
from typing import Dict, Optional, Tuple

inputs = [x.strip() for x in open("2015/inputs/13.txt").readlines()]
me = "ME"


def seating(include_self: Optional[bool] = False) -> int:
    pairings: Dict[Tuple[str, str], int] = dict()
    people = set()

    for input in inputs:
        a, gain, amt, b = re.search(
            r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to"
            r" (\w+).",
            input,
        ).groups()

        pairings[(a, b)] = int(amt) if gain == "gain" else -int(amt)
        people = people.union({a, b})

    if include_self:
        for person in people:
            pairings[(person, me)] = 0
            pairings[(me, person)] = 0
        people = people.union({me})

    best = float("-inf")
    seats = len(people)
    for arrangement in permutations(people):
        seatings = [
            [
                arrangement[(x - 1) % seats],
                arrangement[x % seats],
                arrangement[(x + 1) % seats],
            ]
            for x in range(seats)
        ]

        total = 0
        for seating in seatings:
            a, b, c = seating
            total += pairings[(b, a)] + pairings[(b, c)]

        best = max(total, best)

    return best


print("part1: ", seating())
print("part2: ", seating(True))
