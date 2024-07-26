from map import Map
from constants import WAITING, CLEAR

from os import system
from time import sleep


game_map = Map()
game_map.generate_map()

TICK = 0
while True:
    system(CLEAR)
    game_map.print_map()
    TICK += 1
    sleep(WAITING)
