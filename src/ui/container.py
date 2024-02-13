import pygame

from src.ui.element import Element


class Container(Element):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rect = pygame.Rect(*kwargs["position"], *kwargs["size"])
        self.color = kwargs["color"]
        self.border = kwargs.get("border", [])

    def render(self, surface):
        if not self.border:
            pygame.draw.rect(surface, self.color, self.rect)
            return

        pygame.draw.rect(surface, self.color, self.rect, *self.border)
