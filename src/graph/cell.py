import pygame

from src.constants.constants import CELL_SIZE


class Cell:
    def __init__(self, x, y, color=None, is_moving=False):
        self.rect = pygame.Rect(x, y, *CELL_SIZE)
        self.color = color
        self.is_moving = is_moving

    def render(self, surface):
        if not self.color:
            return

        pygame.draw.rect(surface, self.color, self.rect)
