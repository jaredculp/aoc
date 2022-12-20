from collections import deque
from typing import Optional

inputs = [int(x.strip()) for x in open("2022/inputs/20.txt")]
encrypted = deque([(i, x) for i, x in enumerate(inputs)])

def decrypt(key: Optional[int] = 1, n: Optional[int] = 1) -> int:
    encrypted = deque([(i, x * key) for i, x in enumerate(inputs)])
    for _ in range(n):
        for i, x in enumerate(inputs):
            x *= key
            j = encrypted.index((i, x))
            encrypted.remove((i, x))
            encrypted.rotate(-x)
            encrypted.insert(j, (i, x))

    decrypted = [x[1] for x in encrypted]
    zero = decrypted.index(0)
    return sum(decrypted[(zero + x) % len(decrypted)] for x in [1000, 2000, 3000])

print(decrypt())
print(decrypt(811589153, 10))
