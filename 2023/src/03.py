import re
from functools import reduce

input = [l.strip() for l in open("2023/inputs/03.txt").readlines()]
length = len(input[0])
input = "".join(input)

# fmt: off
adjs = [
    -length - 1, # TL
    -length,     # T
    -length + 1, # TR
    -1,          # L
    1,           # R
    length - 1,  # BL
    length,      # B
    length + 1,  # BR
]
# fmt: on

# part 1
nums = []
for number_group in re.finditer(r"\d+", input):
    matched = False
    for number in range(*number_group.span()):
        for adj in adjs:
            if (offset := int(number) + adj) >= len(input):
                continue

            neighbor = input[offset]
            if neighbor.isnumeric() or neighbor == ".":
                continue

            matched = True

    if matched:
        nums.append(int(number_group.group()))

print(reduce(lambda a, b: a + b, nums, 0))

# part 2
number_groups = list(re.finditer(r"\d+", input))
nums = []
for gear in re.finditer(r"\*", input):
    gear_numbers = set()
    for number in range(*gear.span()):
        for adj in adjs:
            if (offset := int(number) + adj) >= len(input):
                continue

            neighbor = input[offset]
            if neighbor.isnumeric():
                if match := next(
                    (
                        int(n.group())
                        for n in number_groups
                        if n.span()[0] <= offset <= n.span()[1]
                    ),
                    None,
                ):
                    gear_numbers.add(match)

    if len(gear_numbers) == 2:
        nums.append(reduce(lambda a, b: a * b, list(gear_numbers), 1))

print(reduce(lambda a, b: a + b, nums, 0))
