import random

from perlin import Perlin
from additional_components import Cell
from constants import IS_TREE, IS_EMPTY, IS_FIRE


class Map:
    def __init__(self, w=30, h=30):
        self.w, self.h = max(10, w), max(10, h)
        self.rivers, self.forest = ((w + h) // 2 / 4, -0.15), ((w + h) // 2 / 3, 0)
        self.noise = Perlin(random.randint(w + h, w * h))
        self.map = [[Cell.EMPTY for k in range(w)] for j in range(h)]
        self.all_coordinates = [(x, y) for y in range(h) for x in range(w)]

    def check_bound(self, x, y):
        return not (x < 0 or y < 0 or x >= self.w or y >= self.h)

    def generate_map(self, rivers=(), forest=()):
        if not rivers:
            rivers = self.rivers
        if not forest:
            forest = self.forest

        self.__generate_rivers(noise_scale=rivers[0], threshold=rivers[-1])
        self.__generate_forest(noise_scale=forest[0], threshold=forest[-1])
        self.__generate_fire()

        tree_count = sum(1 for y in range(self.h) for x in range(self.w) if self.map[y][x] == Cell.TREE)
        if tree_count < 10:
            self.noise = Perlin(random.randint(self.w + self.h, self.w * self.h))
            self.map = [[Cell.EMPTY for k in range(self.w)] for j in range(self.h)]
            return self.generate_map(rivers, forest)

    def print_map(self, main_helicopter):
        print(Cell.BLOCK * (self.w + 2))
        for row in range(len(self.map)):
            print(Cell.BLOCK, end='')
            for column in range(len(self.map[row])):
                if (row, column) == main_helicopter.xy:
                    cell = Cell.HELICOPTER
                else:
                    cell = self.map[row][column]
                print(cell, end='')
            print(Cell.BLOCK)
        print(Cell.BLOCK * (self.w + 2))

    def update_forest(self):
        tree_coordinates = self.__get_objects(IS_TREE)
        if not tree_coordinates:
            return

        random_tree = random.choice(tree_coordinates)
        tree_x, tree_y = random_tree

        available_coordinates = []
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                neighbor_x, neighbor_y = tree_x + dx, tree_y + dy

                if not self.check_bound(neighbor_x, neighbor_y):
                    continue
                if self.__is_adjacent_to_river(neighbor_x, neighbor_y):
                    continue
                if not self.map[neighbor_y][neighbor_x] == Cell.EMPTY:
                    continue

                available_coordinates.append((neighbor_x, neighbor_y))

        if not available_coordinates:
            return
        if not random.random() < 0.05:
            return

        available_coordinates = []
        empty_coordinates = self.__get_objects(IS_EMPTY)
        for x, y in empty_coordinates:
            if self.__is_adjacent_to_river(x, y):
                continue
            available_coordinates.append((x, y))

        new_tree_position = random.choice(available_coordinates)
        self.map[new_tree_position[1]][new_tree_position[0]] = Cell.TREE

    def update_fire_up(self):
        fire_coordinates = self.__get_objects(IS_FIRE)
        if fire_coordinates:
            random_fire = random.choice(fire_coordinates)
            fire_x, fire_y = random_fire

            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    neighbor_x, neighbor_y = fire_x + dx, fire_y + dy

                    if not self.check_bound(neighbor_x, neighbor_y):
                        continue
                    if not self.map[neighbor_y][neighbor_x] == Cell.TREE:
                        continue
                    if not random.random() < 0.3:
                        continue

                    self.map[neighbor_y][neighbor_x] = Cell.FIRE
                    return

        if not random.random() < 0.1:
            return

        tree_coordinates = self.__get_objects(IS_TREE)
        if not tree_coordinates:
            return

        random_tree = random.choice(tree_coordinates)
        self.map[random_tree[1]][random_tree[0]] = Cell.FIRE

    def update_fire_down(self):
        fire_coordinates = self.__get_objects(IS_FIRE)
        if not fire_coordinates:
            return

        random_fire = random.choice(fire_coordinates)
        fire_x, fire_y = random_fire
        if not random.random() < 0.4:
            return

        adjacent_trees = []
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                neighbor_x, neighbor_y = fire_x + dx, fire_y + dy

                if not self.check_bound(neighbor_x, neighbor_y):
                    continue
                if not self.map[neighbor_y][neighbor_x] == Cell.TREE:
                    continue

                adjacent_trees.append((neighbor_x, neighbor_y))

        if adjacent_trees:
            num_trees_to_burn = min(3, len(adjacent_trees) - 1)
            trees_to_burn = random.sample(adjacent_trees, num_trees_to_burn)

            for tree_x, tree_y in trees_to_burn:
                self.map[tree_y][tree_x] = Cell.FIRE

        self.map[fire_y][fire_x] = Cell.EMPTY

    def __get_objects(self, condition):
        return tuple((x, y) for x, y in self.all_coordinates if condition(self.map[y][x]))

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

    def __generate_fire(self, num_trees_to_burn=3):
        tree_coordinates = self.__get_objects(IS_TREE)
        if not tree_coordinates:
            return

        trees_to_burn = random.sample(tree_coordinates, num_trees_to_burn)

        for tree_x, tree_y in trees_to_burn:
            self.map[tree_y][tree_x] = Cell.FIRE

    def __is_adjacent_to_river(self, x, y):
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                if self.check_bound(x + dx, y + dy) and self.map[y + dy][x + dx] == Cell.RIVER:
                    return True
        return False


map_size = 30
game_map = Map(map_size, map_size)
game_map.generate_map()

from helicopter import Helicopter
game_helicopter = Helicopter(game_map)

game_map.print_map(game_helicopter)
