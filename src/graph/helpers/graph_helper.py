"""This module helps in extracting logic from large classes."""

from typing import TYPE_CHECKING, List

import pygame

from src.constants.constants import GRAPH_HEIGHT, GRAPH_WIDTH

if TYPE_CHECKING:
    from src.graph.graph import Graph
    from src.graph.tetromino import Tetromino


class GraphHelper:
    """This class is used to extract logic from the large classes, 'Graph' and
    'Tetromino'.

    Attributes:
        ghost_positions (list): List of ghost positions.
        graph (Graph): The graph object.
    """

    def __init__(self, graph: "Graph", ui) -> None:
        """Initializes the GraphHelper object.

        Args:
            graph (Graph): The graph object.
        """

        self.ui = ui
        self.graph: "Graph" = graph
        self.is_moving_to_ghost_position = False
        self.ghost_positions: List[List[int]] = []

    def update(self, tetromino: "Tetromino", keys: pygame.key.ScancodeWrapper) -> None:
        """Helps with updating the graph and tetromino. This is all to extract
        from the large graph and tetromino classes.

        Args:
            tetromino (Tetromino): The current tetromino.
            keys (pygame.key.ScancodeWrapper): The keystroke.
        """

        self.set_ghost_positions(tetromino)

        if keys[pygame.K_s] and not self.is_moving_to_ghost_position:
            self.move_to_ghost_positions(tetromino)
        elif not keys[pygame.K_s]:
            self.is_moving_to_ghost_position = False

    def set_ghost_positions(self, tetromino: "Tetromino") -> None:
        """Calculate and set the ghost tetromino positions.

        Args:
            tetromino (Tetromino): The current tetromino.
        """

        height = 0

        for offset_y in range(GRAPH_HEIGHT):
            height = offset_y
            is_collision = False

            for position in tetromino.positions:
                delta = offset_y + position[1]

                if delta >= GRAPH_HEIGHT or self.graph.is_cell_occupied(delta, position[0]):
                    is_collision = True
                    break

            if is_collision:
                break

        self.set_new_ghost_positions(tetromino.positions, height)

    def set_new_ghost_positions(self, positions: List[List[int]], height: int) -> None:
        """Calculate and set the next ghost tetromino position.

        Args:
            positions (List[List[int]]): The current free-falling tetromino positions.
            height (int): The drop distance.
        """

        self.clear_ghost_positions()

        for x, y in positions:
            delta = y + height - 1
            self.ghost_positions.append([x, delta])
            self.graph.set_ghost(delta, x, True)

    def set_falling_cell_positions(self, row: int, column: int, height: int) -> None:
        """Calculate and set the new positions of the cells, i.e. make the cells
        fall into a new position after removal.

        Args:
            row (int): The current row.
            column (int): The current column.
            height (int): The height of the number of rows removed.
        """

        color = self.graph.cells[column][row].color
        delta = row + height

        self.graph.cells[column][delta].color = color
        self.graph.cells[column][row].color = None
        self.graph.cells[column][delta].is_occupied = True
        self.graph.cells[column][row].is_occupied = False

    def clear_ghost_positions(self) -> None:
        """Clears the current ghost position."""

        for x, y in self.ghost_positions:
            self.graph.set_ghost(y, x, False)

        self.ghost_positions.clear()

    def clear_full_rows(self) -> None:
        """Clear and remove all full rows. A full row is a row that is
        occupied by tetrominoes.

        Returns:
            None: Nothing is returned
        """

        rows = []

        for row in range(GRAPH_HEIGHT):
            if all(self.graph.is_cell_occupied(row, column) for column in range(GRAPH_WIDTH)):
                rows.append(row)

        if not rows:
            return

        self.move_cells_down(rows)

    def clear_rows(self, rows: List[int]) -> None:
        """Clear all rows that are in the rows list.

        Args:
            rows (List[int]): The rows to be removed.
        """

        for row in rows:
            for column in range(GRAPH_WIDTH):
                self.graph.set_occupied(row, column, False)
                self.graph.set_color(row, column, None)

    def move_to_ghost_positions(self, tetromino):
        tetromino.color_cells(False)
        tetromino.positions = list(self.ghost_positions)
        self.is_moving_to_ghost_position = True
        self.clear_ghost_positions()

    def move_cells_down(self, rows: List[int]) -> None:
        """Move all the cells down after clearing all full rows.

        Args:
            rows (List[int]): The rows to be removed.
        """

        self.clear_rows(rows)

        start = rows[0]
        height = len(rows)

        self.ui.increment_score(self.graph, height)

        for row in range(start - 1, -1, -1):
            for column in range(GRAPH_WIDTH):
                if not self.graph.is_cell_occupied(row, column):
                    continue

                self.set_falling_cell_positions(row, column, height)
