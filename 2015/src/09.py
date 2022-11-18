from collections import defaultdict
from itertools import permutations
from typing import Dict, Tuple

inputs = [x.strip() for x in open("2015/inputs/09.txt").readlines()]

distances: Dict[Tuple[str, str], int] = defaultdict(lambda: float("inf"))
cities = set()

for input in inputs:
    itinerary, distance = input.split(" = ")
    origin, destination = itinerary.split(" to ")

    distances[(origin, destination)] = int(distance)
    distances[(destination, origin)] = int(distance)
    cities.add(origin)
    cities.add(destination)


shortest = float("inf")
longest = 0
possible_trips = permutations(cities)
for trip in possible_trips:
    distance = 0
    for i in range(len(trip) - 1):
        distance += distances[(trip[i], trip[i + 1])]

    shortest = min(shortest, distance)
    longest = max(longest, distance)

print("part1: ", shortest)
print("part2: ", longest)
