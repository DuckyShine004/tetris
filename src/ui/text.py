import pygame

from src.constants.constants import FONT_SIZE, FONT_COLOR


class Text:
    def __init__(self, **kwargs) -> None:
        self.id = kwargs["id"]
        self.text = kwargs.get("text", "")

        path = kwargs.get("path", None)
        size = kwargs.get("size", FONT_SIZE)

        self.color = kwargs.get("color", FONT_COLOR)
        self.font = pygame.font.Font(path, size)
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect(topleft=kwargs["position"])

    def increment(self):
        self.text = str(int(self.text) + 1)
        self.surface = self.font.render(self.text, True, self.color)

    def render(self, surface):
        surface.blit(self.surface, self.rect)
