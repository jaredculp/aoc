import re
from collections import defaultdict
from itertools import accumulate

inputs = [x.strip() for x in open("2022/inputs/07.txt")]
dir_stack = []
sizes = defaultdict(int)
for input in inputs:
    cd = re.match(r"\$ cd (.+)", input)
    if cd:
        if cd.group(1) == "/":
            dir_stack = ["/"]
        elif cd.group(1) == "..":
            dir_stack.pop()
        else:
            dir_stack.append(cd.group(1) + "/")

    f = re.match(r"(\d+) .+", input)
    if f:
        for d in accumulate(dir_stack):
            sizes[d] += int(f.group(1))

print(sum(x for x in sizes.values() if x <= 100_000))
print(
    min(
        x
        for x in sizes.values()
        if x != "/" and 70_000_000 - sizes["/"] + x >= 30_000_000
    )
)
