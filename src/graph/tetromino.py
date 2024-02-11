import pygame

from src.constants.constants import (
    GRAPH_HEIGHT,
    GRAPH_WIDTH,
    MOVEMENT_DELAY,
)


class Tetromino:
    def __init__(self, graph, **kwargs):
        self.graph = graph

        self.positions = kwargs["positions"]
        self.origin = kwargs["origin"]
        self.color = kwargs["color"]

        self.is_rotating_clockwise = False
        self.is_rotating_anti_clockwise = False

        self.previous_time = 0

    def update(self):
        self.rotate()

        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.previous_time

        if delta_time < MOVEMENT_DELAY:
            return

        self.move_horizontally()
        self.color_cells()

        self.previous_time = current_time

    def color_cells(self, is_color=True):
        color = self.color if is_color else None

        for x, y in self.positions:
            self.graph.cells[x][y].color = color

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
        pivot = self.positions[self.origin]
        rotations = []

        for position in self.positions:
            x = sum(pivot) - position[1]
            y = position[0] + pivot[1] - pivot[0]
            rotation = [x, y]

            if not self.is_valid_rotation(rotation):
                return

            rotations.append(rotation)

        self.color_cells(False)
        self.positions = list(rotations)

    def rotate_anti_clockwise(self):
        pivot = self.positions[self.origin]
        rotations = []

        for position in self.positions:
            x = position[1] + pivot[0] - pivot[1]
            y = sum(pivot) - position[0]
            rotation = [x, y]

            if not self.is_valid_rotation(rotation):
                return

            rotations.append(rotation)

        self.color_cells(False)
        self.positions = list(rotations)

    def is_valid_rotation(self, rotation):
        x, y = rotation

        if x < 0 or x >= GRAPH_WIDTH:
            return False

        if y < 0 or y >= GRAPH_HEIGHT:
            return False

        return True

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
        self.color_cells(False)

        for position in self.positions:
            position[1] += 1

    def is_horizontal_move_valid(self, direction):
        for position in self.positions:
            delta = position[0] + direction

            if delta < 0 or delta >= GRAPH_WIDTH:
                return False

        return True

    def is_next_vertical_move_valid(self):
        for position in self.positions:
            if position[1] == GRAPH_HEIGHT - 1:
                return False

        return True
