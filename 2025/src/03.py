input = [x.strip() for x in open("2025/inputs/03.txt").readlines()]
bank = len(input[0])

# my original approach worked for p1 but suffered from
# combinatorial explosion in p2.
# p1: 100 C 2  = 4950
# p2: 100 C 12 = 1.05e15 :(
#
# from itertools import combinations
#
# joltage = 0
# for line in input:
#     pairs = sorted(
#         combinations(enumerate(line), 2),
#         key=lambda x: int(x[0][1] + x[1][1]),
#         reverse=True,
#     )
#     joltage += next(int(x + y) for (xi, x), (yi, y) in pairs if xi < yi)

for N in [2, 12]:
    joltage = 0
    for line in input:
        batteries = ""
        start = 0
        for _ in range(N):
            # prune the search space:
            # i.e. if we need 12 digits and we only have 2,
            #      then we can't pick anything less than 10
            #      from the end.
            end = bank - N + len(batteries) + 1
            # look for the largest number in the search space
            battery = max(line[start:end])
            # we can inline this because if find has no match
            # then -1 + 1 = 0 and its a no-op.
            start = line.find(battery, start, end) + 1
            batteries += battery
        joltage += int(batteries)

    print(joltage)
