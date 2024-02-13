from src.ui.container import Container
from src.ui.background import Background
from src.ui.text import Text

from src.utility.utility import Utility

from src.constants.constants import SCORE_ID


class UI:
    def __init__(self, path):
        self.data = Utility.get_json_data(path)
        self.elements = []

        self.initialize()

    def initialize(self):
        for elements in self.data.keys():
            self.create_elements(elements)

    def create_elements(self, elements):
        match elements:
            case "background":
                self.create_background()
            case "containers":
                self.create_containers()
            case "texts":
                self.create_texts()

    def create_background(self):
        self.elements.append(Background(**self.data["background"]))

    def create_containers(self):
        for container in self.data["containers"]:
            self.elements.append(Container(**container))

    def create_texts(self):
        for text in self.data["texts"]:
            self.elements.append(Text(**text))

    def increment_score(self, count):
        for element in self.elements:
            if element.id != SCORE_ID:
                continue

            element.increment(count)

    def update(self):
        ...

    def render(self, surface):
        for element in self.elements:
            element.render(surface)
