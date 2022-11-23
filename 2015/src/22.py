import random
from dataclasses import dataclass
from typing import Callable, List, Optional, Union

import enlighten


@dataclass
class Player:
    mana: int
    hp: int
    armor: int = 0
    damage: int = 0

    recharge_timer: int = 0
    shield_timer: int = 0
    poison_timer: int = 0


@dataclass
class Boss:
    hp: int
    damage: int


class Game:
    def __init__(
        self, player: Player, boss: Boss, hard_mode: Optional[bool] = False
    ) -> None:
        self.player = player
        self.boss = boss
        self.hard_mode = hard_mode
        self.mana_spent = 0

    def spells(self) -> List[Callable]:
        spells = []
        if self.player.mana >= 53:
            spells.append(self.magic_missile)

        if self.player.mana >= 73:
            spells.append(self.drain)

        if self.player.mana >= 113 and not self.player.shield_timer:
            spells.append(self.shield)

        if self.player.mana >= 173 and not self.player.poison_timer:
            spells.append(self.poison)

        if self.player.mana >= 229 and not self.player.recharge_timer:
            spells.append(self.recharge)

        return spells

    def magic_missile(self) -> None:
        self.player.mana -= 53
        self.mana_spent += 53
        self.boss.hp -= 4

    def drain(self) -> None:
        self.player.mana -= 73
        self.mana_spent += 73
        self.player.hp += 2
        self.boss.hp -= 2

    def shield(self) -> None:
        self.player.mana -= 113
        self.mana_spent += 113
        self.player.shield_timer = 6
        self.player.armor = 7

    def poison(self) -> None:
        self.player.mana -= 173
        self.mana_spent += 173
        self.player.poison_timer = 6

    def recharge(self) -> None:
        self.player.mana -= 229
        self.mana_spent += 229
        self.player.recharge_timer = 5

    def update_timers(self) -> None:
        if self.player.recharge_timer > 0:
            self.player.mana += 101
            self.player.recharge_timer -= 1

        if self.player.shield_timer > 0:
            self.player.shield_timer -= 1
        else:
            self.player.armor = 0

        if self.player.poison_timer > 0:
            self.boss.hp -= 3
            self.player.poison_timer -= 1

    def player_turn(self) -> Optional[Union[Player, Boss]]:
        if self.hard_mode:
            self.player.hp -= 1
            winner = self.check_for_winner()
            if winner:
                return winner

        self.update_timers()
        winner = self.check_for_winner()
        if winner:
            return winner

        spells = self.spells()
        if not spells:
            return self.boss
        random.choice(spells)()

        winner = self.check_for_winner()
        if winner:
            return winner

    def boss_turn(self) -> Optional[Union[Player, Boss]]:
        self.update_timers()
        winner = self.check_for_winner()
        if winner:
            return winner

        damage = max(1, self.boss.damage - self.player.armor)
        self.player.hp -= damage

        winner = self.check_for_winner()
        if winner:
            return winner

    def check_for_winner(self) -> Optional[Union[Player, Boss]]:
        if self.player.hp <= 0:
            return self.boss

        if self.boss.hp <= 0:
            return self.player


def simulate(hard_mode: Optional[bool] = False) -> int:
    input = [
        int(x.split(": ")[1]) for x in open("2015/inputs/22.txt").readlines()
    ]

    # use some type of path algorithm here instead of brute force?
    iters = 5_000_000
    pbar = manager.counter(total=iters)
    min_mana = float("inf")
    for _ in range(iters):
        game = Game(
            player=Player(hp=50, mana=500),
            boss=Boss(hp=input[0], damage=input[1]),
            hard_mode=hard_mode,
        )
        while True:
            game.player_turn()
            if isinstance(game.check_for_winner(), Player):
                min_mana = min(min_mana, game.mana_spent)
                break
            if isinstance(game.check_for_winner(), Boss):
                break

            game.boss_turn()
            if isinstance(game.check_for_winner(), Player):
                min_mana = min(min_mana, game.mana_spent)
                break
            if isinstance(game.check_for_winner(), Boss):
                break

        pbar.update()

    return min_mana


manager = enlighten.get_manager()

print("part1: ", simulate())
print("part2: ", simulate(True))

manager.stop()
