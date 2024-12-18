import heapq

grid = [list(x.strip()) for x in open("2024/inputs/16.txt").readlines()]
R = len(grid)
C = len(grid[0])


for r in range(R):
    for c in range(C):
        if grid[r][c] == "S":
            S = (r, c)
        if grid[r][c] == "E":
            E = (r, c)


def path_score():
    q = [(0, S, 0, 1)]  # (cost, (r, c), dr, dc)
    visited = set()

    while q:
        cost, (r, c), dr, dc = heapq.heappop(q)

        if (r, c) == E:
            return cost

        if (r, c) in visited:
            continue
        else:
            visited.add((r, c))

        neighbors = [
            ((r + dr, c + dc), dr, dc, 1),  # Move forward
            ((r + dc, c - dr), dc, -dr, 1001),  # Rotate clockwise + move forward
            ((r - dc, c + dr), -dc, dr, 1001),  # Rotate counterclockwise + move forward
        ]

        for (nr, nc), new_dr, new_dc, move_cost in neighbors:
            if grid[nr][nc] != "#":
                new_cost = cost + move_cost
                heapq.heappush(q, (new_cost, (nr, nc), new_dr, new_dc))


print(path_score())
