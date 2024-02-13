import pygame

from src.ui.element import Element

from src.constants.constants import FONT_SIZE, FONT_COLOR


class Text(Element):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.text = kwargs.get("text", "")

        path = kwargs.get("path", None)
        size = kwargs.get("size", FONT_SIZE)

        self.color = kwargs.get("color", FONT_COLOR)
        self.font = pygame.font.Font(path, size)
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect(center=self.position)

    def increment(self, count):
        self.text = str(int(self.text) + count)
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect()
        self.rect.center = self.position

    def render(self, surface):
        surface.blit(self.surface, self.rect)
