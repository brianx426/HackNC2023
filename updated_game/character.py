"""This contains Character and its subclasses, GachaCharacter, and Enemy."""

class Character:
    name: str # the name of the character
    hp: int # current hp of the character
    max_hp: int # max hp of the character
    atk: int # the attack stat of the character, determines the damage output of a character
    defence: int # the defence stat of the character, reduces damage taken
    spd: float # the speed stat of the character. Affects the turn order
    is_alive: bool # boolean to keep track of if the character is alive or not
    c_rate: float # crit rate of the character
    c_dmg: float # crit damage of the character
    moves: list[str] # the list of available moves of a character
    card: str # is the pathname of the image for the card of a character
    splash: str # is the pathname of the image for the splash art of a character
    evasion_rate: float # shows the percentage of evading an attack


    def __init__(self, name: str, hp: int, defence: int, atk: int, spd: int, crit_rate: float, crit_dmg: float, moveset: list[str], card: str, splash: str, evasion_rate: float) -> None:
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.defence = defence
        self.atk = atk
        self.spd = spd
        self.c_rate = crit_rate
        self.c_dmg = crit_dmg
        self.moves = moveset
        self.is_alive = True
        self.card = card
        self.splash = splash
        self.evasion_rate = evasion_rate

    def __str__(self) -> str:
        msg = ""
        msg += self.name + " " + str(self.hp) + "/" + str(self.max_hp)
        return msg


class GachaCharacter(Character):
    drop_rate: float
    constellation: int

    def __init__(self, name: str, hp: int, defence: int, atk: int, spd: int, crit_rate: float, crit_dmg: float, moveset: list[str], drop_rate: float, card: str, splash: str, evasion_rate: float) -> None:
        super().__init__(name, hp, defence, atk, spd, crit_rate, crit_dmg, moveset, card, splash, evasion_rate)
        self.constellation = 0
        self.drop_rate = drop_rate

    def get_splash(self) -> str:
        return self.splash
    
    def get_card(self) -> str:
        return self.card
    

class Enemy(Character):

    def __init__(self, name: str, hp: int, defence: int, atk: int, spd: int, crit_rate: float, crit_dmg: float, moveset: list[str], card: str, splash: str, evasion_rate: float) -> None:
        super().__init__(name, hp, defence, atk, spd, crit_rate, crit_dmg, moveset, card, splash, evasion_rate)

    
