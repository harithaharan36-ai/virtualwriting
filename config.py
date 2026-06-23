import os

# Application Info
APP_NAME = "Virtual Air Writing AI"
VERSION = "1.0.0"

# File Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGS_DIR = os.path.join(BASE_DIR, "logs")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
HISTORY_DIR = os.path.join(OUTPUT_DIR, "history")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# Create necessary directories
for path in [LOGS_DIR, OUTPUT_DIR, HISTORY_DIR]:
    os.makedirs(path, exist_ok=True)

# Camera Settings
DEFAULT_CAMERA_INDEX = 0
FRAME_WIDTH = 1280
FRAME_HEIGHT = 720
FPS_LIMIT = 30

# Handwriting Recognition
OCR_LANGUAGE = ['en']

# Drawing Settings
DEFAULT_BRUSH_SIZE = 5
DEFAULT_BRUSH_COLOR = (255, 255, 255)  # White
ERASER_SIZE = 50

# Gestures
GESTURE_CONFIDENCE_THRESHOLD = 0.7

# Themes
THEMES = {
    "Dark": {
        "bg": "#1e1e1e",
        "fg": "#ffffff",
        "accent": "#007acc",
        "canvas_bg": "#000000"
    },
    "Light": {
        "bg": "#f3f3f3",
        "fg": "#000000",
        "accent": "#007acc",
        "canvas_bg": "#ffffff"
    }
}
