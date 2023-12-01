import string

lines = [x.strip() for x in open("2023/inputs/01.txt").readlines()]


def replace_letters(line: str) -> str:
    for letter in string.ascii_letters:
        line = line.replace(letter, "")
    return line


def replace_numbers(line: str) -> str:
    for target, replacement in {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }.items():
        line = line.replace(target, replacement)
    return line


def sum_line(line: str) -> int:
    if len(line) == 1:
        return int(f"{line[0]}{line[0]}")
    else:
        return int(f"{line[0]}{line[-1]}")


# part 1
sum = 0
for line in lines:
    line = replace_letters(line)
    sum += sum_line(line)
print(sum)

# part 2
sum = 0
for line in lines:
    line = replace_numbers(line)
    line = replace_letters(line)
    sum += sum_line(line)
print(sum)
