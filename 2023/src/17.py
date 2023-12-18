from dataclasses import dataclass
from heapq import heappop, heappush

input = [[int(xx) for xx in x.strip()] for x in open("2023/inputs/17.txt").readlines()]
X = len(input[0])
Y = len(input)


@dataclass(frozen=True, order=True)
class State:
    x: int
    y: int
    dx: int
    dy: int
    moves: int

    def moving(self):
        return (self.dx, self.dy) != (0, 0)

    def valid_turn(self, dx, dy):
        return (self.dx, self.dy) not in {(dx, dy), (-dx, -dy)}


def init_pq():
    return [(0, State(0, 0, 0, 0, 0))]


def keep_moving(state, heat_loss):
    new_x = state.x + state.dx
    new_y = state.y + state.dy
    if 0 <= new_x < X and 0 <= new_y < Y:
        heappush(
            pq,
            (
                heat_loss + input[new_y][new_x],
                State(
                    new_x,
                    new_y,
                    state.dx,
                    state.dy,
                    state.moves + 1,
                ),
            ),
        )


def turn(state, heat_loss):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if state.valid_turn(dx, dy):
            new_x = state.x + dx
            new_y = state.y + dy
            if 0 <= new_x < X and 0 <= new_y < Y:
                heappush(
                    pq,
                    (
                        heat_loss + input[new_y][new_x],
                        State(
                            new_x,
                            new_y,
                            dx,
                            dy,
                            1,
                        ),
                    ),
                )


# p1
pq = init_pq()
seen = set()
while pq:
    heat_loss, state = heappop(pq)

    if (state.x, state.y) == (X - 1, Y - 1):
        print(heat_loss)
        break

    if state in seen:
        continue

    seen.add(state)

    if state.moves < 3 and state.moving():
        keep_moving(state, heat_loss)

    turn(state, heat_loss)

# p2
pq = init_pq()
seen = set()
while pq:
    heat_loss, state = heappop(pq)

    if (state.x, state.y) == (X - 1, Y - 1) and state.moves >= 4:
        print(heat_loss)
        break

    if state in seen:
        continue

    seen.add(state)

    if state.moves < 10 and state.moving():
        keep_moving(state, heat_loss)

    if state.moves >= 4 or not state.moving():
        turn(state, heat_loss)
