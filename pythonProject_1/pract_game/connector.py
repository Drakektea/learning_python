from map import Map
from helicopter import Helicopter
from clouds import Clouds
from stats import Statistic
from additional_components import Cell
from keyboard import is_pressed


class GameConnector:
    def __init__(self, game_stats: Statistic, game_map: Map, game_helicopter: Helicopter, game_clouds: Clouds):
        self.stats = game_stats
        self.map = game_map
        self.helicopter = game_helicopter
        self.clouds = game_clouds

    def print_all(self):
        down = self.map.map
        up = self.clouds.cloud_map

        output = ''
        output += self.stats.info_stats + '\n'
        output += Cell.BLOCK * (self.map.w + 2) + '\n'
        for row in range(len(down)):
            output += Cell.BLOCK
            for column in range(len(down[row])):
                if (column, row) == self.helicopter.xy:
                    cell = Cell.HELICOPTER
                elif up[row][column] == Cell.CLOUD:
                    cell = Cell.CLOUD
                elif up[row][column] == Cell.STORM:
                    cell = Cell.STORM
                else:
                    cell = down[row][column]
                output += cell
            output += Cell.BLOCK + '\n'
        output += Cell.BLOCK * (self.map.w + 2) + '\n'
        return output

    def print_map(self):
        output = ''
        output += self.stats.info_stats + '\n'
        output += Cell.BLOCK * (self.map.w + 2) + '\n'
        for row in range(len(self.map.map)):
            output += Cell.BLOCK
            for column in range(len(self.map.map[row])):
                if (column, row) == self.helicopter.xy:
                    cell = Cell.HELICOPTER
                else:
                    cell = self.map.map[row][column]
                output += cell
            output += Cell.BLOCK + '\n'
        output += Cell.BLOCK * (self.map.w + 2) + '\n'
        return output

    def print_clouds(self):
        output = ''
        output += self.stats.info_stats + '\n'
        output += Cell.BLOCK * (self.map.w + 2) + '\n'
        for row in range(len(self.clouds.cloud_map)):
            output += Cell.BLOCK
            for column in range(len(self.clouds.cloud_map[row])):
                cell = self.clouds.cloud_map[row][column]
                output += cell
            output += Cell.BLOCK + '\n'
        output += Cell.BLOCK * (self.map.w + 2) + '\n'
        return output


class KeyBoardMoveButtons:
    keys = {
        'w': (0, -1),
        'a': (-1, 0),
        's': (0, 1),
        'd': (1, 0),
    }

    @property
    def key_is_pressed(self):
        for key in self.keys:
            if is_pressed(key):
                return self.keys[key]
        return None
