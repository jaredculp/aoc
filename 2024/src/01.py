import re
from collections import Counter

input = [x.strip() for x in open("2024/inputs/01.txt").readlines()]
input = [re.findall(r"\d+", x) for x in input]
input = [int(xx) for x in input for xx in x]
a = sorted(input[::2])
b = sorted(input[1::2])

print(sum(abs(a[i] - b[i]) for i in range(len(a))))

counts = Counter(b)
print(sum(aa * counts.get(aa, 0) for aa in a))
