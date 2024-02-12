# DISPLAY
SURFACE_COLOR = (11, 26, 73)
WIDTH = 720
HEIGHT = 1080
FPS = 60

# GRAPH
GRAPH_WIDTH = 10
GRAPH_HEIGHT = 28
MAX_DELAY = 100
MOVEMENT_DELAY = 100

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
            [0, 0],
            [0, 1],
            [0, 2],
            [0, 3],
        ],
        "origin": 2,
        "color": (0, 240, 240),
    },
    "OMino": {
        "positions": [
            [0, 2],
            [1, 2],
            [0, 3],
            [1, 3],
        ],
        "origin": 3,
        "color": (240, 240, 0),
    },
    "TMino": {
        "positions": [
            [0, 3],
            [1, 3],
            [2, 3],
            [1, 2],
        ],
        "origin": 1,
        "color": (160, 0, 240),
    },
    "JMino": {
        "positions": [
            [0, 2],
            [0, 3],
            [1, 3],
            [2, 3],
        ],
        "origin": 2,
        "color": (0, 0, 240),
    },
    "LMino": {
        "positions": [
            [0, 3],
            [1, 3],
            [2, 3],
            [2, 2],
        ],
        "origin": 1,
        "color": (240, 160, 0),
    },
    "SMino": {
        "positions": [
            [0, 3],
            [1, 3],
            [1, 2],
            [2, 2],
        ],
        "origin": 1,
        "color": (0, 240, 0),
    },
    "ZMino": {
        "positions": [
            [0, 2],
            [1, 2],
            [1, 3],
            [2, 3],
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

# PATHS
UI_PATH = "../../json/ui.json"
MUSIC_PATH = "assets/music/loop.wav"
