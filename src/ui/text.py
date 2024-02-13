import pygame

from src.constants.constants import FONT_SIZE, FONT_COLOR


class Text:
    def __init__(self, **kwargs) -> None:
        self.text: str = kwargs.get("text", "")

        path = kwargs["path"]
        size = kwargs.get("size", FONT_SIZE)
        color = kwargs.get("color", FONT_COLOR)
        font = pygame.font.Font(path, size)

        self.surface = font.render(self.text, True, color)
        self.rect = self.surface.get_rect(topleft=kwargs["position"])

    def render(self, surface):
        surface.blit(self.surface, self.rect)
