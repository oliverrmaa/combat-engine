import numpy as np
import random as rand
import sys
from src.character import Character
from src.simulate import sim_battle, sim_multiple_battles
import yaml


# c1 = Character('Berserker', 5000, 400, 0.20, 2.0,  1, 0.000)
# c2 = Character('Paladin'  , 6000, 300, 0.10, 1.5,  0, 0.030)

# num_battles = 1000
#
# c1_stats_dict = {
#     "name": "Berserker",
#     "health": 5000,
#     "attack": 400,
#     "crit_rate": 0.2,
#     "crit_mult": 2.0,
#     "berserk_percent": 1.0,
#     "pray_percent": 0.0
# }
#
# c2_stats_dict = {
#     "name": "Paladin",
#     "health": 6000,
#     "attack": 300,
#     "crit_rate": 0.1,
#     "crit_mult": 1.5,
#     "berserk_percent": 0.0,
#     "pray_percent": 0.03
# }

if __name__ == '__main__':

    try:
        with open("models/" + sys.argv[1] + ".yaml", "r") as stream:
            try:
                model = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        c1_stats_dict = model["character_1"]
        c2_stats_dict = model["character_2"]
        num_battles = model["num_battles"]

        sim_multiple_battles(c1_stats_dict, c2_stats_dict, num_battles)

    except IndexError:
        print("No model provided")
