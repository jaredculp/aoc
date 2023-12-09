import re

inputs = [
    [int(i) for i in re.findall(r"-?\d+", input)]
    for input in open("2023/inputs/09.txt").readlines()
]

fw_bases = []
bw_bases = []
for input in inputs:
    outputs = [input]
    while not all(x == 0 for x in input):
        output = []
        for i in range(len(input) - 1):
            a, b = [int(x) for x in input[i : i + 2]]
            output.append(b - a)
        input = output
        outputs.append(output)

    fw_base = 0
    bw_base = 0
    for i in reversed(outputs[:-1]):
        delta = i[-1]
        fw_base = i[-1] + fw_base
        bw_base = i[0] - bw_base
    fw_bases.append(fw_base)
    bw_bases.append(bw_base)

print(sum(fw_bases))
print(sum(bw_bases))
