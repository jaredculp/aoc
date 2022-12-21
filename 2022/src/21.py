from collections import defaultdict

inputs = [x.strip() for x in open("2022/inputs/21.txt").readlines()]


G = dict()

for input in inputs:
    lhs, rhs = input.split(": ")
    rhs = rhs.split()
    if len(rhs) == 3:
        m1, op, m2 = rhs
        G[lhs] = (m1, op, m2)
    else:
        G[lhs] = int(rhs[0])


def dfs(G, monkey):
    value = G[monkey]
    if isinstance(value, int):
        return value

    m1, op, m2 = value
    if op == "==":
        return dfs(G, m2) - dfs(G, m1)
    if op == "+":
        return dfs(G, m1) + dfs(G, m2)
    if op == "-":
        return dfs(G, m1) - dfs(G, m2)
    if op == "*":
        return dfs(G, m1) * dfs(G, m2)
    if op == "/":
        return dfs(G, m1) // dfs(G, m2)


print(dfs(G, "root"))

G["root"] = (G["root"][0], "==", G["root"][2])
lo, hi = 0, 99999999999999
while True:
    G["humn"] = (lo + hi) // 2
    result = dfs(G, "root")
    if result < 0:
        lo = G["humn"] + 1
    elif result > 0:
        hi = G["humn"] - 1
    else:
        break

print(G["humn"])
