from dataclasses import dataclass
from itertools import combinations


@dataclass(frozen=True)
class Item:
    cost: int
    damage: int
    armor: int


weapons = [
    Item(cost=x, damage=y, armor=0)
    for x, y in [
        (8, 4),
        (10, 5),
        (25, 6),
        (40, 7),
        (74, 8),
    ]
]

armors = [
    Item(cost=x, damage=0, armor=y)
    for x, y in [
        (0, 0),
        (13, 1),
        (31, 2),
        (53, 3),
        (75, 4),
        (102, 5),
    ]
]

rings = [
    Item(cost=x, damage=y, armor=z)
    for x, y, z in [
        (0, 0, 0),
        (0, 0, 0),
        (25, 1, 0),
        (50, 2, 0),
        (100, 3, 0),
        (20, 0, 1),
        (40, 0, 2),
        (80, 0, 3),
    ]
]


@dataclass(frozen=True)
class Player:
    hp: int
    damage: int
    armor: int


input = [int(x.split(": ")[1]) for x in open("2015/inputs/21.txt").readlines()]
cpu = Player(hp=input[0], damage=input[1], armor=input[2])


def player_wins(you: Player) -> bool:
    you_hp = you.hp
    cpu_hp = cpu.hp
    you_attack = max(1, you.damage - cpu.armor)
    cpu_attack = max(1, cpu.damage - you.armor)

    while True:
        cpu_hp -= you_attack
        if cpu_hp <= 0:
            return True

        you_hp -= cpu_attack
        if you_hp <= 0:
            return False


min_cost = float("inf")
max_cost = float("-inf")
for weapon in weapons:
    for armor in armors:
        for ring1, ring2 in combinations(rings, 2):
            player = Player(
                hp=100,
                damage=weapon.damage + ring1.damage + ring2.damage,
                armor=armor.armor + ring1.armor + ring2.armor,
            )
            cost = weapon.cost + armor.cost + ring1.cost + ring2.cost
            if player_wins(player):
                min_cost = min(min_cost, cost)
            else:
                max_cost = max(max_cost, cost)

print(min_cost)
print(max_cost)
