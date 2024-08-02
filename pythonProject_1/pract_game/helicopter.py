from threading import Timer
from random import choice
from constants import (Item, Cell, IS_HP_RECOVERY,
                       IS_RIVER, IS_FIRE, IS_SHOP, IS_STORMCLOUD,
                       SAVE_TREE_BONUS, UPGRADE_COST,
                       SHOP_WAITING_SECONDS, HP_COST,
                       HP_WAITING_SECONDS)


class Helicopter:
    def __init__(self, main_map, main_clouds,
                 water: Item, rewards: Item, hp: Item):
        self.map = main_map
        self.clouds = main_clouds
        self.x, self.y = choice(main_map.all_coordinates)
        self.water = water
        self.rewards = rewards
        self.hp = hp
        self.got_rewards = 0
        self.got_water = 0
        self.saved_trees = 0
        self.upgrade_level = 1
        self.lost_hp = 0
        self.get_hp = 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new):
        self.__x = new

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new):
        self.__y = new

    @property
    def xy(self):
        self.xy = (self.x, self.y)
        return self.__xy

    @xy.setter
    def xy(self, new):
        self.__xy = new

    def export_data(self):
        return {
            'x': self.x,
            'y': self.y,
            'water.value': self.water.current_value,
            'rewards.value': self.rewards.current_value,
            'hp.value': self.hp.current_value,
            'got_rewards': self.got_rewards,
            'got_water': self.got_water,
            'saved_trees': self.saved_trees,
            'upgrade_level': self.upgrade_level,
            'lost_hp': self.lost_hp,
            'get_hp': self.get_hp,
        }

    def move(self, xy):
        if xy[0] and self.x + xy[0] not in (-1, self.map.w):
            self.x += xy[0]
        if xy[1] and self.y + xy[1] not in (-1, self.map.h):
            self.y += xy[1]

    def processing(self):
        current_map_cell = self.map.map[self.y][self.x]
        current_cloud_cell = self.clouds.cloud_map[self.y][self.x]
        if IS_RIVER(current_map_cell):
            self.got_water += (self.water.max_value - self.water.current_value)
            self.water.current_value = self.water.max_value
        elif IS_FIRE(current_map_cell) and self.water.in_min_max:
            self.water.current_value -= 1
            self.rewards.current_value += SAVE_TREE_BONUS
            self.map.map[self.y][self.x] = Cell.TREE
            self.saved_trees += 1
            self.got_rewards += SAVE_TREE_BONUS
        elif IS_SHOP(current_map_cell) and \
                self.rewards.min_value < self.rewards.current_value - UPGRADE_COST:
            self.rewards.current_value -= UPGRADE_COST
            self.water.max_value += 1
            self.__waiting_object(self.xy, Cell.SHOP, SHOP_WAITING_SECONDS)
            self.upgrade_level += 1
        elif IS_HP_RECOVERY(current_map_cell):
            money = max(0, self.rewards.current_value)
            lost_hp = self.hp.max_value - self.hp.current_value
            hp_to_recover = min(lost_hp, money // HP_COST)
            self.hp.current_value += hp_to_recover
            self.rewards.current_value -= hp_to_recover * HP_COST
            if hp_to_recover < 1:
                return
            self.__waiting_object(self.xy, Cell.HP_RECOVERY, HP_WAITING_SECONDS)
            self.get_hp += hp_to_recover
        if IS_STORMCLOUD(current_cloud_cell):
            self.hp.current_value -= 1
            self.lost_hp += 1

    def __waiting_object(self, coordinate, _object, _wait):
        self.map.map[coordinate[1]][coordinate[0]] = Cell.BLOCK
        self.__update_clock(coordinate,
                            0,
                            _wait / len(Cell.CLOCKS),
                            _wait,
                            _object)

    def __update_clock(self, coordinate, index, timing, remaining_seconds, _object):
        if remaining_seconds > 0:
            self.map.map[coordinate[1]][coordinate[0]] = Cell.CLOCKS[index % len(Cell.CLOCKS)]
            Timer(timing,
                  self.__update_clock,
                  args=[coordinate,
                        index + 1,
                        timing,
                        remaining_seconds - timing,
                        _object]).start()
        else:
            self.map.map[coordinate[1]][coordinate[0]] = _object
