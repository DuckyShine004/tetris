"""This module is a way to create a container UI component."""

from typing import List

import pygame

from src.ui.element import Element


class Container(Element):
    """The container class defines a 'container' UI component.

    Attributes:
        border (list): The component's border arguments.
        color (list): The component's color.
        rect (pygame.Rect): The component's hitbox.
    """

    def __init__(self, **kwargs) -> None:
        """Initializes the Container object.

        Args:
            **kwargs: Keyworded, variable-length argument dictionary.
        """

        super().__init__(**kwargs)

        self.rect: pygame.Rect = pygame.Rect(*kwargs["position"], *kwargs["size"])
        self.color: List[int] = kwargs["color"]
        self.border: List[int] = kwargs.get("border", [])

    def render(self, surface: pygame.Surface) -> None:
        """Renders the container component.

        Args:
            surface (pygame.Surface): The display's surface.

        Returns:
            None: Nothing is returned.
        """

        if not self.border:
            pygame.draw.rect(surface, self.color, self.rect)
            return

        pygame.draw.rect(surface, self.color, self.rect, *self.border)
