from collections import defaultdict

from graphlib import TopologicalSorter

input = open("2024/inputs/05.txt").read()
rules, updates = input.split("\n\n")
rules = [tuple(map(int, r.split("|"))) for r in rules.split()]
updates = [list(map(int, u.split(","))) for u in updates.split()]

ordering = defaultdict(list)
for a, b in rules:
    ordering[a].append(b)

count = 0
bad_updates = []
for update in updates:
    seen = []
    for x in update:
        seen.append(x)
        if any(s in ordering[x] for s in seen):
            bad_updates.append(update)
            break
    else:
        count += update[len(update) // 2]
print(count)

count = 0
for update in bad_updates:
    graph = defaultdict(list)
    for x in update:
        graph[x] = [xx for xx in ordering[x] if xx in update]
    corrected = list(TopologicalSorter(graph).static_order())
    count += corrected[len(corrected) // 2]
print(count)
