import re
from math import prod

inputs = [x.strip() for x in open("2022/inputs/11.txt").read().split("\n\n")]


class Monkey:
    def __init__(self, items, op, test, true_cond, false_cond):
        self.items = [int(x) for x in items]
        self.op = op
        self.test = int(test)
        self.true_cond = int(true_cond)
        self.false_cond = int(false_cond)
        self.inspected = 0


def simulate(rounds: int, divide: bool) -> int:
    monkeys = []
    for input in inputs:
        data = input.splitlines()

        monkeys.append(
            Monkey(
                items=re.findall(r"\d+", data[1]),
                op=data[2].split(" = ")[-1],
                test=re.findall(r"\d+", data[3])[0],
                true_cond=re.findall(r"\d+", data[4])[0],
                false_cond=re.findall(r"\d+", data[5])[0],
            )
        )

    # thanks reddit: https://www.reddit.com/r/adventofcode/comments/zifqmh/2022_day_11_solutions/izrd7iz/
    # (a mod kn) mod n = a mod n for any integer * k
    mod = prod(m.test for m in monkeys)

    for turn in range(rounds):
        for monkey in monkeys:
            while monkey.items:
                monkey.inspected += 1
                old = monkey.items.pop(0) % mod
                new = eval(monkey.op)
                new = new // 3 if divide else new
                i = monkey.true_cond if new % monkey.test == 0 else monkey.false_cond
                monkeys[i].items.append(new)

    return prod(x.inspected for x in sorted(monkeys, key=lambda m: m.inspected)[-2:])


print(simulate(20, True))
print(simulate(10_000, False))
