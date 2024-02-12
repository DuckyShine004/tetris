import os
import json


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
