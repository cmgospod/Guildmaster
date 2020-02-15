# main gameplay loop: send characters to locations
from random import choice, randint, sample

from location import Location, Town, Dungeon
from character import *

hyperia = Town("Hyperia", 40, 50, population=50000)
riverside = Town("Riverside", 50, 50, population=8000)
noctus = Dungeon("Noctus", 66, 66, difficulty=4)
c = Hero("John", hyperia, 1, "Fastidious", 30)
hyperia.road_e = riverside
riverside.road_w = hyperia
riverside.road_n = noctus
noctus.road_s = riverside




classes = (Barbarian, Wizard, Rogue, Cleric)
traits = ("Fastidious", "Wrathful", "Cruel", "Merciful", "Determined", "Clever")
toons = []
# Initial setup

# Random names
firstnames = ("John", "David", "Jacob", "William", "Anna", "Spencer", "Shawn", "Jack")
lastnames = ("Johnson", "Gospodinoff", "Charles", "Seymour", "Crowley", "Williamson", "Abrams")
names = []
while len(names) < 40:
    newname = f'{choice(firstnames)} {choice(lastnames)}'
    if newname in names:
        continue
    else:
        names.append(newname)

for _ in range(20):
    name_ = names.pop(0)
    location_ = choice([riverside, hyperia])
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
