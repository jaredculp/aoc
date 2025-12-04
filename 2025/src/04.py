input = open("2025/inputs/04.txt").readlines()

# neighbor coordinates
n = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def find_rolls(rounds=1):
    G = [list(x) for x in input]
    R = len(G)
    C = len(G[0])
    rolls = set()
    for r in range(rounds):
        for r in range(R):
            for c in range(C):
                if G[r][c] != "@":
                    continue

                if (
                    sum(
                        G[r + dr][c + dc] == "@"
                        for dr, dc in n
                        if 0 <= r + dr < R and 0 <= c + dc < C
                    )
                    < 4
                ):
                    rolls.add((r, c))
                    if rounds > 1:
                        G[r][c] = "."

    return len(rolls)


print(find_rolls())
print(find_rolls(100))
