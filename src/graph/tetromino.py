import pygame

from src.constants.constants import (
    GRAPH_HEIGHT,
    GRAPH_WIDTH,
    MOVEMENT_DELAY,
)
from src.utility.utility import Utility


class Tetromino:
    def __init__(self, graph, **kwargs):
        self.graph = graph

        self.positions = kwargs["positions"]
        self.origin = kwargs["origin"]
        self.color = kwargs["color"]

        self.is_rotating_clockwise = False
        self.is_rotating_anti_clockwise = False

        self.previous_time = 0

    def update(self, keys):
        self.rotate()

        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.previous_time

        if delta_time < MOVEMENT_DELAY:
            return

        self.move_horizontally()
        self.color_cells()

        self.previous_time = current_time

    def occupy_cells(self):
        for x, y in self.positions:
            self.graph.set_occupied(y, x, True)

    def color_cells(self, is_color=True):
        color = self.color if is_color else None

        for x, y in self.positions:
            self.graph.set_color(y, x, color)

    def rotate(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_PERIOD] and not self.is_rotating_clockwise:
            self.rotate_clockwise()
            self.is_rotating_clockwise = True
        elif not keys[pygame.K_PERIOD]:
            self.is_rotating_clockwise = False

        if keys[pygame.K_COMMA] and not self.is_rotating_anti_clockwise:
            self.rotate_anti_clockwise()
            self.is_rotating_anti_clockwise = True
        elif not keys[pygame.K_COMMA]:
            self.is_rotating_anti_clockwise = False

    def rotate_clockwise(self):
        rotations = Utility.get_clockwise_rotations(self, self.graph)

        if not rotations:
            return

        self.color_cells(False)
        self.positions = list(rotations)

    def rotate_anti_clockwise(self):
        rotations = Utility.get_anti_clockwise_rotations(self, self.graph)

        if not rotations:
            return

        self.color_cells(False)
        self.positions = list(rotations)

    def move_horizontally(self):
        keys = pygame.key.get_pressed()
        direction = 0

        if keys[pygame.K_a]:
            direction = -1

        if keys[pygame.K_d]:
            direction = 1

        if not self.is_horizontal_move_valid(direction):
            return

        self.color_cells(False)

        for position in self.positions:
            position[0] += direction

    def move_vertically(self):
        self.color_cells()

        if not self.is_next_vertical_move_valid():
            return False

        self.color_cells(False)

        for position in self.positions:
            position[1] += 1

        return True

    def is_horizontal_move_valid(self, direction):
        for position in self.positions:
            delta = position[0] + direction

            if delta < 0 or delta >= GRAPH_WIDTH:
                return False

            if self.graph.cells[delta][position[1]].is_occupied:
                return False

        return True

    def is_next_vertical_move_valid(self):
        is_vertical_move_valid = True

        for position in self.positions:
            delta = position[1] + 1

            if delta < GRAPH_HEIGHT and not self.graph.cells[position[0]][delta].is_occupied:
                continue

            is_vertical_move_valid = False
            break

        if is_vertical_move_valid:
            return True

        # If not valid, then set the occupancies
        for position in self.positions:
            x, y = position
            self.graph.cells[x][y].is_occupied = True

        return False
