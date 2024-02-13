"""This module is a way to create a container UI component."""

import pygame

from src.ui.element import Element


class Image(Element):
    """The image class defines a 'image' UI component.


    Attributes:
        image (pygame.Surface): The image of the component.
        rect (pygame.Rect): The hitbox of the component.
    """

    def __init__(self, **kwargs) -> None:
        """Initializes the Image object.

        Args:
            **kwargs: Keyworded, variable-length argument dictionary.
        """

        super().__init__(**kwargs)

        self.image: pygame.Surface = pygame.image.load(kwargs["image"])
        self.image: pygame.Surface = pygame.transform.scale(self.image, kwargs["size"])

        if kwargs["topleft"]:
            self.rect: pygame.Rect = self.image.get_rect(topleft=kwargs["position"])
        else:
            self.rect: pygame.Rect = self.image.get_rect(center=kwargs["position"])

    def render(self, surface: pygame.Surface) -> None:
        """Renders the image component.

        Args:
            surface (pygame.Surface): The display's surface.
        """

        surface.blit(self.image, self.rect)
