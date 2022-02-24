import enemies as e
import random as rng

#def attack():
class player():
    def __init__(self, health, attack, defense, level, name):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.level = level
        self.name = name

    def autogen(self):
        self.multiplier = (self.level+7) / 8
        self.health = rng.randint(50,120) * self.multiplier
        self.defense = (rng.randint(0,10), rng.randint(10,15)) * self.multiplier

user = player(100)
user.autogen(120, 35, 10, 1, )

def level_up():
    pass