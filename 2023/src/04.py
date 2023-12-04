import re
from collections import defaultdict, Counter

lines = [l.strip() for l in open("2023/inputs/04.txt").readlines()]

scores = defaultdict(int)
for line in lines:
    winners, numbers = line.split("|")
    card, winners = winners.split(":")
    _, num = card.split()
    num = int(num)
    winners = set(re.findall(r"\d+", winners))
    numbers = set(re.findall(r"\d+", numbers))

    scores[num] = len(winners & numbers)

card_counts = Counter({c: 1 for c in scores.keys()})
for card in scores.keys():
    for new_card in range(card + 1, card + scores[card] + 1):
        card_counts.update({new_card: card_counts[card]})

print(sum([2 ** (s - 1) if s else 0 for s in scores.values()]))
print(sum(card_counts.values()))
