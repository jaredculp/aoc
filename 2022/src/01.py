inputs = [x.strip() for x in open("2022/inputs/01.txt").readlines()]

elves = []
elf = 0
for input in inputs:
    if input == "":
        elves.append(elf)
        elf = 0
        continue

    elf += int(input)

print(max(elves))
print(sum(sorted(elves, reverse=True)[:3]))
