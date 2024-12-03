from hashlib import md5

input = open("2015/inputs/04.txt").read().strip()


num = 0
part1 = None
part2 = None
while not part1 or not part2:
    key = f"{input}{num}"
    hash = md5(key.encode()).hexdigest()
    if not part1 and hash[:5] == "00000":
        part1 = num
    if not part2 and hash[:6] == "000000":
        part2 = num
    num += 1

print(part1)
print(part2)
