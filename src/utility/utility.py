import random

from src.graph.tetromino import Tetromino

from src.constants.constants import TETROMINO_ARGUMENTS, TETROMINOES


class Utility:
    @staticmethod
    def get_random_tetromino(graph):
        index = random.randint(0, len(TETROMINOES) - 1)
        index = 0

        tetromino = TETROMINOES[index]
        arguments = TETROMINO_ARGUMENTS[tetromino]

        instance = globals()["Tetromino"]

        return instance(graph, **arguments)
