from typing import Callable

from additional_components import Cell
from stats import Item


FRAMES = 30
WAITING = 1 / FRAMES
OFFSET = 1 / 1_000_000

SAVE_TREE_BONUS = 100
BURN_TREE_PENALTY = -50
UPGRADE_COST = 500
SHOP_WAITING_SECONDS = 10
HP_COST = 20

HP_COUNT = 5
DAMAGE = 1

TREE_UPDATE = 4
FIRE_UP_UPDATE = 12
FIRE_DOWN_UPDATE = 8
UPDATE_CLOUD = FRAMES // 2

WATER = Item(Cell.WATER, 5)
REWARDS = Item(Cell.REWARD, 10000, -2000)
HP = Item(Cell.HP, 20, 0, 20)

CLEAR = 'cls'


def is_object(_type: Cell) -> Callable:
    def check_with_type(_object: Cell) -> bool:
        return _object == _type
    return check_with_type


IS_EMPTY = is_object(Cell.EMPTY)
IS_TREE = is_object(Cell.TREE)
IS_RIVER = is_object(Cell.RIVER)
IS_FIRE = is_object(Cell.FIRE)
IS_SHOP = is_object(Cell.SHOP)
IS_STORMCLOUD = is_object(Cell.STORM)
IS_HP_RECOVERY = is_object(Cell.HP_RECOVERY)
