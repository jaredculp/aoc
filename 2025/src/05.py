from dataclasses import dataclass

input = open("2025/inputs/05.txt").read()


@dataclass(order=True)
class Range:
    """
    order=True defines the __lt__ method and conveniently
               compares fields by definition order (lo, hi)
    """

    lo: int
    hi: int

    def __init__(self, range: str):
        lo, hi = range.split("-")
        self.lo = int(lo)
        self.hi = int(hi)

    def __len__(self) -> int:
        return self.hi - self.lo + 1

    def __contains__(self, x: int) -> bool:
        return self.lo <= x <= self.hi

    @staticmethod
    def merge(ranges: list["Range"]) -> list["Range"]:
        ranges = sorted(ranges)
        merged = [ranges[0]]
        for r in ranges[1:]:
            last = merged[-1]
            # i.e. [[1, 2]] + [3, 4] => [[1, 2], [3, 4]]
            if r.lo > last.hi + 1:
                merged.append(r)
            # i.e. [[1, 4]] + [2, 3] => [[1, 4]]
            #      [[1, 4]] + [2, 5] => [[1, 5]]
            else:
                last.hi = max(last.hi, r.hi)
        return merged


ranges, ingredients = (s.splitlines() for s in input.split("\n\n"))
ranges = [Range(r) for r in ranges]

print(sum(any(int(i) in r for r in ranges) for i in ingredients))
print(sum(len(r) for r in Range.merge(ranges)))
