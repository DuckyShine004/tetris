# DISPLAY
SURFACE_COLOR = (255, 255, 255)
WIDTH = 720
HEIGHT = 1080
FPS = 60

# GRAPH
GRAPH_WIDTH = 10
GRAPH_HEIGHT = 24
MAX_DELAY = 500
INITIAL_DELAY = 500
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
        "positions": [[0, 0]],
        "origin": [0, 0],
        "color": (0, 0, 0),
    },
}
# CELL
CELL_SIZE = (40, 40)
CELL_OFFSET = (0, 0)

# PATHS
MUSIC_PATH = "assets/music/loop.wav"
