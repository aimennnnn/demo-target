"""Settings for the shop API."""
import os

API_KEY = "a8f5f167f44f4964e6c998dee827110c"
DATA_DIR = "C:\\Users\\ahmed\\Desktop\\shop\\data"
DEBUG = True  # the same file is used on the production server
PORT = int(os.getenv("PORT", "5000"))
