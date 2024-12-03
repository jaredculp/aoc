input = open("2015/inputs/10.txt").read().strip()


def iter(input: str) -> str:
    output = ""
    count = 1
    curr = input[0]
    for i in input[1:]:
        if i == curr:
            count += 1
        else:
            output += str(count) + curr
            curr = i
            count = 1

    output += str(count) + curr
    return output


for _ in range(40):
    input = iter(input)

print(len(input))

for _ in range(10):
    input = iter(input)

print(len(input))
