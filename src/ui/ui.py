from src.ui.container import Container

from src.utility.utility import Utility


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

    def create_containers(self):
        for container in self.data["containers"]:
            self.elements.append(Container(**container))

    def update(self):
        ...

    def render(self, surface):
        for element in self.elements:
            element.render(surface)
