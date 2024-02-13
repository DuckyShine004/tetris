"""This module is a way to create a text UI component."""

from typing import List

import pygame

from src.ui.element import Element

from src.constants.constants import (
    DIFFERENCE,
    FONT_SIZE,
    FONT_COLOR,
    MIN_DELAY,
)


class Text(Element):
    """The Text class defines a 'text' UI component.

    Attributes:
        color (list): The component's color.
        font (pygame.Font): The component's font.
        rect (pygame.Rect): The component's hitbox.
        surface (pygame.Surface): The component's surface.
        text (str): The component's text.
    """

    def __init__(self, **kwargs) -> None:
        """Initializes the Text object.

        Args:
            **kwargs: Keyworded, variable-length argument dictionary.
        """

        super().__init__(**kwargs)

        self.text: str = kwargs.get("text", "")

        path: str = kwargs.get("path", None)
        size: int = kwargs.get("size", FONT_SIZE)

        self.color: List[int] = kwargs.get("color", FONT_COLOR)
        self.font: pygame.Font = pygame.font.Font(path, size)
        self.surface: pygame.Surface = self.font.render(self.text, True, self.color)
        self.rect: pygame.Rect = self.surface.get_rect(center=self.position)

    def increment(self, graph, count: int) -> None:
        """Increment the player's current score.

        Args:
            count (int): How much to increment the score count by.
        """

        score = int(self.text)

        if self.is_score_a_mulitple_of_ten(score, count):
            graph.delay = max(MIN_DELAY, graph.delay - DIFFERENCE)

        self.text = str(score + count)
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect()
        self.rect.center = self.position

    def is_score_a_mulitple_of_ten(self, score, count):
        return count >= 10 - (score % 10)

    def render(self, surface: pygame.Surface) -> None:
        """Renders the text component.

        Args:
            surface (pygame.Surface): The display's surface.
        """

        surface.blit(self.surface, self.rect)
