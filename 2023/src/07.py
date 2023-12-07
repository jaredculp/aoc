from collections import Counter

lines = [l.strip() for l in open("2023/inputs/07.txt").readlines()]


def score_hand(h: str, r: str | None = None) -> int:
    c = Counter(h.replace("J", r) if r else h)
    match sorted(c.values(), reverse=True):
        case [5, *_]:
            rank = "7"
        case [4, *_]:
            rank = "6"
        case [3, 2, *_]:
            rank = "5"
        case [3, *_]:
            rank = "4"
        case [2, 2, *_]:
            rank = "3"
        case [2, *_]:
            rank = "2"
        case _:
            rank = "1"

    for x, y in {
        "A": "E",
        "K": "D",
        "Q": "C",
        "J": "1" if r else "B",
        "T": "A",
    }.items():
        h = h.replace(x, y)

    return int(rank + h, 15)


hand_bids = {h: int(b) for h, b in (line.split() for line in lines)}
parts = [dict(), dict()]
for h, b in hand_bids.items():
    scored_hand = score_hand(h)
    parts[0][scored_hand] = b

    scored_hand = max(score_hand(h, r) for r in "AKQT98765432")
    parts[1][scored_hand] = b

for part in parts:
    print(sum(part[h] * (i + 1) for i, h in enumerate(sorted(part))))
