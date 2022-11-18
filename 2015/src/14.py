import re
from collections import defaultdict
from itertools import cycle, islice
from typing import Dict, Iterator, List

inputs = [x.strip() for x in open("2015/inputs/14.txt").readlines()]


def setup_raindeer() -> Dict[str, Iterator[int]]:
    all_reindeer = dict()
    for input in inputs:
        reindeer, speed, duration, rest = re.match(
            r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must"
            r" rest for"
            r" (\d+) seconds.",
            input,
        ).groups()

        distances = [int(speed)] * int(duration) + [0] * int(rest)
        all_reindeer[reindeer] = cycle(distances)

    return all_reindeer


def reindeer_distances(seconds: int) -> List[int]:
    all_reindeer = setup_raindeer()
    return [
        sum(islice(distances, seconds))
        for reindeer, distances in all_reindeer.items()
    ]


def reindeer_points(seconds: int) -> List[int]:
    all_reindeer = setup_raindeer()

    points = defaultdict(int)
    positions = defaultdict(int)
    for x in range(seconds):
        for reindeer, distances in all_reindeer.items():
            positions[reindeer] += next(distances)

        winners = {
            k for k, v in positions.items() if v == max(positions.values())
        }
        for winner in winners:
            points[winner] += 1

    return points.values()


print("part1: ", max(reindeer_distances(2503)))
print("part2: ", max(reindeer_points(2503)))
