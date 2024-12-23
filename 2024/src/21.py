input = """+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+""".splitlines()
# input = open("2024/inputs/21.txt").readlines()
print(input)

n = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["#", "0", "A"]]
nr, nc = len(n), len(n[0])
d = [["#", "^", "A"], ["<", "v", ">"]]
dr, dc = len(d), len(d[0])

dr1 = (0, 2)
dr2 = (0, 2)
nr = (3, 2)

seq = "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"


def move(r, c, press):
    if press == "^":
        return (r - 1, c)
    if press == "v":
        return (r + 1, c)
    if press == "<":
        return (r, c - 1)
    if press == ">":
        return (r, c + 1)


for s in seq:
    pass
