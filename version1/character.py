from abc import ABC, abstractmethod
from math import floor
from random import randint
from move import Move


class Character:
    name: str
    hp: int
    max_hp: int
    defense: int
    atk: int
    spd: int
    crit_rate: float
    crit_dmg: float
    is_alive: bool
    moveset: list[Move]
    basic: Move
    special: Move

    def __init__(self, name: str, hp: int, defense: int, atk: int, spd: int,
               crit_rate: float, crit_dmg: float, is_alive: bool,
               moveset: list[Move]) -> None:
        assert hp > 0
        self.name = name
        self.hp = hp
        self.defense = defense
        self.atk = atk
        self.spd = spd
        self.crit_rate = crit_rate
        self.crit_dmg = crit_dmg
        self.is_alive = is_alive
        self.moveset = moveset
        self.max_hp = hp

    def __str__(self) -> str:
        return self.name

    @abstractmethod
    def attack_aoe(self, targets, move) -> None:
        pass

    @abstractmethod
    def attack_single(self, target, move) -> None:
        pass


class GachaCharacter(Character):
    drop_rate: float
    constellation: int
    card: str
    splash: str

    def __init__(self, name: str, hp: int, defense: int, atk: int, spd: int,
               crit_rate: float, crit_dmg: float, is_alive: bool,
               moveset: list[Move], drop_rate: float, card: str,
               splash: str) -> None:
        super().__init__(name, hp, defense, atk, spd, crit_rate, crit_dmg,
                     is_alive, moveset)
        self.drop_rate = drop_rate
        self.constellation = 0
        self.card = card
        self.splash = splash

    def is_crit(self) -> bool:
        return randint(0, 100) < self.crit_rate

    def check_special_moves(self, targets: list[Character], move: Move) -> float:
        if move.name == "Glitter Bomb":
            return (.8 + (.05 * len(targets))) * self.atk
        elif move.name == "Chain Sparkle":
            return 1.2 + (.15 * len(targets)) * self.atk
        elif move.name == "Unstoppable Onslaught":
            return randint(1, 9999000) / 100
        elif move.name == "Wide Slash":
            return .95 * self.atk
        elif move.name == "World Ender":
            return 10 * (1 - (self.hp / self.max_hp)) * self.atk
        elif move.name == "Death":
            chance = randint(1, 3)
            if chance == 1:
                return 9999999999
            else:
                return 1 * self.atk
        elif move.name == "Meteor":
            chance = randint(2, 3)
            if chance == 2:
                return 2 * self.atk
            else:
                return 6 * self.atk
        else:
            return 0

    def attack_aoe(self, targets: list[Character], move: Move) -> None:
        damage = self.check_special_moves(targets, move)
        if len(targets) == 0:
            print("There are no enemies alive!")
        else:
            for enemy in targets:
                if self.is_crit():
                    print(f"Critical Hit! {enemy.name} took {damage * (1 - enemy.defense / 100) * (self.crit_dmg)} damage from {self.name}")
                    enemy.hp -= int(damage * (1 - enemy.defense / 100) * (self.crit_dmg))
                else:
                    print(f"{enemy.name} took {int(damage * (1 - enemy.defense / 100))} damage from {self.name}")
                    enemy.hp -= int(damage * (1 - enemy.defense / 100))
                if enemy.hp <= 0:
                    enemy.is_alive = False
                    print(f"{enemy.name} was defeated!")

    def check_special_moves_single(self, target: Character, move: Move) -> float:
        if move.name == "Moonlight Vigil":
            if target.max_hp > self.max_hp:
                return 3 * self.atk
            else:
                return 1.25 * self.atk
        elif move.name == "Lunar Lance":
            return (1 + (1 * (1 - floor((self.hp / self.max_hp) * 100) / 10))) * self.atk
        elif move.name == "Focus Slash":
            return 3 * self.atk
        elif move.name == "Deathbringer Stance":
            return 1.75 * self.atk
        else:
            return 1 * self.atk

    def attack_single(self, target: Character, move: Move) -> None:
        damage = self.check_special_moves_single(target, move)
        if target.hp > 0:
            if self.is_crit():
                print(f"Critical Hit! {target.name} took {int(damage * (1 - target.defense / 100)*(self.crit_dmg))} damage from {self.name}")
                target.hp -= int(damage * (1 - target.defense / 100) * (self.crit_dmg))
            else:
                print(f"{target.name} took {int(damage * (1 - target.defense / 100))} damage from {self.name}")
                target.hp -= int(damage * (1 - target.defense / 100))
            if target.hp <= 0:
                target.is_alive = False
                print(f"{target.name} was defeated!")

    def get_splash(self) -> str:
        return self.splash

    def get_card(self) -> str:
        return self.card


class Enemy(Character):
    ## 1 = single target, 2 = AOE
    type_of_attack: int

    def attack_single(self, target: list[Character]) -> None:
        single_target = Move("Attack", "Attacks an enemy for 100% of character attack", 100, 0, False)
        targett = target[randint(0, len(target) - 1)]
        while not targett.is_alive:
            targett = target[randint(0, len(target) - 1)]
        if self.is_crit():
            print(f"Critical Hit! {targett.name} took {int((self.atk)*(single_target.damage) * (1 - self.defense / 100)*self.crit_dmg)} damage from {self.name}")
            targett.hp -= int((self.atk) * (single_target.damage) * (1 - self.defense / 100) * self.crit_dmg)
        else:
            print(f"{targett.name} took {int(self.atk*single_target.damage * (1 - targett.defense / 100))} damage from {self.name}")
            targett.hp -= int(self.atk * single_target.damage *(1 - targett.defense / 100))
        if targett.hp <= 0:
            targett.is_alive = False
            print(f"{targett.name} was slain!")

    def attack_aoe(self, targets: list[Character]) -> None:
        aoe = Move("AoE Attack", "Attacks all enemies for 100% of character attack", 100, 0, True)
        for character in targets:
            if character.is_alive:
                if self.is_crit():
                    print(f"Critical Hit! {character.name} took {int(self.crit_dmg*(self.atk)*aoe.damage * (1 - character.defense / 100))} damage from {self.name}")
                    character.hp -= int(self.crit_dmg * (self.atk) * aoe.damage * (1 - character.defense / 100))
                else:
                    print(f"{character.name} took {int((self.atk)*aoe.damage * (1 - character.defense / 100))} damage from {self.name}")
                    character.hp -= int((self.atk) * aoe.damage * (1 - character.defense / 100))
                if character.hp <= 0:
                    character.is_alive = False
                    print(f"{character.name} was slain!")
            else:
                continue

    def get_attack_type(self) -> None:
        self.type_of_attack = randint(1, 2)

    def is_crit(self) -> bool:
        return randint(0, 100) < self.crit_rate
