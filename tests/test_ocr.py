import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from config import TESTS_DIR
from ocr import extract_text

IMAGE_PATH = TESTS_DIR / "sample_cv.jpg"

text = extract_text(str(IMAGE_PATH))

print(text)