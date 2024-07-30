from map import Map
from helicopter import Helicopter
from clouds import Clouds
from additional_components import Cell


class GameConnector:
    def __init__(self, game_map: Map, game_helicopter: Helicopter, game_clouds: Clouds):
        self.map = game_map
        self.helicopter = game_helicopter
        self.clouds = game_clouds

    def print_map(self):
        print(Cell.BLOCK * (self.map.w + 2))
        for row in range(len(self.map.map)):
            print(Cell.BLOCK, end='')
            for column in range(len(self.map.map[row])):
                if (row, column) == self.helicopter.xy:
                    cell = Cell.HELICOPTER
                else:
                    cell = self.map.map[row][column]
                print(cell, end='')
            print(Cell.BLOCK)
        print(Cell.BLOCK * (self.map.w + 2))
