from typing import Iterable

input = open("2025/inputs/02.txt").read().strip().split(",")


# my less elegant solution
def is_invalid(s: str, sizes: Iterable[int]) -> bool:
    L = len(s)
    return any(n and L % n == 0 and s == s[:n] * (L // n) for n in sizes)


p1 = p2 = 0
for line in input:
    low, high = line.split("-")
    for n in range(int(low), int(high) + 1):
        S = str(n)
        L = len(S)
        if is_invalid(S, [L // 2]):
            p1 += n
        if is_invalid(S, range(1, L // 2 + 1)):
            p2 += n

print(p1)
print(p2)

# a much more clever way to solve using regex
# p1 = p2 = 0
# for line in input:
#     low, high = line.split("-")
#     for n in range(int(low), int(high) + 1):
#         if re.match(r"^(\d+)\1$", str(n)):
#             p1 += n
#         if re.match(r"^(\d+)\1+$", str(n)):
#             p2 += n
#
# print(p1)
# print(p2)
