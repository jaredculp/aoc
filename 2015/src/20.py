from functools import reduce
from typing import Optional

import enlighten

input = int(open("2015/inputs/20.txt").readline())


# h/t: https://stackoverflow.com/a/6800214
def factors(n):
    return set(
        reduce(
            list.__add__,
            ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0),
        )
    )


def house_presents(house: int, factor: Optional[int] = 10) -> int:
    return sum(x for x in factors(house)) * factor


house = 1
pbar = enlighten.Counter(total=input)
while sum(x for x in factors(house)) * 10 < input:
    house += 1
    pbar.update()

print(house)

house = 1
pbar = enlighten.Counter(total=input)
while sum(x for x in factors(house) if house / x <= 50) * 11 < input:
    house += 1
    pbar.update()

print(house)
