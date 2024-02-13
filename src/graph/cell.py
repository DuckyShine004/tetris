"""The Cell module is a datastructure that makes up a graph."""

from typing import List, Optional

import pygame

from src.constants.constants import (
    CELL_SIZE,
    BORDER_SIZE,
    OUTLINE,
    PREDICTION,
)


class Cell:
    """The Cell class is a datastructure that makes up the definition of a graph.

    Attributes:
        color (list): The color of the cell.
        is_ghost (bool): Is the current cell occupied by a ghost tetromino.
        is_moving (bool): Is the cell moving.
        is_occupied (bool): Is the current cell occupied.
        rect (pygame.Rect): The hitbox of the cell.
    """

    def __init__(
        self,
        x: int,
        y: int,
        color: Optional[List[int]] = None,
        is_moving: Optional[bool] = False,
    ) -> None:
        """Initializes the cell object.

        Args:
            x (int): The x coordinate of the cell.
            y (int): The y coordinate of the cell.
            color (list, optional): The color of the cell.
            is_moving (bool, optional): Is the cell moving.
        """

        self.rect: pygame.Rect = pygame.Rect(x, y, *CELL_SIZE)
        self.color: Optional[List[int]] = color
        self.is_moving: Optional[bool] = is_moving
        self.is_ghost: bool = False
        self.is_occupied: bool = False

    def render(self, surface: pygame.Surface) -> None:
        """Conditionally render the cell.

        Args:
            surface (pygame.Surface): The display surface.

        Returns:
            None: Nothing is returned.
        """

        if self.is_ghost:
            pygame.draw.rect(surface, PREDICTION, self.rect, 2, BORDER_SIZE)

        if not self.color:
            return

        pygame.draw.rect(surface, self.color, self.rect, 0, BORDER_SIZE)
        pygame.draw.rect(surface, OUTLINE, self.rect, 2, BORDER_SIZE)
