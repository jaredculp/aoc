input = open("2025/inputs/04.txt").readlines()

# neighbor coordinates
n = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def find_rolls(rounds=1):
    G = [list(x) for x in input]
    R = len(G)
    C = len(G[0])
    rolls = set()
    for _ in range(rounds):
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


# a more clever approach which uses set theory
# calculate the roll locations and intersect with all neighbor rolls
# you don't even need to do bounds checking on this one, since any
# neighbor that is out of bounds won't be in the first set
#
# def find_rolls(rounds=1):
#     G = [list(x) for x in input]
#     R = len(G)
#     C = len(G[0])
#     rolls = {(r, c) for r in range(R) for c in range(C) if G[r][c] == "@"}
#     removed_rolls = set()
#     for _ in range(rounds):
#         for r, c in list(rolls): # copy since we modify size in loop
#             neighbors = {(r + dr, c + dc) for dr, dc in n}
#             if len(rolls & neighbors) < 4:
#                 removed_rolls.add((r, c))
#
#                 if rounds > 1:
#                     rolls.remove((r, c))
#
#     return len(removed_rolls)
#
#
# print(find_rolls())
# print(find_rolls(100))
