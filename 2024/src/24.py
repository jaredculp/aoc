import operator

input = open("2024/inputs/24.txt").read()

inits, wires = input.split("\n\n")
ops = {
    "AND": operator.and_,
    "XOR": operator.xor,
    "OR": operator.or_,
}
gates = {}
for init in inits.splitlines():
    gate, value = init.split(": ")
    gates[gate] = lambda value=int(value): value
for gate in wires.splitlines():
    a, op, b, _, gate = gate.split()
    gates[gate] = lambda a=a, b=b, op=op: ops[op](gates[a](), gates[b]())

print(
    int(
        "".join(
            str(gates[g]()) for g in sorted(gates, reverse=True) if g.startswith("z")
        ),
        2,
    )
)
