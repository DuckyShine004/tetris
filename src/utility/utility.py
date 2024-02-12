"""This module provides useful functionalities."""

from typing import TYPE_CHECKING, List, Any

import os
import json

from src.constants.constants import GRAPH_WIDTH, GRAPH_HEIGHT

if TYPE_CHECKING:
    from src.graph.graph import Graph
    from src.graph.tetromino import Tetromino


class Utility:
    """The Utility class is useful for providing methods that are used alot in
    this program.
    """

    @staticmethod
    def clamp(value: int, lower: int, upper: int) -> int:
        """Clamps a value between a lower bound and an upper bound.

        Args:
            value (int): The value to be clamped.
            lower (int): The lower bound.
            upper (int): The upper bound.

        Returns:
            int: The clamped value.
        """
        if value < lower:
            return lower

        if value > upper:
            return upper

        return value

    @staticmethod
    def get_json_data(path: str) -> Any:
        """Returns the deserialized JSON data.

        Args:
            path (str): The path to the JSON file.

        Returns:
            Any: The JSON data.
        """

        directory_path = os.path.dirname(os.path.realpath(__file__))
        absolute_path = os.path.join(directory_path, path)

        with open(absolute_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    @staticmethod
    def get_clockwise_rotations(tetromino: "Tetromino", graph: "Graph") -> List[List[int]]:
        """Get the clockwise rotated position.

        Args:
            tetromino (Tetromino): The current tetromino.
            graph (Graph): The graph object.

        Returns:
            List[int]: List of rotated positions.
        """

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
    def get_anti_clockwise_rotations(tetromino: "Tetromino", graph: "Graph") -> List[List[int]]:
        """Get the anti clockwise rotated positions.

        Args:
            tetromino (Tetromino): The current tetromino.
            graph (Graph): The graph object.

        Returns:
            List[int]: List of rotated positions.
        """

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
    def is_valid_rotation(graph: "Graph", rotation: List[int]) -> bool:
        """Returns if the rotation - clockwise or anti-clockwise is valid
        or not.

        Args:
            graph (Graph): The graph object.
            rotation (Tuple[int, int]): The rotated position.

        Returns:
            bool: If the rotation is valid.
        """

        x, y = rotation

        if x < 0 or x >= GRAPH_WIDTH:
            return False

        if y < 0 or y >= GRAPH_HEIGHT:
            return False

        if graph.is_cell_occupied(y, x):
            return False

        return True
