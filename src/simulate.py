import numpy as np
from src.character import Character

def sim_battle(c1, c2):
    """Simulates battle between c1 and c2 and returns name of winner."""
    c1hp_init = c1.health
    c2hp_init = c2.health

    turn_count = 0

    # this is the core loop of a single combat simulation
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
        victor = c2.name

    elif c2.dead() and not c1.dead():
        victor = c1.name

    else:
        victor = None

    return victor

def sim_multiple_battles(c1_stats_dict, c2_stats_dict, num_battles):
    """Simulates multiple battles and returns printed results"""

    c1_victories = 0
    c2_victories = 0

    # Iterate through num_battles configured in the YAML file
    for i in range(1, num_battles):
        c1 = Character(
            c1_stats_dict["name"],
            c1_stats_dict["health"],
            c1_stats_dict["attack"],
            c1_stats_dict["crit_rate"],
            c1_stats_dict["crit_mult"],
            c1_stats_dict["berserk_percent"],
            c1_stats_dict["pray_percent"]
        )
        c2 = Character(
            c2_stats_dict["name"],
            c2_stats_dict["health"],
            c2_stats_dict["attack"],
            c2_stats_dict["crit_rate"],
            c2_stats_dict["crit_mult"],
            c2_stats_dict["berserk_percent"],
            c2_stats_dict["pray_percent"]
        )

        whowin = sim_battle(c1, c2)
        if whowin == c1.name:
            c1_victories += 1
        elif whowin == c2.name:
            c2_victories += 1
        else:
            pass

    # print results
    print("_______________________________________________")
    print("{} vs. {} results for {} battles:".format(c1.name, c2.name, num_battles))
    print("{} won: {} times".format(c1.name, c1_victories))
    print("{} won: {} times".format(c2.name, c2_victories))
    print("_______________________________________________")
