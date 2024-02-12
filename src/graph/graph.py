import copy
import pygame
import random
from src.graph.helper import Helper

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
        self.predictions = []
        self.helper = Helper(self)

    def is_cell_occupied(self, row, column):
        return self.cells[column][row].is_occupied

    def set_ghost(self, row, column, is_ghost):
        self.cells[column][row].is_ghost = is_ghost

    def update(self):
        self.handle_tetromino()
        self.helper.set_ghost_positions(self.tetromino)

        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.previous_time

        if delta_time < self.delay:
            return

        if not self.tetromino.move_vertically():
            self.helper.clear_full_rows()
            self.tetromino = None

        self.previous_time = current_time

    def get_prediction(self):
        print(self.tetromino, self.predictions)
        offset = 0

        for dy in range(GRAPH_HEIGHT):
            offset = dy
            is_prediction_found = False

            for position in self.tetromino.positions:
                delta = dy + position[1]

                if delta >= GRAPH_HEIGHT or self.cells[position[0]][delta].is_occupied:
                    is_prediction_found = True
                    break

            if is_prediction_found:
                break

        for x, y in self.predictions:
            self.cells[x][y].is_prediction = False

        self.predictions = [[positions[0], positions[1] + offset - 1] for positions in self.tetromino.positions]

        for x, y in self.predictions:
            self.cells[x][y].is_prediction = True

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

        self.tetromino.update(keys)

    def render(self, surface):
        for y in range(GRAPH_HEIGHT):
            if y <= 3:
                continue

            for x in range(GRAPH_WIDTH):
                self.cells[x][y].render(surface)
