# Location class

class Location():
    def __init__(self, name, x, y):
        self.name = name
        self.x =  x
        self.y = y
    def __str__(self):
        return f'{self.name} at {self.x}, {self.y}.'

class Town(Location):
    def __init__(self, name, x, y, population):
        super().__init__(name, x, y)
        self.population = population

    def __str__(self):
        super().__str__(self)


class Dungeon(Location):
    def __init__(self, name, x, y, difficulty):
        super().__init__(name, x, y)
        self.difficulty = difficulty

    def __str__(self):
        super().__str__(self)
