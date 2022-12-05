import re
from collections import defaultdict

input = open("2022/inputs/05.txt").read()
inputs, commands = [x.split("\n") for x in input.split("\n\n")]
inputs.pop()
commands.pop()

s1 = defaultdict(list)
s2 = defaultdict(list)

for input in reversed(inputs):
    for i, letter in enumerate(input[1::4]):
        if letter != " ":
            s1[i + 1].append(letter)
            s2[i + 1].append(letter)

for command in commands:
    amt, fr, to = re.findall(r"\d+", command)

    i = len(s2[int(to)])
    for _ in range(int(amt)):
        move = s1[int(fr)].pop()
        s1[int(to)].append(move)

        move = s2[int(fr)].pop()
        s2[int(to)].insert(i, move)

for stack in [s1, s2]:
    print("".join(s.pop() for s in stack.values()))
