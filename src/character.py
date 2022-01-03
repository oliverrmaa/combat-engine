import random as rand
import numpy as np

class Character(object):
    def __init__(self, name, health, attack, crit_rate, crit_mult, berserk_percent, pray_percent):
        self.name = name
        self.health = health
        self.attack = attack
        self.crit_rate = crit_rate
        self.crit_mult = crit_mult
        self.berserk_percent = berserk_percent
        self.pray_percent = pray_percent

    def getname(self):
        return self.name

    def dead(self):
        if self.health < 0:
            return True
        return False

    def printstat(self):
        return self.health, self.attack, self.crit_rate, self.crit_mult,

    def gen_attack (self, hp_init):
        if self.health < hp_init/10:
            if np.random.uniform() < self.crit_rate:
                attack_val = self.crit_mult*(self.attack + self.berserk_percent*self.attack)
            else:
                attack_val = self.attack + self.berserk_percent*self.attack
        else:
            if np.random.uniform() < self.crit_rate:
                attack_val = self.crit_mult*self.attack
            else:
                attack_val = self.attack
        return attack_val

    def gen_heal (self):
        health_val = self.health + self.pray_percent*self.health
        return health_val
