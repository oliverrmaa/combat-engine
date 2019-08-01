import random as rand
import numpy as np


# Create the Character Class first
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

    
# Create the function for simulating 1 battle
def sim_battle(c1, c2):
    c1hp_init = c1.health
    c2hp_init = c2.health
    
    turn_count = 0

    # this is the core loop of the game
    while not c1.dead() and not c2.dead():    
        c1a = c1.gen_attack(c1hp_init)
        c2a = c2.gen_attack(c2hp_init)
        c1h = c1.gen_heal()
        c2h = c2.gen_heal()
        
        turn_count += 1
        
        if np.random.uniform() < 0.5:
            c1.health = c1h - c2a
        else:
            c2.health = c2h - c1a
  
    # if someone gets defeated
    if c1.dead() and not c2.dead():
#         print(c2.getname(), 'is the victor')
        victor = "B"

    elif c2.dead() and not c1.dead():
#         print(c1.getname(), 'is the victor')
        victor = "A"
        
    else:
        print('Draw')             

#     If we need to view the results of each fight uncomment the print statements        
#     print('Final stats') 
#     print('Number of Turns:', turn_count)
#     print(c1.getname(), c1.printstat())
#     print(c2.getname(), c2.printstat())
    return victor




# Now we can simulate the battle 1000 times

# simulate
c_Bvictor = 0
c_Avictor = 0

i = 1
while i <= 1000 :
    i += 1
    # Input the character data
    c1 = Character('Berserker', 5000, 400, 0.20, 2.0,  1, 0.000)
    c2 = Character('Paladin'  , 6000, 300, 0.10, 1.5,  0, 0.030)

    
    whowin = sim_battle(c1, c2)
    if whowin == "A":
        c_Avictor += 1
    else:
        c_Bvictor += 1

print("_______________________________________________")
print("Berserker vs. Paladin results for 1000 battles:")
print("Berserker won:", c_Avictor)
print("Paladin won:", c_Bvictor)
print("_______________________________________________")