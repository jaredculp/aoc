from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def move(self, dir):
        if dir == "U":
            return Point(self.x, self.y + 1)

        if dir == "D":
            return Point(self.x, self.y - 1)

        if dir == "R":
            return Point(self.x + 1, self.y)

        if dir == "L":
            return Point(self.x - 1, self.y)

    def neighbors(self):
        return [
            Point(self.x - 1, self.y),
            Point(self.x + 1, self.y),
            Point(self.x - 1, self.y - 1),
            Point(self.x, self.y - 1),
            Point(self.x + 1, self.y - 1),
            Point(self.x - 1, self.y + 1),
            Point(self.x, self.y + 1),
            Point(self.x + 1, self.y + 1),
        ]


def sign(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1


inputs = [x.strip().split(" ") for x in open("2022/inputs/09.txt").readlines()]


def snake(size=2):
    rope = [Point(0, 0)] * size
    visited = set()
    for dir, amt in inputs:
        for _ in range(int(amt)):
            rope[0] = rope[0].move(dir)
            for i in range(1, size):
                head, tail = rope[i - 1], rope[i]
                if tail not in head.neighbors():
                    rope[i] = Point(
                        tail.x + sign(head.x - tail.x), tail.y + sign(head.y - tail.y)
                    )
                visited.add(rope[-1])

    return len(visited)


print(snake())
print(snake(10))
