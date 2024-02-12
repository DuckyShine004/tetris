"""This module contains application constants.

Attributes:
    BORDER_SIZE (int): The size of the cell's border.
    CAPTION (str): The application name.
    CELL_OFFSET (tuple): Offset of each cell.
    CELL_SIZE (tuple): The cell's size.
    FPS (int): Frames per second.
    GRAPH_HEIGHT (int): The graph's height.
    GRAPH_WIDTH (int): The graph's width.
    HEIGHT (int): The display's height.
    MAX_DELAY (int): The delay of the vertical movement.
    MOVEMENT_DELAY (int): The delay of the horizontal movement.
    MUSIC_PATH (str): The path to the music.
    OUTLINE (tuple): The outline color of the cell.
    PREDICTION (tuple): The prediction outline.
    START_HEIGHT (int): The height at which the tetrominoes are rendered.
    SURFACE_COLOR (tuple): The background default color.
    TETROMINO_ARGUMENTS (dict): Dictionary of tetrominoes.
    TETROMINOES (list): Tetromino string identifiers.
    UI_PATH (str): The path to the ui.
    WIDTH (int): The display width.
"""

# DISPLAY
SURFACE_COLOR = (11, 26, 73)
WIDTH = 720
HEIGHT = 1080
FPS = 60
CAPTION = "Tetris"

# GRAPH
GRAPH_WIDTH = 10
GRAPH_HEIGHT = 28
MAX_DELAY = 100
MOVEMENT_DELAY = 100
START_HEIGHT = 3

# TETROMINO
TETROMINOES = [
    "IMino",
    "OMino",
    "TMino",
    "JMino",
    "LMino",
    "SMino",
    "ZMino",
]

TETROMINO_ARGUMENTS = {
    "IMino": {
        "positions": [
            [5, 0],
            [5, 1],
            [5, 2],
            [5, 3],
        ],
        "origin": 2,
        "color": (0, 240, 240),
    },
    "OMino": {
        "positions": [
            [4, 2],
            [5, 2],
            [4, 3],
            [5, 3],
        ],
        "origin": 3,
        "color": (240, 240, 0),
    },
    "TMino": {
        "positions": [
            [4, 3],
            [5, 3],
            [6, 3],
            [5, 2],
        ],
        "origin": 1,
        "color": (160, 0, 240),
    },
    "JMino": {
        "positions": [
            [4, 2],
            [4, 3],
            [5, 3],
            [6, 3],
        ],
        "origin": 2,
        "color": (0, 0, 240),
    },
    "LMino": {
        "positions": [
            [4, 3],
            [5, 3],
            [6, 3],
            [6, 2],
        ],
        "origin": 1,
        "color": (240, 160, 0),
    },
    "SMino": {
        "positions": [
            [4, 3],
            [5, 3],
            [5, 2],
            [6, 2],
        ],
        "origin": 1,
        "color": (0, 240, 0),
    },
    "ZMino": {
        "positions": [
            [4, 2],
            [5, 2],
            [5, 3],
            [6, 3],
        ],
        "origin": 2,
        "color": (240, 0, 0),
    },
}

# CELL
CELL_SIZE = (30, 30)
BORDER_SIZE = 3
CELL_OFFSET = (200, 80)
OUTLINE = (11, 26, 73)
PREDICTION = (255, 255, 255)

# PATHS
UI_PATH = "../../json/ui.json"
MUSIC_PATH = "assets/music/loop.wav"
