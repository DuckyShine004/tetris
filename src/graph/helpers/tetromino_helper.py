"""This module helps in extracting logic from large classes."""

from typing import TYPE_CHECKING

import pygame

from src.constants.constants import GRAPH_WIDTH, MOVEMENT_DELAY

if TYPE_CHECKING:
    from src.graph.graph import Graph
    from src.graph.tetromino import Tetromino


class TetrominoHelper:
    """This class is used to extract logic from the large classes, 'Graph' and
    'Tetromino'.

    Attributes:
        graph (Graph): The graph object.
        is_rotating_anti_clockwise (bool): Is the current tetromino rotating
        anti-clockwise.
        is_rotating_clockwise (bool): Is the current tetromino rotating
        clockwise.
        previous_time (int): The previous frame before delay.
    """

    def __init__(self, graph: "Graph") -> None:
        """Initializes the TetrominoHelper object.

        Args:
            graph (Graph): The graph object.
        """

        self.graph: "Graph" = graph

        self.is_rotating_clockwise: bool = False
        self.is_rotating_anti_clockwise: bool = False

        self.previous_time: int = 0

    def update(self, tetromino: "Tetromino", keys: pygame.key.ScancodeWrapper) -> None:
        """Updates the current tetromino.

        Args:
            tetromino (Tetromino): The current tetromino.
            keys (pygame.key.ScancodeWrapper): The keystrokes.

        Returns:
            None: Nothing is returned.
        """

        if not tetromino:
            return

        self.rotate(tetromino, keys)

        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.previous_time

        if delta_time < MOVEMENT_DELAY:
            return

        self.move_horizontally(tetromino, keys)
        tetromino.color_cells()

        self.previous_time = current_time

    def rotate(self, tetromino: "Tetromino", keys: pygame.key.ScancodeWrapper) -> None:
        """Rotates the current tetromino clockwise or anti-clockwise, depending
        on the keystroke.

        Args:
            tetromino (Tetromino): The current tetromino.
            keys (pygame.key.ScancodeWrapper): The keystrokes.
        """

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

    def move_horizontally(self, tetromino: "Tetromino", keys: pygame.key.ScancodeWrapper) -> None:
        """Moves the current tetromino horizontally.

        Args:
            tetromino (Tetromino): The current tetromino.
            keys (pygame.key.ScancodeWrapper): The keystrokes.

        Returns:
            None: Nothing is returned.
        """

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

    def is_horizontal_move_valid(self, tetromino: "Tetromino", direction: int) -> bool:
        """Checks whether the queried horizontal movement is valid.

        Args:
            tetromino (Tetromino): The current tetromino.
            direction (int): The direction of movement.

        Returns:
            bool: Is the horizontal move valid.
        """

        for position in tetromino.positions:
            delta = position[0] + direction

            if delta < 0 or delta >= GRAPH_WIDTH:
                return False

            if self.graph.is_cell_occupied(position[1], delta):
                return False

        return True
