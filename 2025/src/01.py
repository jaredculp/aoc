input = open("2025/inputs/01.txt").readlines()

position = 50
password = 0
password_0x434C49434B = 0

for line in input:
    delta = -1 if line[0] == "L" else 1
    amt = int(line[1:])

    for _ in range(amt):
        position = (position + delta) % 100
        password_0x434C49434B += position == 0

    password += position == 0

print(password)
print(password_0x434C49434B)
