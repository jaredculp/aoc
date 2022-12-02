inputs = [x.strip() for x in open("2022/inputs/02.txt").readlines()]


part1 = {
    # wins
    "A Y": 8,
    "B Z": 9,
    "C X": 7,
    # draws
    "A X": 4,
    "B Y": 5,
    "C Z": 6,
    # loses
    "A Z": 3,
    "B X": 1,
    "C Y": 2,
}
print("part1", sum(part1[x] for x in inputs))

part2 = {
    # wins
    "A Z": 8,
    "B Z": 9,
    "C Z": 7,
    # draws
    "A Y": 4,
    "B Y": 5,
    "C Y": 6,
    # losses
    "A X": 3,
    "B X": 1,
    "C X": 2,
}
print("part2", sum(part2[x] for x in inputs))
