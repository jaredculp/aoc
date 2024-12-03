import re

input = open("2024/inputs/03.txt").read()
matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do|don't)\(\)", input)
print(sum(int(a) * int(b) for a, b, c in matches if not c))

enabled = True
count = 0
for a, b, flip in matches:
    if flip == "do":
        enabled = True
    elif flip == "don't":
        enabled = False
    elif enabled:
        count += int(a) * int(b)
print(count)
