from functools import reduce
from operator import add, mul

input = open("2025/inputs/06.txt").readlines()

rows = [list(r.split()) for r in input if r.strip()]


def math(cs):
    ops = {"+": add, "*": mul}
    return sum(reduce(ops[op], [int(n) for n in nums if n.strip()]) for *nums, op in cs)


cols = list(zip(*rows))
print(math(cols))


W = max(len(r) for r in input if r.strip())
rows = [list(r.ljust(W)) for r in input if r.strip()]

buff = []
cols = []
for *nums, op in list(zip(*rows)):
    num = "".join(n for n in nums if n.strip())
    if not num.strip():
        continue

    if op.strip():
        if buff:
            cols.append(buff)
        buff = [op]

    buff.insert(0, num)
cols.append(buff)

print(math(cols))
