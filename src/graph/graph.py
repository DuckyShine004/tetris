import pygame
import random

from src.graph.cell import Cell

from src.constants.constants import (
    GRAPH_WIDTH,
    GRAPH_HEIGHT,
    MAX_DELAY,
    INITIAL_DELAY,
    CELL_SIZE,
    CELL_OFFSET,
)
from src.utility.utility import Utility


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
        self.delay = INITIAL_DELAY
        self.previous_time = 0
        self.tetromino = None

    def update(self, event):
        self.handle_rotations(event)

        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.previous_time

        if delta_time >= self.delay:
            self.move_piece()
            self.previous_time = current_time

    def handle_rotations(self, event):
        if not self.tetromino:
            return

        if event.type != pygame.KEYDOWN:
            return

        if event.key not in [pygame.K_COMMA, pygame.K_PERIOD]:
            return

        self.tetromino.rotate(event.key == pygame.K_COMMA)

    def move_piece(self):
        if not self.tetromino:
            self.set_random_piece()
            return

        if not self.tetromino.is_next_move_valid():
            self.tetromino = None
            return

        self.tetromino.move()

    def set_random_piece(self):
        self.tetromino = Utility.get_random_tetromino(self)

    def render(self, surface):
        for row in self.cells:
            for cell in row:
                cell.render(surface)
