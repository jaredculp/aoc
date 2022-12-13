import string
from collections import defaultdict

inputs = [x.strip() for x in open("2022/inputs/12.txt").readlines()]

points = {}
graph = defaultdict(list)
start, starts, end = None, [], None
for y, line in enumerate(inputs):
    for x, letter in enumerate(line):
        point = complex(x, y)
        if letter == "S":
            value = 0
            start = point
            starts.append(point)
        elif letter == "a":
            value = 0
            starts.append(point)
        elif letter == "E":
            value = 25
            end = point
        else:
            value = string.ascii_lowercase.index(letter)
        points[point] = value

for point in points:
    for neighbor in [1 + 0j, -1 + 0j, 0 + 1j, 0 - 1j]:
        if (point + neighbor) in points:
            graph[point].append(point + neighbor)


def bfs(graph, start, end):
    visited = []
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            for neighbor in graph[node]:
                new_path = list(path)

                if points[neighbor] - points[node] > 1:
                    continue

                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == end:
                    return len(new_path[1:])

            visited.append(node)

    return float("inf")


print(bfs(graph, start, end))
print(min(bfs(graph, s, end) for s in starts))
