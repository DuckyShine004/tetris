import copy
import pygame
import random

from src.graph.helpers.graph_helper import GraphHelper
from src.graph.helpers.tetromino_helper import TetrominoHelper

from src.graph.cell import Cell
from src.graph.tetromino import Tetromino

from src.constants.constants import (
    GRAPH_WIDTH,
    GRAPH_HEIGHT,
    MAX_DELAY,
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

        self.graph_helper = GraphHelper(self)
        self.tetromino_helper = TetrominoHelper(self)

    def update(self):
        self.handle_tetromino()

        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.previous_time

        if delta_time < self.delay:
            return

        if not self.tetromino.move_vertically():
            self.graph_helper.clear_full_rows()
            self.tetromino = None

        self.previous_time = current_time

    def is_cell_occupied(self, row, column):
        return self.cells[column][row].is_occupied

    def set_occupied(self, row, column, is_occupied):
        self.cells[column][row].is_occupied = is_occupied

    def set_ghost(self, row, column, is_ghost):
        self.cells[column][row].is_ghost = is_ghost

    def set_color(self, row, column, color):
        self.cells[column][row].color = color

    def set_tetromino(self):
        index = random.randint(0, len(TETROMINOES) - 1)
        tetromino = TETROMINOES[index]
        arguments = copy.deepcopy(TETROMINO_ARGUMENTS[tetromino])

        self.tetromino = Tetromino(self, **arguments)

    def handle_tetromino(self):
        if not self.tetromino:
            self.set_tetromino()
            return

        keys = pygame.key.get_pressed()

        self.graph_helper.update(self.tetromino, keys)
        # self.tetromino_helper.update(self.tetromino, keys)

        self.tetromino.update(keys)

    def render(self, surface):
        for y in range(GRAPH_HEIGHT):
            if y <= 3:
                continue

            for x in range(GRAPH_WIDTH):
                self.cells[x][y].render(surface)
