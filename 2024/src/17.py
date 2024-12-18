import re


def literal(op):
    return op


def combo(op, a, b, c):
    match op:
        case 0 | 1 | 2 | 3:
            return op
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c
    raise


def run(a, b, c, program):
    ip = 0
    output = []

    literal = lambda op: op
    combo = lambda op: [0, 1, 2, 3, a, b, c, None][op]

    while ip < len(program):
        instr, op = program[ip], program[ip + 1]
        match instr:
            case 0:
                a = a // (2 ** combo(op))
            case 1:
                b ^= literal(op)
            case 2:
                b = combo(op) % 8
            case 3:
                if a != 0:
                    ip = literal(op)
                    continue
            case 4:
                b = b ^ c
            case 5:
                output.append(combo(op) % 8)
            case 6:
                b = a // (2 ** combo(op))
            case 7:
                c = a // (2 ** combo(op))

        ip += 2

    return output


input = open("2024/inputs/17.txt").read()
registers, program = input.split("\n\n")
a, b, c = map(int, re.findall(r"\d+", registers))
program = list(map(int, re.findall(r"\d+", program)))

print(",".join(str(x) for x in run(a, b, c, program)))
