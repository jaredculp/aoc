from collections import defaultdict

input = [list(x.strip()) for x in open("2024/inputs/12.txt").readlines()]
R = len(input)
C = len(input[0])


def find_plot(r, c, shape):
    shape.add((r, c))

    for dr, dc in [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]:
        if (r + dr, c + dc) in shape:
            continue

        if not 0 <= r + dr < R or not 0 <= c + dc < C:
            continue

        if input[r][c] != input[r + dr][c + dc]:
            continue

        else:
            find_plot(r + dr, c + dc, shape)

    return frozenset(shape)


# map plant => plot (each plot is a set of points)
plots = defaultdict(set)
for r in range(R):
    for c in range(C):
        plots[input[r][c]].add(find_plot(r, c, set()))


def area(points):
    return len(points)


def perimeter(points):
    edges = 0
    for r, c in points:
        N = (r - 1, c)
        E = (r, c + 1)
        S = (r + 1, c)
        W = (r, c - 1)
        if N not in points:
            edges += 1
        if E not in points:
            edges += 1
        if S not in points:
            edges += 1
        if W not in points:
            edges += 1
    return edges


def corners(points):
    corners = 0
    for r, c in points:
        NN = (r - 1, c)
        NE = (r - 1, c + 1)
        EE = (r, c + 1)
        SE = (r + 1, c + 1)
        SS = (r + 1, c)
        SW = (r + 1, c - 1)
        WW = (r, c - 1)
        NW = (r - 1, c - 1)
        if NN not in points and EE not in points:
            corners += 1
        if NN not in points and WW not in points:
            corners += 1
        if SS not in points and EE not in points:
            corners += 1
        if SS not in points and WW not in points:
            corners += 1
        if NN in points and EE in points and NE not in points:
            corners += 1
        if NN in points and WW in points and NW not in points:
            corners += 1
        if SS in points and EE in points and SE not in points:
            corners += 1
        if SS in points and WW in points and SW not in points:
            corners += 1
    return corners


print(
    sum(
        area(plot) * perimeter(list(plot))
        for plant_plots in plots.values()
        for plot in plant_plots
    )
)

print(
    sum(
        area(plot) * corners(plot)
        for plant_plots in plots.values()
        for plot in plant_plots
    )
)
