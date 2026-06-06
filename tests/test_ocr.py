import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from ocr import extract_text

text = extract_text("167261684.jpg")

with open("extracted_cv.txt", "w", encoding="utf-8") as f:
    f.write(text)

print(text)