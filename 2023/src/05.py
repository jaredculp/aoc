import sys

lines = [l.strip() for l in open("2023/inputs/05.txt").readlines() if l.strip()]

_, seeds = lines.pop(0).split(":")
seeds = [int(s) for s in seeds.split()]

src, dst = None, None
mappings = dict()
inverse_mappings = dict()
for line in lines:
    if "map" in line:
        line, _ = line.split()
        src, _, dst = line.split("-")
        mappings[src] = (dst, [])
        inverse_mappings[dst] = (src, [])
    else:
        dst_start, src_start, l = [int(l) for l in line.split()]
        range_a, range_b = (
            range(src_start, src_start + l),
            range(dst_start, dst_start + l),
        )

        _, ranges = mappings[src]
        mappings[src] = (dst, ranges + [(range_a, range_b)])

        _, ranges = inverse_mappings[dst]
        inverse_mappings[dst] = (src, ranges + [(range_b, range_a)])


location = sys.maxsize
for seed in seeds:
    src, value = "seed", seed
    while src in mappings:
        dst, ranges = mappings[src]
        for src_range, dst_range in ranges:
            if value in src_range:
                value = dst_range.start + (value - src_range.start)
                break
        src = dst
    location = min(location, value)
print(location)

seed_ranges = [
    range(start, start + l)
    for start, l in (seeds[i : i + 2] for i in range(0, len(seeds), 2))
]
location = 0
while True:
    src, value = "location", location
    while src in inverse_mappings:
        dst, ranges = inverse_mappings[src]
        for src_range, dst_range in ranges:
            if value in src_range:
                value = dst_range.start + (value - src_range.start)
                break
        src = dst

    if any(value in r for r in seed_ranges):
        break

    location += 1
print(location)
