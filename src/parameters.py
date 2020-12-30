# Display
MASTER_VOLUMEN = 1
#WIDTH  = 1920
#HEIGHT = 1080
WIDTH  = 1280
HEIGHT = 720

GOD_MODE = False
HORIZONTAL_VELOCITY = 0.2 if not GOD_MODE else 1  # default 0.2
GRAVITY = - 0.6
INITIAL_VELOCITY = 14 # default 14
MAX_VELOCITY = 40
MARGIN_COLLISION_RECT = 18
FRAME_PER_SPRITE = 6

FALL_VELOCITY_OVER = -50
RESET_DISTANCE = 700
FLOAT_STEP = 2

FIX_TIME = 50
FLY_TIME = 250
STORM_TIME = 200
STORM_INTERVAL = 5


TRACK_LIST = (
	(14650, "waves.mp3"),
	(12400, "forest.mp3"),
	(9700, "night_forest.mp3"),
	(7150, "scary_forest.wav"),
	(5050, "wind.mp3"),
	(300, "hard_wind.mp3"),
    (-1000, "None")
)
