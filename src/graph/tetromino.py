from src.constants.constants import GRAPH_HEIGHT


class Tetromino:
    def __init__(self, graph, **kwargs):
        self.graph = graph

        self.positions = kwargs["positions"]
        self.origin = kwargs["origin"]
        self.color = kwargs["color"]

    def rotate(self, is_clockwise):
        if is_clockwise:
            self.rotate_clockwise()
        else:
            self.rotate_anti_clockwise()

    def rotate_clockwise(self):
        pass

    def rotate_anti_clockwise(self):
        pass

    def move(self):
        self.graph.cells[self.origin[0]][self.origin[1]].color = self.color

        for position in self.positions:
            x, y = position
            position = [x, y + 1]

        self.origin[1] += 1

    def is_next_move_valid(self):
        for position in self.positions:
            if position[1] + 1 >= GRAPH_HEIGHT:
                return False

        return True
