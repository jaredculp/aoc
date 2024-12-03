f = open("2015/inputs/01.txt")
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

print(count)
print(basement)
