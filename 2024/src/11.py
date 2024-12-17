from functools import cache

input = tuple(map(int, open("2024/inputs/11.txt").read().split()))


@cache
def blink(stones, blinks_left):
    if blinks_left == 0:
        return len(stones)

    return sum(blink(blink_stone(stone), blinks_left - 1) for stone in stones)


def blink_stone(stone):
    if stone == 0:
        return (1,)

    stone = str(stone)
    if len(stone) % 2 == 0:
        midpoint = len(stone) // 2
        l, r = stone[:midpoint], stone[midpoint:]
        return (int(l), int(r))
    else:
        return (int(stone) * 2024,)


print(blink(input, 25))
print(blink(input, 75))
