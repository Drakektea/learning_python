from map import Map
from constants import (WAITING, TREE_UPDATE,
                       FIRE_UP_UPDATE, FIRE_DOWN_UPDATE,
                       TICK, CLEAR)

from os import system
from time import sleep


game_map = Map()
game_map.generate_map()

while True:
    TICK += 1
    system(CLEAR)
    game_map.print_map()
    if TICK % TREE_UPDATE == 0:
        game_map.update_forest()
    if TICK % FIRE_UP_UPDATE == 0:
        game_map.update_fire_up()
    if TICK % FIRE_DOWN_UPDATE == 0:
        game_map.update_fire_down()
    sleep(WAITING)
