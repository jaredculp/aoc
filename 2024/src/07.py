import re
from itertools import product
from operator import add, mul

input = open("2024/inputs/07.txt").readlines()
input = [list(map(int, re.findall(r"\d+", i))) for i in input]


def solve(ops):
    count = 0
    for target, *nums in input:
        for op in product(ops, repeat=len(nums) - 1):
            result = nums[0]
            for f, num in zip(op, nums[1:]):
                result = f(result, num)
            if result == target:
                count += target
                break
    return count


cat = lambda x, y: int(f"{x}{y}")

print(solve([add, mul]))
print(solve([add, mul, cat]))
