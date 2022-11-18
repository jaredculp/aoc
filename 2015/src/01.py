f = open("inputs/2015/01.txt")
input = f.read()

count = 0
basement = None
for i, x in enumerate(input):
    if count < 0 and not basement:
        basement = i
    if x == "(":
        count += 1
    elif x == ")":
        count -= 1

print("part1: ", count)
print("part2: ", basement)
