from curses import wrapper, curs_set
from time import sleep

from helicopter import Helicopter
from clouds import Clouds
from map import Map
from stats import Statistic
from connector import GameConnector, KeyBoardMoveButtons
from constants import (WAITING, TREE_UPDATE,
                       FIRE_UP_UPDATE, FIRE_DOWN_UPDATE,
                       FRAMES,
                       WATER, REWARDS)


def main(stdscr):
    curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(int(WAITING * 1000))

    game_map = Map()
    game_map.generate_map()
    game_helicopter = Helicopter(game_map, WATER, REWARDS)
    game_clouds = Clouds()

    game_stats = Statistic(WATER, REWARDS)
    game_keyboard = KeyBoardMoveButtons()
    game = GameConnector(game_stats, game_map, game_helicopter, game_clouds)

    TICK = 0
    while True:
        TICK += 1
        key = game_keyboard.key_is_pressed
        if key and TICK % 2 == 0:
            game_helicopter.move(key)

        game_helicopter.processing()

        if TICK % FRAMES == 0:
            REWARDS.current_value += 1
        if TICK % TREE_UPDATE == 0:
            game_map.update_forest()
        if TICK % FIRE_UP_UPDATE == 0:
            game_map.update_fire_up()
        if TICK % FIRE_DOWN_UPDATE == 0:
            game_map.update_fire_down()

        output = 'user: ' + str(game_helicopter.xy) + '\n' + game.print_map()

        stdscr.clear()
        stdscr.addstr(output)
        sleep(WAITING)
        stdscr.refresh()


if __name__ == "__main__":
    wrapper(main)
