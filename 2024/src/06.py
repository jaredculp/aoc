from concurrent.futures import ProcessPoolExecutor, as_completed

input = [x.strip() for x in open("2024/inputs/06.txt").readlines()]
R = len(input)
C = len(input[0])


def patrol(pos, obstacle=None):
    seen = set()
    dir = 0 - 1j
    while True:
        if (pos, dir) in seen:
            return -1
        else:
            seen.add((pos, dir))

        next_pos = pos + dir

        r, c = int(next_pos.imag), int(next_pos.real)
        if not (0 <= r < R and 0 <= c < C):
            break

        if input[r][c] == "#" or next_pos == obstacle:
            dir *= 1j
        else:
            pos = next_pos
    return len({p for p, _ in seen})


if __name__ == "__main__":
    pos = next(complex(c, r) for r in range(R) for c in range(C) if input[r][c] == "^")
    print(patrol(pos))

    cycles = 0
    with ProcessPoolExecutor() as executor:
        futures = [
            executor.submit(patrol, pos, complex(c, r))
            for r in range(R)
            for c in range(C)
            if input[r][c] == "."
        ]
        print(sum(1 for f in as_completed(futures) if f.result() == -1))
