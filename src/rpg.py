# main gameplay loop: send characters to locations
from random import choice, randint, sample

from location import Location, Town, Dungeon
from character import *

t = Town("Hyperia", 40, 50, 50000)

c = Hero("John", t, 1, "Fastidious", 30)


classes = (Barbarian, Wizard, Rogue, Cleric)
traits = ("Fastidious", "Wrathful", "Cruel", "Merciful", "Determined", "Clever")
toons = []
# Initial setup

# Random names
firstnames = ("John", "David")
lastnames = ("Johnson", "Gospodinoff")
names = []
while len(names) < 4:
    newname = f'{choice(firstnames)} {choice(lastnames)}'
    if newname in names:
        continue
    else:
        names.append(newname)

for _ in range(4):
    name_ = names.pop(0)
    location_ = t
    level_ = 1
    second_trait_probability = randint(1,4)
    if second_trait_probability == 4:
        traits_ = sample(traits, 2)
    else:
        traits_ = [choice(traits)]
    char = choice(classes)(name_, location_, level_, traits_)
    toons.append(char)
for toon in toons:
    print(toon)
