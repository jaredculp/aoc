from functools import cache

input = open("2025/inputs/11.txt").readlines()


G = {a: b.split() for line in input for a, b, *_ in [line.split(":")]}


@cache
def paths(n, to_see=()):
    if n == "out":
        return not to_see
    return sum(paths(nn, tuple(x for x in to_see if x != n)) for nn in G[n])


print(paths("you"))
print(paths("svr", ("dac", "fft")))
