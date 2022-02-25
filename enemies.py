import random as rng
import player as p

class enemy():
    def __init__(self, health, attack, defense, model, level):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.model = model
        self.level = level
