import json


def import_game(filename='game_save.json', addstr=None):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        if addstr:
            addstr('СОХРАНЕНИЕ НАЙДЕНО')
        else:
            print('СОХРАНЕНИЕ НАЙДЕНО')
        return data
    except FileNotFoundError:
        if addstr:
            addstr("СОХРАНЕНИЯ НЕ НАШЛОСЬ")
        else:
            print("СОХРАНЕНИЯ НЕ НАШЛОСЬ")
    except:
        if addstr:
            addstr("ОШИБКА ЧТЕНИЯ ФАЙЛА СОХРАНЕНИЯ")
        else:
            print("ОШИБКА ЧТЕНИЯ ФАЙЛА СОХРАНЕНИЯ")
