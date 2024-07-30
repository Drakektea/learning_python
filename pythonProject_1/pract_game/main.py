from os import system
from time import sleep

from helicopter import Helicopter
from connector import GameConnector
from map import Map
from constants import (WAITING, TREE_UPDATE,
                       FIRE_UP_UPDATE, FIRE_DOWN_UPDATE,
                       TICK, CLEAR)


game_map = Map()
game_map.generate_map()
game_helicopter = Helicopter(game_map)

game = GameConnector(game_map, game_helicopter, None)
while True:
    TICK += 1
    system(CLEAR)
    game.print_map()
    if TICK % TREE_UPDATE == 0:
        game_map.update_forest()
    if TICK % FIRE_UP_UPDATE == 0:
        game_map.update_fire_up()
    if TICK % FIRE_DOWN_UPDATE == 0:
        game_map.update_fire_down()
    sleep(WAITING)
