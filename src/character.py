# characters
from random import randint

class Character():
    def __init__(self, name="", location=None, level=1, hp=0):
        self.name = name
        self.location = location
        self.level = level
        self.hp = hp
    def __str__(self):
        return f'{self.name}, a level {self.level} {type(self).__name__} currently at {self.location.name} with {self.hp} HP.'

    def move(self, place):
        self.location = place

class Hero(Character):
    def __init__(self, name, location, level, traits=[], hp=0):
        super().__init__(name, location, level, hp)
        self.traits = traits

    def __str__(self):
        return super().__str__()

class Barbarian(Hero):
    def __init__(self, name, location, level, traits, hp=randint(25, 35)):
        super().__init__(name, location, level, traits, hp)

    def __str__(self):
        return super().__str__()

class Wizard(Hero):
    def __init__(self, name, location, level, traits, hp=randint(13, 17)):
        super().__init__(name, location, level, traits, hp)

    def __str__(self):
        return super().__str__()

class Rogue(Hero):
    def __init__(self, name, location, level, traits, hp=randint(17, 23)):
        super().__init__(name, location, level, traits, hp)

    def __str__(self):
        return super().__str__()

class Cleric(Hero):
    def __init__(self, name, location, level, traits, hp=randint(21, 29)):
        super().__init__(name, location, level, traits, hp)

    def __str__(self):
        return super().__str__()
