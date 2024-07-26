import random
from perlin import Perlin
from additional_components import Cell


class Map:
    def __init__(self, w=30, h=30):
        self.w, self.h = w, h
        self.rivers, self.forest = ((w + h) // 2 / 4, -0.15), ((w + h) // 2 / 3, 0)
        self.noise = Perlin(random.randint(self.w + self.h, self.w * self.h))
        self.map = [[Cell.EMPTY for j in range(w)] for k in range(h)]

    def check_bound(self, x, y):
        return not (x < 0 or y < 0 or x >= self.w or y >= self.h)

    def generate_map(self, rivers=(), forest=()):
        if not rivers:
            rivers = self.rivers
        if not forest:
            forest = self.forest
        self.__generate_rivers(noise_scale=rivers[0], threshold=rivers[-1])
        self.__generate_forest(noise_scale=forest[0], threshold=forest[-1])
        return self.map

    def print_map(self):
        print(Cell.BLOCK * (self.w + 2))
        for row in self.map:
            print(Cell.BLOCK, end='')
            for cell in row:
                print(cell, end='')
            print(Cell.BLOCK)
        print(Cell.BLOCK * (self.w + 2))

    def update_forest(self):
        for y in range(self.h):
            for x in range(self.w):
                if self.map[y][x] == Cell.TREE:
                    available_coordinates = (((k, j) for k in (-1, 0, 1) if k != 0 and j != 0) for j in (-1, 0, 1))
                    for dx, dy in available_coordinates:
                        if not self.check_bound(x + dx, y + dy):
                            continue
                        if self.map[y + dy][x + dx] not in (Cell.RIVER,) and\
                           not self.__is_adjacent_to_river(x + dx, y + dy) and\
                           random.randint(0, 1):
                            self.map[y + dy][x + dx] = Cell.TREE
                            return

    def __generate_rivers(self, noise_scale, threshold):
        for y in range(self.h):
            for x in range(self.w):
                value = self.noise.noise(x / noise_scale, y / noise_scale)
                if value < threshold:
                    self.map[y][x] = Cell.RIVER

    def __generate_forest(self, noise_scale, threshold):
        for y in range(self.h):
            for x in range(self.w):
                if self.map[y][x] == Cell.RIVER:
                    continue
                value = self.noise.noise(x / noise_scale, y / noise_scale)
                if value > threshold and not self.__is_adjacent_to_river(x, y):
                    self.map[y][x] = Cell.TREE

    def __is_adjacent_to_river(self, x, y):
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                if self.check_bound(x + dx, y + dy) and self.map[y + dy][x + dx] == Cell.RIVER:
                    return True
        return False


'''
map_size = 30
game_map = Map(map_size, map_size)
game_map.generate_map()
game_map.print_map()
'''
