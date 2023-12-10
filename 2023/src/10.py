input = [l.strip() for l in open("2023/inputs/10.txt").readlines()]
X = len(input)
Y = len(input[0])

S = next((x, y) for x in range(X) for y in range(Y) if input[y][x] == "S")
sx, sy = S
for x, y in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
    seen = {S}
    path = [S]
    q = [(sx + x, sy + y)]
    while q:
        sx, sy = q.pop(0)
        if (sx, sy) in seen or not ((0 < sx <= X) and (0 < sy <= Y)):
            sx, sy = S
        else:
            seen.add((sx, sy))
            path.append((sx, sy))

        s = input[sy][sx]
        if s == ".":
            sx, sy = S
        else:
            for x, y in {
                "|": [(sx, sy - 1), (sx, sy + 1)],
                "-": [(sx - 1, sy), (sx + 1, sy)],
                "L": [(sx, sy - 1), (sx + 1, sy)],
                "J": [(sx, sy - 1), (sx - 1, sy)],
                "7": [(sx, sy + 1), (sx - 1, sy)],
                "F": [(sx, sy + 1), (sx + 1, sy)],
            }[s]:
                if (x, y) not in seen:
                    q.append((x, y))

path.append(S)
print(len(path) // 2)
