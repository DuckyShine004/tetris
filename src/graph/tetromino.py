import pygame

from src.utility.utility import Utility
from src.constants.constants import GRAPH_HEIGHT, GRAPH_WIDTH


class Tetromino:
    ROTATION_KEYSTROKES = [pygame.K_COMMA, pygame.K_PERIOD]
    MOVEMENT_KEYSTROKES = [pygame.K_a, pygame.K_d]

    def __init__(self, graph, **kwargs):
        self.graph = graph

        self.positions = kwargs["positions"]
        self.origin = kwargs["origin"]
        self.color = kwargs["color"]

    @staticmethod
    def get_random_tetromino():
        return self()

    def update(self, keystroke):
        if keystroke in Tetromino.ROTATION_KEYSTROKES:
            self.rotate(keystroke)

        if keystroke in Tetromino.MOVEMENT_KEYSTROKES:
            self.move_horizontally(keystroke)

        self.update_graph_cell_colors()

        self.graph.cells[self.origin[0]][self.origin[1]].color = self.color

    def update_graph_cell_colors(self):
        pass

    def rotate(self, keystroke):
        if keystroke == pygame.K_PERIOD:
            self.rotate_clockwise()
        else:
            self.rotate_anti_clockwise()

    def rotate_clockwise(self):
        pass

    def rotate_anti_clockwise(self):
        pass

    def move_horizontally(self, keystroke):
        offset = 0

        if keystroke == pygame.K_a:
            offset = 1
        else:
            offset = -1

        self.origin[0] = Utility.clamp(self.origin[0] + offset, 0, GRAPH_WIDTH - 1)

    def move_vertically(self, keystroke):
        for position in self.positions:
            x, y = position
            position = [x, y + 1]

        self.origin[1] += 1

    def is_next_move_valid(self):
        for position in self.positions:
            if position[1] + 1 >= GRAPH_HEIGHT:
                return False

        return True
