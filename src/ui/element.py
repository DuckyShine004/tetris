"""This module is an abstract parent class for UI components."""

from abc import ABC, abstractmethod


class Element(ABC):

    """Summary

    Attributes:
        id (TYPE): Description
        position (TYPE): Description
        z_buffer (TYPE): Description
    """

    def __init__(self, **kwargs) -> None:
        """Summary

        Args:
            **kwargs: Description
        """
        self.id = kwargs.get("id", "")
        self.position = kwargs["position"]
        self.z_buffer = kwargs["z-buffer"]

    @abstractmethod
    def render(self, surface):
        """Summary

        Args:
            surface (TYPE): Description
        """
        pass
