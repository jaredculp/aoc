input = open("2024/inputs/25.txt").read()

schematics = input.split("\n\n")

locks = []
keys = []
for s in schematics:
    heights = [col.count("#") - 1 for col in zip(*(list(x) for x in s.split()))]
    if all(x == "#" for x in s[0]):
        locks.append(heights)
    else:
        keys.append(heights)

max_height = len(schematics[0].split()[0])
print(
    sum(
        all(lock[i] + key[i] <= max_height for i in range(max_height))
        for lock in locks
        for key in keys
    )
)
