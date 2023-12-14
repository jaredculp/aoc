input = open("2023/inputs/14.txt").readlines()


def tilt_north():
    for i in range(len(input) - 1):
        line, next_line = input[i : i + 2]

        for j in range(len(line)):
            if line[j] == "." and next_line[j] == "O":
                line = line[:j] + "O" + line[j + 1 :]
                next_line = next_line[:j] + "." + next_line[j + 1 :]
            input[i] = line
            input[i + 1] = next_line


for _ in range(len(input)):
    tilt_north()

total = 0
for i, line in enumerate(reversed(input)):
    total += (i + 1) * line.count("O")
print(total)
