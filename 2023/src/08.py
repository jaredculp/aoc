import re
from math import lcm
from itertools import cycle

input = [l.strip() for l in open("2023/inputs/08.txt").readlines()]

instr = input.pop(0).replace("L", "0").replace("R", "1")
instr = cycle(int(x) for x in instr)

instrs = dict()
for i in input:
    if not i.strip():
        continue

    l, ll, rr = re.findall(r"\w{3}", i)
    instrs[l] = (ll, rr)

# part 1
curr = "AAA"
count = 0
while curr != "ZZZ":
    count += 1
    curr = instrs[curr][next(instr)]
print(count)

# part 2
currs = [k for k in instrs.keys() if k.endswith("A")]
counts = []
for c in currs:
    count = 0
    while not c.endswith("Z"):
        count += 1
        c = instrs[c][next(instr)]
    counts.append(count)
print(lcm(*counts))
