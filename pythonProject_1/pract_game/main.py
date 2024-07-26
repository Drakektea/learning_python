from map import Map
from constants import TICK, CLEAR

from os import system
from time import sleep


game_map = Map()
game_map.generate_map()

while True:
    system(CLEAR)
    game_map.print_map()
    sleep(TICK)
