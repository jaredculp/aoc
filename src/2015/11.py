import string

letters = string.ascii_lowercase
indices = {d: i for i, d in enumerate(letters, 1)}
triples = [letters[i : i + 3] for i in range(len(letters) - 2)]
invalid = "iol"
pairs = {f"{x}{x}" for x in letters}


def to_str(x: int) -> str:
    if x == 0:
        return ""

    q, r = divmod(x - 1, 26)
    return to_str(q) + letters[r]


def to_int(x: str) -> int:
    result = 0
    for c in x:
        result = result * 26 + indices[c]
    return result


def first_req(pw: str) -> bool:
    return any(pw.count(x) for x in triples)


def second_req(pw: str) -> bool:
    return not any(x in invalid for x in pw)


def third_req(pw: str) -> bool:
    return sum(1 if pw.count(x) else 0 for x in pairs) >= 2


def valid(pw: str) -> bool:
    return first_req(pw) and second_req(pw) and third_req(pw)


def increment_pw(pw: str) -> str:
    return to_str(to_int(pw) + 1)


def next_pw(pw: str) -> str:
    pw = increment_pw(pw)
    while not valid(pw):
        pw = increment_pw(pw)
    return pw


part1 = next_pw("vzbxkghb")
print("part1: ", part1)

part2 = next_pw(part1)
print("part2: ", part2)
