from enum import StrEnum, Enum, unique


@unique
class Cell(StrEnum):
    CLOCKS = '🕛🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚'
    BLOCK = '🚫'
    REWARD = '🏆'
    HP = '⚙️'
    HP_RECOVERY = '🏥'
    SHOP = '🏪'
    HELICOPTER = '🚁'
    EMPTY = '🟩'
    TREE = '🌳'
    RIVER = '🌊'
    CLOUD = '☁️'
    STORM = '⛈️'
    FIRE = '🔥'
    WATER = '💧'


@unique
class WindDirection(Enum):
    NW = (-1, -1)
    N = (0, -1)
    NE = (1, -1)
    E = (1, 0)
    SE = (1, 1)
    S = (0, 1)
    W = (-1, 0)
    SW = (-1, 1)
