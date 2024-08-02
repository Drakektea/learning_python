import json


def export_game(game_connector, tick, filename='game_save.json', addstr=None):
    try:
        data = {
            'tick': tick,
            'clouds': game_connector.clouds.export_data(),
            'map': game_connector.map.export_data(),
            'helicopter': game_connector.helicopter.export_data(),
        }
        with open(filename, 'w+') as f:
            json.dump(data, f)
        if addstr:
            addstr('ИГРА СОХРАНЕНА')
        else:
            print('ИГРА СОХРАНЕНА')
    except Exception as e:
        if addstr:
            addstr('ИГРА НЕ БЫЛА СОХРАНЕНА' + '\n' + f'{e}')
        else:
            print('ИГРА НЕ БЫЛА СОХРАНЕНА')
