# Location class

class Location():
    def __init__(self, name, x, y, road_n=None, road_e=None, road_s=None, road_w=None, road_u=None, road_d=None):
        self.name = name
        self.x =  x
        self.y = y
        self.road_n = road_n
        self.road_e = road_e
        self.road_s = road_s
        self.road_w = road_w
        self.road_u = road_u
        self.road_d = road_d
    def __str__(self):
        return f'{self.name}, located at coordinates: {self.x}, {self.y}.'

class Town(Location):
    def __init__(self, name, x, y, road_n=None, road_e=None, road_s=None, road_w=None, road_u=None, road_d=None, population=0):
        super().__init__(name, x, y, road_n, road_e, road_s, road_w, road_u, road_d)
        self.population = population

    def __str__(self):
        return super().__str__()


class Dungeon(Location):
    def __init__(self, name, x, y, road_n=None, road_e=None, road_s=None, road_w=None, road_u=None, road_d=None, difficulty=0):
        super().__init__(name, x, y, road_n, road_e, road_s, road_w, road_u, road_d)
        self.difficulty = difficulty

    def __str__(self):
        return super().__str__(self)
