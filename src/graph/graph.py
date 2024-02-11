import pygame
import random

from src.graph.cell import Cell
from src.graph.tetromino import Tetromino

from src.constants.constants import (
    GRAPH_WIDTH,
    GRAPH_HEIGHT,
    MAX_DELAY,
    INITIAL_DELAY,
    CELL_SIZE,
    CELL_OFFSET,
    TETROMINOES,
    TETROMINO_ARGUMENTS,
)


class Graph:
    def __init__(self):
        self.cells = [
            [
                Cell(
                    x * CELL_SIZE[0] + CELL_OFFSET[0],
                    y * CELL_SIZE[1] + CELL_OFFSET[1],
                )
                for y in range(GRAPH_HEIGHT)
            ]
            for x in range(GRAPH_WIDTH)
        ]

        self.max_delay = MAX_DELAY
        self.delay = MAX_DELAY
        self.previous_time = 0
        self.tetromino = None

    def update(self, keystroke):
        self.handle_tetromino(keystroke)

        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.previous_time

        if delta_time < self.delay:
            return

        self.tetromino.move_vertically()
        self.previous_time = current_time

    def set_tetromino(self):
        index = random.randint(0, len(TETROMINOES) - 1)
        index = 0

        tetromino = TETROMINOES[index]
        arguments = TETROMINO_ARGUMENTS[tetromino]

        self.tetromino = Tetromino(self, **arguments)

    def handle_tetromino(self, keystroke):
        if not self.tetromino:
            self.set_tetromino()
            return

        self.tetromino.update(keystroke)

    def render(self, surface):
        for row in self.cells:
            for cell in row:
                cell.render(surface)
