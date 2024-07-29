from typing import Callable

from additional_components import Cell


WAITING = 0.2
TICK = 0

TREE_UPDATE = 5
FIRE_UP_UPDATE = 4
FIRE_DOWN_UPDATE = 3

CLEAR = 'cls'


def is_object(_type: Cell) -> Callable:
    def check_with_type(_object: Cell) -> bool:
        return _object == _type
    return check_with_type


IS_EMPTY = is_object(Cell.EMPTY)
IS_TREE = is_object(Cell.TREE)
IS_WATER = is_object(Cell.WATER)
IS_FIRE = is_object(Cell.FIRE)
