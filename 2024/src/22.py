from collections import deque

buyers = list(map(int, open("2024/inputs/22.txt").readlines()))


N = 2000


def window(gen, n):
    w = deque(maxlen=n)
    for g in gen:
        w.append(g)
        if len(w) == n:
            yield w


def secrets_seq(secret):
    yield secret
    for _ in range(N):
        secret = ((secret * 64) ^ secret) % 16777216
        secret = ((secret // 32) ^ secret) % 16777216
        secret = ((secret * 2048) ^ secret) % 16777216
        yield secret


def price_changes(s):
    for a, b in window(s, 2):
        yield b % 10, b % 10 - a % 10


part_1 = 0
for b in buyers:
    secrets = list(secrets_seq(b))
    part_1 += secrets[-1]

print(part_1)
