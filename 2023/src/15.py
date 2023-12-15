from dataclasses import dataclass

input = open("2023/inputs/15.txt").read().split(",")


def hash(x):
    cv = 0
    for xx in x:
        cv += ord(xx)
        cv *= 17
        cv %= 256
    return cv


print(sum(hash(x) for x in input))


@dataclass
class Lens:
    label: str
    length: int


class HashMap:
    def __init__(self):
        self._boxes: list[list[Lens]] = [[] for _ in range(256)]

    def parse(self, instr):
        if "=" in instr:
            h, l = instr.split("=")
            box = self._boxes[hash(h)]
            lens = Lens(h, int(l))
            if (
                i := next((i for i, l in enumerate(box) if l.label == h), None)
            ) is not None:
                box[i] = lens
            else:
                box.append(lens)
        elif "-" in instr:
            h, _ = instr.split("-")
            hh = hash(h)
            self._boxes[hh] = [l for l in self._boxes[hh] if not l.label == h]

    def focus_power(self):
        total = 0
        for i, b in enumerate(self._boxes):
            for j, bb in enumerate(b):
                total += (i + 1) * (j + 1) * bb.length
        return total


h = HashMap()
for i in input:
    h.parse(i)
print(h.focus_power())
