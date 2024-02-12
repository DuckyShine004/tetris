import pygame

from src.constants.constants import (
    CELL_SIZE,
    BORDER_SIZE,
    OUTLINE,
    PREDICTION,
)


class Cell:
    def __init__(self, x, y, color=None, is_moving=False):
        self.rect = pygame.Rect(x, y, *CELL_SIZE)
        self.color = color
        self.is_moving = is_moving
        self.is_prediction = False
        self.is_occupied = False

    def render(self, surface):
        if self.is_prediction:
            pygame.draw.rect(surface, PREDICTION, self.rect, 2, BORDER_SIZE)
        if not self.color:
            return

        pygame.draw.rect(surface, self.color, self.rect, 0, BORDER_SIZE)
        pygame.draw.rect(surface, OUTLINE, self.rect, 2, BORDER_SIZE)
