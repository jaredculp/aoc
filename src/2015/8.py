import ast

inputs = [x.strip() for x in open("inputs/2015/8.txt").readlines()]

length = 0
for input in inputs:
    length += len(input)
    length -= len(ast.literal_eval(input))

print("part1: ", length)

length = 0
for input in inputs:
    length += 2
    length += input.count('"')
    length += input.count("\\")

print("part2: ", length)
