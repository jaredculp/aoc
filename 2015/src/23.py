from typing import Dict

inputs = [x.strip() for x in open("2015/inputs/23.txt").readlines()]


def run_program(registers: Dict[str, int]) -> Dict[str, int]:
    i = 0
    while i < len(inputs):
        input = inputs[i]
        if input.startswith("hlf"):
            r = input.split(" ")[1]
            registers[r] //= 2
        elif input.startswith("tpl"):
            r = input.split(" ")[1]
            registers[r] *= 3
        elif input.startswith("inc"):
            r = input.split(" ")[1]
            registers[r] += 1
        elif input.startswith("jmp"):
            offset = input.split(" ")[1]
            i += int(offset) - 1
        elif input.startswith("jie"):
            _, r, offset = input.replace(",", "").split(" ")
            if registers[r] % 2 == 0:
                i += int(offset) - 1
        elif input.startswith("jio"):
            _, r, offset = input.replace(",", "").split(" ")
            if registers[r] == 1:
                i += int(offset) - 1

        i += 1

    return registers


print(run_program({"a": 0, "b": 0})["b"])
print(run_program({"a": 1, "b": 0})["b"])
