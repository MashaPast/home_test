from enum import Enum


class AvailableColors(Enum):
    default_color = 0
    white = 1
    black = 2
    red = 3
    yellow = 4
    orange = 5
    green = 6
    blue = 7
    purple = 8
    pink = 9
    brown = 10
    grey = 11


available_colors_names = tuple(AvailableColors.__members__.keys())
