"""This module is useful for loading user interfaces."""

from typing import TYPE_CHECKING, List, Dict, Any

import pygame

from src.ui.element import Element
from src.ui.container import Container
from src.ui.image import Image
from src.ui.text import Text

from src.utility.utility import Utility

from src.constants.constants import SCORE_ID

if TYPE_CHECKING:
    from src.graph.graph import Graph


class UI:
    """The UI class defines the user interface. The user interface can be loaded
    by specifying a path to a JSON file.

    Deleted Attributes:
        data (dict): The loaded JSON data.
        elements (list): List of elements that make up the user interface.
    """

    def __init__(self, path: str) -> None:
        """Initializes the user interface.

        Args:
            path (str): The path to the JSON file.
        """

        self.data: Dict[str, Any] = Utility.get_json_data(path)
        self.elements: List[Element] = []

        self.initialize()

    def initialize(self) -> None:
        """Initializes the components of the user interface."""

        for elements in self.data.keys():
            self.create_elements(elements)

    def create_elements(self, elements: str) -> None:
        """Create elements. Elements will be created based on the contents
        of the JSON data.

        Args:
            elements (str): List of elements loaded from the JSON file.
        """

        match elements:
            case "containers":
                self.create_containers()
            case "images":
                self.create_images()
            case "texts":
                self.create_texts()

        self.elements.sort(key=lambda x: -x.z_buffer)

    def create_containers(self) -> None:
        """Create container components."""

        for container in self.data["containers"]:
            self.elements.append(Container(**container))

    def create_images(self) -> None:
        """Create image components."""

        for image in self.data["images"]:
            self.elements.append(Image(**image))

    def create_texts(self) -> None:
        """Create text components."""

        for text in self.data["texts"]:
            self.elements.append(Text(**text))

    def increment_score(self, graph: "Graph", count: int) -> None:
        """Increments the player's score by the input count.

        Args:
            graph (Graph): The graph object.
            count (int): How much to increment the score count by.
        """

        for element in self.elements:
            if element.id != SCORE_ID:
                continue

            element.increment(graph, count)

    def render(self, surface: pygame.Surface) -> None:
        """Renders the user interface.

        Args:
            surface (pygame.Surface): The display's surface.
        """

        for element in self.elements:
            element.render(surface)
