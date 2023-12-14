patterns = open("2023/inputs/13.txt").read().split("\n\n")


def differences(input: str | list[str], i: int) -> int:
    return sum(
        c != d for a, b in zip(reversed(input[:i]), input[i:]) for c, d in zip(a, b)
    )


def score(smudge: int = 0) -> int:
    total = 0
    for pattern in patterns:
        lines = pattern.splitlines()

        for i in range(1, len(lines[0])):
            if sum(differences(line, i) for line in lines) == smudge:
                total += i

        for i in range(len(lines)):
            if differences(lines, i) == smudge:
                total += 100 * i

    return total


print(score(0))
print(score(1))
