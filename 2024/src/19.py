from functools import cache

input = open("2024/inputs/19.txt").read().strip()
towels, designs = input.split("\n\n")
towels = set(towels.split(", "))
designs = designs.split("\n")


@cache
def arrange(todo):
    if todo == "":
        return 1

    arrangements = 0
    for j in range(1, len(todo) + 1):
        towel, new_todo = todo[:j], todo[j:]
        if towel in towels:
            arrangements += arrange(new_todo)
    return arrangements


print(sum(arrange(design) > 0 for design in designs))
print(sum(arrange(design) for design in designs))
