import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Path to your test dataset
TEST_DATA_PATH = DATA_DIR / "test_FD001.txt"
