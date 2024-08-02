from random import choice, randint
from perlin import Perlin
from additional_components import Cell, WindDirection
from constants import OFFSET


class Clouds:
    def __init__(self, main_map):
        self.w = main_map.w
        self.h = main_map.h
        self.wind_direction = choice([direction for direction in WindDirection])
        self.noise = Perlin(randint(self.w + self.h, self.w * self.h))
        self.noise_scale = (self.w + self.h) // 2 / 9
        self.cloud_map = [[' ' for _ in range(self.w)] for _ in range(self.h)]
        self.time_step = 0
        self.cloud_threshold = 0.1

    def export_data(self):
        return {
            'wind_direction': self.wind_direction.value,
            'cloud_map': self.cloud_map,
            'time_step': self.time_step,
            'cloud_threshold': self.cloud_threshold
        }

    def check_bound(self, x, y):
        return not (x < 0 or y < 0 or x >= self.w or y >= self.h)

    def generate_clouds(self):
        self.__generate_just_clouds()
        self.__generate_storm_clouds()

    def update_clouds(self, tick):
        self.time_step = tick
        self.cloud_threshold += OFFSET
        self.__generate_just_clouds(update=True)
        self.__generate_storm_clouds(update=True)

    def __generate_just_clouds(self, noise_scale=None, threshold=None, update=False):
        if threshold is None:
            threshold = self.cloud_threshold
        direction_offset = (self.wind_direction.value[0] * self.time_step,
                            self.wind_direction.value[1] * self.time_step) if update else (0, 0)
        if noise_scale is None:
            noise_scale = self.noise_scale
        for y in range(self.h):
            for x in range(self.w):
                noise_value = self.noise.noise((x + direction_offset[0]) / noise_scale,
                                               (y + direction_offset[1]) / noise_scale)
                if noise_value > threshold:
                    self.cloud_map[y][x] = Cell.CLOUD
                else:
                    self.cloud_map[y][x] = ' '

    def __generate_storm_clouds(self, noise_scale=None, threshold=None, update=False):
        if threshold is None:
            threshold = self.cloud_threshold + 0.5
        direction_offset = (self.wind_direction.value[0] * self.time_step,
                            self.wind_direction.value[1] * self.time_step) if update else (0, 0)
        if noise_scale is None:
            noise_scale = self.noise_scale
        for y in range(self.h):
            for x in range(self.w):
                noise_value = self.noise.noise((x + direction_offset[0]) / noise_scale,
                                               (y + direction_offset[1]) / noise_scale)
                if noise_value > threshold and self.__is_surrounded_by_clouds(x, y):
                    self.cloud_map[y][x] = Cell.STORM

    def __is_surrounded_by_clouds(self, x, y):
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                if not self.check_bound(x + dx, y + dy):
                    continue
                if self.cloud_map[y + dy][x + dx] not in (Cell.CLOUD, Cell.STORM):
                    return False
        return True
