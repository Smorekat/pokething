import random as rng
import player as p

class enemy():
    def __init__(self, health, attack, defense, model, level):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.model = model
        self.level = level

    def autogen(self):
        self.level = rng.randint(6,10) + int(p.player.level / 5)
        self.multiplier = self.level / 8
        self.health = rng.randint(50,120) * self.multiplier
        self.defense = (rng.randint(0,10), rng.randint(10,15)) * self.multiplier
        
