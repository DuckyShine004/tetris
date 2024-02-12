import copy
import pygame
import random

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

    def update(self):
        self.handle_tetromino()

        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.previous_time

        if delta_time < self.delay:
            return

        if not self.tetromino.move_vertically():
            self.handle_row_deletion()
            self.tetromino = None

        self.previous_time = current_time

    def set_tetromino(self):
        index = random.randint(0, len(TETROMINOES) - 1)
        tetromino = TETROMINOES[index]
        arguments = copy.deepcopy(TETROMINO_ARGUMENTS[tetromino])

        self.tetromino = Tetromino(self, **arguments)

    def handle_tetromino(self):
        if not self.tetromino:
            self.set_tetromino()
            return

        self.tetromino.update()

    def handle_row_deletion(self):
        rows = []

        for row in range(GRAPH_HEIGHT):
            is_row_full = True

            for column in range(GRAPH_WIDTH):
                if not self.cells[column][row].is_occupied:
                    is_row_full = False
                    break

            if is_row_full:
                rows.append(row)

        if not rows:
            return

        self.delete_rows(rows)
        self.make_cells_fall(rows[0], len(rows))

    def make_cells_fall(self, first_row, falling_height):
        for row in range(first_row - 1, -1, -1):
            for column in range(GRAPH_WIDTH):
                if not self.cells[column][row].is_occupied:
                    continue

                color = self.cells[column][row].color

                self.cells[column][row + falling_height].color = color
                self.cells[column][row + falling_height].is_occupied = True

                self.cells[column][row].color = None
                self.cells[column][row].is_occupied = False

    def delete_rows(self, rows):
        for row in rows:
            for column in range(GRAPH_WIDTH):
                self.cells[column][row].is_occupied = False
                self.cells[column][row].color = None

    def render(self, surface):
        for row in self.cells:
            for cell in row:
                cell.render(surface)
