from functools import reduce
from itertools import combinations
from operator import mul
from typing import Optional

inputs = [int(x.strip()) for x in open("2015/inputs/24.txt").readlines()]

total = sum(inputs)


def quantum_entanglement(compartments: Optional[int] = 3):
    weight = total // compartments
    cs = []
    for i in range(len(inputs)):
        cs = [c for c in combinations(inputs, i) if sum(c) == weight]
        if cs:
            return min([reduce(mul, c) for c in cs])


print(quantum_entanglement())
print(quantum_entanglement(4))
