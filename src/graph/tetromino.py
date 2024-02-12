"""This module defines the tetromino object."""

from typing import TYPE_CHECKING, List, Optional

from src.utility.utility import Utility

from src.constants.constants import GRAPH_HEIGHT

if TYPE_CHECKING:
    from src.graph.graph import Graph


class Tetromino:
    """The tetromino class defines the structure of a tetromino, but also
    contains useful methods that alters the application states.

    Attributes:
        color (list): The color of the tetromino.
        graph (Graph): The graph object.
        origin (int): The tetromino's origin position.
        positions (list): The positions of the tetromino cells.
    """

    def __init__(self, graph: "Graph", **kwargs) -> None:
        """Initializes the tetromino object.

        Args:
            graph (Graph): The graph object.
            **kwargs: Keyworded, variable-length argument dictionary.
        """

        self.graph: "Graph" = graph

        self.positions: List[int] = kwargs["positions"]
        self.origin: int = kwargs["origin"]
        self.color: List[int] = kwargs["color"]

    def occupy_cells(self, is_occupied: bool) -> None:
        """Change the occupation status of cells based on the current cells occupied
        by the current tetromino and the input boolean value.

        Args:
            is_occupied (bool): Should the cells be occupied.
        """

        for x, y in self.positions:
            self.graph.set_occupied(y, x, is_occupied)

    def color_cells(self, is_color: Optional[bool] = True) -> None:
        """Color in cells occupied by the current tetromino, depending on
        the input boolean value.

        Args:
            is_color (bool, optional): Should the cells be colored.
        """

        color = self.color if is_color else None

        for x, y in self.positions:
            self.graph.set_color(y, x, color)

    def rotate_clockwise(self) -> None:
        """Rotate the current tetromino clockwise.

        Returns:
            None: Nothing is returned.
        """

        rotations = Utility.get_clockwise_rotations(self, self.graph)

        if not rotations:
            return

        self.color_cells(False)
        self.positions = list(rotations)

    def rotate_anti_clockwise(self) -> None:
        """Rotate the current tetromino anti-clockwise.

        Returns:
            None: Nothing is returned.
        """

        rotations = Utility.get_anti_clockwise_rotations(self, self.graph)

        if not rotations:
            return

        self.color_cells(False)
        self.positions = list(rotations)

    def move_vertically(self) -> bool:
        """Move the current tetromino until it cannot move anymore.

        Returns:
            bool: Returns if the vertical move is valid or not.
        """

        self.color_cells()

        if not self.is_vertical_move_valid():
            self.occupy_cells(True)
            return False

        self.color_cells(False)

        for position in self.positions:
            position[1] += 1

        return True

    def is_vertical_move_valid(self) -> bool:
        """Returns if the vertical move is valid or not. The tetromino
        will not be able to move anymore if it has reached the bottom of the
        graph or it has collided with an occupied cell.

        Returns:
            bool: Is the vertical move valid.
        """

        for position in self.positions:
            delta = position[1] + 1

            if delta >= GRAPH_HEIGHT:
                return False

            if self.graph.is_cell_occupied(delta, position[0]):
                return False

        return True
