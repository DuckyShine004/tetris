"""This module allows for a graph datastructure."""

from typing import TYPE_CHECKING, List, Optional

import copy
import random
import pygame

from src.graph.cell import Cell
from src.graph.tetromino import Tetromino

from src.graph.helpers.graph_helper import GraphHelper
from src.graph.helpers.tetromino_helper import TetrominoHelper

from src.constants.constants import (
    GRAPH_WIDTH,
    GRAPH_HEIGHT,
    START_HEIGHT,
    MAX_DELAY,
    CELL_SIZE,
    CELL_OFFSET,
    TETROMINOES,
    TETROMINO_ARGUMENTS,
)


class Graph:
    """The Graph datastructure allows me to create Tetris using a cell-based
    approach.

    Attributes:
        cells (list): List of graph cells.
        delay (int): The vertical movement delay.
        graph_helper (GraphHelper): The GraphHelper object.
        max_delay (int): The maximum delay of vertical movement.
        previous_time (int): The previous frame.
        tetromino (Tetromino): The tetromino object.
        tetromino_helper (TetrominoHelper): The TetrominoHelper object.
    """

    def __init__(self):
        """Initializes the graph object."""

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

        self.max_delay: int = MAX_DELAY
        self.delay: int = MAX_DELAY
        self.previous_time: int = 0
        self.tetromino: Optional[Tetromino] = None

        self.graph_helper: GraphHelper = GraphHelper(self)
        self.tetromino_helper: TetrominoHelper = TetrominoHelper(self)

    def update(self) -> None:
        """Updates the graph.

        Returns:
            None: Nothing is returned.
        """

        self.handle_tetromino()

        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.previous_time

        if delta_time < self.delay:
            return

        if not self.tetromino.move_vertically():
            self.graph_helper.clear_full_rows()
            self.tetromino = None

        self.previous_time = current_time

    def is_cell_occupied(self, row: int, column: int) -> bool:
        """Returns if the queried cell is occupied or not.

        Args:
            row (int): The queried row.
            column (int): The queried column.

        Returns:
            bool: Is the queried cell occupied.
        """

        return self.cells[column][row].is_occupied

    def set_occupied(self, row: int, column: int, is_occupied: bool) -> None:
        """Set the queried cell's occupation status to the input occupation
        status.

        Args:
            row (int): The queried row.
            column (int): The queried column.
            is_occupied (bool): The boolean value to be set.
        """

        self.cells[column][row].is_occupied = is_occupied

    def set_ghost(self, row: int, column: int, is_ghost: bool) -> None:
        """Set the queried cell's is_ghost status to the input is_ghost status.

        Args:
            row (int): The queried row.
            column (int): The queried column.
            is_ghost (bool): The boolean value to be set.
        """

        self.cells[column][row].is_ghost = is_ghost

    def set_color(self, row: int, column: int, color: Optional[List[int]]) -> None:
        """Set the queried cell's color to the input color.

        Args:
            row (int): The queried row.
            column (int): The queried column.
            color (Optional[List[int]]): The color to be set.
        """

        self.cells[column][row].color = color

    def set_tetromino(self) -> None:
        """Create and set a new tetromino."""

        index = random.randint(0, len(TETROMINOES) - 1)
        tetromino = TETROMINOES[index]
        arguments = copy.deepcopy(TETROMINO_ARGUMENTS[tetromino])

        self.tetromino = Tetromino(self, **arguments)

    def handle_tetromino(self) -> None:
        """Handle the current tetromino. If there is no tetromino, create one.

        Returns:
            None: Nothing is returned.
        """

        if not self.tetromino:
            self.set_tetromino()
            return

        keys = pygame.key.get_pressed()

        self.graph_helper.update(self.tetromino, keys)
        self.tetromino_helper.update(self.tetromino, keys)

    def render(self, surface: pygame.Surface) -> None:
        """Renders the graph.

        Args:
            surface (pygame.Surface): The display surface.
        """

        for y in range(GRAPH_HEIGHT):
            if y <= START_HEIGHT:
                continue

            for x in range(GRAPH_WIDTH):
                self.cells[x][y].render(surface)
