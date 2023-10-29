import pygame
import sys
from random import random, randint, choice
from abc import ABC, abstractmethod
from character import Character, GachaCharacter, Enemy
from move import Move
from special_moves import Chadwick, Serenity, Sora, Zohphia, Kana, Huamao, Shizuo, Rabadon


class Battle:
    turn_count: int
    player_party: list[GachaCharacter]
    enemy_party: list[Enemy]
    is_over: bool

    def __init__(self, player_party: list[GachaCharacter], enemy_party: list[Enemy]) -> None:
        self.player_party = player_party
        self.enemy_party = enemy_party
        self.is_over = False
        self.turn_count = 0
        print("Battle Started!")
        print("You are going against:")
        names = ""
        for enemy in self.enemy_party:
            names += ", " + enemy.name
        print(names)
        print(f"Enemies are selected with 1 - {len(self.enemy_party)}")

    def print_party_status(self) -> None:
        print("Player's Party")
        for character in self.player_party:
            if character.is_alive:
                print(f"{character.name} - {character.hp} HP")
            else:
                print(f"{character.name} - DEAD")
            print("Enemy Party:")
        for character in self.enemy_party:
            if character.is_alive:
                print(f"{character.name} - {character.hp} HP")
            else:
                print(f"{character.name} - DEAD")
        print("")

    def check_for_dead_enemies(self) -> None:
        i = 0
        while i < len(self.enemy_party):
            if self.enemy_party[i].hp <= 0:
                self.enemy_party[i].is_alive = False
            i += 1

    def check_for_dead_characters(self) -> None:
        i = 0
        while i < len(self.player_party):
            if self.player_party[i].hp <= 0:
                self.player_party[i].is_alive = False
            i += 1

    def check_end_game(self) -> bool:
        player_dead_count = 0
        enemy_dead_count = 0
        for chrt in self.player_party:
            if not chrt.is_alive:
                player_dead_count += 1
        if player_dead_count == len(self.player_party):
            self.is_over = True
            return True

        for enemy in self.enemy_party:
            if not enemy.is_alive:
                enemy_dead_count += 1
        if enemy_dead_count == len(self.enemy_party):
            self.is_over = True
            return True
        return False

    def player_turn(self) -> None:
        if self.check_end_game():
            pass
        else:
            print("Player's Turn")
            self.check_for_dead_enemies()
            for chrt in self.player_party:
                if chrt.is_alive and not self.check_end_game():
                    print(f"{chrt.name}'s turn!")
                    self.print_party_status()
                    print("What would you like to do?")
                    print("1. Attack\n2. Use a Skill")
                    player_choice = input("Enter your choice: ")
                while player_choice not in ["1", "2"]:
                    player_choice = input("That's not a valid choice! Choose again: ")
                if player_choice == "1":
                    # This is the basic attack
                    enemies = ""
                    for enemy in self.enemy_party:
                        if not enemy.is_alive:
                            enemies += enemy.name + "{X}, "
                        else:
                            enemies += enemy.name + ", "
                    print("Which enemy would you like to attack? Dead enemies are marked with an {X}. ")
                    print(enemies)
                    pick = input("Enter the index of the enemy you wish to attack (First enemy is 0): ")
                    while pick not in [str(i) for i in range(len(self.enemy_party))
                               ] or not self.enemy_party[int(pick)].is_alive:
                        pick = input("That's not a valid choice! Choose again: ")
                    chrt.attack_single(self.enemy_party[int(pick)], chrt.moveset[0])
                elif player_choice == "2":
                    # This is the skill attack
                    print("These are the skills you can use: ")
                    i = 1
                    for move in chrt.moveset:
                        if chrt.moveset[0] == move:
                            pass
                        else:
                            print(f"{i}. {move.name} - {move.description}")
                            i += 1
                p_choice = input("Which move would you like to use? Enter the number of the move you wish to use: ")
                while p_choice not in [str(i) for i in range(1, len(chrt.moveset) + 1)]:
                    p_choice = input("That's not a valid choice! Choose again: ")
                if p_choice == "1":
                    if chrt.moveset[1].cooldown == 0 and chrt.moveset[1].is_aoe:
                        chrt.attack_aoe(list[Character](self.enemy_party), chrt.moveset[1])
                    else:
                        enemies = ""
                        for enemy in self.enemy_party:
                            if not enemy.is_alive:
                                enemies += enemy.name + "{X}, "
                            else:
                                enemies += enemy.name + ", "
                        pick = input("Which enemy would you like to attack? Dead enemies are marked with an {X}. Enter the index of the enemy you wish to attack (First enemy is 0): ")
                        print(enemies)
                        while pick not in [str(i) for i in range(len(self.enemy_party))] or not self.enemy_party[int(pick)].is_alive:
                            pick = input("That's not a valid choice! Choose again: ")
                        chrt.attack_single(self.enemy_party[int(pick)], chrt.moveset[1])
                else:
                    if chrt.moveset[2].cooldown == 0 and chrt.moveset[2].is_aoe:
                        chrt.attack_aoe(list[Character](self.enemy_party), chrt.moveset[2])
                    else:
                        enemies = ""
                        for enemy in self.enemy_party:
                            if not enemy.is_alive:
                                enemies += enemy.name + "{X}, "
                            else:
                                enemies += enemy.name + ", "
                        print("Which enemy would you like to attack? Dead enemies are marked with an {X}. ")
                        print(enemies)
                        pick = input("Enter the index of the enemy you wish to attack (First enemy is 0): ")
                        while pick not in [str(i) for i in range(len(self.enemy_party))]:
                            pick = input("That's not a valid choice! Choose again: ")
                        chrt.attack_single(self.enemy_party[int(pick)], chrt.moveset[2])

    def enemy_turn(self):
        if self.check_end_game():
            pass
        else:
            print("Enemy's Turn")
            for enemy in self.enemy_party:
                if enemy.is_alive and not self.check_end_game():
                    print(f"{enemy.name}'s Turn!")
                    enemy.get_attack_type()
                    if enemy.type_of_attack == 1:
                        enemy.attack_single(list[Character](self.player_party))
                    else:
                        enemy.attack_aoe(list[Character](self.player_party))
                else:
                    pass

    def take_turn(self) -> None:
        while not self.is_over:
            self.turn_count += 1
            for character in self.player_party:
                for move in character.moveset:
                    move.cooldown -= 1
                    if move.cooldown < 0:
                        move.cooldown = 0
            print(f"=== Turn {self.turn_count} ===")
            self.player_turn()
            i = 0
            j = 0
            for character in self.enemy_party:
                if not character.is_alive:
                    i += 1

            for character in self.player_party:
                if not character.is_alive:
                    j += 1

            if (i == len(self.enemy_party)):
                print("You win")

            if j == len(self.player_party):
                print("You lose")

            if self.check_end_game():
                break

            self.enemy_turn()

            i = 0
            j = 0
            for character in self.enemy_party:
                if not character.is_alive:
                    i += 1

            for character in self.player_party:
                if not character.is_alive:
                    j += 1

            if (i == len(self.enemy_party)):
                print("You win")

            if j == len(self.player_party):
                print("You lose")

            if self.check_end_game():
                break


attack = Move("Attack", "Attacks a single enemy for 100% of character attack.",
              2, 0, True)
single = Move("IKUUUUUUUUUU", "The dragon's rage", 5, 0, False)

aoe_skill = Move("AoE Attack",
                 "Attacks all enemies for 100% of character attack", 9, 0,
                 True)

bandit1 = Enemy("Bandit 1", 1000, 2, 2, 20, .20, 2, True,
                [Move("Single Target", "attack character", 1, 0, False)])

bandit2 = Enemy("Bandit 2", 1000, 2, 2, 20, .20, 2, True,
                [Move("Single Target", "attack character", 1, 0, False)])

bandit3 = Enemy("Bandit 3", 1000, 2, 2, 20, .20, 2, True,
                [Move("Single Target", "attack character", 1, 0, False)])

bandit4 = Enemy("Bandit 4", 1000, 2, 2, 20, .20, 2, True,
                [Move("Single Target", "attack character", 1, 0, False)])

bandit5 = Enemy("Bandit 5", 1000, 2, 2, 20, .20, 2, True,
                [Move("Single Target", "attack character", 1, 0, False)])

bandit6 = Enemy("Bandit 6", 1000, 2, 2, 20, .20, 2, True,
                [Move("Single Target", "attack character", 1, 0, False)])

bandit7 = Enemy("Bandit 7", 1000, 2, 2, 20, .20, 2, True,
                [Move("Single Target", "attack character", 1, 0, False)])

bandit8 = Enemy("Bandit 8", 1000, 2, 2, 20, .20, 2, True,
                [Move("Single Target", "attack character", 1, 0, False)])

a_player_party = []
for x in range(4):
    select_char = input("Choose a character: Chadwick, Serenity, Zohphia, Kana, Shizuo, Rabadon: ")
    if select_char.lower() == "chadwick":
        a_player_party.append(Chadwick)
    if select_char.lower() == "serenity":
        a_player_party.append(Serenity)
    if select_char.lower() == "zohphia":
        a_player_party.append(Zohphia)
    if select_char.lower() == "kana":
        a_player_party.append(Kana)
    if select_char.lower() == "shizuo":
        a_player_party.append(Shizuo)
    if select_char.lower() == "rabadon":
        a_player_party.append(Rabadon)

battle = Battle(
    a_player_party,
    [bandit1, bandit2, bandit3, bandit4, bandit5, bandit6, bandit7, bandit8])

while not battle.is_over:
    battle.take_turn()