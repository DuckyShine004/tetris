# DISPLAY
SURFACE_COLOR = (255, 255, 255)
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
            [0, 3],
            [1, 3],
            [2, 3],
            [1, 2],
        ],
        "origin": 1,
        "color": (160, 0, 240),
    },
}
# CELL
CELL_SIZE = (30, 30)
CELL_OFFSET = (0, 0)
BLACK = (0, 0, 0)

# PATHS
MUSIC_PATH = "assets/music/loop.wav"
