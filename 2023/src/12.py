from itertools import groupby
from functools import cache

lines = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""".splitlines()
# lines = [x for x in open("2023/inputs/12.txt").readlines()]


@cache
def arrangements_recursive(springs, arrangement, index=0):
    if "?" not in springs:
        return (
            1
            if tuple(
                sum(1 for _ in group) for key, group in groupby(springs) if key == "#"
            )
            == arrangement
            else 0
        )
    else:
        count = 0
        for replacement in ".#":
            count += arrangements_recursive(
                springs[1:].replace("?", replacement, 1), arrangement
            )
        return count


count = 0
for line in lines:
    springs, arrangement = line.split()
    arrangement = tuple(int(x) for x in arrangement.split(","))
    print(springs, arrangement, arrangements_recursive(springs, arrangement))

    count += arrangements_recursive(springs, arrangement)
print(count)

# count = 0
# for line in lines:
#     springs, arrangement = line.split()
#     arrangement = [int(x) for x in arrangement.split(",")]
#     springs = "".join([springs + "?"] * 5)
#     arrangement = arrangement * 5

#     count += arrangements(springs, arrangement)
# print(count)
