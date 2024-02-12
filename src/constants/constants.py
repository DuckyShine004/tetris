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
