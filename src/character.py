# adventuring hero
class Character():
    def __init__(self, name, level, class, major_trait=None, minor_trait=None):
        self.name = name
        self.level = level
        self.class = class
        self.major_trait = major_trait
        self.minor_trait = minor_trait

    def __str__(self):
        return f'{self.name}, a level {self.level} {self.class}.'


class Hero(Character):
    def
