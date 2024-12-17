input = open("2024/inputs/10.txt").readlines()
input = [list(map(int, x.strip())) for x in input]

R = len(input)
C = len(input[0])

starts = []
for r in range(R):
    for c in range(C):
        if input[r][c] == 0:
            starts.append((r, c))

dirs = []


def dfs(r, c, seen, all_trails=False):
    seen.add((r, c))

    height = input[r][c]
    if height == 9:
        return 1

    count = 0
    for dr, dc in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        rr = r + dr
        cc = c + dc

        if not all_trails and (rr, cc) in seen:
            continue

        if 0 <= rr < R and 0 <= cc < C and input[rr][cc] == height + 1:
            count += dfs(rr, cc, seen, all_trails)

    return count


print(sum(dfs(r, c, seen=set()) for r, c in starts))
print(sum(dfs(r, c, seen=set(), all_trails=True) for r, c in starts))
