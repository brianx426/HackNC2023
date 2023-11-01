"""Represents a single battle between gacha characters and enemies."""

from character import *
from characters import *

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

    def create_party(self) -> None:
        available_characters = [serenity, sora, kana, chadwick, rabadon, huamao, zohphia, shizuo]
        i = 0
        msg = ""
        while i < len(available_characters):
            msg += str(i) + ". " + available_characters[i].name + ", "
            i += 1
        print("Create a party of four by entering four numbers from the pool. Example: 0123")
        print(msg)
        chosen = []
        player_choice = str(input("Enter your choices: "))
        while len(player_choice) != 4:
            player_choice = str(input("Try again: "))
        for num in player_choice:
            if int(num) in range(len(available_characters)) and num not in chosen:
                chosen.append(num)
                self.player_party.append(available_characters[int(num)])
                print(f"{available_characters[int(num)].name} was added to your party!")
            else:
                raise RuntimeError("Your number was not in the range of available numbers or you entered a duplicate number, please rerun the program to try again.")
        
        




battle = Battle("Battle 1", [], [])
battle.create_party()
print(battle.player_party)