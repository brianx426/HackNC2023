"""Represents a single battle between gacha characters and enemies."""

from character import *

class Battle:
    name: str
    player_party: list[Character]
    enemy_party: list[Enemy]
    turn_count: int

    def __init__(self, name: str, party1: list[GachaCharacter], party2: list[Enemy]) -> None:
        self.name = name
        self.player_party = party1
        self.enemy_party = party2
        self.turn_count = 0

    