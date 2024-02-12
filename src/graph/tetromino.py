from src.utility.utility import Utility

from src.constants.constants import GRAPH_HEIGHT


class Tetromino:
    def __init__(self, graph, **kwargs):
        self.graph = graph

        self.positions = kwargs["positions"]
        self.origin = kwargs["origin"]
        self.color = kwargs["color"]

    def occupy_cells(self, is_occupied):
        for x, y in self.positions:
            self.graph.set_occupied(y, x, is_occupied)

    def color_cells(self, is_color=True):
        color = self.color if is_color else None

        for x, y in self.positions:
            self.graph.set_color(y, x, color)

    def rotate_clockwise(self):
        rotations = Utility.get_clockwise_rotations(self, self.graph)

        if not rotations:
            return

        self.color_cells(False)
        self.positions = list(rotations)

    def rotate_anti_clockwise(self):
        rotations = Utility.get_anti_clockwise_rotations(self, self.graph)

        if not rotations:
            return

        self.color_cells(False)
        self.positions = list(rotations)

    def move_vertically(self):
        self.color_cells()

        if not self.is_vertical_move_valid():
            self.occupy_cells(True)
            return False

        self.color_cells(False)

        for position in self.positions:
            position[1] += 1

        return True

    def is_vertical_move_valid(self):
        for position in self.positions:
            delta = position[1] + 1

            if delta >= GRAPH_HEIGHT:
                return False

            if self.graph.is_cell_occupied(delta, position[0]):
                return False

        return True
