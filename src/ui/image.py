from typing import List

import pygame

from src.ui.element import Element


class Image(Element):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.image = pygame.image.load(kwargs["image"])
        self.image = pygame.transform.scale(self.image, kwargs["size"])

        if kwargs["topleft"]:
            self.rect = self.image.get_rect(topleft=kwargs["position"])
        else:
            self.rect = self.image.get_rect(center=kwargs["position"])

    def render(self, surface):
        surface.blit(self.image, self.rect)
