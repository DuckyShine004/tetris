"""This module is an abstract parent class for UI components.
"""

from abc import ABC, abstractmethod

from typing import List

import pygame


class Element(ABC):
    """The Element class removes redundant assignments, and unifies all child
    components under on parent class.

    Deleted Attributes:
        id (str): The component's identifier.
        position (list): The component's position.
        z_buffer (int): The component's z-buffer.
    """

    def __init__(self, **kwargs) -> None:
        """Initializes the Element class.

        Args:
            **kwargs: Keyworded, variable-length argument dictionary.
        """

        self.id: str = kwargs.get("id", "")
        self.position: List[int] = kwargs["position"]
        self.z_buffer: int = kwargs["z-buffer"]

    @abstractmethod
    def render(self, surface: pygame.Surface) -> None:
        """Renders UI components.

        Args:
            surface (pygame.Surface): The display's surface.

        Returns:
            None: Nothing is returned.
        """

        return
