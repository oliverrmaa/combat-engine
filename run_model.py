import numpy as np
import sys
import yaml
from src.simulate import sim_battle, sim_multiple_battles

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
