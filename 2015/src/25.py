import re

input = open("2015/inputs/25.txt").readline()
row, col = [int(x) for x in re.search(r".*row (\d+), column (\d+).", input).groups()]


i = 20151125
x, y = 1, 1

while True:
    if y == 1:
        y = x + 1
        x = 1
    else:
        y -= 1
        x += 1

    i = (i * 252533) % 33554393

    if y == row and x == col:
        print(i)
        break
