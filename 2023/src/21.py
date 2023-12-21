input = [list(x) for x in open("2023/inputs/21.txt").readlines()]
X = len(input[0])
Y = len(input)
N = 64

x, y = next((x, y) for x in range(X) for y in range(Y) if input[y][x] == "S")

plot = tuple[int, int, int]

count = 0
seen: set[plot] = set()
q: list[plot] = [(x, y, 0)]
while q:
    x, y, n = q.pop()

    if n == N:
        count += 1
        continue

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x = x + dx
        new_y = y + dy
        new_n = n + 1
        if (
            (new_x, new_y, new_n) not in seen
            and 0 <= new_x < X
            and 0 <= new_y < Y
            and input[new_y][new_x] in "S."
            and new_n <= N
        ):
            seen.add((new_x, new_y, new_n))
            q.append((new_x, new_y, new_n))

print(count)
