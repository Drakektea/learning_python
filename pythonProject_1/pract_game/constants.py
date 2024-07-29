from typing import Callable

from additional_components import Cell


WAITING = 0.2
TICK = 0

TREE_UPDATE = 5
FIRE_UP_UPDATE = 4
FIRE_DOWN_UPDATE = 3

CLEAR = 'cls'


def IS_OBJECT(_object: Cell) -> Callable:
    def FOR_TYPE(_type: Cell) -> bool:
        return _object == _type
    return FOR_TYPE


IS_EMPTY = IS_OBJECT(Cell.EMPTY)
IS_TREE = IS_OBJECT(Cell.TREE)
IS_WATER = IS_OBJECT(Cell.WATER)
IS_FIRE = IS_OBJECT(Cell.FIRE)
