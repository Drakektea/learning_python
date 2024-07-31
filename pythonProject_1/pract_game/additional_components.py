from enum import StrEnum, unique


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
    STORM = '🌩️'
    FIRE = '🔥'
    WATER = '💧'
