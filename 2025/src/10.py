import re
from dataclasses import dataclass
from itertools import combinations

input = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}""".splitlines()
input = [x.strip() for x in open("2025/inputs/10.txt").readlines()]


@dataclass(frozen=True)
class Machine:
    diagram: list[int]
    lights: list[int]
    buttons: list[list[int]]
    joltage: list[int]

    digits = re.compile(r"\d+")
    on_off = {".": 0, "#": 1}
    toggle = {0: 1, 1: 0}

    @classmethod
    def from_input(cls, line: str) -> "Machine":
        diagram, *buttons, joltage = line.split()

        diagram = [Machine.on_off[x] for x in diagram[1:-1]]
        buttons = [[int(d) for d in re.findall(Machine.digits, b)] for b in buttons]
        joltage = [int(d) for d in re.findall(Machine.digits, joltage[1:-1])]

        return cls(diagram, [0] * len(diagram), buttons, joltage)

    def push(self, *buttons: int) -> bool:
        machine = self
        for b in buttons:
            lights = [
                Machine.toggle[indicator] if i in machine.buttons[b] else indicator
                for i, indicator in enumerate(machine.lights)
            ]
            machine = Machine(machine.diagram, lights, machine.buttons, machine.joltage)

        return machine.lights == machine.diagram


machines = [Machine.from_input(line) for line in input]
p1 = 0
for machine in machines:
    buttons = len(machine.buttons)
    p1 += min(
        n
        for n in range(1, buttons + 1)
        for pushes in combinations(range(buttons), n)
        if machine.push(*pushes)
    )

print(p1)
