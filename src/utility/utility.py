import random

from src.constants.constants import TETROMINO_ARGUMENTS, TETROMINOES


class Utility:
    @staticmethod
    def clamp(value, lower, upper):
        if value < lower:
            return lower

        if value > upper:
            return upper

        return value
