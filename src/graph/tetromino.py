import pygame

from src.utility.utility import Utility
from src.constants.constants import GRAPH_HEIGHT, GRAPH_WIDTH, MOVEMENT_DELAY


class Tetromino:
    ROTATION_KEYSTROKES = [pygame.K_COMMA, pygame.K_PERIOD]
    MOVEMENT_KEYSTROKES = [pygame.K_a, pygame.K_d]

    def __init__(self, graph, **kwargs):
        self.graph = graph

        self.positions = kwargs["positions"]
        self.origin = kwargs["origin"]
        self.color = kwargs["color"]

        self.previous_time = 0

    def update(self, keystroke):
        if keystroke in Tetromino.ROTATION_KEYSTROKES:
            self.rotate(keystroke)

        if keystroke in Tetromino.MOVEMENT_KEYSTROKES:
            self.move_horizontally(keystroke)

        self.color_cells()

    def color_cells(self, is_color=True):
        color = self.color if is_color else None

        for x, y in self.positions:
            self.graph.cells[x][y].color = color

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
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.previous_time

        if delta_time < MOVEMENT_DELAY:
            return

        direction = 1 if keystroke == pygame.K_d else -1
        self.color_cells(False)

        for position in self.positions:
            position[0] = Utility.clamp(position[0] + direction, 0, GRAPH_WIDTH - 1)

        self.previous_time = current_time

    def move_vertically(self, keystroke):
        self.color_cells(False)

        for position in self.positions:
            position[1] += 1

    def is_next_move_valid(self):
        for position in self.positions:
            if position[1] + 1 >= GRAPH_HEIGHT:
                return False

        return True
