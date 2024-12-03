import re
from random import shuffle
from typing import List, Tuple

inputs = [x.strip() for x in open("2015/inputs/19.txt").readlines()]
target_molecule = inputs.pop()

mods: List[Tuple[str, str]] = []
for input in inputs[:-1]:
    lhs, rhs = input.split(" => ")
    mods.append((lhs, rhs))

molecule = target_molecule
molecules = set()
for src, repl in mods:
    for p in [m.start() for m in re.finditer(src, molecule)]:
        molecules.add(molecule[:p] + repl + molecule[p + len(src) :])

print(len(molecules))

count = 0
while molecule != "e":
    for src, repl in mods:
        if repl not in molecule:
            continue

        molecule = molecule.replace(repl, src, 1)
        count += 1

    shuffle(mods)

print(count)
