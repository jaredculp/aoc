from collections import defaultdict

input = [list(l) for l in open("2024/inputs/04.txt").readlines()]

R = len(input)
C = len(input[0])
rows = input
cols = list(zip(*input))
diags_tlbr = defaultdict(list)
diags_trbl = defaultdict(list)
for r in range(R):
    for c in range(C):
        diags_tlbr[r + c].append(input[r][c])  # tl->br diag have a constant r + c
        diags_trbl[r - c].append(input[r][c])  # tr->bl diag have a constant r - c

print(
    sum(
        "".join(s).count("XMAS") + "".join(s).count("SAMX")
        for search in [rows, cols, diags_tlbr.values(), diags_trbl.values()]
        for s in search
    )
)

print(
    sum(
        1
        for r in range(1, R - 1)
        for c in range(1, C - 1)
        if all(
            diag in {"SAM", "MAS"}
            for diag in (
                input[r - 1][c - 1] + input[r][c] + input[r + 1][c + 1],  # tl->br diag
                input[r + 1][c - 1] + input[r][c] + input[r - 1][c + 1],  # tr->bl diag
            )
        )
    )
)
