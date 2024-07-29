from random import choice


class Helicopter:
    def __init__(self, main_map):
        self.x, self.y = choice(main_map.all_coordinates)
        self.xy = (self.x, self.y)
