import re


def manhattan(a: complex, b: complex) -> int:
    return int(abs(a.real - b.real) + abs(a.imag - b.imag))


inputs = [x.strip() for x in open("2022/inputs/15.txt").readlines()]

S = dict()
B = set()
for input in inputs:
    x1, y1, x2, y2 = map(int, re.findall(r"-?\d+", input))
    s, b = complex(x1, y1), complex(x2, y2)
    S[s] = manhattan(s, b)
    B.add(b)


# B = set()
# y = 2_000_000
# for s, d in S.items():
#    for x in range(int(s.real - d), int(s.real + d)):
#        target = complex(x, y)
#        if manhattan(s, target) <= d:
#            B.add(target)
#
# print(len(B) - 1)

for s, d in S.items():
    for dx in range(d + 2):
        for n in {-1 - 1j, 1 - 1j, -1 + 1j, 1 + 1j}:
            target = s + (dx * n)

            if not (0 <= target.real <= 4e6 and 0 <= target.imag <= 4e6):
                continue

            if all(manhattan(s, target) > d for s in S):
                print(target)
                exit(0)
