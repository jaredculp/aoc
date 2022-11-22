import re
from typing import List, Optional, Tuple

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

print("part1: ", len(molecules))


def steps(molecule: str, count: int) -> Optional[int]:
    print(count)
    if molecule == target_molecule:
        return steps

    for src, repl in mods:
        for p in [m.start() for m in re.finditer(src, molecule)]:
            new_molecule = molecule[:p] + repl + molecule[p + len(src) :]
            return steps(new_molecule, count + 1)


print(steps("e", 0))
