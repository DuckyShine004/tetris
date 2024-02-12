import pygame

from src.constants.constants import GRAPH_HEIGHT, GRAPH_WIDTH, MOVEMENT_DELAY


class TetrominoHelper:
    def __init__(self, graph):
        self.graph = graph

        self.is_rotating_clockwise = False
        self.is_rotating_anti_clockwise = False

        self.previous_time = 0

    def update(self, tetromino, keys):
        self.rotate(tetromino, keys)

        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.previous_time

        if delta_time < MOVEMENT_DELAY:
            return

        self.move_horizontally(tetromino, keys)
        tetromino.color_cells()

        self.previous_time = current_time

    def rotate(self, tetromino, keys):
        if keys[pygame.K_PERIOD] and not self.is_rotating_clockwise:
            tetromino.rotate_clockwise()
            self.is_rotating_clockwise = True
        elif not keys[pygame.K_PERIOD]:
            self.is_rotating_clockwise = False

        if keys[pygame.K_COMMA] and not self.is_rotating_anti_clockwise:
            tetromino.rotate_anti_clockwise()
            self.is_rotating_anti_clockwise = True
        elif not keys[pygame.K_COMMA]:
            self.is_rotating_anti_clockwise = False

    def move_horizontally(self, tetromino, keys):
        direction = 0

        if keys[pygame.K_a]:
            direction = -1

        if keys[pygame.K_d]:
            direction = 1

        if not self.is_horizontal_move_valid(tetromino, direction):
            return

        tetromino.color_cells(False)

        for position in tetromino.positions:
            position[0] += direction

    def is_horizontal_move_valid(self, tetromino, direction):
        for position in tetromino.positions:
            delta = position[0] + direction

            if delta < 0 or delta >= GRAPH_WIDTH:
                return False

            if self.graph.is_cell_occupied(position[1], delta):
                return False

        return True

    def is_vertical_move_valid(self, tetromino):
        for position in tetromino.positions:
            delta = position[1] + 1

            if delta >= GRAPH_HEIGHT:
                return False

            if self.graph.is_cell_occupied(delta, position[0]):
                return False

        return True
