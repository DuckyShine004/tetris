import os
import json

from src.constants.constants import GRAPH_WIDTH, GRAPH_HEIGHT


class Utility:
    @staticmethod
    def clamp(value, lower, upper):
        if value < lower:
            return lower

        if value > upper:
            return upper

        return value

    @staticmethod
    def get_json_data(path):
        directory_path = os.path.dirname(os.path.realpath(__file__))
        absolute_path = os.path.join(directory_path, path)

        with open(absolute_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    @staticmethod
    def get_clockwise_rotations(tetromino, graph):
        pivot = tetromino.positions[tetromino.origin]
        rotations = []

        for position in tetromino.positions:
            x = sum(pivot) - position[1]
            y = position[0] + pivot[1] - pivot[0]
            rotation = [x, y]

            if not Utility.is_valid_rotation(graph, rotation):
                return []

            rotations.append(rotation)

        return rotations

    @staticmethod
    def get_anti_clockwise_rotations(tetromino, graph):
        pivot = tetromino.positions[tetromino.origin]
        rotations = []

        for position in tetromino.positions:
            x = position[1] + pivot[0] - pivot[1]
            y = sum(pivot) - position[0]
            rotation = [x, y]

            if not Utility.is_valid_rotation(graph, rotation):
                return []

            rotations.append(rotation)

        return rotations

    @staticmethod
    def is_valid_rotation(graph, rotation):
        x, y = rotation

        if x < 0 or x >= GRAPH_WIDTH:
            return False

        if y < 0 or y >= GRAPH_HEIGHT:
            return False

        if graph.is_cell_occupied(y, x):
            return False

        return True
