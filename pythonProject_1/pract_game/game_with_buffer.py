from curses import wrapper, curs_set
from time import sleep
from exporter import export_game
from importer import import_game
from keyboard import wait, is_pressed
from helicopter import Helicopter
from clouds import Clouds
from map import Map
from stats import Statistic
from additional_components import WindDirection
from connector import GameConnector, KeyBoardMoveButtons
from constants import (WAITING, TREE_UPDATE, FIRE_UP_UPDATE,
                       FIRE_DOWN_UPDATE, FRAMES, UPDATE_CLOUD,
                       WATER, REWARDS, HP)


def main(stdscr):
    curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(int(WAITING * 1000))

    game_map = Map()
    game_map.generate_map()
    game_clouds = Clouds(game_map)
    game_clouds.generate_clouds()
    game_helicopter = Helicopter(game_map, game_clouds, WATER, REWARDS, HP)

    game_stats = Statistic(WATER, REWARDS, HP)
    game_keyboard = KeyBoardMoveButtons()
    game = GameConnector(game_stats, game_map, game_helicopter, game_clouds)

    TICK = 0
    while True:
        TICK += 1
        key = game_keyboard.key_is_pressed
        if key and TICK % 2 == 0:
            game_helicopter.move(key)
        if is_pressed('s+g'):
            stdscr.clear()
            export_game(game, TICK - 1, addstr=stdscr.addstr)
            output = 'user: ' + str(game_helicopter.xy) + '\n' + game.print_all()
            stdscr.refresh()
            sleep(3)
            stdscr.clear()
            stdscr.addstr(output)
            sleep(WAITING)
            stdscr.refresh()
        elif is_pressed('l+g'):
            stdscr.clear()
            data = import_game(addstr=stdscr.addstr)
            if data:
                TICK = data['tick']

                data_map = data['map']
                game_map = Map(data_map['w'], data_map['h'])
                game_map.map = data_map['map']
                game_map.burn_trees = data_map['burn_trees']
                game_map.born_trees = data_map['born_trees']

                data_clouds = data['clouds']
                game_clouds = Clouds(game_map)
                direct = [direct for direct in WindDirection if direct.value == tuple(data_clouds['wind_direction'])][0]
                game_clouds.wind_direction = direct
                game_clouds.cloud_map = data_clouds['cloud_map']
                game_clouds.time_step = data_clouds['time_step']
                game_clouds.cloud_threshold = data_clouds['cloud_threshold']

                data_user = data['helicopter']
                WATER.current_value = data_user['water.value']
                REWARDS.current_value = data_user['rewards.value']
                HP.current_value = data_user['hp.value']
                game_helicopter = Helicopter(game_map, game_clouds, WATER, REWARDS, HP)
                game_helicopter.x = data_user['x']
                game_helicopter.y = data_user['y']
                game_helicopter.got_rewards = data_user['got_rewards']
                game_helicopter.got_water = data_user['got_water']
                game_helicopter.saved_trees = data_user['saved_trees']
                game_helicopter.upgrade_level = data_user['upgrade_level']
                game_helicopter.lost_hp = data_user['lost_hp']
                game_helicopter.get_hp = data_user['get_hp']

                game_stats = Statistic(WATER, REWARDS, HP)
                game = GameConnector(game_stats, game_map, game_helicopter, game_clouds)
            output = 'user: ' + str(game_helicopter.xy) + '\n' + game.print_all()

            stdscr.refresh()
            sleep(3)
            stdscr.clear()
            stdscr.addstr(output)
            sleep(WAITING)
            stdscr.refresh()

        game_helicopter.processing()
        if TICK % UPDATE_CLOUD == 0:
            game_clouds.update_clouds(TICK // UPDATE_CLOUD)

        if TICK % FRAMES == 0:
            REWARDS.current_value += 1
            game_helicopter.got_rewards += 1
        if TICK % TREE_UPDATE == 0:
            game_map.update_forest()
        if TICK % FIRE_UP_UPDATE == 0:
            game_map.update_fire_up()
        if TICK % FIRE_DOWN_UPDATE == 0:
            game_map.update_fire_down()

        output = 'user: ' + str(game_helicopter.xy) + '\n' + game.print_all()

        stdscr.clear()
        if HP.current_value <= HP.min_value:
            game.lose(f'Ваше здоровье достигло минимума({HP.min_value})')
            game.print_statistic(TICK)
            break
        elif REWARDS.current_value <= REWARDS.min_value:
            game.lose(f'Ваш баланс дошел до минимума({REWARDS.min_value})')
            game.print_statistic(TICK)
            break
        elif REWARDS.current_value >= REWARDS.max_value:
            game.win()
            game.print_statistic(TICK)
            break
        stdscr.addstr(output)
        sleep(WAITING)
        stdscr.refresh()


if __name__ == "__main__":
    wrapper(main)
    print('PRESS ENTER TO EXIT')
    wait(hotkey='enter')
