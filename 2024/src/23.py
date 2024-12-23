from collections import defaultdict

input = open("2024/inputs/23.txt").readlines()

network = defaultdict(set)

for line in input:
    a, b = line.strip().split("-")
    network[a].add(b)
    network[b].add(a)


print(
    sum(
        a in network[c] and any(x.startswith("t") for x in [a, b, c])
        for a in network
        for b in network[a]
        for c in network[b]
    )
    // 6  # duplicates of [a, b, c] has 3! orderings
)


def password():
    cliques = set()

    def find_cliques(node, clique):
        for conn in network[node]:
            new_clique = clique | {conn}
            if clique <= network[conn]:
                if (c := tuple(new_clique)) and c not in cliques:
                    cliques.add(c)
                    find_cliques(conn, new_clique)

    for node in network:
        find_cliques(node, {node})

    return cliques


print(",".join(sorted(max(password(), key=len))))
