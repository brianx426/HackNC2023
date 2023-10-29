from move import Move
from character import Character, GachaCharacter, Enemy
from random import randint

#ssr rarities = 0.025 droprate
#sr rarities = 0.05 droprate
#everything else is "trash"

Serenity = GachaCharacter("Serenity", 3000, 10, 200, 7, 10, 1.5, True, [
    Move("Basic Attack",
         "Serenity's flying swords slash one enemy for 100% of her attack.", 1,
         0, False),
    Move(
        "Chain Sparkle",
        "Hits all enemies with a chain sparkle for 100% of her attack. This ability deals 15% more per enemy alive.",
        1, 0, True),
    Move(
        "Glitter Bomb",
        "Launches a glitter bomb towards her enemies, dealing 80% of her attack. This ability deals 20% more damage for each ally alive.",
        1, 0, True)
], .025, "img/serenity.png", "img/serenity_splash.png")

SoraAA: Move = Move(
    "Basic Attack",
    "Sora swings her staff and deals damage equivalent to 50% of her attack to one enemy",
    0.5, 1, False)
SoraS1: Move = Move("Salvation",
                    "Heals a target ally by 50% of their missing health.",
                    -0.5, 1, False)
SoraS2: Move = Move(
    "Seraph’s Embrace",
    "Recovers 10% hp herself,  and recovers 20% hp to rest of the team.", -0.2,
    1, True)
Sora = GachaCharacter("Sora", 2000, 7, 50, 5, 10, 1.5, True,
                      [SoraAA, SoraS1, SoraS2], .025, "img/sora.png",
                      "img/sora_splash.png")

ZohphiaAA: Move = Move(
    "Basic Attack",
    "Zohphia slashes an enemy with her sword, dealing 100% of her attack to that enemy.",
    1.0, 1, False)
ZohphiaS1: Move = Move(
    "Moonlight Vigil",
    "Leaps into the sky and plunges her sword into an enemy, dealing 1000%/total number of enemies of attack to that enemy.",
    10, 1, False)
ZohphiaS2: Move = Move(
    "Lunar Lance",
    "Charges an enemy with her moonlit lance, dealing 100% damage to that enemy and 100% more for every 10% hp she is missing.",
    1, 1, False)
Zohphia = GachaCharacter("Zohphia", 1500, 0, 200, 50, 20, 2.25, True,
                         [ZohphiaAA, ZohphiaS1, ZohphiaS2], .025,
                         "img/zohphia.png", "img/zohphia_splash.png")

ChadwickAA: Move = Move(
    "Basic Attack",
    "Chadwick slashes an enemy, dealing 75% of his atk to that enemy.", 0.75,
    1, False)
ChadwickS1: Move = Move(
    "Divine Radiance",
    "Heals a random amount(1-1000% of Chadwick's attack) of hp to all allies.",
    1, 1, True)
ChadwickS2: Move = Move(
    "Unstoppable Onslaught",
    "Deals a random amount(1-1000% of Chadwick's attack) of damage to all enemies.",
    randint(100, 1000) / 100, 1, True)
Chadwick = GachaCharacter("Chadwick", 3000, 20, 200, 7, 10, 1.5, True,
                          [ChadwickAA, ChadwickS1, ChadwickS2], .025,
                          "img/chadwick.png", "img/chadwick_splash.png")
#name, hp, defense, atk, spd, crit_rate, crit_dmg,
KanaAA: Move = Move(
    "Basic Attack",
    "Kana slashes her enemy with her katanas, dealing 100% of her attack to one enemy.",
    1.0, 1, False)
KanaS1: Move = Move("Focus Slash", "300% of atk to one enemy.", 3.0, 1, False)
KanaS2: Move = Move("Wide Slash", "Slashes all enemes for 75% of Kana's atk.",
                    .75, 1, True)
Kana = GachaCharacter("Kana", 1700, 3, 125, 10, 10, 1.5, True,
                      [KanaAA, KanaS1, KanaS2], .05, "img/kana.png",
                      "img/kana_splash.png")

ShizuoAA: Move = Move(
    "Basic Attack",
    "Shizuo brings down his blade onto his enemy, dealing 75% of Shizuo's atk to a single enemy.",
    0.75, 1, False)
ShizuoS1: Move = Move(
    "Deathbringer Stance",
    "Shizuo enters his Deathbringer Stance before plunging his blade into his enemy, dealing 175% of Shizuo's attack to a single enemy, healing him for 50% of the damage dealt.",
    1.75, 1, False)
ShizuoS2: Move = Move(
    "World Ender",
    "Shizuo slashes all enemies for 50% of Shizuo's missing HP, healing him 10% for each enemy hit.",
    0.5, 1, True)
Shizuo = GachaCharacter("Shizuo", 3500, 15, 100, 5, 10, 1.5, True,
                        [ShizuoAA, ShizuoS1, ShizuoS2], .05, "img/shizuo.png",
                        "img/shizuo_splash.png")

# Name, Description, Damage, Cooldown, is AoE
HuamaoAA: Move = Move(
    "Basic Attack",
    "Huamao casts a spell and attacks an enemy for 100% of her attack.", 1, 1,
    False)
HuamaoS1: Move = Move("Healing Halo",
                      "Huamao heals 500% of her attack to the party.", 5, 1,
                      True)
HuamaoS2: Move = Move("Philosopher's Will",
                      "Huamao heals 1000% of her attack to a party member.",
                      10, 1, False)
Huamao = GachaCharacter("Huamao", 1700, 5, 50, 3, 10, 1.5, True,
                        [HuamaoAA, HuamaoS1, HuamaoS2], .05, "img/huamao.png",
                        "img/huamao_splash.png")

RabadonAA: Move = Move(
    "Basic Attack",
    "Rabadon summons her familiar to ravage an enemy for 75% of her attackk.",
    0.75, 1, False)
RabadonS1: Move = Move(
    "Meteor",
    "Rabadon summons a meteor that deals 500% or her attack to all characters on the field.",
    500, 1, True)
RabadonS2: Move = Move(
    "Death",
    "Rabadon crushes all enemies dealing 50% max HP damage to all enemies.",
    0.5, 1, True)
Rabadon = GachaCharacter("Rabadon", 1000, 7, 200, 0, 10, 1.5, True,
                         [RabadonAA, RabadonS1, RabadonS2], .05,
                         "img/rabadon.png", "img/rabadon_splash.png")
