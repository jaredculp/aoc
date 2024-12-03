import ast

inputs = [x.strip() for x in open("2015/inputs/08.txt").readlines()]

length = 0
for input in inputs:
    length += len(input)
    length -= len(ast.literal_eval(input))

print(length)

length = 0
for input in inputs:
    length += 2
    length += input.count('"')
    length += input.count("\\")

print(length)
