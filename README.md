# Video-Game-Fight-Simulation
This simulator runs a 1v1 match up between two classic character classes often found in RPG and fighting games.

The program constructs character classes for two fighters which are inspired by the standard trope of Berserker and Paladin character classes. Then 1000 battles are simulated (similar to the now-cancelled TV Show "Deadliest Warrior") to determine the better fighter. The end result is of interest as it allows us to test whether the match is "balanced" or not so to speak. 

# Combat Model

This is a simple simulation. There is no movement, the characters are face-to-face fighting with a random chance of 50% for which character will land a hit on the other. There are both standard attacks and critical hits. There are no weapons (other than the ones implicit in their attacking abilities) or armour. As a way to demonstrate their character tropes, each character has a special ability. 

The ability for the berserker is that when the berserker's health drops below some percentage, they enter berserk mode where their attack can increase by multiples. The ability for the paladin is that they are constantly gaining health through their prayer ability. 

# Interpretation of the Results

Results where the the amount of matches won by both characters is close to 50% each, would demonstrate that the two character classes are close to equal and therefore in a real life context, the game would then depend on the individual skills of the players. If the match is unbalanced it would suggest one character is overpowered resulting in the potential emergence of a "dominant strategy" in a real life context because players using these characters would just pick the overpowered one. This would suggest a poorly designed character class as it leads to an unbalanced game.
