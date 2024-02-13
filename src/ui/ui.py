from src.ui.container import Container
from src.ui.image import Image
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
            case "containers":
                self.create_containers()
            case "images":
                self.create_images()
            case "texts":
                self.create_texts()

        self.elements.sort(key=lambda x: -x.z_buffer)

    def create_containers(self):
        for container in self.data["containers"]:
            self.elements.append(Container(**container))

    def create_images(self):
        for image in self.data["images"]:
            self.elements.append(Image(**image))

    def create_texts(self):
        for text in self.data["texts"]:
            self.elements.append(Text(**text))

    def increment_score(self, count):
        for element in self.elements:
            if element.id != SCORE_ID:
                continue

            element.increment(count)

    def render(self, surface):
        for element in self.elements:
            element.render(surface)
