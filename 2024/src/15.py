input = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""
# input = """########
# #..O.O.#
# ##@.O..#
# #...O..#
# #.#.O..#
# #...O..#
# #......#
# ########
#
# <^^>>>vv<v>>v<<"""
input = open("2024/inputs/15.txt").read()
grid, moves = input.split("\n\n")
grid = [list(x) for x in grid.splitlines()]
R = len(grid)
C = len(grid[0])
robot = (0, 0)
for r in range(R):
    for c in range(C):
        if grid[r][c] == "@":
            robot = (r, c)
            break

directions = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
for move in moves:
    if move == "\n":
        continue

    r, c = robot
    dr, dc = directions[move]
    nr, nc = r + dr, c + dc

    if grid[nr][nc] == "#":
        # wall, cannot move
        continue
    if grid[nr][nc] == ".":
        # open spot, swap robot and open spot
        grid[r][c], grid[nr][nc] = ".", "@"
    else:
        # rock, but we need to determine how many and if we can move them
        rocks = 1
        while grid[r + ((rocks + 1) * dr)][c + ((rocks + 1) * dc)] == "O":
            rocks += 1

        rock_r = r + ((rocks + 1) * dr)
        rock_c = c + ((rocks + 1) * dc)
        if grid[rock_r][rock_c] == "#":
            # wall at end of rock chain, cannot move
            continue
        # rather than moving the entire chain
        # move the front to the end and put the robot at the front
        grid[rock_r][rock_c] = "O"
        grid[r][c] = "."
        grid[r + dr][c + dc] = "@"

    robot = (nr, nc)

score = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] == "O":
            score += 100 * r + c
print(score)
